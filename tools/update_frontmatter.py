import sys
import os
from tqdm import tqdm
import compare_hash
import frontmatter
import yaml

posts_dir = '../_posts/'
source_lang_code = "ko"
list_lang_codes = ["en", "es", "pt-BR", "ja", "fr", "de"]
exclude_keys = ["title", "description"]

class InlineSeqDumper(yaml.SafeDumper):
    """Custom Dumper that forces all lists to be inline."""
    pass

def inline_list_representer(dumper, data):
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)

InlineSeqDumper.add_representer(list, inline_list_representer)

def reorder_metadata(post):
    """
    Reorder post.metadata so that 'title', 'description',
    'categories', 'tags' appear first, followed by any remaining keys.
    """

    new_metadata = {}

    # 1. Add the four fields in fixed order if they exist
    for key in ["title", "description", "categories", "tags"]:
        if key in post.metadata:
            new_metadata[key] = post.metadata[key]

    # 2. Add remaining keys in original order
    for key in post.metadata:
        if key not in new_metadata:
            new_metadata[key] = post.metadata[key]

    # 3. Assign it back
    post.metadata = new_metadata

def read_frontmatter(file_path):
    """
    Reads the YAML frontmatter from a Markdown file.

    Args:
        file_path (str): Path to the Markdown file.

    Returns:
        dict: Parsed YAML frontmatter as a dictionary.
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
    excluding specified keys.

    Args:
        target_file_path (str): Path to the target Markdown file.
        new_frontmatter (dict): New YAML frontmatter data.
    """
    try:
        # Read the existing content and frontmatter
        with open(target_file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        # Preserve existing values for excluded keys
        for key in exclude_keys:
            if key in post.metadata:
                new_frontmatter[key] = post.metadata[key]

        # Update the frontmatter except the excluded keys
        post.metadata = new_frontmatter
        reorder_metadata(post)  # enforce the desired key order

        # Now dump the frontmatter with inline lists
        yaml_part = yaml.dump(post.metadata, sort_keys=False, Dumper=InlineSeqDumper)
        # Combine the YAML part with the content
        updated_post_str = f"---\n{yaml_part}---\n{post.content}"

        with open(target_file_path, 'w', encoding='utf-8') as f:
            f.write(updated_post_str)

        print(f"Successfully updated frontmatter for {target_file_path}")
    except FileNotFoundError:
        print(f"Warning: The file {target_file_path} does not exist. Skipping.")
    except Exception as e:
        print(f"Error writing to {target_file_path}: {e}")

def update_frontmatter_bulk(filename):
    source_path = os.path.join(posts_dir, source_lang_code, filename)
    source_frontmatter = read_frontmatter(source_path)

    if source_frontmatter is None:
        print("Aborting operation due to previous errors.")
        return

    # Strip out excluded keys from the *source* so we don't overwrite them
    filtered_frontmatter = {
        k: v for k, v in source_frontmatter.items() 
        if k not in exclude_keys
    }

    # Iterate through each language code and update the frontmatter
    for lang_code in list_lang_codes:
        target_path = os.path.join(posts_dir, lang_code, filename)
        overwrite_frontmatter(target_path, filtered_frontmatter)

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files()
    if not changed_files:
        sys.exit("No files have changed.")

    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("\n*** Overwriting frontmatter! ***")
    for changed_file in tqdm(changed_files):
        update_frontmatter_bulk(changed_file)

    os.chdir(initial_wd)