import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

posts_dir = '../_posts/ko/'
source_lang = "Korean"
target_langs = ["English", "Spanish", "Brazilian Portuguese", "Japanese", "French", "German"]

if __name__ == "__main__":
    filelist = []
    for root, _, files in os.walk(posts_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=posts_dir)
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
        filepath = os.path.join(posts_dir, file)
        for target_lang in tqdm(target_langs):
            prompt.translate(filepath, source_lang, target_lang)
