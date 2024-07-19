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
    language_code = {"English":"en", "Spanish":"es", "Brazilian Portuguese":"pt-BR", "Japanese":"ja", "French":"fr", "German":"de", "Korean":"ko"}
    
    system_prompt = f"You are a professional technical translator. \
        Your client is an engineering blogger who writes mainly about math, \
        physics (especially nuclear physics, quantum mechanics, and quantum information theory), \
        and data science. Translate the markdown-formatted text provided by the user \
        from {source_lang} to {target_lang} while preserving the format. \
        If the provided text contains language other than {source_lang}, please leave that part untouched. \
        For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English \
        and 'Atténuation des neutrons (Neutron Attenuation)' in French. \
        Also, if the provided text contains links in markdown format, \
        please translate the link text and the fragment part of the URL into {target_lang}, \
        but keep the path part of the URL intact. \
        For example, the German translation of '[중성자 상호작용과 반응단면적]\
        (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
        would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
        #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'. \
        The output should only contain the translated text."
    f = open(filepath, 'r')
    prompt = f.read()
    f.close()

    result_text = submit_prompt(prompt, system_prompt)
    if not result_text[:3] == "---":
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
