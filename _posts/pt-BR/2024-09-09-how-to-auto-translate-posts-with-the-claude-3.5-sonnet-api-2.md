---
title: Como traduzir posts automaticamente com a API Claude 3.5 Sonnet (2) - Escrevendo e aplicando scripts de automação
description: Aborda o processo de projetar prompts para tradução multilíngue de arquivos de texto markdown e automatizar o trabalho em Python usando a chave de API emitida pela Anthropic e os prompts criados. Este post é o segundo da série e introduz métodos para obter e integrar a API, bem como escrever scripts Python.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Introdução
Recentemente, implementei a API Claude 3.5 Sonnet da Anthropic para tradução multilíngue dos posts do blog. Nesta série, abordarei os motivos para escolher a API Claude 3.5 Sonnet, métodos de design de prompts e como implementar a automação através de scripts Python conectados à API.  
A série consiste em 2 posts, e este que você está lendo é o segundo post da série.
- Parte 1: [Introdução ao modelo Claude 3.5 Sonnet, razões para seleção e engenharia de prompts](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Parte 2: Escrevendo e aplicando scripts de automação Python usando a API (este post)

## Antes de começar
Este post é uma continuação da [Parte 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1), então recomendo ler o post anterior primeiro se ainda não o fez.

## Integração da API Claude
### Obtendo uma chave de API Claude

> Esta seção explica como obter uma nova chave de API Claude. Se você já possui uma chave de API para usar, pode pular esta etapa.
{: .prompt-tip }

Acesse <https://console.anthropic.com> e faça login. Se você ainda não tem uma conta, precisará se cadastrar primeiro. Após fazer login, você verá uma tela de painel como a mostrada abaixo.  
![Painel do Console Anthropic](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Clique no botão 'Get API keys' nesta tela para ver a seguinte tela.  
![Chaves de API](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Como já tenho uma chave criada, uma chave chamada `yunseo-secret-key` é exibida, mas se você acabou de criar sua conta e ainda não obteve uma chave de API, provavelmente não terá nenhuma chave listada. Basta clicar no botão 'Create Key' no canto superior direito para obter uma nova chave.

> Quando você terminar de obter a chave, sua chave de API será exibida na tela. Como essa chave não poderá ser visualizada novamente posteriormente, certifique-se de registrá-la separadamente em um local seguro.
{: .prompt-warning }

### (Recomendado) Registrar a chave de API Claude como variável de ambiente
Para utilizar a API Claude em scripts Python ou Shell, é necessário carregar a chave de API. Embora seja possível registrar a chave de API diretamente no script, isso não é viável se você precisar fazer upload do script no GitHub ou compartilhá-lo com outras pessoas de alguma forma. Além disso, mesmo que você não planeje compartilhar o arquivo do script, há o risco de vazamento acidental da chave de API se ela estiver registrada no arquivo do script. Portanto, recomenda-se registrar a chave de API como uma variável de ambiente no sistema que apenas você usa e, em seguida, carregar essa variável de ambiente no script. Abaixo, introduzimos como registrar a chave de API como uma variável de ambiente do sistema, com base em sistemas UNIX. Para Windows, consulte outros artigos na web.

1. No terminal, execute `nano ~/.bashrc` ou `nano ~/.zshrc`, dependendo do shell que você usa, para abrir o editor.
2. Adicione `export ANTHROPIC_API_KEY='your-api-key-here'` ao conteúdo do arquivo. Substitua 'your-api-key-here' pela sua chave de API real, e note que deve ser envolvida por aspas simples.
3. Salve as alterações e saia do editor.
4. Execute `source ~/.bashrc` ou `source ~/.zshrc` no terminal para aplicar as alterações.

### Instalando os pacotes Python necessários
Se o pacote anthropic não estiver instalado no seu ambiente Python, instale-o com o seguinte comando:
```bash
pip3 install anthropic
```
Além disso, os seguintes pacotes também são necessários para usar o script de tradução de posts que será introduzido mais adiante, então instale-os ou atualize-os com o seguinte comando:
```bash
pip3 install -U argparse tqdm
```

### Escrevendo scripts Python
O script de tradução de posts que será introduzido neste artigo consiste em 3 arquivos de script Python e 1 arquivo CSV:

- `compare_hash.py`: Calcula os valores de hash SHA256 dos posts originais em coreano no diretório `_posts/ko`{: .filepath}, compara com os valores de hash existentes registrados no arquivo `hash.csv` e retorna uma lista de nomes de arquivos alterados ou recém-adicionados
- `hash.csv`: Arquivo CSV que registra os valores de hash SHA256 dos arquivos de posts existentes
- `prompt.py`: Recebe os valores de filepath, source_lang, target_lang, carrega o valor da chave de API Claude da variável de ambiente do sistema, chama a API e submete o prompt que escrevemos anteriormente como prompt do sistema e o conteúdo do post a ser traduzido em 'filepath' como prompt do usuário. Em seguida, recebe a resposta (resultado da tradução) do modelo Claude 3.5 Sonnet e a grava como um arquivo de texto no caminho `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`: Possui uma variável de string source_lang e uma lista 'target_langs', chama a função `changed_files()` em `compare_hash.py` para receber a lista de variáveis changed_files. Se houver arquivos alterados, executa um loop duplo para todos os arquivos na lista changed_files e todos os elementos na lista target_langs, chamando a função `translate(filepath, source_lang, target_lang)` em `prompt.py` dentro desse loop para realizar a tarefa de tradução.

O conteúdo dos arquivos de script completos também pode ser encontrado no repositório GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
    # Ordena os hashes dos arquivos pelo nome do arquivo (as chaves do dicionário)
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
            if not file.endswith('.md'):  # Processa apenas arquivos .md
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
        print("Arquivos alterados:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("Nenhum arquivo foi alterado.")

    os.chdir(initial_wd)
```

#### prompt.py
Como o conteúdo inclui o prompt que escrevemos anteriormente e o arquivo é um pouco longo, substituímos pelo link do arquivo fonte no repositório GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> No arquivo `prompt.py` no link acima, `max_tokens` é uma variável que especifica o comprimento máximo de saída, separadamente do tamanho da janela de contexto. Ao usar a API Claude, o tamanho da janela de contexto que pode ser inserida de uma vez é de 200k tokens (cerca de 680.000 caracteres), mas separadamente disso, há um número máximo de tokens de saída suportado para cada modelo, então é recomendado verificar antecipadamente na [documentação oficial da Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) antes de usar a API. Os modelos da série Claude 3 anteriores podiam produzir até 4096 tokens, e embora não houvesse problemas com a maioria dos posts deste blog nos testes, para alguns posts mais longos com cerca de 8000 caracteres ou mais em coreano, ocorreu um problema em que a parte final da tradução era cortada em alguns idiomas de saída por exceder 4096 tokens. No caso do Claude 3.5 Sonnet, o número máximo de tokens de saída dobrou para 8192, então raramente houve problemas excedendo esse limite máximo de tokens de saída, e no `prompt.py` do repositório GitHub acima, também foi especificado `max_tokens=8192`.
{: .prompt-tip }

#### translate_changes.py

```python
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

def is_valid_file(filename):
    # Padrões de arquivos a serem excluídos
    excluded_patterns = [
        '.DS_Store',  # Arquivo de sistema macOS
        '~',          # Arquivo temporário
        '.tmp',       # Arquivo temporário
        '.temp',      # Arquivo temporário
        '.bak',       # Arquivo de backup
        '.swp',       # Arquivo temporário vim
        '.swo'        # Arquivo temporário vim
    ]
    
    # Retorna False se o nome do arquivo incluir qualquer um dos padrões de exclusão
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin","Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    # Filtragem de arquivos temporários
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("Nenhum arquivo foi alterado.")
    print("Arquivos alterados:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Início da tradução! ***")
    # Loop externo: progresso dos arquivos alterados
    for changed_file in tqdm(changed_files, desc="Arquivos", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # Loop interno: progresso da tradução por idioma para cada arquivo
        for target_lang in tqdm(target_langs, desc="Idiomas", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nTradução concluída!")
    os.chdir(initial_wd)
```

### Como usar os scripts Python
Com base em um blog Jekyll, crie subdiretórios para cada código de idioma [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) dentro do diretório `/_posts`{: .filepath} onde os posts estão localizados, como `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Em seguida, coloque os scripts Python e o arquivo CSV mencionados acima no diretório `/tools`{: .filepath}, abra um terminal nesse local e execute o seguinte comando:

```bash
python3 translate_changes.py
```

O script será executado e você verá uma tela como esta:  
![Captura de tela da execução do script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Captura de tela da execução do script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Experiência de uso real
Como mencionado acima, estou usando a tradução automática de posts usando a API Claude 3.5 neste blog há cerca de 2 meses. Na maioria dos casos, é possível obter traduções de excelente qualidade sem necessidade de intervenção humana adicional, e após publicar posts traduzidos em vários idiomas, confirmei que o tráfego de Organic Search através de buscas de regiões fora da Coreia, como Brasil, Canadá, Estados Unidos e França, está realmente chegando. Além do tráfego do blog, houve vantagens adicionais em termos de aprendizado para o autor do post. Como o Claude produz textos bastante fluentes em inglês, durante o processo de revisão antes de fazer o Push dos posts para o repositório do GitHub Pages, tenho a oportunidade de verificar como certos termos ou expressões que escrevi no texto original em coreano são naturalmente expressos em inglês. Embora isso por si só não seja suficiente para um aprendizado completo de inglês, para um estudante de graduação em engenharia de um país não anglófono como a Coreia, parece ser uma vantagem considerável poder frequentemente encontrar expressões naturais em inglês, não apenas cotidianas, mas também acadêmicas e terminológicas, usando como exemplo o texto que eu mesmo escrevi, que é mais familiar do que qualquer outro, sem nenhum esforço adicional.
