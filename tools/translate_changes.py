# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
#     "argparse",
# ]
# ///
import sys
import os
import subprocess
import logging
from pathlib import Path
from tqdm import tqdm
import compare_hash
import prompt


def is_valid_file(filename):
    # 제외할 파일 패턴들
    excluded_patterns = [
        ".DS_Store",  # macOS 시스템 파일
        "~",  # 임시 파일
        ".tmp",  # 임시 파일
        ".temp",  # 임시 파일
        ".bak",  # 백업 파일
        ".swp",  # vim 임시 파일
        ".swo",  # vim 임시 파일
    ]

    # 파일명이 제외 패턴 중 하나라도 포함하면 False 반환
    return not any(pattern in filename for pattern in excluded_patterns)


posts_dir = "../_posts/"
source_lang = "Korean"
target_langs = [
    "English",
    "Japanese",
    "Traditional Chinese (Taiwan)",
    "Spanish",
    "Brazilian Portuguese",
    "French",
    "German",
    "Polish",
    "Czech",
    "Swahili",
    "Amharic",
]
source_lang_code = "ko"

FAILURE_CODES = {
    "GIT_DIFF_COMMAND_FAILED": "GIT_DIFF_COMMAND_FAILED",
    "GIT_DIFF_EMPTY_OR_UNCHANGED": "GIT_DIFF_EMPTY_OR_UNCHANGED",
}

LOGS_DIR = Path(__file__).resolve().parent / "logs"
SCRIPT_LOG_FILE = LOGS_DIR / "translate_changes.log"

_SCRIPT_LOGGER = None


def ensure_logs_dir():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


def get_script_logger():
    global _SCRIPT_LOGGER
    if _SCRIPT_LOGGER is not None:
        return _SCRIPT_LOGGER

    ensure_logs_dir()
    logger = logging.getLogger("translate_changes")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.FileHandler(SCRIPT_LOG_FILE, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s", "%Y-%m-%dT%H:%M:%S%z"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    _SCRIPT_LOGGER = logger
    return _SCRIPT_LOGGER


def format_failure_header(code, message):
    get_script_logger().error("[%s] %s", code, message)
    return f"\n❌ [{code}] {message}"


def get_git_diff(filepath):
    """Get the diff of the file using git"""
    try:
        # Get the diff of the file
        result = subprocess.run(
            ["git", "diff", "--no-color", "--", filepath],
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except Exception as e:
        print(
            format_failure_header(
                FAILURE_CODES["GIT_DIFF_COMMAND_FAILED"],
                f"Error getting git diff for {filepath}",
            )
        )
        print(f"  - Error: {e}")
        return None


def translate_incremental(filepath, source_lang, target_lang, model, source_filename):
    """Translate only changed parts using git diff with filename context metadata.

    Args:
        filepath: Path to the source file
        source_lang: Source language
        target_lang: Target language
        model: Model identifier used for translation
        source_filename: Source filename context (relative to source posts dir)
            passed to prompt.translate_with_diff.
    """
    # Get the git diff
    diff_output = get_git_diff(filepath)
    # print(f"Diff output: {diff_output}")
    if not diff_output:
        print(
            format_failure_header(
                FAILURE_CODES["GIT_DIFF_EMPTY_OR_UNCHANGED"],
                f"No incremental diff available for {filepath}",
            )
        )
        print(
            "  - Reason: No changes detected, file unchanged, or diff retrieval failed."
        )
        return

    # Call the translation function with the diff
    prompt.translate_with_diff(
        filepath,
        source_lang,
        target_lang,
        diff_output,
        model,
        source_filename=source_filename,
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Translate markdown files with optional incremental updates"
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        help="Only translate changed parts of files using git diff",
    )
    args, _ = parser.parse_known_args()

    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    # Filter temporary files
    changed_files = [f for f in changed_files if is_valid_file(f)]

    if not changed_files:
        sys.exit("No files have changed.")

    get_script_logger().info(
        "Translation run started incremental=%s changed_files=%s",
        args.incremental,
        len(changed_files),
    )

    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")

    model = "gpt-5.4-2026-03-05"  # model = "gemini-2.5-pro" if target_lang in ["English", "Traditional Chinese (Taiwan)", "German"] else "claude-sonnet-4-20250514"

    # Outer loop: Progress through changed files
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)

        # Inner loop: Progress through target languages
        for target_lang in tqdm(
            target_langs, desc="Languages", position=1, leave=False
        ):
            if args.incremental:
                translate_incremental(
                    filepath,
                    source_lang,
                    target_lang,
                    model,
                    source_filename=changed_file,
                )
            else:
                prompt.translate(
                    filepath,
                    source_lang,
                    target_lang,
                    model,
                    source_filename=changed_file,
                )

    print("\nTranslation completed!")
    get_script_logger().info("Translation run completed")
    os.chdir(initial_wd)
