import sys
import os
from tqdm import tqdm
import compare_hash
import frontmatter

posts_dir = '../_posts/'
source_lang_code = "ko"

# Define the list of language codes
list_lang_codes = ["en", "es", "pt-BR", "ja", "fr", "de"]

# Define the attributes to exclude from overwriting
exclude_keys = ["title", "description"]

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
            elif key not in new_frontmatter:
                # If the key doesn't exist in new_frontmatter and not in target, ensure it's not added
                pass

        # Update the frontmatter except the excluded keys
        post.metadata = new_frontmatter

        # Write back to the file
        with open(target_file_path, 'w', encoding='utf-8') as f:
            frontmatter.dump(post, f)

        print(f"Successfully updated frontmatter for {target_file_path}")
    except FileNotFoundError:
        print(f"Warning: The file {target_file_path} does not exist. Skipping.")
    except Exception as e:
        print(f"Error writing to {target_file_path}: {e}")

def update_frontmatter_bulk(filename):
    """
    Reads the YAML frontmatter from the Korean version of the file and
    overwrites the frontmatter of the file in each specified language directory,
    excluding certain keys.

    Args:
        filename (str): Name of the Markdown file (e.g., 'example-file.md').
    """
    # Define the source path (assuming Korean is the source language)
    source_path = os.path.join(posts_dir, source_lang_code, filename)

    # Read the frontmatter from the source file
    source_frontmatter = read_frontmatter(source_path)

    if source_frontmatter is None:
        print("Aborting operation due to previous errors.")
        return

    # Remove excluded keys from the source frontmatter
    filtered_frontmatter = {k: v for k, v in source_frontmatter.items() if k not in exclude_keys}

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
    
    print("")
    print("*** Overwriting frontmatter! ***")
    for changed_file in tqdm(changed_files):
        update_frontmatter_bulk(changed_file)
    
    os.chdir(initial_wd)
