# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
# ]
# ///
import sys
import os
from tqdm import tqdm
import update_frontmatter

posts_dir = '../_posts/'
source_lang_code = "ko"
list_lang_codes = ["en", "es", "pt-BR", "ja", "fr", "de"]
exclude_keys = ["title", "description"]

# A function to decide the 'image' attribute based on categories and tags
def get_image_for_post(metadata):
    """
    Returns an image path based on categories/tags rules:
      - If categories has "AI & Data" or "Programming":
          "/assets/img/technology.jpg"
      - If categories has "Nuclear Engineering":
          - If tags has "Plasma Physics" or "Fusion Power":
              "/assets/img/tokamak-plasma-cropped.png"
            else:
              "/assets/img/atoms.png"
      - If tags has "Quantum Mechanics":
          "/assets/img/schrodinger-cat-cropped.png"
      - Else:
          "/assets/img/math-and-physics-cropped.png"
    """

    # Safely convert categories and tags to lists
    categories = metadata.get("categories", [])
    if isinstance(categories, str):
        categories = [categories]

    tags = metadata.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]

    # 1. AI & Markdown or Programming
    if any(cat in ["AI & Data", "Programming"] for cat in categories):
        return "/assets/img/technology.jpg"

    # 2. Nuclear Engineering
    if "Nuclear Engineering" in categories:
        # If tags have "Plasma Physics" or "Fusion Power"
        if any(t in ["Plasma Physics", "Fusion Power"] for t in tags):
            return "/assets/img/tokamak-plasma-cropped.png"
        else:
            return "/assets/img/atoms.png"

    # 3. Modern Physics
    if "Quantum Mechanics" in tags:
        return "/assets/img/schrodinger-cat-cropped.png"

    # 4. Default
    return "/assets/img/math-and-physics-cropped.png"

def update_frontmatter_bulk(filename):
    """
    Reads the YAML frontmatter from the 'ko' version (source_lang_code) and
    overwrites the frontmatter in each language directory, excluding certain keys,
    then sets 'image' based on categories/tags.
    """
    source_path = os.path.join(posts_dir, source_lang_code, filename)
    source_frontmatter = update_frontmatter.read_frontmatter(source_path)
    if source_frontmatter is None:
        print("Aborting operation due to previous errors.")
        return

    # Remove excluded keys from the *source* so we don't overwrite them
    filtered_frontmatter = {
        k: v for k, v in source_frontmatter.items() if k not in exclude_keys
    }

    filtered_frontmatter["image"] = get_image_for_post(filtered_frontmatter)

    # Overwrite each translation file
    target_path = os.path.join(posts_dir, source_lang_code, filename)
    update_frontmatter.overwrite_frontmatter(target_path, filtered_frontmatter)
    for lang_code in list_lang_codes:
        target_path = os.path.join(posts_dir, lang_code, filename)
        update_frontmatter.overwrite_frontmatter(target_path, filtered_frontmatter)

# Main script flow
if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    source_dir = os.path.join(posts_dir, source_lang_code)
    filelist = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=source_dir)
            if relative_path == ".DS_Store":
                continue
            filelist.append(relative_path)

    if not filelist:
        sys.exit("No files to translate.")

    print("These files will be translated:")
    for file in filelist:
        print(f"- {file}")

    print("\n*** Assigning 'image' attribute ***")
    for file in tqdm(filelist):
        update_frontmatter_bulk(file)

    os.chdir(initial_wd)