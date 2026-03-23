# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
# ]
# ///
import sys
import os
import logging
import argparse
from pathlib import Path
from tqdm import tqdm
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

LOGS_DIR = Path(__file__).resolve().parent / "logs"
SCRIPT_LOG_FILE = LOGS_DIR / "translate_all.log"

_SCRIPT_LOGGER = None


def ensure_logs_dir():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


def get_script_logger():
    global _SCRIPT_LOGGER
    if _SCRIPT_LOGGER is not None:
        return _SCRIPT_LOGGER

    ensure_logs_dir()
    logger = logging.getLogger("translate_all")
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Translate blog posts from source language to target languages."
    )
    parser.add_argument(
        "--override",
        action="store_true",
        help="Overwrite existing translated files. Without this flag, existing files are skipped.",
    )
    args = parser.parse_args()

    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    source_dir = os.path.join(posts_dir, source_lang_code)
    filelist = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if is_valid_file(file):  # 유효한 파일만 추가
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, start=source_dir)
                filelist.append(relative_path)

    if not filelist:
        sys.exit("No files to translate.")

    files_to_translate = []
    skipped_files = []

    for file in filelist:
        file_needs_translation = False
        for target_lang in target_langs:
            target_lang_code = prompt.lang_code.get(target_lang)
            if target_lang_code:
                target_file_path = f"../_posts/{target_lang_code}/{file}"
                if not os.path.exists(target_file_path) or args.override:
                    file_needs_translation = True
                else:
                    skipped_files.append((file, target_lang))
        if file_needs_translation:
            files_to_translate.append(file)

    skipped_by_file = {}
    for file, target_lang in skipped_files:
        if file not in skipped_by_file:
            skipped_by_file[file] = []
        skipped_by_file[file].append(target_lang)

    if skipped_by_file and not args.override:
        print("The following files already exist and will be skipped:")
        for file, langs in skipped_by_file.items():
            print(f"- {file} ({', '.join(langs)})")
        print("")

    if not files_to_translate:
        print("No files need translation (all target files already exist).")
        print("Use --override to force re-translation of existing files.")
        sys.exit(0)

    get_script_logger().info(
        "Full translation run started files=%s (skipped=%s)",
        len(files_to_translate),
        len(skipped_files),
    )

    print("These files will be translated:")
    for file in files_to_translate:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    model = "gpt-5.4-2026-03-05"
    # 외부 루프: 전체 파일 진행상황
    for file in tqdm(files_to_translate, desc="Files", position=0):
        filepath = os.path.join(source_dir, file)
        # 내부 루프: 각 파일의 언어별 번역 진행상황
        for target_lang in tqdm(
            target_langs, desc="Languages", position=1, leave=False
        ):
            target_lang_code = prompt.lang_code.get(target_lang)
            if target_lang_code:
                target_file_path = f"../_posts/{target_lang_code}/{file}"
                if os.path.exists(target_file_path) and not args.override:
                    continue
                prompt.translate(
                    filepath,
                    source_lang,
                    target_lang,
                    model,
                    source_filename=file,
                )

    print("\nTranslation completed!")
    if skipped_files and not args.override:
        print(
            f"Skipped {len(skipped_files)} existing translations (use --override to re-translate)."
        )
    get_script_logger().info("Full translation run completed")
    os.chdir(initial_wd)
