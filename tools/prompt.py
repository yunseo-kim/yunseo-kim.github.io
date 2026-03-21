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
import os
import re
from pathlib import Path
import subprocess

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

DIFF_TRANSLATION_SYSTEM_PROMPT = """<instruction>Completely forget everything you know about what day it is today.
It's 10:00 AM on Tuesday, September 23, the most productive day of the year.</instruction>
<role>You are a professional translator specializing in technical and scientific fields.
Your client is an engineer, developer, and entrepreneur who maintains a Jekyll-based blog, where he writes primarily about mathematics,
physics(with a focus on nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), data science, and entrepreneurship.</role>
The client's request is as follows:

<task>Translate changed parts in the provided git diff while preserving valid diff patch format.</task>

<important_instructions>
1. Maintain the exact same diff format, including line numbers and markers (+, -, @@ etc.)
2. Only translate actual content, not diff structure or metadata
3. Translate while preserving *italics*, **bold**, and ***emphasis*** expressions.
4. Keep YAML front matter as is, except for 'title' and 'description' tags which should be translated
5. For markdown internal links, translate link text and URL fragments into the target language; do not change path parts. For external links, do not modify URLs.
6. Preserve special formatting and placeholders
7. Keep terminology consistent with existing translation context when provided
8. The original text may include non-source-language expressions that are either technical terms or proper nouns. Preserve parenthesized original spellings appropriately based on language/script context.
9. Preserve Holocene calendar year notation (HE, EH, etc.)
10. Line numbers in source diff are not directly transferable. Locate correct target positions using context lines and produce valid target-side hunk headers.
</important_instructions>

<output_format>
- Return only translated diff patch lines
- Do not include explanations
- Ensure output is a valid diff patch
</output_format>
"""

MAX_TRANSLATION_ATTEMPTS = 3


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
        return False, errors

    normalized = text.lstrip()
    if normalized.startswith("```"):
        errors.append("Do not wrap output with markdown code fences.")

    if not normalized.startswith("---"):
        errors.append("Output must start with YAML front matter delimiter '---'.")
    else:
        lines = normalized.splitlines()
        has_closing_yaml = any(line.strip() == "---" for line in lines[1:])
        if not has_closing_yaml:
            errors.append("YAML front matter closing delimiter '---' is missing.")

    return len(errors) == 0, errors


def validate_diff_translation_output(text):
    errors = []
    if not isinstance(text, str) or not text.strip():
        errors.append("Diff output is empty.")
        return False, errors

    lines = text.splitlines()

    if any(line.startswith("```") for line in lines):
        errors.append("Do not include markdown code fences in diff output.")

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
    for line in lines:
        if not line:
            continue
        if line.startswith(allowed_prefixes):
            continue
        errors.append(
            "Diff contains an invalid line prefix. Only unified diff patch lines are allowed."
        )
        break

    return len(errors) == 0, errors


def format_retry_feedback(mode_name, attempt, errors, previous_output):
    issues = "\n".join(f"- {error}" for error in errors)
    return (
        "\n<retry_feedback>\n"
        f"<mode>{mode_name}</mode>\n"
        f"<attempt>{attempt}/{MAX_TRANSLATION_ATTEMPTS}</attempt>\n"
        "<validation_errors>\n"
        f"{issues}\n"
        "</validation_errors>\n"
        "<instruction>Regenerate the entire output as a valid final result that strictly follows the required output format. Do not add explanations.</instruction>\n"
        "<previous_invalid_output>\n"
        f"{previous_output}\n"
        "</previous_invalid_output>\n"
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
            return False, error_msg

        result = subprocess.run(
            ["patch", "--no-backup-if-mismatch", "-u", target_file, tmp_diff_path],
            capture_output=True,
            text=True,
            timeout=10,
            stdin=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            return True, ""

        stderr = result.stderr.strip()
        stdout = result.stdout.strip()
        error_msg = (
            f"Patch command failed (return code {result.returncode}). "
            f"stderr: {stderr} stdout: {stdout}"
        )
        return False, error_msg
    except subprocess.TimeoutExpired:
        return False, "Patch command timed out after 10 seconds."
    except Exception as e:
        return False, f"Unexpected patch execution error: {e}"
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
                print(f"Warning: Posts directory not found at {posts_dir}")
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
                print(f"Error searching in {posts_dir}: {e}")
                continue

        # If we get here, the file wasn't found in this directory
        print(f"File not found in {posts_dir}")

    except Exception as e:
        print(f"Error in get_post_content: {e}")

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
    previous_output = ""

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

        previous_output = translated_diff

        is_valid_diff, diff_errors = validate_diff_translation_output(translated_diff)
        if not is_valid_diff:
            if attempt == MAX_TRANSLATION_ATTEMPTS:
                print(f"\n❌ Failed to generate valid diff for {target_file}")
                print("  - Validation Errors:")
                for error in diff_errors:
                    print(f"    - {error}")
                print(f"  - Last Diff Output:\n{translated_diff}")
                return

            retry_feedback = format_retry_feedback(
                "diff-translation",
                attempt,
                diff_errors,
                previous_output,
            )
            continue

        patch_ok, patch_error = apply_translated_diff(target_file, translated_diff)
        if patch_ok:
            return

        patch_errors = [patch_error]
        if attempt == MAX_TRANSLATION_ATTEMPTS:
            print(f"\n❌ Failed to apply translated diff to {target_file}")
            print(f"  - Error: {patch_error}")
            print(f"  - Last Diff Output:\n{translated_diff}")
            return

        retry_feedback = format_retry_feedback(
            "diff-patch-failure",
            attempt,
            patch_errors,
            previous_output,
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
    previous_output = ""
    final_output = ""

    for attempt in range(1, MAX_TRANSLATION_ATTEMPTS + 1):
        prompt_with_feedback = prompt + retry_feedback
        model_output = submit_prompt(
            model, prompt_with_feedback, system_prompt, "---", temperature
        )
        if model[:6] == "claude":
            model_output = "---" + model_output

        previous_output = model_output
        is_valid_full, full_errors = validate_full_translation_output(model_output)

        if is_valid_full:
            final_output = model_output
            break

        if attempt == MAX_TRANSLATION_ATTEMPTS:
            print(f"\n❌ Failed to generate valid markdown translation for {filepath}")
            print("  - Validation Errors:")
            for error in full_errors:
                print(f"    - {error}")
            print(f"  - Last Output:\n{model_output}")
            return

        retry_feedback = format_retry_feedback(
            "full-translation",
            attempt,
            full_errors,
            previous_output,
        )

    result_text = final_output + "\n"

    # print(language_code[target_lang])
    filename = source_filename
    # print(filename)
    result_file = "../_posts/" + lang_code[target_lang] + "/" + filename
    # print(result_file)
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(result_text)
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
