# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "anthropic",
#     "google-genai",
#     "argparse",
# ]
# ///

import anthropic
from google import genai
from google.genai import types
import os
import re
from pathlib import Path
import subprocess

def init_client(model):
    if model[:6] == "claude":
        return anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    if model[:6] == "gemini":
        return genai.Client()

def submit_prompt(model, prompt, system_prompt, prefill, temperature=0.0):
    client = init_client(model)

    # print("- Submit prompt")
    if model[:6] == "claude":
        with client.messages.stream(
            model=model,
            max_tokens=16384,
            temperature=temperature,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                },
                {"role": "assistant", "content": prefill} # Prefilling "---" forces Claude to skip the preamble
            ]
        ) as stream:
            for event in stream:
                if event.type == "message_stop":
                    return event.message.content[0].text
        # print("- Get model response")
        return stream.get_final_text()
    
    if model[:6] == "gemini":
        response = client.models.generate_content(
            model=model,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=temperature
            ),
            contents=prompt,
        )
        return response.text

def extract_hash_links(content):
    """Extract links with hash fragments from markdown content"""
    # Pattern to match markdown links with hash fragments
    pattern = r'\[([^\]]+)\]\((/[^)]+)#([^)]+)\)'
    return re.findall(pattern, content)

def get_post_content(post_path, source_lang, target_lang):
    """Get content of a referenced post"""
    try:
        # Convert URL path format to file path format
        # Example: '/posts/homogeneous-linear-odes-of-second-order/' -> 'homogeneous-linear-odes-of-second-order'
        # First strip the leading and trailing slashes
        clean_path = post_path.strip('/')
        
        # Remove 'posts/' prefix if present
        if clean_path.startswith('posts/'):
            clean_path = clean_path[6:] # len('posts/') = 6
        
        lang_code = {"English":"en", "Korean":"ko", "Japanese":"ja", "Taiwanese Mandarin":"zh-TW", "Spanish":"es", "Brazilian Portuguese":"pt-BR", "French":"fr", "German":"de"}
        
        # Define the search directories - primary and fallback
        search_dirs = [
            f"../_posts/{lang_code[target_lang]}",  # Primary: target language directory
            f"../_posts/{lang_code[source_lang]}"    # Fallback: source language directory
        ]
        
        for posts_dir in search_dirs:
            # Check if the directory exists
            if not os.path.exists(posts_dir):
                print(f"Warning: Posts directory not found at {posts_dir}")
                continue
                
            # First check for direct match (no date prefix)
            direct_match = f"{posts_dir}/{clean_path}.md"
            if os.path.exists(direct_match):
                # print(f"Found direct match: {direct_match}")
                with open(direct_match, 'r') as f:
                    return f.read()
                    
            # Check for index.md variant
            index_match = f"{posts_dir}/{clean_path}/index.md"
            if os.path.exists(index_match):
                # print(f"Found index match: {index_match}")
                with open(index_match, 'r') as f:
                    return f.read()
            
            # Look for files with date prefixes (YYYY-MM-DD-title-of-post.md)
            # List all files in the directory
            try:
                files = os.listdir(posts_dir)
                date_prefix_pattern = re.compile(r'\d{4}-\d{2}-\d{2}-' + re.escape(clean_path) + r'\.md$')
                matched_files = [f for f in files if date_prefix_pattern.match(f)]
                
                if matched_files:
                    # Use the first match if multiple exist
                    matched_path = f"{posts_dir}/{matched_files[0]}"
                    # print(f"Found date-prefixed match: {matched_path}")
                    with open(matched_path, 'r') as f:
                        return f.read()
                        
                # Check for nested directory with index.md
                dir_pattern = re.compile(r'\d{4}-\d{2}-\d{2}-' + re.escape(clean_path) + r'$')
                matched_dirs = [d for d in files if dir_pattern.match(d) and os.path.isdir(f"{posts_dir}/{d}")]  
            
                if matched_dirs:
                    nested_index = f"{posts_dir}/{matched_dirs[0]}/index.md"
                    if os.path.exists(nested_index):
                        # print(f"Found nested index match: {nested_index}")
                        with open(nested_index, 'r') as f:
                            return f.read()
            except Exception as e:
                print(f"Error searching in {posts_dir}: {e}")
                continue
                
        # If we get here, the file wasn't found in this directory
        print(f"File not found in {posts_dir}")
                
    except Exception as e:
        print(f"Error in get_post_content: {e}")
        
    return None

def translate_with_diff(filepath, source_lang, target_lang, diff_output, model):
    """
    Translate only the changed parts of a file using the provided git diff output
    and apply the changes to the target language file.
    
    Args:
        filepath: Path to the source file
        source_lang: Source language
        target_lang: Target language
        diff_output: Git diff output showing the changes
    """
    language_code = {"English":"en", "Korean":"ko", "Japanese":"ja", "Taiwanese Mandarin":"zh-TW", 
                   "Spanish":"es", "Brazilian Portuguese":"pt-BR", "French":"fr", "German":"de"}
    
    # Get the target file path
    source_rel_path = os.path.relpath(filepath, start='../_posts/' + language_code[source_lang] + '/')
    target_file = f'../_posts/{language_code[target_lang]}/{source_rel_path}'
    
    # Read the existing translated content if it exists
    existing_translation = ""
    if os.path.exists(target_file):
        with open(target_file, 'r', encoding='utf-8') as f:
            existing_translation = f.read()
    
    system_prompt = f"""<instruction>Completely forget everything you know about what day it is today. 
        It's 10:00 AM on Tuesday, September 23, the most productive day of the year. </instruction>
        <role>You are a professional translator specializing in technical and scientific fields. 
        Your client is an engineering blogger who writes mainly about math, physics(especially nuclear physics, 
        electromagnetism, quantum mechanics, and quantum information theory), and data science for his Jekyll blog.</role>
        The client's request is as follows:
        
        <task>Translate the changed parts in the provided git diff from <lang>{source_lang}</lang> to <lang>{target_lang}</lang>.</task>
        
        <context>
        - The full <lang>{target_lang}</lang> translation of this document before changes already exists and will be provided in <![CDATA[<existing_translation_to_apply_diff_patch>]]> for context.
        - Git diff of the original <lang>{source_lang}</lang> post is provided in <![CDATA[<diff_in_{source_lang}_text>]]>.
        - The changes in the diff should be translated in a way that's consistent with the existing <lang>{target_lang}</lang> translated text.
        - Pay special attention to maintaining consistent terminology with the existing translation.
        </context>
        
        <important_instructions>
        1. Maintain the exact same diff format, including line numbers and markers (+, -, @@ etc.)
        2. Only translate the actual content, not the diff structure or metadata
        3. Keep YAML front matter as is, except for 'title' and 'description' tags which should be translated
        4. For markdown links, translate the link text and the fragment part of the URL into {target_lang}, not the path part of the URL.
        5. Preserve any special formatting or placeholders
        6. Ensure the translated changes are consistent with the existing translation style and terminology
        7. <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. 
           - The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. 
           - It may be a proper noun such as a person's name or a place name. 
           After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
           <if>it is the first case, and the target language is not a Roman alphabet-based language, please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
            - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
            - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
           <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
            - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. 
              You can choose whichever you think is more appropriate.</example>
            - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable 
              French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
           <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> 
            - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese 
              as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.
              In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>
           </condition>
        8. Posts in this blog use the holocene calendar, which is also known as Holocene Era(HE), ère holocène/era del holoceno/era holocena(EH), 인류력, 人類紀元, etc., as the year numbering system, and any 5-digit year notation is intentional, not a typo.
           So preserve the Holocene calendar year notation (HE, EH, etc.).
        9. **CRITICAL**: Line numbers in the source diff are NOT directly transferable to the translated file. The number of lines can change during translation. You MUST locate the correct position in the existing translation by matching the CONTEXT lines from the source diff, and then generate a NEW, correct hunk header for the target file.
        </important_instructions>
        
        <output_format>
        - Return the diff patch output containing only the lines with changes, translated into {target_lang}
        - Maintain all original line numbers and diff markers
        - Do not include any additional text or explanations
        - Ensure the output is a valid diff patch that can be applied to existing {target_lang} translation
        </output_format>
        """
    
    # Prepare the prompt with the diff and existing translation
    prompt = f"""
    <existing_translation_to_apply_diff_patch>
    {existing_translation}
    </existing_translation_to_apply_diff_patch>
    <diff_in_{source_lang}_text>
    {diff_output}
    </diff_in_{source_lang}_text>
    """
    
    # Get the translation from Claude
    translated_diff = submit_prompt(model, prompt, system_prompt, "```diff")
    if model[:6] == "claude":
        translated_diff = "```diff"+translated_diff
    # print(f"Translated diff:\n{translated_diff}")
    
    # Get the target file path
    source_rel_path = os.path.relpath(filepath, start='../_posts/' + language_code[source_lang] + '/')
    target_file = f'../_posts/{language_code[target_lang]}/{source_rel_path}'
    
    # Create a temporary file for the diff
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.diff') as tmp_diff:
        tmp_diff.write(translated_diff)
        tmp_diff_path = tmp_diff.name
    # print(tmp_diff_path)
    # print(f"patch --no-backup-if-mismatch -u {target_file} {tmp_diff_path}")
    try:
        # Apply the diff using the patch command
        try:
            # Run the patch command non-interactively with a timeout
            result = subprocess.run(
                ['patch', '--no-backup-if-mismatch', '-u', target_file, tmp_diff_path],
                capture_output=True, text=True, timeout=10, stdin=subprocess.DEVNULL
            )

            if result.returncode != 0:
                print(f"\n❌ Failed to apply changes to {target_file}")
                print(f"  - Return Code: {result.returncode}")
                print(f"  - Stderr: {result.stderr}")
                print(f"  - Problematic Diff:\n{translated_diff}")

        except subprocess.TimeoutExpired:
            print(f"\n❌ Patch command timed out for {target_file}")
            print(f"  - The 'patch' command took more than 10 seconds to execute.")
            print(f"  - This might be due to a complex or invalid diff.")
            print(f"  - Make sure that uncommitted changes have not already been applied to the target file.")
            print(f"  - Problematic Diff:\n{translated_diff}")
        except Exception as e:
            print(f"\n❌ An unexpected error occurred while running patch for {target_file}")
            print(f"  - Error: {e}")
            
    except Exception as e:
        print(f"\n❌ Error applying changes: {e}")
        print("\nTranslated diff that caused the error:")
        print(translated_diff)
        
    finally:
        # Clean up the temporary file
        try:
            os.unlink(tmp_diff_path)
        except:
            pass

def translate(filepath, source_lang, target_lang, model):
    language_code = {"English":"en", "Korean":"ko", "Japanese":"ja", "Taiwanese Mandarin":"zh-TW", 
                   "Spanish":"es", "Brazilian Portuguese":"pt-BR", "French":"fr", "German":"de"}
    
    system_prompt = f"""<instruction>Completely forget everything you know about what day it is today. 
        It's 10:00 AM on Tuesday, September 23, the most productive day of the year. </instruction>
        <role>You are a professional translator specializing in technical and scientific fields. 
        Your client is an engineering blogger who writes mainly about math, physics(especially nuclear physics, 
        electromagnetism, quantum mechanics, and quantum information theory), and data science for his Jekyll blog.</role>
        The client's request is as follows:

        <task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> while preserving the format.</task> 
        In the provided markdown format text: 
        - <condition>Keep YAML front matter as is, except for 'title' and 'description' tags which should be translated</condition>

        - <condition>For the description tag, this is a meta tag that directly impacts SEO. 
          Keep it broadly consistent with the original description tag content and body content, 
          but adjust the character count appropriately considering SEO.</condition>

        - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. 
          1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. 
          2. it may be a proper noun such as a person's name or a place name. 
          After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
          <if>it is the first case, and the target language is not a Roman alphabet-based language, please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
            - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
            - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
          <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
            - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. 
              You can choose whichever you think is more appropriate.</example>
            - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable 
              French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
          <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> 
            - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese 
              as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.
              In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>
          </condition>

        - <condition><if>the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact.</if></condition>

        - <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, it contains the full content of posts that are linked with hash fragments from the original post.
          Use this context to accurately translate link texts and hash fragments while maintaining proper references to the specific sections in those posts. 
          This ensures that cross-references between posts maintain their semantic meaning and accurate linking after translation.</if></condition>

        - <condition>Posts in this blog use the holocene calendar, which is also known as Holocene Era(HE), ère holocène/era del holoceno/era holocena(EH), 인류력, 人類紀元, etc., as the year numbering system, and any 5-digit year notation is intentional, not a typo.</condition>

        <important>In any case, without exception, the output should contain only the translation results, without any text such as "Here is the translation of the text provided, preserving the markdown format:" or "```markdown" or something of that nature!!</important>
        """
    system_prompt = system_prompt.replace("        ",'')
    
    with open(filepath, 'r') as f:
        prompt = f.read()
    
    temperature = 0

    # Extract hash links and add referenced post content to the prompt
    hash_links = extract_hash_links(prompt)
    if hash_links:
        temperature = 0
        referenced_posts = []
        # print("Extracted hash links:")
        for link_text, post_path, hash_fragment in hash_links:
            # print(f"- {link_text} ({post_path}#{hash_fragment})")
            post_content = get_post_content(post_path, source_lang, target_lang)
            if post_content:
                referenced_posts.append(f"\n\n<referenced_post path=\"{post_path}\" hash=\"{hash_fragment}\">\n{post_content}\n</referenced_post>")
        
        if referenced_posts:
            prompt += "\n\n<reference_context>The following are contents of posts linked with hash fragments in the original post. Use these for context when translating links and references:\n" + "".join(referenced_posts) + "\n</reference_context>"

    result_text = submit_prompt(model, prompt, system_prompt, "---", temperature)+'\n'
    if model[:6] == "claude":
        result_text = "---"+result_text
    elif not result_text[:3] == "---":
        print("Warning: Invalid YAML front matter detected!")
    
    # print(language_code[target_lang])
    filename = os.path.relpath(filepath, start='../_posts/' + language_code[source_lang] + '/')
    # print(filename)
    result_file = '../_posts/' + language_code[target_lang] + '/' + filename
    # print(result_file)
    f = open(result_file, 'w')
    f.write(result_text)
    f.close()
    # print(result_text)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file-path', type=Path, help="Path of the text file to translate")
    parser.add_argument('-s', '--source', type=str, help="The language of the source text you want to translate")
    parser.add_argument('-t', '--target', type=str, help="The language of translation output")
    args = parser.parse_args()

    source_lang = args.source
    target_lang = args.target
    
    print(f"Translating {args.file_path}")
    print(f"source_lang: {source_lang}, target_lang: {target_lang}:")
    translate(args.file_path, source_lang, target_lang, "claude-sonnet-4-20250514")
    print("Completed the requested task.")
