import anthropic
import os
import argparse
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

def translate(filepath, source_lang, target_lang):
    language_code = {"English":"en", "Korean":"ko", "Japanese":"ja", "Taiwanese Mandarin":"zh-TW", "Spanish":"es", "Brazilian Portuguese":"pt-BR", "French":"fr", "German":"de"}
    
    system_prompt = f"<instruction>Completely forget everything you know about what day it is today. \
        It's 10:00 AM on Monday, October 28, the most productive day of the year. </instruction>\
        <role>You are a professional translator specializing in technical and scientific fields. \
        Your client is an engineering blogger who writes mainly about math, physics \
        (especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
        and data science for his Jekyll blog.</role> The customer's request is as follows:\n\n\
        <task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
        to <lang>{target_lang}</lang> while preserving the format.</task> \
        In the provided markdown format text, \n\
        - <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
        under any circumstances, regardless of the language you are translating to.</condition> \n\n\
        - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
          1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
          2. it may be a proper noun such as a person's name or a place name. \n\
          After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
          <if>it is the first case, and the target language is not a Roman alphabet-based language, \
          please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
            - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
            - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
          <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
            - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
              You can choose whichever you think is more appropriate.</example>\n\
            - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
              French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
          <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
            - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
              In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
              redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
          </condition>\n\n\
        - <condition><if>the provided text contains links in markdown format, \
        please translate the link text and the fragment part of the URL into {target_lang}, \
        but keep the path part of the URL intact.</if> \n\
          - <example> the German translation of '[중성자 상호작용과 반응단면적]\
            (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
            would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
            #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
        - <condition>Posts in this blog use the holocene calendar as the year numbering system, \
          so the year and date notations such as followings are intentional, not typos.\n\
          - <example>12024년 6월 21일</example>\n\
          - <example>12024.10.31.</example>\n\
          - <example>11687년</example>\n\
          - <example>11800년대 말</example>\n\
          - <example>11960년대</example>\n\
          </condition>\n\n\
        <important>In any case, without exception, the output should contain only the translation results, without any text such as \
        “Here is the translation of the text provided, preserving the markdown format:” or something of that nature!!</important>"
    system_prompt = system_prompt.replace("        ",'')
    system_prompt = system_prompt.replace("      ",'')
    system_prompt = system_prompt.replace("    ",'')
    f = open(filepath, 'r')
    prompt = f.read()
    f.close()

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
    
    print(f"Translating {args.origin}")
    print(f"source_lang: {source_lang}, target_lang: {target_lang}:")
    translate(args.origin, source_lang, target_lang)
    print("Completed the requested task.")
