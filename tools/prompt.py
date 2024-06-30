import anthropic
import os
import argparse
from pathlib import Path

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

def submit_prompt(prompt, system_prompt):
    # print("- Submit prompt")
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4000,
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
            }
        ]
    )
    # print("- Get model response")
    return response.content[0].text

def translate(filepath, source_lang, target_lang):
    language_code = {"English":"en", "Spanish":"es", "Brazilian Portuguese":"pt_BR", "Japanese":"ja", 
                     "French":"fr", "German":"de", "Korean":"ko"}
    
    system_prompt = f"You are a professional technical translator. \
        Your client is an engineering blogger who writes mainly about math, \
        physics (especially nuclear physics, quantum mechanics, and quantum information theory), \
        and data science. Translate the markdown-formatted text provided by the user \
        from {source_lang} to {target_lang} while preserving the format. \
        If some terms in the provided text are in both {source_lang} and {target_lang}, \
        leave only the {target_lang} version in parentheses. \
        For example, ‘중성자 감쇠(Neutron Attenuation)’ can be translated as ‘Neutron Attenuation’. \
        The output should only contain the translated text."
    f = open(filepath, 'r')
    prompt = f.read()
    f.close()

    result_text = submit_prompt(prompt, system_prompt)
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
    
    print(f"Translating {args.origin}")
    print(f"source_lang: {source_lang}, target_lang: {target_lang}:")
    translate(args.origin, source_lang, target_lang)
    print("Completed the requested task.")