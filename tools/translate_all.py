import sys
import os
from tqdm import tqdm
import prompt

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Spanish", "Brazilian Portuguese", "Japanese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "es", "pt-BR", "ja", "fr", "de"]

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    source_dir = os.path.join(posts_dir, source_lang_code)
    filelist = []
    for root, _, files in os.walk(source_dir):
        for file in files:
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
    for file in filelist:
        print(f"- Translating {file}")
        filepath = os.path.join(source_dir, file)
        for target_lang in tqdm(target_langs):
            prompt.translate(filepath, source_lang, target_lang)

    os.chdir(initial_wd)
