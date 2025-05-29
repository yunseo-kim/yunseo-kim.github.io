# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
# ]
# ///
import sys
import os
from tqdm import tqdm
import prompt

def is_valid_file(filename):
    # 제외할 파일 패턴들
    excluded_patterns = [
        '.DS_Store',  # macOS 시스템 파일
        '~',          # 임시 파일
        '.tmp',       # 임시 파일
        '.temp',      # 임시 파일
        '.bak',       # 백업 파일
        '.swp',       # vim 임시 파일
        '.swo'        # vim 임시 파일
    ]
    
    # 파일명이 제외 패턴 중 하나라도 포함하면 False 반환
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin","Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

if __name__ == "__main__":
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

    print("These files will be translated:")
    for file in filelist:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    # 외부 루프: 전체 파일 진행상황
    for file in tqdm(filelist, desc="Files", position=0):
        filepath = os.path.join(source_dir, file)
        # 내부 루프: 각 파일의 언어별 번역 진행상황
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
        
    print("\nTranslation completed!")
    os.chdir(initial_wd)
