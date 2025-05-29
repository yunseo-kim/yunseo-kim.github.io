#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "python-frontmatter",
#     "tqdm",
# ]
# ///
import sys
import os
import re
from tqdm import tqdm
import frontmatter

# 디렉토리 및 언어 설정
posts_dir = '../_posts/'
source_lang_code = "ko"
list_lang_codes = ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

def convert_image_extension_to_webp(image_path):
    """
    기존 이미지 경로는 유지하되 확장자만 .png, .jpg, .jpeg에서 .webp로 변경
    """
    if not image_path:
        return None
    base, ext = os.path.splitext(image_path)
    if ext.lower() in [".png", ".jpg", ".jpeg"]:
        return f"{base}.webp"
    return image_path

# frontmatter에서 image 값을 읽고, 파일 내 image: 라인만 교체
def overwrite_frontmatter_image_only(file_path):
    """
    파일의 YAML frontmatter에서 image: 라인을 찾고,
    확장자를 변경하여 파일에 다시 씁니다.
    """
    try:
        # 메타데이터 읽기
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        orig_image = post.metadata.get('image')
        new_image = convert_image_extension_to_webp(orig_image)
        if orig_image and new_image != orig_image:
            # 파일 전체 텍스트 로드
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            # image: 라인만 교체
            updated = re.sub(
                r'(?m)^(\s*image:\s*).+$',
                fr"\1{new_image}",
                text
            )
            # 덮어쓰기
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def update_frontmatter_bulk(filename):
    """
    Bulk update YAML Frontmatter.
    """
    paths = [
        os.path.join(posts_dir, lang, filename)
        for lang in list_lang_codes
    ]
    for path in paths:
        if os.path.isfile(path):
            overwrite_frontmatter_image_only(path)


if __name__ == "__main__":
    # 스크립트 위치로 이동
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    source_dir = os.path.join(posts_dir, source_lang_code)
    filelist = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file == ".DS_Store":
                continue
            rel = os.path.relpath(os.path.join(root, file), start=source_dir)
            filelist.append(rel)

    if not filelist:
        sys.exit("No files found.")

    print("Updating image extensions to .webp for the following files:")
    for f in filelist:
        print(f"- {f}")

    for f in tqdm(filelist):
        update_frontmatter_bulk(f)
