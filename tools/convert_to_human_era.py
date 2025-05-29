#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
# ]
# ///
import os
import re
from tqdm import tqdm

# Advanced regex pattern for file content candidate matching:
# Matches a 4-digit number (not preceded or followed by another digit)
# optionally followed by either a date separator pattern (e.g. .03.26 or /03/26)
# or by a Korean suffix such as "년" or "년도"
advanced_pattern = re.compile(
    r'(?:(?<!\d)(\d{4})((?:[./]\d{1,2}[./]\d{1,2})|\s*년(?:도)?)?(?!\d)|(\d{1,2})세기)'
)

# Simple regex pattern for file name conversion (only standalone 4-digit number)
simple_pattern = re.compile(r'\b(\d{4})\b')

def convert_advanced(match):
    """
    Convert the Gregorian year (captured in group 1) to a Holocene year (add 10000),
    preserving any suffix (captured in group 2).
    """
    year = int(match.group(1))
    holocene_year = year + 10000
    suffix = match.group(2) if match.group(2) is not None else ''
    return f"{holocene_year}{suffix}"

def process_filename(filename):
    """Convert Gregorian year in the filename to Holocene year using the simple pattern."""
    return re.sub(simple_pattern, lambda m: str(int(m.group(1)) + 10000), filename)

def scan_file_for_matches(file_path):
    """
    Scan the file and return a list of tuples (line_number, line_content)
    for each line that contains a match for the advanced pattern.
    """
    matches = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            if advanced_pattern.search(line):
                matches.append((line_num, line.rstrip('\n')))
    return matches

def main():
    # Get the absolute path for the target _posts directory.
    # (This code assumes the _posts/ko directory is one level up from the current script directory.)
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    target_dir = os.path.join(root_dir, "_posts", "ko")
    
    files_to_modify = []       # Files that contain convertible patterns (in filename or content)
    content_matches = {}       # Mapping: file_path -> list of (line_number, line_content) with convertible content

    # Walk through _posts/ko and its subdirectories to find all .md files.
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                # Check if the file name contains a convertible Gregorian year.
                filename_has_year = simple_pattern.search(file)
                # Scan file content for convertible patterns.
                matches = scan_file_for_matches(file_path)
                if filename_has_year:
                    files_to_modify.append(file_path)
                if matches:
                    content_matches[file_path] = matches

    # Summary: total number of files with Gregorian year patterns in their filenames.
    total_files = len(files_to_modify)

    # Walk through _posts and its subdirectories to find all .md files.
    target_dir = os.path.join(root_dir, "_posts")
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                # Check if the file name contains a convertible Gregorian year.
                filename_has_year = simple_pattern.search(file)
                if filename_has_year:
                    files_to_modify.append(file_path)
    
    print(f"Total number of files with Gregorian year patterns in their filenames: {total_files}\n")

    # Print list of files that contain convertible content (not just file name changes).
    if content_matches:
        print("Files with potential convertible content candidates:")
        for file_path, lines in content_matches.items():
            print(f"\nFile: {file_path}")
            for line_num, line in lines:
                print(f"  Line {line_num}: {line}")
    else:
        print("No files contain potential convertible content in their content.")

    # Confirm with the user before proceeding with filename conversion only.
    answer = input("\nDo you want to proceed with filename conversion? (y/n): ")
    if answer.lower() != 'y':
        print("Conversion cancelled.")
        return

    # Process each file with a progress bar: perform only file name conversion.
    for file_path in tqdm(files_to_modify, desc="Renaming files"):
        dir_name, file_name = os.path.split(file_path)
        new_file_name = process_filename(file_name)
        if new_file_name != file_name:
            new_file_path = os.path.join(dir_name, new_file_name)
            os.rename(file_path, new_file_path)
            # If the file is in the candidate list, update the key to the new path.
            if file_path in content_matches:
                content_matches[new_file_path] = content_matches.pop(file_path)
            # print(f"\nRenamed file: {file_path} -> {new_file_path}")

    print("\nFilename conversion complete.")
    print("Please review the candidate content lines above for manual conversion if necessary.")

if __name__ == '__main__':
    main()