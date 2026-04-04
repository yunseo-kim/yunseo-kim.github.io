---
title: "በ Claude Sonnet 4 API ፖስቶችን በራስ-ሰር መተርጎም እንዴት እንደሚቻል (2) - የአውቶሜሽን ስክሪፕት መጻፍና መተግበር"
description: "ለ Markdown ጽሑፍ ፋይሎች የባለብዙ ቋንቋ ትርጉም ፕሮምፕት እንዴት እንደሚዘጋጅ እና Anthropic/Gemini API ቁልፎችን ከተዘጋጀ ፕሮምፕት ጋር በPython በመጠቀም ሥራውን እንዴት በራስ-ሰር እንደሚፈጽሙ ያብራራል። ይህ ፖስት የተከታታዩ ሁለተኛ ክፍል ሲሆን API መስጠትና ማገናኘት እንዲሁም የPython ስክሪፕት መጻፍ ያስተዋውቃል።"
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2/
---

## መግቢያ
በ12024 ዓ.ም ሰኔ ወር ለብሎግ ፖስቶቼ የባለብዙ ቋንቋ ትርጉም Anthropic ၏ Claude 3.5 Sonnet API ከገባሁ በኋላ፣ ፕሮምፕትንና የአውቶሜሽን ስክሪፕቶችን ብዙ ጊዜ አሻሽዬ እንዲሁም የሞዴል ስሪቶችን እያዘመንኩ ለአንድ ዓመት የሚጠጋ ጊዜ ይህን የትርጉም ስርዓት እጅግ በእርካታ አስኬድኩት። ስለዚህ በዚህ ተከታታይ ጽሑፍ፣ በመጀመሪያ Claude Sonnet ሞዴልን ለምን እንደመረጥሁ፣ ከዚያም Gemini 2.5 Pro ለምን እንደጨመርሁ፣ ፕሮምፕት እንዴት እንደተዘጋጀ እና Python ስክሪፕት በመጠቀም API እንዴት እንደተገናኘ እና አውቶሜሽን እንዴት እንደተተገበረ እናቀርባለን።  
ይህ ተከታታይ 2 ጽሑፎችን ያካትታል፣ እያነበቡት ያሉትም ይህ ጽሑፍ የሁለተኛው ክፍል ነው።
- ክፍል 1: [Claude Sonnet/Gemini 2.5 ሞዴሎች ማስተዋወቂያ እና የመምረጫ ምክንያቶች፣ ፕሮምፕት ኢንጂነሪንግ](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- ክፍል 2: API በመጠቀም የPython አውቶሜሽን ስክሪፕት መጻፍና መተግበር (ይህ ጽሑፍ)

## ከመጀመርዎ በፊት
ይህ ጽሑፍ [ክፍል 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1) ቀጣይ ስለሆነ፣ እስካሁን ካላነበቡት መጀመሪያ ያንን ያንብቡ ብዬ እመክራለሁ።

## የተጠናቀቀው የሲስተም ፕሮምፕት
ቀደም ብሎ [በክፍል 1 የተተዋወቀውን ሂደት](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#የፕሮምፕት-ንድፍ) ካለፍን በኋላ የተጠናቀቀው የፕሮምፕት ንድፍ ውጤት እንዲህ ነው።

```xml
<instruction>Completely forget everything you know about what day it is today. 
It's 10:00 AM on Tuesday, September 23, the most productive day of the year. </instruction>
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics\
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
The client's request is as follows:

<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> while preserving the format.</task> 
In the provided markdown format text: 
- <condition>Please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> 

- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>

- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. 
  1. The term may be a technical term used in a specific field with a specific meaning, \
  so a standard English expression is written along with it. 
  2. it may be a proper noun such as a person's name or a place name. 
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language, \
  please maintain the <format>[target language expression(original English expression)]</format> \
  in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, \
  you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. 
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable 
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. \
      You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses \
  must be preserved in the translation output in some form.</else> 
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese 
      as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.
      In languages ​​such as Spanish or Portuguese, they can be translated as \
      'Faraday', 'Maxwell', 'Einstein', in which case, redundant expressions \
      such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' \
      would be highly inappropriate.</example>
  </condition>

- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>

- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>

- <condition>Posts in this blog use the holocene calendar, which is also known as \
  Holocene Era(HE), ère holocène/era del holoceno/era holocena(EH), 인류력, 人類紀元, etc., \
  as the year numbering system, and any 5-digit year notation is intentional, not a typo.</condition>

<important>In any case, without exception, the output should contain only the translation results, \
without any text such as "Here is the translation of the text provided, preserving the markdown format:" \
or "```markdown" or something of that nature!!</important>
```

> [አዲስ የተጨመረው የጭማሪ ትርጉም ባህሪ](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#120250704) ጥቂት የተለየ የሲስተም ፕሮምፕት ይጠቀማል። የሚደጋገሙ ክፍሎች ብዙ ስለሆኑ እዚህ አልጻፍኩትም፤ ካስፈለገ [በ GitHub ሪፖዚቶሪ ውስጥ ያለውን `prompt.py`{: .filepath }] (https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py) ይመልከቱ።
{: .prompt-tip }

## API ማገናኘት
### API ቁልፍ መፍጠር

> እዚህ አዲስ Anthropic ወይም Gemini API ቁልፍ እንዴት መፍጠር እንደሚቻል እናብራራለን። አስቀድሞ የሚጠቀሙበት API ቁልፍ ካለዎት ይህን ደረጃ መዝለል ይችላሉ።
{: .prompt-tip }

#### Anthropic Claude
ወደ <https://console.anthropic.com> ገብተው በAnthropic Console መለያ ይግቡ። Anthropic Console መለያ ካልዎት በመጀመሪያ መመዝገብ ይኖርብዎታል። ከገቡ በኋላ ከታች ያለው ዓይነት ዳሽቦርድ ይታያል።  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

በዚያ ስክሪን ላይ 'Get API keys' የሚለውን አዝራር ጠቅ ካደረጉ ቀጣዩን ስክሪን ያያሉ።  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) እኔ አስቀድሜ የፈጠርኩት ቁልፍ ስላለኝ `yunseo-secret-key` የሚባል ቁልፍ ይታያል፤ መለያዎን አዲስ ከፈጠሩ በኋላ API ቁልፍ እስካሁን ካላወጡ ግን ምናልባት ምንም ቁልፍ አይኖርዎትም። በቀኝ ላይ ያለውን 'Create Key' የሚለውን አዝራር ጠቅ በማድረግ አዲስ ቁልፍ ማውጣት ይችላሉ።

> ቁልፉን ካወጡ በኋላ የራስዎ API ቁልፍ በስክሪን ላይ ይታያል፣ ነገር ግን ያንን ቁልፍ በኋላ ዳግም ማየት አይቻልም፤ ስለዚህ በግድ በደህና ቦታ በተለየ መልኩ መዝግበው ያስቀምጡት።
{: .prompt-warning }

#### Google Gemini
Gemini API በ Google AI Studio ውስጥ ማስተዳደር ይቻላል። ወደ <https://aistudio.google.com/apikey> ገብተው በGoogle መለያ ከገቡ በኋላ ቀጣዩ ዓይነት ዳሽቦርድ ይታያል።  
![Google AI Studio Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/get-api-key-google-ai-studio.png)

በዚህ ስክሪን ላይ 'API 키 만들기' የሚለውን አዝራር ጠቅ በማድረግ እና መመሪያውን በመከተል ቀጥሉ። Google Cloud ፕሮጀክት እና ለእሱ የሚያገለግል የክፍያ መለያ ከፈጠሩና ካገናኙ በኋላ API ቁልፉን ለመጠቀም ዝግጁ ይሆናሉ፤ ከAnthropic API ይልቅ ሂደቱ ጥቂት ውስብስብ ቢሆንም እጅግ አስቸጋሪ አይሆንም።

> ከAnthropic Console በተለየ ሁኔታ፣ የራስዎን API ቁልፍ በማንኛውም ጊዜ በዳሽቦርድ ላይ ማየት ይችላሉ። ~~እንዲያውም Anthropic Console መለያ ቢጠለፍ እንኳ የAPI ቁልፉን ብቻ ካስጠበቁ ጉዳቱን መገደብ ይቻላል፤ ግን የGoogle መለያ ቢጠለፍ ከGemini API ቁልፍ ውጭም አስቸኳይ ችግሮች ብዙ ይኖራሉ~~  
> ስለዚህ API ቁልፉን በተለይ መመዝገብ አያስፈልግም፤ ነገር ግን የራስዎን Google መለያ ደህንነት በጥሩ ሁኔታ ይጠብቁ።
{: .prompt-tip }

### (የሚመከር) API ቁልፉን በአካባቢ ተለዋዋጭ(Environment Variable) ላይ መመዝገብ
በPython ወይም Shell ስክሪፕት ውስጥ Claude API ለመጠቀም API ቁልፉን መጫን ያስፈልጋል። ቁልፉን በስክሪፕቱ ውስጥ በቀጥታ hardcode ማድረግም ይቻላል፣ ግን ስክሪፕቱን GitHub ወይም በሌላ መንገድ ከሌሎች ጋር ሊካፈሉ ከሆነ ይህ መንገድ ተገቢ አይደለም። እንዲሁም ፋይሉን ለመካፈል አላሰቡም ብለውም በአልፎ አልፎ ስህተት ፋይሉ ሊፈስ ይችላል፤ በዚህ ጊዜ በፋይሉ ውስጥ API ቁልፍ ከተመዘገበ ከፋይሉ ጋር ቁልፉም አብሮ ሊፈስ ይችላል። ስለዚህ API ቁልፉን በራስዎ ብቻ በሚጠቀሙበት ስርዓት የenvironment variable ውስጥ መመዝገብና በስክሪፕቱ ውስጥ ከዚያ መጫን ይመከራል። ከታች በUNIX ስርዓት ላይ የስርዓት environment variable ውስጥ API ቁልፉን እንዴት መመዝገብ እንደሚቻል እናሳያለን። Windows ከሆነ በድር ላይ ያሉ ሌሎች መመሪያዎችን ይመልከቱ።

1. በተርሚናል ውስጥ በሚጠቀሙት shell አይነት መሠረት `nano ~/.bashrc` ወይም `nano ~/.zshrc` ያስገቡ እና editor ይክፈቱ።
2. Anthropic API የሚጠቀሙ ከሆነ በፋይሉ ውስጥ `export ANTHROPIC_API_KEY=your-api-key-here` ይጨምሩ። `your-api-key-here` በሚለው ቦታ የራስዎን API ቁልፍ ያስገቡ። Gemini API ከሆነ `export GEMINI_API_KEY=your-api-key-here` በተመሳሳይ መንገድ ይጨምሩ።
3. ለውጦቹን ያስቀምጡ እና editor ይዝጉ።
4. በተርሚናል `source ~/.bashrc` ወይም `source ~/.zshrc` ያስኬዱ እና ለውጦቹን እንዲተገበሩ ያድርጉ።

### የሚያስፈልጉ የPython ፓኬጆችን መጫን
በሚጠቀሙት Python አካባቢ API library ካልተጫነ ከሆነ በሚከተለው ትእዛዝ ይጫኑ።

#### Anthropic Claude
```bash
pip3 install anthropic
```

#### Google Gemini
```bash
pip3 install google-genai
```

#### የጋራ
ከዚህ በኋላ የምናስተዋውቀውን የፖስት ትርጉም ስክሪፕት ለመጠቀም የሚከተሉት ፓኬጆችም ያስፈልጋሉ፤ ስለዚህ በዚህ ትእዛዝ ይጫኑ ወይም ያዘምኑ።
```bash
pip3 install -U argparse tqdm
```

### የPython ስክሪፕት መጻፍ
በዚህ ጽሑፍ የምናስተዋውቀው የፖስት ትርጉም ስክሪፕት 3 የPython ስክሪፕት ፋይሎችና 1 CSV ፋይል ያካትታል።

- `compare_hash.py`{: .filepath}: በ `_posts/ko`{: .filepath} ዳይሬክቶሪ ውስጥ ያሉ የኮሪያኛ መነሻ ፖስቶችን SHA256 hash እሴት ያስላል፣ ከዚያም `hash.csv`{: .filepath} ፋይል ውስጥ ከተመዘገቡት ነባር hash እሴቶች ጋር ያነጻጽራል እና የተቀየሩ ወይም አዲስ የተጨመሩ ፋይሎች ዝርዝር ይመልሳል
- `hash.csv`{: .filepath}: የነባር ፖስት ፋይሎች SHA256 hash እሴቶችን የሚመዘግብ CSV ፋይል
- `prompt.py`{: .filepath}: filepath, source_lang, target_lang እሴቶችን ግብዓት አድርጎ ከስርዓት environment variable ውስጥ Claude API ቁልፍን ያነባል፣ ከዚያ API ይጠራል። የሲስተም ፕሮምፕት እንደ ቀደም የተዘጋጀውን ፕሮምፕት ይጠቀማል፣ የተጠቃሚ ፕሮምፕት ደግሞ በ `filepath` ውስጥ ያለውን የሚተረጎም ፖስት ይላካል። ከዚያ Claude Sonnet 4 ሞዴል የተመለሰውን ውጤት በ `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath} መንገድ ላይ እንደ ጽሑፍ ፋይል ይጻፋል
- `translate_changes.py`{: .filepath}: source_lang የሚባል የstring ተለዋዋጭና `target_langs` የሚባል የlist ተለዋዋጭ አለው፣ እና `compare_hash.py`{: .filepath} ውስጥ ያለውን `changed_files()` ፋንክሽን በመጥራት changed_files የሚባል list ይቀበላል። ከተቀየሩ ፋይሎች ካሉ፣ በchanged_files ውስጥ ያሉ ፋይሎችን ሁሉ እና በtarget_langs ውስጥ ያሉ ቋንቋዎችን ሁሉ በሁለት-ደረጃ ዙር ይመራል፣ እና በዚህ ዙር ውስጥ `prompt.py`{: .filepath} ውስጥ ያለውን `translate(filepath, source_lang, target_lang)` ፋንክሽን በመጥራት የትርጉም ስራውን ያስኬዳል።

የተጠናቀቁትን ስክሪፕት ፋይሎች በGitHub ላይ ባለው [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) ሪፖዚቶሪም ማየት ይችላሉ።

#### compare_hash.py

```python
import os
import hashlib
import csv

default_source_lang_code = "ko"

def compute_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load_existing_hashes(csv_path):
    existing_hashes = {}
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 2:
                    existing_hashes[row[0]] = row[1]
    return existing_hashes

def update_hash_csv(csv_path, file_hashes):
    # Sort the file hashes by filename (the dictionary keys)
    sorted_file_hashes = dict(sorted(file_hashes.items()))

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, hash_value in sorted_file_hashes.items():
            writer.writerow([file_path, hash_value])

def changed_files(source_lang_code):
    posts_dir = '../_posts/' + source_lang_code + '/'
    hash_csv_path = './hash.csv'
    
    existing_hashes = load_existing_hashes(hash_csv_path)
    current_hashes = {}
    changed_files = []

    for root, _, files in os.walk(posts_dir):
        for file in files:
            if not file.endswith('.md'):  # Process only .md files
                continue

            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=posts_dir)
            
            current_hash = compute_file_hash(file_path)
            current_hashes[relative_path] = current_hash
            
            if relative_path in existing_hashes:
                if current_hash != existing_hashes[relative_path]:
                    changed_files.append(relative_path)
            else:
                changed_files.append(relative_path)

    update_hash_csv(hash_csv_path, current_hashes)
    return changed_files

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = changed_files(default_source_lang_code)
    if changed_files:
        print("Changed files:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("No files have changed.")

    os.chdir(initial_wd)
```

#### prompt.py
ቀደም ብለን የጻፍነውን ፕሮምፕት ይዘት ጨምሮ ፋይሉ ጥቂት ረጅም ስለሆነ፣ እዚህ በGitHub ሪፖዚቶሪ ውስጥ ወዳለው ምንጭ ፋይል አገናኝ ብቻ እተካዋለሁ።  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> በላይ ባለው አገናኝ ውስጥ በ `prompt.py`{: .filepath} ፋይል ያለው `max_tokens` ከContext window መጠን የተለየ ሆኖ ከፍተኛውን የውጤት ርዝመት የሚወስን ተለዋዋጭ ነው። Claude API ሲጠቀሙ በአንድ ጊዜ ማስገባት የሚቻለው Context window መጠን 200k token ነው (ወደ 680,000 ፊደላት የሚጠጋ መጠን)፣ ነገር ግን ከዚህ በተለየ ሁኔታ ለእያንዳንዱ ሞዴል የሚደገፈው ከፍተኛ የoutput token ብዛት ተወስኗል፤ ስለዚህ API ከመጠቀምዎ በፊት [የAnthropic ኦፊሴላዊ ሰነድ](https://docs.anthropic.com/en/docs/about-claude/models) ላይ አስቀድሞ ማረጋገጥ ይመከራል። የቀድሞው Claude 3 ተከታታይ ሞዴሎች እስከ 4096 token ድረስ ውጤት ማቅረብ ይችሉ ነበር፣ ግን በዚህ ብሎግ ጽሑፎች ላይ ሞክሬ እንደተገነዘብኩት በኮሪያኛ ወደ 8,000 ፊደላት የሚበልጥ ረጅም ፖስት ሲሆን በአንዳንድ የመድረሻ ቋንቋዎች 4096 token በመብለጥ የትርጉሙ ኋላ ክፍል ተቆርጦ የሚወጣ ችግር ነበር። Claude 3.5 Sonnet ግን ከፍተኛው የoutput token ብዛት ወደ 8192 በእጥፍ ስለጨመረ፣ በአብዛኛው ጊዜ ይህን ከፍተኛ ገደብ በመብለጥ ችግር አልተፈጠረም፤ ከClaude 3.7 ጀምሮ ከዚያም እጅግ ረጅም የሆነ ውጤት የሚደግፍ ማሻሻያ ተከናውኗል። በላይ ባለው GitHub ሪፖዚቶሪ ውስጥ በ `prompt.py`{: .filepath} ውስጥ `max_tokens=16384` ተደርጎ ተቀናብሯል።
{: .prompt-tip }

> Gemini በስፋት የሚበቃ ከፍተኛ የoutput token ገደብ ከጥንት ጀምሮ ነበረው፤ በGemini 2.5 Pro መሠረት እስከ 65536 token ድረስ ውጤት ማቅረብ ስለሚችል በአብዛኛው ጊዜ ይህን ገደብ መብለጥ አይገጥምም። [የGemini API ኦፊሴላዊ ሰነድ](https://ai.google.dev/gemini-api/docs/models#token-size) እንደሚለው፣ በGemini ሞዴል 1 token በእንግሊዝኛ 4 ፊደላት ያህል ሲሆን 100 token ደግሞ ወደ 60-80 የእንግሊዝኛ ቃላት ያህል ነው።
{: .prompt-tip }

#### translate_changes.py

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
#     "argparse",
# ]
# ///
import sys
import os
import subprocess
from tqdm import tqdm
import compare_hash
import prompt

def is_valid_file(filename):
    # 제외할 파일 패턴들
    excluded_patterns = [
        '.DS_Store',  # macOS 시스템 파일
        '~',          # 임시 파일
        '.tmp',       # 임시 파일
        '.temp',      # 임시 파일
        '.bak',       # 백업 파일
        '.swp',       # vim 임시 파일
        '.swo'        # vim 임시 파일
    ]
    
    # 파일명이 제외 패턴 중 하나라도 포함하면 False 반환
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin", "Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

def get_git_diff(filepath):
    """Get the diff of the file using git"""
    try:
        # Get the diff of the file
        result = subprocess.run(
            ['git', 'diff', '--unified=0', '--no-color', '--', filepath],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting git diff: {e}")
        return None

def translate_incremental(filepath, source_lang, target_lang, model):
    """Translate only the changed parts of a file using git diff"""
    # Get the git diff
    diff_output = get_git_diff(filepath)
    # print(f"Diff output: {diff_output}")
    if not diff_output:
        print(f"No changes detected or error getting diff for {filepath}")
        return
    
    # Call the translation function with the diff
    prompt.translate_with_diff(filepath, source_lang, target_lang, diff_output, model)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Translate markdown files with optional incremental updates')
    parser.add_argument('--incremental', action='store_true', 
                       help='Only translate changed parts of files using git diff')
    args, _ = parser.parse_known_args()
    
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    # Filter temporary files
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No files have changed.")
        
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    
    # Outer loop: Progress through changed files
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        
        # Inner loop: Progress through target languages
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            model = "gemini-2.5-pro" if target_lang in ["English", "Taiwanese Mandarin", "German"] else "claude-sonnet-4-20250514"
            if args.incremental:
                translate_incremental(filepath, source_lang, target_lang, model)
            else:
                prompt.translate(filepath, source_lang, target_lang, model)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### የPython ስክሪፕት አጠቃቀም
በJekyll ብሎግ መሠረት፣ በ `/_posts`{: .filepath} ዳይሬክቶሪ ውስጥ በ [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) የቋንቋ ኮዶች መሠረት `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath} ወዘተ እንደ ንዑስ ዳይሬክቶሪ ያዘጋጁ። ከዚያ `/_posts/ko`{: .filepath} ዳይሬክቶሪ ውስጥ የኮሪያኛ መነሻ ጽሑፎችን ያኑሩ (ወይም በPython ስክሪፕት ውስጥ `source_lang` ተለዋዋጩን እንደሚፈልጉት በመቀየር ከእሱ ጋር የሚዛመደውን የመነሻ ቋንቋ በተመለከተው ዳይሬክቶሪ ውስጥ ያኑሩ)። እንዲሁም በ `/tools`{: .filepath} ዳይሬክቶሪ ውስጥ ከላይ የተገለጹትን Python ስክሪፕቶችና `hash.csv`{: .filepath} ፋይሉን ያኑሩ፣ በዚያም ቦታ ተርሚናል ከፍተው ከታች ያለውን ትእዛዝ ያስኬዱ።

```bash
python3 translate_changes.py
```

ከዚያ ስክሪፕቱ ሲሰራ በታች እንደሚታየው ዓይነት ስክሪን ውጤት ይታያል።  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

ልዩ አማራጭ ካልገለጹ ነባሪው የሙሉ ትርጉም ሁኔታ ይሰራል፣ `--incremental` አማራጭን ከጨመሩ ግን የጭማሪ ትርጉም ባህሪን መጠቀም ይችላሉ።

```bash
python3 translate_changes.py --incremental
```

## የተግባር ልምድ
ቀደም ብዬ እንደጠቀስኩት፣ Claude Sonnet API በመጠቀም የፖስት ራስ-ሰር ትርጉምን በ12024 ዓ.ም ሰኔ መጨረሻ በዚህ ብሎግ ላይ ካስገባሁ በኋላ በቀጣይነት እያሻሻልኩ በተግባር እጠቀምበታለሁ። በአብዛኛው ጊዜ ሰው በተጨማሪ ሳይገባ ተፈጥሯዊ የሆነ ትርጉም ማግኘት ይቻላል፣ እና ፖስቶቹን ወደ ብዙ ቋንቋዎች ተርጉመን ካስቀመጥን በኋላ ከብራዚል፣ ካናዳ፣ አሜሪካ፣ ፈረንሳይ፣ ጃፓን ወዘተ ከኮሪያ ውጭ ክልሎች በፍለጋ በኩል የሚመጣ የOrganic Search ትራፊክ በእውነት እጅግ እንደጨመረ አረጋግጫለሁ። በተጨማሪም የተቀዳ ሴሽኖችን ሲመለከቱ በትርጉም ገጾች እንዲሁ የገቡ ጎብኚዎች ከጥቂት ደቂቃዎች እስከ ከብዙ አስር ደቂቃዎች በላይ በገፁ ላይ የሚቆዩ ጉዳዮች እጅግ አሉ፤ ብዙ ጊዜ ድረ-ገጹ ግልጽ የሆነ የማሽን ትርጉም የሚሰማ ያልተፈጥሯዊ ጽሑፍ ካለው ተጠቃሚዎች ወደ ኋላ በመሄድ ይወጣሉ ወይም በቀጥታ የእንግሊዝኛ ስሪት ይፈልጋሉ ብለን ካስበን፣ ይህ የትርጉሙ ጥራት እንኳ በነባር ተናጋሪዎች መለኪያ ላይ በጣም እንግዳ አይደለም ማለትን ያመለክታል። በተጨማሪም ይህ ከብሎጉ ትራፊክ አውጪ በላይ ለእኔ እንደ ጸሐፊው በመማር አይነት ተጨማሪ ጥቅሞችም አሉት፤ Claude ወይም Gemini ያሉ LLM-ዎች በተለይ በእንግሊዝኛ እጅግ ለስላሳ ጽሑፍ ስለሚፈጥሩ፣ ፖስቱን ወደ GitHub Pages ሪፖዚቶሪ Commit & Push ከማድረጌ በፊት በሚደረገው ግምገማ ውስጥ እኔ በኮሪያኛ የጻፍኳቸው የተወሰኑ ቃላት ወይም አገላለጾች በእንግሊዝኛ ተፈጥሯዊ እንዴት እንደሚገለጹ ለማየት ዕድል ይሰጣሉ። ይህ ብቻ በቂ የእንግሊዝኛ ትምህርት ነው ማለት አይቻልም፣ ግን ከዕለታዊ አገላለጾች በላይ በአካዳሚክ አገላለጾችና በቃላት ላይ የተፈጥሯዊ እንግሊዝኛ አገላለጽ ለማየት፣ ከሁሉም ጽሑፎች ይልቅ በጣም የማውቀውን እኔ ራሴ የጻፍኩትን ጽሑፍ እንደ ምሳሌ እያጠቀምኩ፣ ተጨማሪ ልዩ ጥረት ሳላደርግ በተደጋጋሚ መገናኘት እንኳ እንደ ኮሪያ ያሉ እንግሊዝኛ የማይነገርባቸው ክልሎች ውስጥ ለሚማሩ የምህንድስና ዲግሪ ተማሪዎች አስፈላጊ ጥቅም ያለው ነገር እንደሆነ ይመስለኛል።
