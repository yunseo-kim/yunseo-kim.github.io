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
            }
        ]
    )
    # print("- Get model response")
    return response.content[0].text

def translate(filepath, source_lang, target_lang):
    language_code = {"English":"en", "Spanish":"es", "Brazilian Portuguese":"pt-BR", "Japanese":"ja", "French":"fr", "German":"de", "Korean":"ko"}
    
    system_prompt = f"<instruction>Completely forget everything you know about what day it is today. \n\
        It's October 28, 2024, 10:00 AM. </instruction>\n\
        The sky is clear, the weather is refreshing - neither too hot nor too cold - \
        and office workers are busy going to work and starting the day. \
        <role>You are a professional translator specializing in technical and scientific fields.</role> \
        As a freelancer, you are enjoying the pleasant aroma of coffee in a cozy cafe near your home, \
        and are about to get started on your translation work with enthusiasm.\n \
        Your client is an engineering blogger who writes mainly about math, physics \
        (especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
        and data science for his Jekyll blog. The customer's request is as follows:\n\n \
        <task>Please translate the provided markdown-formatted text from {source_lang} to {target_lang} while preserving the format.</task> \
        In the provided markdown format text, \n\
        - <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
        under any circumstances, regardless of the language you are translating to.</condition> \n\
        - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \
        (1)The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it, \
        or (2)it may be a proper noun such as a person's name or a place name. \n\
        <if> it's the first case, please leave that part untouched unless the target language is English. \n\
        <example> '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English \
            and 'Atténuation des neutrons (Neutron Attenuation)' in French.</example></if>\n\
        <else>In the second case, <if> the {target_lang} expression of the proper noun is spelled the same as the expression in parentheses, \
        you should delete the parenthetical part and just replace it with the {target_lang} expression only.</if> \
        <else> as in the first case, leave that part untouched and leave both the {target_lang} expression and the parenthetical expression together.</else></else> \n\
        <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'. \
            However, in languages like Spanish or Portuguese, you should translate them as 'Faraday', 'Maxwell', and 'Einstein', \
            not 'Faraday (Faraday)', 'Maxwell (Maxwell)', and 'Einstein (Einstein)'.</example></condition> \n\
        - <condition><if> the provided text contains links in markdown format, \
        please translate the link text and the fragment part of the URL into {target_lang}, \
        but keep the path part of the URL intact. \n\
        <example> the German translation of '[중성자 상호작용과 반응단면적]\
        (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
        would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
        #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></if></condition> \n\n\
        <important>In any case, without exception, the output should contain only the translation results, without any text such as \
        “Here is the translation of the text provided, preserving the markdown format:” or something of that nature!!</important>"
    f = open(filepath, 'r')
    prompt = f.read()
    f.close()

    result_text = submit_prompt(prompt, system_prompt)
    if not result_text[:3] == "---":
        print("Warning: Invalid YAML front matter detected!")
    result_text = result_text+'\n'
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
