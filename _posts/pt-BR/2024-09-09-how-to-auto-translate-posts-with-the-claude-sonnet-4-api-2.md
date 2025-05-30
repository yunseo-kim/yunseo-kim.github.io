---
title: Como traduzir posts automaticamente com a API do Claude Sonnet 4 (2) - Criação e aplicação de script de automação
description: "Aborda o processo de design de prompts para tradução multilíngue de arquivos de texto markdown e automação do trabalho com Python aplicando a chave API obtida da Anthropic e o prompt criado. Este post é o segundo da série, apresentando métodos de emissão de API, integração e criação de scripts Python."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Introdução
Desde a introdução da API do Claude 3.5 Sonnet da Anthropic em junho de 12024 para tradução multilíngue de posts do blog, após várias melhorias de prompt e script de automação, além de atualizações de versão do modelo, venho operando esse sistema de tradução de forma satisfatória por quase um ano. Nesta série, pretendo abordar as razões para escolher o modelo Claude Sonnet no processo de introdução, métodos de design de prompt e métodos de implementação de integração de API e automação através de scripts Python.  
A série consiste em 2 artigos, e este artigo que você está lendo é o segundo da série.
- Parte 1: [Introdução ao modelo Claude Sonnet e razões para seleção, engenharia de prompt](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- Parte 2: Criação e aplicação de script de automação Python usando API (texto atual)

## Antes de começar
Este artigo é uma continuação da [Parte 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1), então se ainda não leu, recomendo ler o artigo anterior primeiro.

## Prompt do sistema completo
O resultado do design de prompt completado através do [processo apresentado na Parte 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#design-de-prompt) é o seguinte.

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
or something of that nature!!</important>
```

## Integração da API Claude
### Emissão de chave API Claude

> Aqui explico como emitir uma nova chave API Claude. Se já possui uma chave API para usar, pode pular esta etapa.
{: .prompt-tip }

Acesse <https://console.anthropic.com> e faça login. Se ainda não tem uma conta, deve primeiro fazer o cadastro. Após o login, verá uma tela de dashboard como a seguinte.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

Nesta tela, clique no botão 'Get API keys' para ver a seguinte tela.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) Como já tenho uma chave criada, aparece uma chave chamada `yunseo-secret-key`, mas se acabou de criar a conta e ainda não emitiu uma chave API, provavelmente não terá nenhuma chave. Clique no botão 'Create Key' no canto superior direito para emitir uma nova chave.

> Após completar a emissão da chave, sua chave API será exibida na tela, mas como não poderá verificá-la novamente depois, certifique-se de anotá-la em um local seguro.
{: .prompt-warning }

### (Recomendado) Registrar chave API Claude nas variáveis de ambiente
Para usar a API Claude em scripts Python ou Shell, é necessário carregar a chave API. Embora seja possível registrar a chave API no próprio script, se for um script que precisa ser carregado no GitHub ou compartilhado com outras pessoas de outras formas, este método não pode ser usado. Além disso, mesmo que não tenha intenção de compartilhar o arquivo de script, existe o risco de o arquivo de script vazar por engano, e se a chave API estiver registrada no arquivo de script, pode ocorrer o acidente de a chave API também vazar junto. Portanto, recomenda-se registrar a chave API nas variáveis de ambiente do sistema que apenas você usa e carregar essa variável de ambiente no script. Abaixo apresento como registrar a chave API nas variáveis de ambiente do sistema baseado em sistemas UNIX. Para Windows, consulte outros artigos na web.

1. No terminal, execute `nano ~/.bashrc` ou `nano ~/.zshrc` de acordo com o tipo de shell que usa para executar o editor.
2. Adicione `export ANTHROPIC_API_KEY='your-api-key-here'` ao conteúdo do arquivo. Substitua 'your-api-key-here' pela sua chave API, e note que deve envolver com aspas simples.
3. Salve as alterações e saia do editor.
4. Execute `source ~/.bashrc` ou `source ~/.zshrc` no terminal para aplicar as alterações.

### Instalação de pacotes Python necessários
Se o pacote anthropic não estiver instalado no ambiente Python que você usa, instale com o seguinte comando.
```bash
pip3 install anthropic
```
Além disso, os seguintes pacotes também são necessários para usar o script de tradução de posts que será apresentado posteriormente, então instale ou atualize com o seguinte comando.
```bash
pip3 install -U argparse tqdm
```

### Criação de script Python
O script de tradução de posts apresentado neste artigo consiste em 3 arquivos de script Python e 1 arquivo CSV.

- `compare_hash.py`{: .filepath}: Calcula os valores hash SHA256 dos posts originais em coreano no diretório `_posts/ko`{: .filepath} e compara com os valores hash existentes registrados no arquivo `hash.csv`{: .filepath} para retornar uma lista de nomes de arquivos alterados ou recém-adicionados
- `hash.csv`{: .filepath}: Arquivo CSV que registra os valores hash SHA256 dos arquivos de posts existentes
- `prompt.py`{: .filepath}: Recebe valores de filepath, source_lang, target_lang e carrega o valor da chave API Claude das variáveis de ambiente do sistema, depois chama a API e submete o prompt criado anteriormente como prompt do sistema e o conteúdo do post a ser traduzido em 'filepath' como prompt do usuário. Depois recebe a resposta (resultado da tradução) do modelo Claude Sonnet 4 e produz como arquivo de texto no caminho `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`{: .filepath}: Possui a variável string source_lang e a variável lista 'target_langs', chama a função `changed_files()` em `compare_hash.py`{: .filepath} para receber a variável lista changed_files. Se houver arquivos alterados, executa um loop duplo para todos os arquivos na lista changed_files e todos os elementos na lista target_langs, e dentro desse loop chama a função `translate(filepath, source_lang, target_lang)` em `prompt.py`{: .filepath} para executar o trabalho de tradução.

O conteúdo dos arquivos de script completos também pode ser verificado no repositório GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
Como o conteúdo do arquivo é longo devido à inclusão do conteúdo do prompt criado anteriormente, substituo pelo link do arquivo fonte no repositório GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> No arquivo `prompt.py`{: .filepath} do link acima, `max_tokens` é uma variável que especifica o comprimento máximo de saída separadamente do tamanho da janela de contexto. Ao usar a API Claude, o tamanho da janela de contexto que pode ser inserido de uma vez é de 200k tokens (aproximadamente 680.000 caracteres), mas separadamente disso, há um número máximo de tokens de saída suportado para cada modelo, então recomenda-se verificar antecipadamente na [documentação oficial da Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) antes de usar a API. Os modelos da série Claude 3 existentes podiam produzir até 4096 tokens, mas quando testei com os artigos deste blog, para posts um pouco longos com mais de 8000 caracteres em coreano, ocorreu o problema de exceder 4096 tokens em alguns idiomas de saída, cortando a parte final da tradução. No caso do Claude 3.5 Sonnet, o número máximo de tokens de saída dobrou para 8192, então raramente houve problemas por exceder esse número máximo de tokens de saída, e a partir do Claude 3.7, foi atualizado para suportar saídas muito mais longas. No `prompt.py`{: .filepath} do repositório GitHub acima, está especificado como `max_tokens=16384`.
{: .prompt-tip }

#### translate_changes.py

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
# ]
# ///
import sys
import os
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

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    # 임시 파일 필터링
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    # 외부 루프: 변경된 파일 진행상황
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # 내부 루프: 각 파일의 언어별 번역 진행상황
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### Como usar o script Python
Baseado em blog Jekyll, dentro do diretório `/_posts`{: .filepath}, crie subdiretórios por código de idioma [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) como `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Coloque o texto original em coreano no diretório `/_posts/ko`{: .filepath} (ou modifique a variável `source_lang` no script Python conforme necessário e coloque o texto original no idioma correspondente no diretório correspondente), coloque os scripts Python apresentados acima e o arquivo `hash.csv`{: .filepath} no diretório `/tools`{: .filepath}, abra o terminal nessa localização e execute o seguinte comando.

```bash
python3 translate_changes.py
```

Então o script será executado e uma tela como a seguinte será exibida.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

## Experiência de uso real
Como mencionado anteriormente, introduzi a tradução automática de posts usando a API Claude Sonnet no final de junho de 12024 neste blog e venho utilizando com melhorias contínuas. Na maioria dos casos, posso receber traduções naturais sem necessidade de intervenção humana adicional, e após publicar posts traduzidos em múltiplos idiomas, confirmei que há um influxo considerável de tráfego de Busca Orgânica através de pesquisas de regiões fora da Coreia, como Brasil, Canadá, Estados Unidos, França e Japão. Além disso, verificando as sessões gravadas, não são poucos os visitantes que chegaram através das traduções e permanecem por vários minutos ou até dezenas de minutos, o que sugere que a qualidade das traduções não é muito estranha mesmo para falantes nativos, considerando que normalmente quando o conteúdo de uma página web mostra sinais óbvios de tradução automática estranha, as pessoas clicam em voltar ou procuram a versão em inglês. Além do influxo de tráfego do blog, também houve vantagens adicionais do ponto de vista de aprendizado para mim como autor dos artigos, pois como Claude escreve textos bastante fluidos em inglês, no processo de revisão antes de fazer Commit & Push dos posts no repositório GitHub Pages, tenho a oportunidade de verificar como expressar naturalmente em inglês certos termos ou expressões do meu texto original em coreano. Embora isso sozinho não seja suficiente para um aprendizado completo de inglês, para um estudante de graduação em engenharia de um país não anglófono como a Coreia, poder ter contato frequente com expressões naturais em inglês não apenas cotidianas, mas também acadêmicas e terminológicas, usando como exemplo o texto mais familiar - o que eu mesmo escrevi - sem esforço adicional, parece ser uma vantagem considerável.
