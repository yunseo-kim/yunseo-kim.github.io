---
title: Como traduzir posts automaticamente com a API do Claude 3.5 Sonnet (2) - Escrevendo e aplicando scripts de automação
description: >-
  Aborda o processo de design de prompts para aplicar na tradução multilíngue dos posts deste blog, e como automatizar o trabalho em Python usando a chave API obtida da Anthropic e os prompts criados. Este é o segundo post da série, que introduz a obtenção e integração da API e os métodos de escrita de scripts Python.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introdução
Recentemente, implementei a API do Claude 3.5 Sonnet da Anthropic para tradução multilíngue dos posts do blog. Nesta série, abordaremos os motivos para escolher a API do Claude 3.5 Sonnet, os métodos de design de prompts e como implementar a integração e automação da API através de scripts Python.  
A série consiste em 2 posts, e este que você está lendo é o segundo post da série.
- Parte 1: [Introdução ao modelo Claude 3.5 Sonnet, motivos da seleção e engenharia de prompts](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Parte 2: Escrevendo e aplicando scripts de automação Python usando a API (este post)

## Antes de começar
Este post é uma continuação da [Parte 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1), então recomendo ler o post anterior primeiro se ainda não o fez.

## Integração com a API do Claude
### Obtendo a chave API do Claude

> Esta seção explica como obter uma nova chave API do Claude. Se você já possui uma chave API para usar, pode pular esta etapa.
{: .prompt-tip }

Acesse <https://console.anthropic.com> e faça login. Se ainda não tiver uma conta, precisará se registrar primeiro. Após fazer login, você verá uma tela de dashboard como a mostrada abaixo.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Clique no botão 'Get API keys' nesta tela e você verá a seguinte tela.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Como já tenho uma chave criada, aparece uma chave chamada `yunseo-secret-key`, mas se você acabou de criar sua conta e ainda não obteve uma chave API, provavelmente não terá nenhuma chave listada. Basta clicar no botão 'Create Key' no canto superior direito para gerar uma nova chave.

> Quando terminar de gerar a chave, sua chave API será exibida na tela, mas não será possível verificá-la novamente depois, então certifique-se de registrá-la em um local seguro.
{: .prompt-warning }

### (Recomendado) Registrando a chave API do Claude como variável de ambiente
Para usar a API do Claude em scripts Python ou Shell, você precisa carregar a chave API. Embora seja possível registrar a chave API no próprio script, isso não é viável se você precisar compartilhar o script com outras pessoas através do GitHub ou outros meios. Além disso, mesmo que você não planeje compartilhar o arquivo do script, existe o risco de vazamento acidental da chave API se ela estiver registrada no arquivo do script. Portanto, recomenda-se registrar a chave API como uma variável de ambiente no sistema que apenas você usa e carregar essa variável de ambiente no script. Abaixo, introduzimos como registrar a chave API como uma variável de ambiente do sistema baseado em UNIX. Para Windows, consulte outros artigos na web.

1. No terminal, execute `nano ~/.bashrc` ou `nano ~/.zshrc` dependendo do seu shell para abrir o editor.
2. Adicione `export ANTHROPIC_API_KEY='your-api-key-here'` ao conteúdo do arquivo. Substitua 'your-api-key-here' pela sua chave API e note que deve ser envolvida por aspas simples.
3. Salve as alterações e saia do editor.
4. Execute `source ~/.bashrc` ou `source ~/.zshrc` no terminal para aplicar as alterações.

### Instalando os pacotes Python necessários
Se o pacote anthropic não estiver instalado no seu ambiente Python, instale-o com o seguinte comando:
```bash
pip3 install anthropic
```
Além disso, os seguintes pacotes também são necessários para usar o script de tradução de posts que apresentaremos a seguir, então instale ou atualize-os com o seguinte comando:
```bash
pip3 install -U argparse tqdm
```

### Escrevendo scripts Python
O script de tradução de posts que apresentaremos neste artigo consiste em 3 arquivos Python e 1 arquivo CSV.

- `compare_hash.py`: Calcula os valores hash SHA256 dos posts originais em coreano no diretório `_posts/ko`{: .filepath} e compara com os valores hash existentes registrados no arquivo `hash.csv` para retornar uma lista de nomes de arquivos alterados ou recém-adicionados
- `hash.csv`: Arquivo CSV que registra os valores hash SHA256 dos arquivos de posts existentes
- `prompt.py`: Recebe valores filepath, source_lang, target_lang e carrega o valor da chave API do Claude das variáveis de ambiente do sistema, então chama a API usando o prompt que criamos anteriormente como prompt do sistema e o conteúdo do post a ser traduzido em 'filepath' como prompt do usuário. Em seguida, recebe a resposta (resultado da tradução) do modelo Claude 3.5 Sonnet e salva como arquivo de texto no caminho `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`: Possui uma variável string source_lang e uma lista 'target_langs', chama a função `changed_files()` de `compare_hash.py` para receber a lista changed_files. Se houver arquivos alterados, executa um loop duplo para todos os arquivos na lista changed_files e todos os elementos na lista target_langs, chamando a função `translate(filepath, source_lang, target_lang)` de `prompt.py` dentro desse loop para realizar a tradução.

O conteúdo dos scripts completos também pode ser encontrado no repositório GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

#### compare_hash.py

```python
import os
import hashlib
import csv

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

def changed_files():
    posts_dir = '../_posts/ko/'
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

    changed_files = changed_files()
    if changed_files:
        print("Changed files:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("No files have changed.")

    os.chdir(initial_wd)
```

#### prompt.py
Como inclui o conteúdo do prompt que criamos anteriormente e o arquivo é um pouco longo, substituímos pelo link do arquivo fonte no repositório GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> No arquivo `prompt.py` do link acima, `max_tokens` é uma variável que especifica o comprimento máximo de saída, independentemente do tamanho da janela de contexto. Ao usar a API do Claude, você pode inserir até 200k tokens (aproximadamente 680.000 caracteres) na janela de contexto de uma vez, mas separadamente, cada modelo tem um número máximo de tokens de saída suportado, então recomenda-se verificar antecipadamente na [documentação oficial da Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) antes de usar a API. Os modelos anteriores da série Claude 3 podiam gerar até 4096 tokens, e embora isso não tenha sido um problema para a maioria dos posts deste blog em nossos experimentos, alguns posts mais longos com mais de 8000 caracteres em coreano tiveram problemas com a parte final da tradução sendo cortada em algumas línguas de saída por exceder 4096 tokens. No caso do Claude 3.5 Sonnet, o número máximo de tokens de saída dobrou para 8192, então raramente houve problemas excedendo este limite máximo de tokens de saída, e no `prompt.py` do repositório GitHub acima, também definimos `max_tokens=8192`.
{: .prompt-tip }

#### translate_changes.py

```python
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

posts_dir = '../_posts/ko/'
source_lang = "Korean"
target_langs = ["English", "Spanish", "Brazilian Portuguese", "Japanese", "French", "German"]

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files()
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    for changed_file in changed_files:
        print(f"- Translating {changed_file}")
        filepath = os.path.join(posts_dir, changed_file)
        for target_lang in tqdm(target_langs):
            prompt.translate(filepath, source_lang, target_lang)
    
    os.chdir(initial_wd)
```

### Como usar os scripts Python
Para blogs Jekyll, crie subdiretórios por código de idioma [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) dentro do diretório `/_posts`{: .filepath} onde os posts estão localizados, como `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Em seguida, coloque os scripts Python e o arquivo CSV apresentados acima no diretório `/tools`{: .filepath}, abra o terminal nessa localização e execute o seguinte comando:

```bash
python3 translate_changes.py
```

O script será executado e você verá uma tela como esta:  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Experiência de uso real
Como mencionado acima, venho usando a tradução automática de posts usando a API do Claude 3.5 neste blog por cerca de 2 meses. Na maioria dos casos, é possível receber traduções de alta qualidade sem necessidade de intervenção humana adicional, e após publicar posts traduzidos em vários idiomas, confirmei que há tráfego orgânico real através de pesquisas de regiões fora da Coreia, como Brasil, Canadá, Estados Unidos e França. Além do tráfego do blog, também houve benefícios adicionais em termos de aprendizado para o autor do post, pois como o Claude produz textos muito fluentes em inglês, durante o processo de revisão antes de fazer push dos posts para o repositório do GitHub Pages, tenho a oportunidade de verificar como certos termos ou expressões que escrevi em coreano podem ser naturalmente expressos em inglês. Embora isso sozinho não seja suficiente para um aprendizado completo do inglês, para um estudante de graduação em engenharia de um país não anglófono como a Coreia, parece ser bastante vantajoso poder frequentemente encontrar expressões naturais em inglês, tanto cotidianas quanto acadêmicas, usando como exemplo o texto que eu mesmo escrevi, que é mais familiar do que qualquer outro texto, sem necessidade de esforço adicional.
