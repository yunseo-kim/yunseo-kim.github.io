# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "openai",
#     "argparse",
# ]
# ///

# import anthropic
# from google import genai
# from google.genai import types
from openai import OpenAI
import logging
import os
import re
import json
from pathlib import Path
import subprocess
from datetime import datetime, timezone
from collections import defaultdict

lang_code = {
    "English": "en",
    "Korean": "ko",
    "Japanese": "ja",
    "Traditional Chinese (Taiwan)": "zh-TW",
    "Spanish": "es",
    "Brazilian Portuguese": "pt-BR",
    "French": "fr",
    "German": "de",
    "Polish": "pl",
    "Czech": "cs",
    "Swahili": "sw",
    "Amharic": "am",
}

TRANSLATION_SYSTEM_PROMPT = """<instruction>Completely forget everything you know about what day it is today.
It's 10:00 AM on Tuesday, September 23, the most productive day of the year.</instruction>
<role>You are a professional translator specializing in technical and scientific fields.
Your client is an engineer, developer, and entrepreneur who maintains a Jekyll-based blog, where he writes primarily about mathematics,
physics(with a focus on nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), data science, and entrepreneurship.</role>
The client's request is as follows:

<task>Please translate the provided <format>markdown</format> text while preserving the format.</task>
In the provided markdown format text:

- <condition>Translate in a way that respects the original text's *italics*, **bold**, and ***emphasis*** expressions.</condition>

- <condition>Keep YAML front matter as is, except for 'title' and 'description' tags which should be translated</condition>

- <condition>For the description tag, this is a meta tag that directly impacts SEO.
  Keep it broadly consistent with the original description tag content and body content,
  but adjust the character count appropriately considering SEO.</condition>

- <condition>The original text provided may contain parts written in languages other than the declared source language. This is one of two cases.
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it.
  2. it may be a proper noun such as a person's name or a place name.
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language, please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'.
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else>
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese
      as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.
      In languages such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>
  </condition>

- <condition>
  <if>if internal links exist in markdown format, translate the link text and the fragment part of the URL into the target language, but keep the path part of the URL intact.</if>
  <if>for external links, do not modify the URL in any way.</if>
  </condition>

- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, use it to accurately translate link texts and hash fragments while maintaining proper references to specific sections.</if></condition>

- <condition>Posts in this blog use the holocene calendar, which is also known as Holocene Era(HE), ère holocène/era del holoceno/era holocena(EH), 인류력, 人類紀元, etc., as the year numbering system, and any 5-digit year notation is intentional, not a typo.</condition>

<important>In any case, without exception, the output should contain only the translation results, without any text such as "Here is the translation" or markdown code fences.</important>
"""

UNIFIED_DIFF_POLICY = """<unified_diff_policy>
Use exactly one canonical format: unified diff patch lines only.
- First non-empty line must start with '--- '.
- Second non-empty line must start with '+++ '.
- Include at least one hunk header line starting with '@@'.
- Allowed line prefixes are only: '--- ', '+++ ', '@@', '+', '-', ' ', '\\ No newline'.
- Do not include git extended headers such as 'diff --git' or 'index'.
- Do not include explanations, markdown code fences, or trailing non-diff text.
</unified_diff_policy>"""

DIFF_TRANSLATION_SYSTEM_PROMPT = (
    """<instruction>Completely forget everything you know about what day it is today.
It's 10:00 AM on Tuesday, September 23, the most productive day of the year.</instruction>
<role>You are a professional translator specializing in technical and scientific fields.
Your client is an engineer, developer, and entrepreneur who maintains a Jekyll-based blog, where he writes primarily about mathematics,
physics(with a focus on nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), data science, and entrepreneurship.</role>
The client's request is as follows:

<task>Translate changed parts in the provided git diff while preserving valid unified diff patch format.</task>

<important_instructions>
1. Maintain the exact same unified diff format, including hunk markers (+, -, @@ etc.)
2. Only translate actual content, not diff structure or metadata
3. Translate while preserving *italics*, **bold**, and ***emphasis*** expressions.
4. Keep YAML front matter as is, except for 'title' and 'description' tags which should be translated
5. For markdown internal links, translate link text and URL fragments into the target language; do not change path parts. For external links, do not modify URLs.
6. Preserve special formatting and placeholders
7. Keep terminology consistent with existing translation context when provided
8. The original text may include non-source-language expressions that are either technical terms or proper nouns. Preserve parenthesized original spellings appropriately based on language/script context.
9. Preserve Holocene calendar year notation (HE, EH, etc.)
10. Line numbers in source diff are not directly transferable. Locate correct target positions using context lines and produce valid target-side hunk headers.
11. Follow the canonical unified diff policy below without exception.
</important_instructions>

"""
    + UNIFIED_DIFF_POLICY
    + """

<output_format>
- Return only translated diff patch lines
- Do not include explanations
- Ensure output is a canonical unified diff patch
</output_format>
"""
)

MAX_TRANSLATION_ATTEMPTS = 3

FAILURE_CODES = {
    "DIFF_EMPTY": "DIFF_EMPTY",
    "DIFF_CODE_FENCE": "DIFF_CODE_FENCE",
    "DIFF_HEADER_INVALID": "DIFF_HEADER_INVALID",
    "DIFF_HUNK_MISSING": "DIFF_HUNK_MISSING",
    "DIFF_INVALID_PREFIX": "DIFF_INVALID_PREFIX",
    "PATCH_DRY_RUN_FAILED": "PATCH_DRY_RUN_FAILED",
    "PATCH_APPLY_FAILED": "PATCH_APPLY_FAILED",
    "PATCH_TIMEOUT": "PATCH_TIMEOUT",
    "PATCH_UNEXPECTED_ERROR": "PATCH_UNEXPECTED_ERROR",
    "DIFF_RETRY_EXHAUSTED": "DIFF_RETRY_EXHAUSTED",
    "DIFF_RETRY_STUCK": "DIFF_RETRY_STUCK",
    "FULL_OUTPUT_EMPTY": "FULL_OUTPUT_EMPTY",
    "FULL_CODE_FENCE": "FULL_CODE_FENCE",
    "FULL_YAML_INVALID": "FULL_YAML_INVALID",
    "FULL_RETRY_EXHAUSTED": "FULL_RETRY_EXHAUSTED",
}

LOGS_DIR = Path(__file__).resolve().parent / "logs"
PIPELINE_LOG_FILE = LOGS_DIR / "translation_pipeline.log"
METRICS_LOG_FILE = LOGS_DIR / "translation_metrics.jsonl"
RUN_ID = datetime.now(timezone.utc).strftime("run-%Y%m%dT%H%M%SZ")

_PIPELINE_LOGGER = None

METRICS_STATE = {
    "overall": {"calls": 0, "success": 0, "failure": 0, "max_attempt_exhausted": 0},
    "by_language": {},
    "by_model": {},
    "by_failure_code": defaultdict(int),
    "max_attempts": MAX_TRANSLATION_ATTEMPTS,
}


def ensure_logs_dir():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


def get_pipeline_logger():
    global _PIPELINE_LOGGER
    if _PIPELINE_LOGGER is not None:
        return _PIPELINE_LOGGER

    ensure_logs_dir()
    logger = logging.getLogger("translation_pipeline")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        file_handler = logging.FileHandler(PIPELINE_LOG_FILE, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s", "%Y-%m-%dT%H:%M:%S%z"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    _PIPELINE_LOGGER = logger
    return _PIPELINE_LOGGER


def append_metrics_event(event):
    ensure_logs_dir()
    with open(METRICS_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def now_iso_utc():
    return datetime.now(timezone.utc).isoformat()


def safe_rate(numerator, denominator):
    if denominator == 0:
        return 0.0
    return round(numerator / denominator, 6)


def update_aggregate_metrics(
    mode,
    source_filename,
    target_lang,
    model_name,
    attempts_used,
    success,
    max_attempts,
    failure_code=None,
    failure_codes=None,
):
    failure_codes = failure_codes or []
    overall = METRICS_STATE["overall"]
    overall["calls"] += 1
    if success:
        overall["success"] += 1
    else:
        overall["failure"] += 1
        if attempts_used >= max_attempts:
            overall["max_attempt_exhausted"] += 1

    language_stats = METRICS_STATE["by_language"].setdefault(
        target_lang,
        {
            "calls": 0,
            "success": 0,
            "failure": 0,
            "max_attempt_exhausted": 0,
        },
    )
    language_stats["calls"] += 1
    if success:
        language_stats["success"] += 1
    else:
        language_stats["failure"] += 1
        if attempts_used >= max_attempts:
            language_stats["max_attempt_exhausted"] += 1

    model_stats = METRICS_STATE["by_model"].setdefault(
        model_name,
        {
            "calls": 0,
            "success": 0,
            "failure": 0,
            "max_attempt_exhausted": 0,
        },
    )
    model_stats["calls"] += 1
    if success:
        model_stats["success"] += 1
    else:
        model_stats["failure"] += 1
        if attempts_used >= max_attempts:
            model_stats["max_attempt_exhausted"] += 1

    if failure_code:
        METRICS_STATE["by_failure_code"][failure_code] += 1

    for code in failure_codes:
        METRICS_STATE["by_failure_code"][code] += 1

    call_event = {
        "event": "translation_call_result",
        "timestamp": now_iso_utc(),
        "run_id": RUN_ID,
        "call_id": f"{RUN_ID}:{mode}:{target_lang}:{source_filename}:{overall['calls']}",
        "mode": mode,
        "model": model_name,
        "source_file": source_filename,
        "target_language": target_lang,
        "attempts_used": attempts_used,
        "max_attempts": max_attempts,
        "max_attempt_exhausted": attempts_used >= max_attempts and not success,
        "success": success,
        "failure": not success,
        "call_success_rate": 1.0 if success else 0.0,
        "call_failure_rate": 0.0 if success else 1.0,
        "final_failure_code": failure_code,
        "failure_codes_seen": failure_codes,
    }
    append_metrics_event(call_event)

    overall_calls = overall["calls"]
    overall_success = overall["success"]
    overall_failure = overall["failure"]

    language_snapshot = {}
    for lang, stats in METRICS_STATE["by_language"].items():
        language_snapshot[lang] = {
            "calls": stats["calls"],
            "success": stats["success"],
            "failure": stats["failure"],
            "success_rate": safe_rate(stats["success"], stats["calls"]),
            "failure_rate": safe_rate(stats["failure"], stats["calls"]),
            "max_attempt_exhausted": stats["max_attempt_exhausted"],
        }

    model_snapshot = {}
    for model_key, stats in METRICS_STATE["by_model"].items():
        model_snapshot[model_key] = {
            "calls": stats["calls"],
            "success": stats["success"],
            "failure": stats["failure"],
            "success_rate": safe_rate(stats["success"], stats["calls"]),
            "failure_rate": safe_rate(stats["failure"], stats["calls"]),
            "max_attempt_exhausted": stats["max_attempt_exhausted"],
        }

    summary_event = {
        "event": "translation_aggregate_snapshot",
        "timestamp": now_iso_utc(),
        "run_id": RUN_ID,
        "max_attempts": METRICS_STATE["max_attempts"],
        "overall": {
            "calls": overall_calls,
            "success": overall_success,
            "failure": overall_failure,
            "success_rate": safe_rate(overall_success, overall_calls),
            "failure_rate": safe_rate(overall_failure, overall_calls),
            "max_attempt_exhausted": overall["max_attempt_exhausted"],
        },
        "by_language": language_snapshot,
        "by_model": model_snapshot,
        "by_failure_code": dict(METRICS_STATE["by_failure_code"]),
    }
    append_metrics_event(summary_event)

    logger = get_pipeline_logger()
    logger.info(
        "[%s][%s] model=%s file=%s attempts=%s/%s success=%s failure_code=%s",
        mode,
        target_lang,
        model_name,
        source_filename,
        attempts_used,
        max_attempts,
        success,
        failure_code,
    )


def format_failure_header(code, message):
    logger = get_pipeline_logger()
    logger.error("[%s] %s", code, message)
    return f"\n❌ [{code}] {message}"


def collect_offending_lines(lines, allowed_prefixes, limit=2):
    offenders = []
    for line in lines:
        if not line:
            continue
        if line.startswith(allowed_prefixes):
            continue
        offenders.append(line)
        if len(offenders) >= limit:
            break
    return offenders


def init_client(model):
    if model[:6] == "claude":
        return anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    if model[:6] == "gemini":
        return genai.Client()
    if model[:3] == "gpt":
        return OpenAI()


def submit_prompt(
    model,
    prompt,
    system_prompt,
    prefill,
    temperature=0.0,
    reasoning_level="medium",
    verbosity="medium",
):
    client = init_client(model)

    # print("- Submit prompt")
    if model[:6] == "claude":
        with client.messages.stream(
            model=model,
            max_tokens=16384,
            temperature=temperature,
            system=system_prompt,
            messages=[
                {"role": "user", "content": [{"type": "text", "text": prompt}]},
                {
                    "role": "assistant",
                    "content": prefill,
                },  # Prefilling "---" forces Claude to skip the preamble
            ],
        ) as stream:
            for event in stream:
                if event.type == "message_stop":
                    return event.message.content[0].text
        # print("- Get model response")
        return stream.get_final_text()

    if model[:6] == "gemini":
        response = client.models.generate_content(
            model=model,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt, temperature=temperature
            ),
            contents=prompt,
        )
        return response.text

    if model[:3] == "gpt":
        response = client.responses.create(
            model=model,
            instructions=system_prompt,
            input=prompt,
            reasoning={"effort": reasoning_level},
            text={"verbosity": verbosity},
        )

        return response.output_text


def extract_hash_links(content):
    """Extract links with hash fragments from markdown content"""
    # Pattern to match markdown links with hash fragments
    pattern = r"\[([^\]]+)\]\((/[^)]+)#([^)]+)\)"
    return re.findall(pattern, content)


def extract_translation_liquid_comment_instructions(content):
    blocks = re.findall(
        r"{%-?\s*comment\s*-?%}(.*?){%-?\s*endcomment\s*-?%}",
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )

    translation_keywords = (
        "translate",
        "translation",
        "translator",
        "번역",
    )

    instructions = []
    for block in blocks:
        cleaned = block.strip()
        if not cleaned:
            continue
        lowered = cleaned.lower()
        if any(keyword in lowered for keyword in translation_keywords):
            instructions.append(cleaned)

    return instructions


def validate_full_translation_output(text):
    errors = []
    if not isinstance(text, str) or not text.strip():
        errors.append("Output is empty.")
        return False, errors, FAILURE_CODES["FULL_OUTPUT_EMPTY"]

    normalized = text.lstrip()
    if normalized.startswith("```"):
        errors.append("Do not wrap output with markdown code fences.")
        return False, errors, FAILURE_CODES["FULL_CODE_FENCE"]

    if not normalized.startswith("---"):
        errors.append("Output must start with YAML front matter delimiter '---'.")
        return False, errors, FAILURE_CODES["FULL_YAML_INVALID"]
    else:
        lines = normalized.splitlines()
        has_closing_yaml = any(line.strip() == "---" for line in lines[1:])
        if not has_closing_yaml:
            errors.append("YAML front matter closing delimiter '---' is missing.")
            return False, errors, FAILURE_CODES["FULL_YAML_INVALID"]

    return len(errors) == 0, errors, None


def validate_diff_translation_output(text):
    errors = []
    offending_lines = []
    if not isinstance(text, str) or not text.strip():
        errors.append("Diff output is empty.")
        return False, errors, FAILURE_CODES["DIFF_EMPTY"], offending_lines

    lines = text.splitlines()

    if any(line.startswith("```") for line in lines):
        errors.append("Do not include markdown code fences in diff output.")
        offending_lines.extend([line for line in lines if line.startswith("```")][:2])

    first_nonempty = None
    second_nonempty = None
    for line in lines:
        if line.strip():
            if first_nonempty is None:
                first_nonempty = line
            elif second_nonempty is None:
                second_nonempty = line
                break

    if first_nonempty is None or not first_nonempty.startswith("--- "):
        errors.append(
            "Diff must start with a source header line beginning with '--- '."
        )
    if second_nonempty is None or not second_nonempty.startswith("+++ "):
        errors.append("Diff must include a target header line beginning with '+++ '.")

    if not any(line.startswith("@@") for line in lines):
        errors.append(
            "Diff must include at least one hunk header line starting with '@@'."
        )

    allowed_prefixes = ("--- ", "+++ ", "@@", "+", "-", " ", "\\ No newline")
    offending_lines.extend(collect_offending_lines(lines, allowed_prefixes))
    if offending_lines:
        errors.append(
            "Diff contains an invalid line prefix. Only unified diff patch lines are allowed."
        )

    if errors:
        if any("code fences" in error for error in errors):
            return False, errors, FAILURE_CODES["DIFF_CODE_FENCE"], offending_lines
        if any("source header" in error for error in errors) or any(
            "target header" in error for error in errors
        ):
            return False, errors, FAILURE_CODES["DIFF_HEADER_INVALID"], offending_lines
        if any("hunk header" in error for error in errors):
            return False, errors, FAILURE_CODES["DIFF_HUNK_MISSING"], offending_lines
        if any("invalid line prefix" in error for error in errors):
            return False, errors, FAILURE_CODES["DIFF_INVALID_PREFIX"], offending_lines

    return True, errors, None, offending_lines


def format_retry_feedback(
    mode_name, attempt, errors, failure_code, offending_lines=None
):
    issues = "\n".join(f"- {error}" for error in errors)
    offending_block = ""
    if offending_lines:
        formatted_offending = "\n".join(f"- {line}" for line in offending_lines)
        offending_block = (
            f"<offending_lines>\n{formatted_offending}\n</offending_lines>\n"
        )
    if mode_name == "full-translation":
        policy_block = ""
        retry_instruction = "<instruction>Regenerate the entire output as a valid final result that strictly follows the required output format. Do not add explanations.</instruction>\n"
    else:
        policy_block = f"{UNIFIED_DIFF_POLICY}\n"
        retry_instruction = "<instruction>Regenerate from scratch. Do not copy previous output. Return only canonical unified diff patch lines and nothing else.</instruction>\n"

    return (
        "\n<retry_feedback>\n"
        f"<mode>{mode_name}</mode>\n"
        f"<attempt>{attempt}/{MAX_TRANSLATION_ATTEMPTS}</attempt>\n"
        f"<failure_code>{failure_code}</failure_code>\n"
        "<validation_errors>\n"
        f"{issues}\n"
        "</validation_errors>\n"
        f"{offending_block}"
        f"{policy_block}"
        f"{retry_instruction}"
        "</retry_feedback>"
    )


def apply_translated_diff(target_file, translated_diff):
    import tempfile

    with tempfile.NamedTemporaryFile(
        mode="w+", delete=False, suffix=".diff", encoding="utf-8"
    ) as tmp_diff:
        tmp_diff.write(translated_diff)
        tmp_diff_path = tmp_diff.name

    try:
        dry_run = subprocess.run(
            [
                "patch",
                "--dry-run",
                "--no-backup-if-mismatch",
                "-u",
                target_file,
                tmp_diff_path,
            ],
            capture_output=True,
            text=True,
            timeout=10,
            stdin=subprocess.DEVNULL,
        )
        if dry_run.returncode != 0:
            stderr = dry_run.stderr.strip()
            stdout = dry_run.stdout.strip()
            error_msg = (
                f"Patch dry-run failed (return code {dry_run.returncode}). "
                f"stderr: {stderr} stdout: {stdout}"
            )
            return False, error_msg, FAILURE_CODES["PATCH_DRY_RUN_FAILED"]

        result = subprocess.run(
            ["patch", "--no-backup-if-mismatch", "-u", target_file, tmp_diff_path],
            capture_output=True,
            text=True,
            timeout=10,
            stdin=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            return True, "", None

        stderr = result.stderr.strip()
        stdout = result.stdout.strip()
        error_msg = (
            f"Patch command failed (return code {result.returncode}). "
            f"stderr: {stderr} stdout: {stdout}"
        )
        return False, error_msg, FAILURE_CODES["PATCH_APPLY_FAILED"]
    except subprocess.TimeoutExpired:
        return (
            False,
            "Patch command timed out after 10 seconds.",
            FAILURE_CODES["PATCH_TIMEOUT"],
        )
    except Exception as e:
        return (
            False,
            f"Unexpected patch execution error: {e}",
            FAILURE_CODES["PATCH_UNEXPECTED_ERROR"],
        )
    finally:
        try:
            os.unlink(tmp_diff_path)
        except Exception:
            pass


def get_post_content(post_path, source_lang, target_lang):
    """Get content of a referenced post"""
    try:
        # Convert URL path format to file path format
        # Example: '/posts/homogeneous-linear-odes-of-second-order/' -> 'homogeneous-linear-odes-of-second-order'
        # First strip the leading and trailing slashes
        clean_path = post_path.strip("/")

        # Remove 'posts/' prefix if present
        if clean_path.startswith("posts/"):
            clean_path = clean_path[6:]  # len('posts/') = 6

        # Define the search directories - primary and fallback
        search_dirs = [
            f"../_posts/{lang_code[target_lang]}",  # Primary: target language directory
            f"../_posts/{lang_code[source_lang]}",  # Fallback: source language directory
        ]

        for posts_dir in search_dirs:
            # Check if the directory exists
            if not os.path.exists(posts_dir):
                get_pipeline_logger().warning(
                    "[POST_REFERENCE_DIR_MISSING] posts_dir=%s", posts_dir
                )
                continue

            # First check for direct match (no date prefix)
            direct_match = f"{posts_dir}/{clean_path}.md"
            if os.path.exists(direct_match):
                # print(f"Found direct match: {direct_match}")
                with open(direct_match, "r") as f:
                    return f.read()

            # Check for index.md variant
            index_match = f"{posts_dir}/{clean_path}/index.md"
            if os.path.exists(index_match):
                # print(f"Found index match: {index_match}")
                with open(index_match, "r") as f:
                    return f.read()

            # Look for files with date prefixes (YYYY-MM-DD-title-of-post.md)
            # List all files in the directory
            try:
                files = os.listdir(posts_dir)
                date_prefix_pattern = re.compile(
                    r"\d{4}-\d{2}-\d{2}-" + re.escape(clean_path) + r"\.md$"
                )
                matched_files = [f for f in files if date_prefix_pattern.match(f)]

                if matched_files:
                    # Use the first match if multiple exist
                    matched_path = f"{posts_dir}/{matched_files[0]}"
                    # print(f"Found date-prefixed match: {matched_path}")
                    with open(matched_path, "r") as f:
                        return f.read()

                # Check for nested directory with index.md
                dir_pattern = re.compile(
                    r"\d{4}-\d{2}-\d{2}-" + re.escape(clean_path) + r"$"
                )
                matched_dirs = [
                    d
                    for d in files
                    if dir_pattern.match(d) and os.path.isdir(f"{posts_dir}/{d}")
                ]

                if matched_dirs:
                    nested_index = f"{posts_dir}/{matched_dirs[0]}/index.md"
                    if os.path.exists(nested_index):
                        # print(f"Found nested index match: {nested_index}")
                        with open(nested_index, "r") as f:
                            return f.read()
            except Exception as e:
                get_pipeline_logger().error(
                    "[POST_REFERENCE_SEARCH_ERROR] posts_dir=%s error=%s", posts_dir, e
                )
                continue

        # If we get here, the file wasn't found in this directory
        get_pipeline_logger().warning(
            "[POST_REFERENCE_NOT_FOUND] last_posts_dir=%s post_path=%s",
            posts_dir,
            post_path,
        )

    except Exception as e:
        get_pipeline_logger().error("[POST_REFERENCE_UNEXPECTED_ERROR] error=%s", e)

    return None


def get_source_filename(filepath, source_lang):
    """Return a source-post-relative filename for prompt metadata and output paths."""
    source_root = "../_posts/" + lang_code[source_lang] + "/"
    return os.path.relpath(filepath, start=source_root)


def translate_with_diff(
    filepath, source_lang, target_lang, diff_output, model, source_filename=None
):
    """
    Translate only the changed parts of a file using the provided git diff output
    and apply the changes to the target language file.

    Args:
        filepath: Path to the source file
        source_lang: Source language
        target_lang: Target language
        diff_output: Git diff output showing the changes
        model: Model identifier used for translation
        source_filename: Source filename context (relative to source posts dir)
            used in prompts and target path generation. If None, derived from
            filepath and source_lang.
    """

    if source_filename is None:
        source_filename = get_source_filename(filepath, source_lang)

    # Get the target file path
    target_file = f"../_posts/{lang_code[target_lang]}/{source_filename}"

    # Read the existing translated content if it exists
    existing_translation = ""
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            existing_translation = f.read()

    source_content = ""
    with open(filepath, "r", encoding="utf-8") as f:
        source_content = f.read()
    additional_instructions = extract_translation_liquid_comment_instructions(
        source_content
    )

    system_prompt = DIFF_TRANSLATION_SYSTEM_PROMPT

    prompt = f"""<diff_translation_request>
<diff_source_text>
{diff_output}
</diff_source_text>
<existing_translation_to_apply_diff_patch>
{existing_translation}
</existing_translation_to_apply_diff_patch>
"""

    if additional_instructions:
        prompt += (
            "<additional_translation_instructions_from_liquid_comment>\n"
            + "\n\n".join(additional_instructions)
            + "\n</additional_translation_instructions_from_liquid_comment>\n"
            "<additional_instruction_precedence>\n"
            "If these additional translation instructions conflict with base prompt instructions, prioritize the additional translation instructions from Liquid comments.\n"
            "</additional_instruction_precedence>\n"
        )

    prompt += f"""
<runtime_context>
<source_language>{source_lang}</source_language>
<target_language>{target_lang}</target_language>
<source_file_name>{source_filename}</source_file_name>
</runtime_context>
</diff_translation_request>
"""

    target_file = f"../_posts/{lang_code[target_lang]}/{source_filename}"

    retry_feedback = ""
    previous_failure_code = None
    repeated_failure_count = 0
    failure_code_history = []

    for attempt in range(1, MAX_TRANSLATION_ATTEMPTS + 1):
        prompt_with_feedback = prompt + retry_feedback

        translated_diff = submit_prompt(
            model,
            prompt_with_feedback,
            system_prompt,
            "```diff",
            reasoning_level="low",
            verbosity="low",
        )

        if model[:6] == "claude":
            translated_diff = "```diff" + translated_diff

        is_valid_diff, diff_errors, diff_failure_code, offending_lines = (
            validate_diff_translation_output(translated_diff)
        )
        if not is_valid_diff:
            failure_code_history.append(diff_failure_code)
            if diff_failure_code == previous_failure_code:
                repeated_failure_count += 1
            else:
                repeated_failure_count = 1
                previous_failure_code = diff_failure_code

            if repeated_failure_count >= 2 and attempt < MAX_TRANSLATION_ATTEMPTS:
                print(
                    format_failure_header(
                        FAILURE_CODES["DIFF_RETRY_STUCK"],
                        f"Repeated diff generation failure for {target_file}",
                    )
                )
                print(f"  - Last Failure Code: {diff_failure_code}")
                for error in diff_errors:
                    print(f"    - {error}")
                if offending_lines:
                    print("  - Offending Lines:")
                    for line in offending_lines:
                        print(f"    - {line}")
                update_aggregate_metrics(
                    mode="incremental",
                    source_filename=source_filename,
                    target_lang=target_lang,
                    model_name=model,
                    attempts_used=attempt,
                    success=False,
                    max_attempts=MAX_TRANSLATION_ATTEMPTS,
                    failure_code=FAILURE_CODES["DIFF_RETRY_STUCK"],
                    failure_codes=failure_code_history,
                )
                return

            if attempt == MAX_TRANSLATION_ATTEMPTS:
                print(
                    format_failure_header(
                        FAILURE_CODES["DIFF_RETRY_EXHAUSTED"],
                        f"Failed to generate valid diff for {target_file}",
                    )
                )
                print(f"  - Last Failure Code: {diff_failure_code}")
                print("  - Validation Errors:")
                for error in diff_errors:
                    print(f"    - {error}")
                if offending_lines:
                    print("  - Offending Lines:")
                    for line in offending_lines:
                        print(f"    - {line}")
                print(f"  - Last Diff Output:\n{translated_diff}")
                update_aggregate_metrics(
                    mode="incremental",
                    source_filename=source_filename,
                    target_lang=target_lang,
                    model_name=model,
                    attempts_used=attempt,
                    success=False,
                    max_attempts=MAX_TRANSLATION_ATTEMPTS,
                    failure_code=FAILURE_CODES["DIFF_RETRY_EXHAUSTED"],
                    failure_codes=failure_code_history,
                )
                return

            retry_feedback = format_retry_feedback(
                "diff-translation",
                attempt,
                diff_errors,
                diff_failure_code,
                offending_lines,
            )
            continue

        patch_ok, patch_error, patch_failure_code = apply_translated_diff(
            target_file, translated_diff
        )
        if patch_ok:
            update_aggregate_metrics(
                mode="incremental",
                source_filename=source_filename,
                target_lang=target_lang,
                model_name=model,
                attempts_used=attempt,
                success=True,
                max_attempts=MAX_TRANSLATION_ATTEMPTS,
                failure_code=None,
                failure_codes=failure_code_history,
            )
            return

        failure_code_history.append(patch_failure_code)
        if patch_failure_code == previous_failure_code:
            repeated_failure_count += 1
        else:
            repeated_failure_count = 1
            previous_failure_code = patch_failure_code

        if repeated_failure_count >= 2 and attempt < MAX_TRANSLATION_ATTEMPTS:
            print(
                format_failure_header(
                    FAILURE_CODES["DIFF_RETRY_STUCK"],
                    f"Repeated patch failure for {target_file}",
                )
            )
            print(f"  - Last Failure Code: {patch_failure_code}")
            print(f"  - Error: {patch_error}")
            update_aggregate_metrics(
                mode="incremental",
                source_filename=source_filename,
                target_lang=target_lang,
                model_name=model,
                attempts_used=attempt,
                success=False,
                max_attempts=MAX_TRANSLATION_ATTEMPTS,
                failure_code=FAILURE_CODES["DIFF_RETRY_STUCK"],
                failure_codes=failure_code_history,
            )
            return

        patch_errors = [patch_error]
        if attempt == MAX_TRANSLATION_ATTEMPTS:
            print(
                format_failure_header(
                    FAILURE_CODES["DIFF_RETRY_EXHAUSTED"],
                    f"Failed to apply translated diff to {target_file}",
                )
            )
            print(f"  - Last Failure Code: {patch_failure_code}")
            print(f"  - Error: {patch_error}")
            print(f"  - Last Diff Output:\n{translated_diff}")
            update_aggregate_metrics(
                mode="incremental",
                source_filename=source_filename,
                target_lang=target_lang,
                model_name=model,
                attempts_used=attempt,
                success=False,
                max_attempts=MAX_TRANSLATION_ATTEMPTS,
                failure_code=FAILURE_CODES["DIFF_RETRY_EXHAUSTED"],
                failure_codes=failure_code_history,
            )
            return

        retry_feedback = format_retry_feedback(
            "diff-patch-failure",
            attempt,
            patch_errors,
            patch_failure_code,
        )


def translate(filepath, source_lang, target_lang, model, source_filename=None):
    """Translate a full source file and provide source filename as model context.

    Args:
        filepath: Path to the source markdown file
        source_lang: Source language
        target_lang: Target language
        model: Model identifier used for translation
        source_filename: Source filename context (relative to source posts dir)
            used in prompts and output path generation. If None, derived from
            filepath and source_lang.
    """
    if source_filename is None:
        source_filename = get_source_filename(filepath, source_lang)

    system_prompt = TRANSLATION_SYSTEM_PROMPT

    with open(filepath, "r", encoding="utf-8") as f:
        source_markdown = f.read()

    additional_instructions = extract_translation_liquid_comment_instructions(
        source_markdown
    )

    prompt = (
        "<translation_request>\n"
        "<source_markdown>\n"
        f"{source_markdown}\n"
        "</source_markdown>\n"
    )

    temperature = 0

    # Extract hash links and add referenced post content to the prompt
    hash_links = extract_hash_links(prompt)
    if hash_links:
        temperature = 0
        referenced_posts = []
        # print("Extracted hash links:")
        for link_text, post_path, hash_fragment in hash_links:
            # print(f"- {link_text} ({post_path}#{hash_fragment})")
            post_content = get_post_content(post_path, source_lang, target_lang)
            if post_content:
                referenced_posts.append(
                    f'\n\n<referenced_post path="{post_path}" hash="{hash_fragment}">\n{post_content}\n</referenced_post>'
                )

        if referenced_posts:
            prompt += (
                "<reference_context>The following are contents of posts linked with hash fragments in the original post. Use these for context when translating links and references:\n"
                + "".join(referenced_posts)
                + "\n</reference_context>\n"
            )

    prompt += (
        "<runtime_context>\n"
        f"<source_language>{source_lang}</source_language>\n"
        f"<target_language>{target_lang}</target_language>\n"
        f"<source_file_name>{source_filename}</source_file_name>\n"
        "</runtime_context>\n"
    )

    if additional_instructions:
        prompt += (
            "<additional_translation_instructions_from_liquid_comment>\n"
            + "\n\n".join(additional_instructions)
            + "\n</additional_translation_instructions_from_liquid_comment>\n"
            "<additional_instruction_precedence>\n"
            "If these additional translation instructions conflict with base prompt instructions, prioritize the additional translation instructions from Liquid comments.\n"
            "</additional_instruction_precedence>\n"
        )

    prompt += "</translation_request>"

    retry_feedback = ""
    final_output = ""
    previous_failure_code = None
    repeated_failure_count = 0
    failure_code_history = []
    attempt = 0

    for attempt in range(1, MAX_TRANSLATION_ATTEMPTS + 1):
        prompt_with_feedback = prompt + retry_feedback
        model_output = submit_prompt(
            model, prompt_with_feedback, system_prompt, "---", temperature
        )
        if model[:6] == "claude":
            model_output = "---" + model_output

        is_valid_full, full_errors, full_failure_code = (
            validate_full_translation_output(model_output)
        )

        if is_valid_full:
            final_output = model_output
            break

        failure_code_history.append(full_failure_code)
        if full_failure_code == previous_failure_code:
            repeated_failure_count += 1
        else:
            repeated_failure_count = 1
            previous_failure_code = full_failure_code

        if repeated_failure_count >= 2 and attempt < MAX_TRANSLATION_ATTEMPTS:
            print(
                format_failure_header(
                    FAILURE_CODES["FULL_RETRY_EXHAUSTED"],
                    f"Repeated markdown generation failure for {filepath}",
                )
            )
            print(f"  - Last Failure Code: {full_failure_code}")
            for error in full_errors:
                print(f"    - {error}")
            update_aggregate_metrics(
                mode="full",
                source_filename=source_filename,
                target_lang=target_lang,
                model_name=model,
                attempts_used=attempt,
                success=False,
                max_attempts=MAX_TRANSLATION_ATTEMPTS,
                failure_code=FAILURE_CODES["FULL_RETRY_EXHAUSTED"],
                failure_codes=failure_code_history,
            )
            return

        if attempt == MAX_TRANSLATION_ATTEMPTS:
            print(
                format_failure_header(
                    FAILURE_CODES["FULL_RETRY_EXHAUSTED"],
                    f"Failed to generate valid markdown translation for {filepath}",
                )
            )
            print(f"  - Last Failure Code: {full_failure_code}")
            print("  - Validation Errors:")
            for error in full_errors:
                print(f"    - {error}")
            print(f"  - Last Output:\n{model_output}")
            update_aggregate_metrics(
                mode="full",
                source_filename=source_filename,
                target_lang=target_lang,
                model_name=model,
                attempts_used=attempt,
                success=False,
                max_attempts=MAX_TRANSLATION_ATTEMPTS,
                failure_code=FAILURE_CODES["FULL_RETRY_EXHAUSTED"],
                failure_codes=failure_code_history,
            )
            return

        retry_feedback = format_retry_feedback(
            "full-translation",
            attempt,
            full_errors,
            full_failure_code,
        )

    result_text = final_output + "\n"

    # print(language_code[target_lang])
    filename = source_filename
    # print(filename)
    result_file = "../_posts/" + lang_code[target_lang] + "/" + filename
    # print(result_file)
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(result_text)
    update_aggregate_metrics(
        mode="full",
        source_filename=source_filename,
        target_lang=target_lang,
        model_name=model,
        attempts_used=attempt,
        success=True,
        max_attempts=MAX_TRANSLATION_ATTEMPTS,
        failure_code=None,
        failure_codes=failure_code_history,
    )
    # print(result_text)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file-path", type=Path, help="Path of the text file to translate"
    )
    parser.add_argument(
        "-s",
        "--source",
        type=str,
        help="The language of the source text you want to translate",
    )
    parser.add_argument(
        "-t", "--target", type=str, help="The language of translation output"
    )
    args = parser.parse_args()

    source_lang = args.source
    target_lang = args.target

    print(f"Translating {args.file_path}")
    print(f"source_lang: {source_lang}, target_lang: {target_lang}:")
    translate(args.file_path, source_lang, target_lang, "gpt-5.4-2026-03-05")
    print("Completed the requested task.")
