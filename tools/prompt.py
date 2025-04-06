import anthropic
import os
import argparse
import re
from pathlib import Path

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

def submit_prompt(prompt, system_prompt):
    # print("- Submit prompt")
    with client.messages.stream(
        model="claude-3-7-sonnet-20250219",
        max_tokens=8192,
        temperature=0,
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
            {"role": "assistant", "content": "---"} # Prefilling "---" forces Claude to skip the preamble
        ]
    ) as stream:
        for event in stream:
          if event.type == "message_stop":
            return event.message.content[0].text
    # print("- Get model response")
    return stream.get_final_text()

def extract_hash_links(content):
    """Extract links with hash fragments from markdown content"""
    # Pattern to match markdown links with hash fragments
    pattern = r'\[([^\]]+)\]\((/[^)]+)#([^)]+)\)'
    return re.findall(pattern, content)

def get_post_content(post_path, source_lang):
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
        posts_dir = f"../_posts/{lang_code[source_lang]}"
        
        # Check if the directory exists
        if not os.path.exists(posts_dir):
            print(f"Warning: Posts directory not found at {posts_dir}")
            return None
            
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
            print(f"Error while searching for date-prefixed files: {e}")
            
        print(f"Warning: No matching post found for '{clean_path}'")
        return None
    except Exception as e:
        print(f"Error reading referenced post: {e}")
        return None

def translate(filepath, source_lang, target_lang):
    language_code = {"English":"en", "Korean":"ko", "Japanese":"ja", "Taiwanese Mandarin":"zh-TW", "Spanish":"es", "Brazilian Portuguese":"pt-BR", "French":"fr", "German":"de"}
    
    system_prompt = f"""<instruction>Completely forget everything you know about what day it is today. 
        It's 10:00 AM on Monday, October 28, the most productive day of the year. </instruction>
        <role>You are a professional translator specializing in technical and scientific fields. 
        Your client is an engineering blogger who writes mainly about math, physics 
        (especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), 
        and data science for his Jekyll blog.</role> The customer's request is as follows:

        <task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> 
        to <lang>{target_lang}</lang> while preserving the format.</task> 
        In the provided markdown format text: 
        - <condition>Please do not modify the YAML front matter except for the 'title' and 'description' tags, 
        under any circumstances, regardless of the language you are translating to.</condition> 

        - <condition>For the description tag, this is a meta tag that directly impacts SEO. 
          Keep it broadly consistent with the original description tag content and body content, 
          but adjust the character count appropriately considering SEO. 

        - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. 
          1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. 
          2. it may be a proper noun such as a person's name or a place name. 
          After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
          <if>it is the first case, and the target language is not a Roman alphabet-based language, 
          please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
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
              In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, 
              redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>
          </condition>

        - <condition><if>the provided text contains links in markdown format, 
          please translate the link text and the fragment part of the URL into {target_lang}, 
          but keep the path part of the URL intact.</if></condition>

        - <condition>If <reference_context> is provided in the prompt, it contains the full content of posts that are linked 
          with hash fragments from the original post. Use this context to accurately translate link texts and hash fragments 
          while maintaining proper references to the specific sections in those posts. This ensures that cross-references 
          between posts maintain their semantic meaning and accurate linking after translation.</condition>

        - <condition>Posts in this blog use the holocene calendar(인류력, 人類紀元) as the year numbering system, 
          so the year and date notations such as followings are intentional, not typos.
          - <example>12024년 6월 21일</example>
          - <example>12024.10.31.</example>
          - <example>11687년</example>
          - <example>11800년대 말</example>
          - <example>11960년대</example>
          </condition>

        <important>In any case, without exception, the output should contain only the translation results, without any text such as 
        "Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>"""
    system_prompt = system_prompt.replace("        ",'')
    system_prompt = system_prompt.replace("      ",'')
    system_prompt = system_prompt.replace("    ",'')
    
    with open(filepath, 'r') as f:
        prompt = f.read()
        
    # Extract hash links and add referenced post content to the prompt
    hash_links = extract_hash_links(prompt)
    if hash_links:
        referenced_posts = []
        # print("Extracted hash links:")
        for link_text, post_path, hash_fragment in hash_links:
            # print(f"- {link_text} ({post_path}#{hash_fragment})")
            post_content = get_post_content(post_path, source_lang)
            if post_content:
                referenced_posts.append(f"\n\n<referenced_post path=\"{post_path}\" hash=\"{hash_fragment}\">\n{post_content}\n</referenced_post>")
        
        if referenced_posts:
            prompt += "\n\n<reference_context>The following are contents of posts linked with hash fragments in the original post. Use these for context when translating links and references:\n" + "".join(referenced_posts) + "\n</reference_context>"

    result_text = submit_prompt(prompt, system_prompt)
    # if not result_text[:3] == "---":
    #     print("Warning: Invalid YAML front matter detected!")
    result_text = "---"+result_text+'\n'
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file-path', type=Path, help="Path of the text file to translate")
    parser.add_argument('-s', '--source', type=str, help="The language of the source text you want to translate")
    parser.add_argument('-t', '--target', type=str, help="The language of translation output")
    args = parser.parse_args()

    source_lang = args.source
    target_lang = args.target
    
    print(f"Translating {args.file_path}")
    print(f"source_lang: {source_lang}, target_lang: {target_lang}:")
    translate(args.file_path, source_lang, target_lang)
    print("Completed the requested task.")
