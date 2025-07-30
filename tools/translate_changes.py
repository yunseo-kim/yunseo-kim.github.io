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
from tqdm import tqdm
import compare_hash
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
target_langs = ["English", "Japanese", "Taiwanese Mandarin", "Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"

def get_git_diff(filepath):
    """Get the diff of the file using git"""
    try:
        # Get the diff of the file
        result = subprocess.run(
            ['git', 'diff', '--unified=0', '--no-color', '--', filepath],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting git diff: {e}")
        return None

def translate_incremental(filepath, source_lang, target_lang, model):
    """Translate only the changed parts of a file using git diff"""
    # Get the git diff
    diff_output = get_git_diff(filepath)
    # print(f"Diff output: {diff_output}")
    if not diff_output:
        print(f"No changes detected or error getting diff for {filepath}")
        return
    
    # Call the translation function with the diff
    prompt.translate_with_diff(filepath, source_lang, target_lang, diff_output, model)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Translate markdown files with optional incremental updates')
    parser.add_argument('--incremental', action='store_true', 
                       help='Only translate changed parts of files using git diff')
    args, _ = parser.parse_known_args()
    
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    # Filter temporary files
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No files have changed.")
        
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    
    # Outer loop: Progress through changed files
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        
        # Inner loop: Progress through target languages
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            model = "gemini-2.5-pro" if target_lang in ["English", "Taiwanese Mandarin", "German"] else "claude-sonnet-4-20250514"
            if args.incremental:
                translate_incremental(filepath, source_lang, target_lang, model)
            else:
                prompt.translate(filepath, source_lang, target_lang, model)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
