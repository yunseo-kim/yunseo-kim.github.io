# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "python-frontmatter",
#     "pyyaml",
#     "tqdm",
# ]
# ///
import sys
import os
from tqdm import tqdm
import compare_hash
import frontmatter
import yaml

posts_dir = '../_posts/'
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
exclude_keys = ["title", "description"]

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
# 3) Standard read_frontmatter and overwrite_frontmatter logic
###############################################################################
def read_frontmatter(file_path):
    """
    Reads the YAML frontmatter from a Markdown file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        return post.metadata
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def overwrite_frontmatter(target_file_path, new_frontmatter):
    """
    Overwrites the YAML frontmatter of a Markdown file with new data,
    excluding specified keys, and dumps in a custom format.
    """
    try:
        # Read the existing content and frontmatter
        with open(target_file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        # Preserve excluded keys from the target
        for key in exclude_keys:
            if key in post.metadata:
                new_frontmatter[key] = post.metadata[key]

        # Update the post's metadata
        post.metadata = new_frontmatter
        reorder_metadata(post)  # enforce the desired key order

        # Dump to YAML with our custom dumper rules
        #   allow_unicode=True -> don't escape non-ASCII
        yaml_part = yaml.dump(
            post.metadata,
            sort_keys=False,
            Dumper=CustomDumper,
            allow_unicode=True
        )

        # Construct the final Markdown content
        updated_post_str = f"---\n{yaml_part}---\n{post.content}\n"

        with open(target_file_path, 'w', encoding='utf-8') as f:
            f.write(updated_post_str)

        # print(f"Successfully updated frontmatter for {target_file_path}")

    except FileNotFoundError:
        print(f"Warning: The file {target_file_path} does not exist. Skipping.")
    except Exception as e:
        print(f"Error writing to {target_file_path}: {e}")


def update_frontmatter_bulk(filename):
    """
    Reads the YAML frontmatter from the source_lang_code version
    of the file, updates each translation's frontmatter, excluding
    certain keys.
    """
    # Define the source path (assuming 'ko' is the source language)
    source_path = os.path.join(posts_dir, source_lang_code, filename)

    # Read the frontmatter from the source file
    source_frontmatter = read_frontmatter(source_path)
    if source_frontmatter is None:
        print("Aborting operation due to previous errors.")
        return

    # Remove excluded keys from the source frontmatter
    filtered_frontmatter = {
        k: v for k, v in source_frontmatter.items() if k not in exclude_keys
    }

    # Overwrite for each language
    for lang_code in target_lang_codes:
        target_path = os.path.join(posts_dir, lang_code, filename)
        overwrite_frontmatter(target_path, filtered_frontmatter)


###############################################################################
# 4) Main script flow
###############################################################################
if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("\n*** Overwriting frontmatter! ***")
    for changed_file in tqdm(changed_files):
        update_frontmatter_bulk(changed_file)

    os.chdir(initial_wd)