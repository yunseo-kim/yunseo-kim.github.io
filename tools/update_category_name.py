#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "python-frontmatter",
#     "pyyaml",
# ]
# ///
import os
import sys
import frontmatter
import yaml

###############################################################################
# 1) Define a custom YAML dumper that:
#    - Prints all lists in inline style: [item1, item2]
#    - Does not escape non-ASCII characters
#    - Uses folded block style (">-") for multiline strings
###############################################################################
class CustomDumper(yaml.SafeDumper):
    """
    Custom PyYAML dumper that:
      - Prints all lists in inline style ([item1, item2])
      - Allows non-ASCII characters (no escaping)
      - Folds multiline strings with the style ">-"
    """
    pass

def inline_list_representer(dumper, data):
    """
    Force all Python lists into inline style, e.g.:
        categories: [cat1, cat2]
    """
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)

def folded_multiline_str_representer(dumper, data):
    """
    Represent multiline strings in folded block style ">-".
    Single-line strings remain unquoted unless needed.
    """
    if '\n' in data:
        # Use folded style only if there's an actual newline
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='>-')
    else:
        # For single-line strings, let PyYAML decide automatically
        # or use a plain style if you prefer unquoted:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

# Register our custom representers
CustomDumper.add_representer(list, inline_list_representer)
CustomDumper.add_representer(str, folded_multiline_str_representer)

###############################################################################
# 2) Reordering logic to ensure frontmatter keys appear in the specified order
###############################################################################
def reorder_metadata(post):
    """
    Reorder the post.metadata so that 'title', 'description',
    'categories', 'tags' appear first, followed by any other keys.
    
    Note: In Python 3.7+, regular dicts preserve insertion order.
    """
    desired_order = ["title", "description", "categories", "tags"]
    new_metadata = {}

    # First, add the keys in the desired order (if they exist)
    for key in desired_order:
        if key in post.metadata:
            new_metadata[key] = post.metadata[key]

    # Then add the remaining keys in their original order
    for key in post.metadata:
        if key not in new_metadata:
            new_metadata[key] = post.metadata[key]

    post.metadata = new_metadata

###############################################################################
# 3) Logic to update categories
###############################################################################
def update_categories_in_file(filepath, old_category, new_category):
    """
    파일의 YAML 프론트매터 내 categories 값을 검사하여,
    기존 카테고리와 일치하는 경우 새 카테고리로 변경합니다.
    
    - categories 값이 리스트인 경우 각 항목을 검사하여 변경
    - 문자열인 경우 정확히 일치하면 변경
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
    except Exception as e:
        print(f"파일 읽기 오류({filepath}): {e}")
        return False

    changed = False
    if 'categories' in post.metadata:
        cat_val = post.metadata['categories']
        if isinstance(cat_val, list):
            new_list = []
            for cat in cat_val:
                if cat == old_category:
                    new_list.append(new_category)
                    changed = True
                else:
                    new_list.append(cat)
            post.metadata['categories'] = new_list
        elif isinstance(cat_val, str):
            if cat_val == old_category:
                post.metadata['categories'] = new_category
                changed = True

    # 변경이 이루어졌다면 메타데이터 순서 재정렬 후 인라인 리스트 형식으로 덮어쓰기
    if changed:
        try:
            reorder_metadata(post)
            yaml_str = yaml.dump(
                post.metadata, 
                sort_keys=False, 
                Dumper=CustomDumper,
                allow_unicode=True
            )
            updated_post_str = f"---\n{yaml_str}---\n{post.content}\n"
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_post_str)
        except Exception as e:
            print(f"파일 쓰기 오류({filepath}): {e}")
            return False
    return changed

def main():
    if len(sys.argv) != 3:
        print("사용법: python update_categories.py <기존 카테고리> <새 카테고리>")
        sys.exit(1)

    old_category = sys.argv[1]
    new_category = sys.argv[2]

    # 변경할 파일들이 위치한 디렉터리: ../_posts
    posts_dir = "../_posts"
    updated_files = []

    # ../_posts 디렉터리 및 하위 디렉터리 내의 .md, .markdown 파일 탐색
    for root, dirs, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md') or file.endswith('.markdown'):
                filepath = os.path.join(root, file)
                if update_categories_in_file(filepath, old_category, new_category):
                    updated_files.append(filepath)
                    print(f"변경됨: {filepath}")

    print(f"\n총 {len(updated_files)}개의 파일에서 카테고리를 변경하였습니다.")

if __name__ == "__main__":
    main()