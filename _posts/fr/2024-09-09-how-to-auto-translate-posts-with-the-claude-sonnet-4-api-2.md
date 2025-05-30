---
title: Comment traduire automatiquement des posts avec l'API Claude Sonnet 4 (2) - Rédaction et application de scripts d'automatisation
description: "Conception d'un prompt pour la traduction multilingue de fichiers texte markdown, et processus d'automatisation du travail avec Python en appliquant la clé API obtenue d'Anthropic et le prompt rédigé. Ce post est le deuxième article de cette série, présentant l'émission d'API et l'intégration ainsi que la méthode de rédaction de scripts Python."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Introduction
Depuis l'introduction de l'API Claude 3.5 Sonnet d'Anthropic en juin 12024 pour la traduction multilingue des posts de blog, après plusieurs améliorations du prompt et du script d'automatisation, ainsi que des mises à niveau de version du modèle, j'utilise ce système de traduction de manière satisfaisante depuis près d'un an. Cette série vise donc à couvrir les raisons du choix du modèle Claude Sonnet lors du processus d'introduction, la méthode de conception du prompt, et la méthode d'implémentation de l'intégration API et de l'automatisation via des scripts Python.  
La série se compose de 2 articles, et celui que vous lisez est le deuxième article de cette série.
- 1ère partie : [Présentation du modèle Claude Sonnet et raisons de sélection, ingénierie de prompt](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- 2ème partie : Rédaction et application de scripts d'automatisation Python utilisant l'API (texte principal)

## Avant de commencer
Cet article fait suite à la [1ère partie](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1), donc si vous ne l'avez pas encore lu, il est recommandé de lire d'abord l'article précédent.

## Prompt système complété
Le résultat de la conception de prompt complété à travers [le processus présenté dans la 1ère partie](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#conception-du-prompt) est le suivant.

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

## Intégration de l'API Claude
### Émission de clé API Claude

> Ici, nous expliquons comment émettre une nouvelle clé API Claude. Si vous avez déjà une clé API à utiliser, vous pouvez ignorer cette étape.
{: .prompt-tip }

Accédez à <https://console.anthropic.com> et connectez-vous. Si vous n'avez pas encore de compte, vous devez d'abord vous inscrire. Une fois connecté, vous verrez l'écran de tableau de bord suivant.  
![Tableau de bord de la console Anthropic](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

Sur cet écran, cliquez sur le bouton 'Get API keys' pour voir l'écran suivant.  
![Clés API](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) J'ai déjà une clé créée, donc une clé nommée `yunseo-secret-key` s'affiche, mais si vous venez de créer un compte et n'avez pas encore émis de clé API, vous n'aurez probablement aucune clé en possession. Cliquez sur le bouton 'Create Key' en haut à droite pour émettre une nouvelle clé.

> Une fois l'émission de clé terminée, votre clé API s'affichera à l'écran, mais cette clé ne pourra plus être vérifiée par la suite, vous devez donc absolument la noter séparément dans un endroit sûr.
{: .prompt-warning }

### (Recommandé) Enregistrement de la clé API Claude dans les variables d'environnement
Pour utiliser l'API Claude dans des scripts Python ou Shell, vous devez charger la clé API. Il est possible d'enregistrer la clé API directement dans le script, mais si le script doit être téléchargé sur GitHub ou partagé avec d'autres personnes d'une autre manière, cette méthode ne peut pas être utilisée. De plus, même si vous n'aviez pas l'intention de partager le fichier script, il existe un risque que le fichier script soit divulgué par erreur involontaire, et si la clé API est enregistrée dans le fichier script, il y a un risque d'accident où la clé API soit également divulguée. Il est donc recommandé d'enregistrer la clé API dans les variables d'environnement du système que vous seul utilisez et de charger cette variable d'environnement dans le script. Ci-dessous, nous présentons la méthode d'enregistrement de la clé API dans les variables d'environnement système basée sur les systèmes UNIX. Pour Windows, veuillez vous référer à d'autres articles sur le web.

1. Dans le terminal, exécutez l'éditeur en tapant `nano ~/.bashrc` ou `nano ~/.zshrc` selon le type de shell que vous utilisez.
2. Ajoutez `export ANTHROPIC_API_KEY='your-api-key-here'` au contenu du fichier. Remplacez 'your-api-key-here' par votre clé API, et notez qu'il faut absolument l'entourer de guillemets simples.
3. Sauvegardez les modifications et quittez l'éditeur.
4. Exécutez `source ~/.bashrc` ou `source ~/.zshrc` dans le terminal pour appliquer les modifications.

### Installation des packages Python nécessaires
Si le package anthropic n'est pas installé dans votre environnement Python, installez-le avec la commande suivante.
```bash
pip3 install anthropic
```
De plus, les packages suivants sont également nécessaires pour utiliser le script de traduction de posts présenté plus loin, installez-les ou mettez-les à jour avec la commande suivante.
```bash
pip3 install -U argparse tqdm
```

### Rédaction de scripts Python
Le script de traduction de posts présenté dans cet article se compose de 3 fichiers de scripts Python et 1 fichier CSV suivants.

- `compare_hash.py`{: .filepath} : Calcule les valeurs de hachage SHA256 des posts originaux en coréen dans le répertoire `_posts/ko`{: .filepath}, puis les compare avec les valeurs de hachage existantes enregistrées dans le fichier `hash.csv`{: .filepath} pour retourner une liste des noms de fichiers modifiés ou nouvellement ajoutés
- `hash.csv`{: .filepath} : Fichier CSV enregistrant les valeurs de hachage SHA256 des fichiers de posts existants
- `prompt.py`{: .filepath} : Reçoit les valeurs filepath, source_lang, target_lang et charge la valeur de clé API Claude depuis les variables d'environnement système, puis appelle l'API et soumet le prompt rédigé précédemment comme prompt système et le contenu du post à traduire dans 'filepath' comme prompt utilisateur. Ensuite, reçoit la réponse (résultat de traduction) du modèle Claude Sonnet 4 et l'exporte comme fichier texte dans le chemin `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`{: .filepath} : Possède la variable chaîne source_lang et la variable liste 'target_langs', et appelle la fonction `changed_files()` dans `compare_hash.py`{: .filepath} pour recevoir la variable liste changed_files. S'il y a des fichiers modifiés, exécute une double boucle pour tous les fichiers dans la liste changed_files et tous les éléments dans la liste target_langs, et dans cette boucle, appelle la fonction `translate(filepath, source_lang, target_lang)` dans `prompt.py`{: .filepath} pour effectuer le travail de traduction.

Le contenu des fichiers scripts complétés peut également être consulté dans le dépôt GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
Comme le contenu du fichier est assez long car il inclut le contenu du prompt rédigé précédemment, nous le remplaçons par un lien vers le fichier source dans le dépôt GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> Dans le fichier `prompt.py`{: .filepath} du lien ci-dessus, `max_tokens` est une variable qui spécifie la longueur maximale de sortie, séparément de la taille de la fenêtre de contexte. Lors de l'utilisation de l'API Claude, la taille de la fenêtre de contexte qui peut être saisie en une fois est de 200k tokens (environ 680 000 caractères), mais séparément de cela, le nombre maximum de tokens de sortie pris en charge est défini pour chaque modèle, il est donc recommandé de vérifier à l'avance dans la [documentation officielle d'Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) avant d'utiliser l'API. Les modèles de la série Claude 3 existants pouvaient sortir jusqu'à 4096 tokens maximum, et lors des expérimentations avec les articles de ce blog, pour les posts d'une longueur assez longue d'environ 8000 caractères ou plus en coréen, il y avait des problèmes où la fin du texte traduit était coupée car cela dépassait 4096 tokens dans certaines langues de sortie. Dans le cas de Claude 3.5 Sonnet, le nombre maximum de tokens de sortie a doublé à 8192, donc il n'y avait généralement pas de problèmes dus au dépassement de ce nombre maximum de tokens de sortie, et depuis Claude 3.7, il a été mis à niveau pour prendre en charge des sorties de longueur beaucoup plus longue. Dans le `prompt.py`{: .filepath} du dépôt GitHub ci-dessus, `max_tokens=16384` est spécifié.
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
    # Modèles de fichiers à exclure
    excluded_patterns = [
        '.DS_Store',  # Fichier système macOS
        '~',          # Fichier temporaire
        '.tmp',       # Fichier temporaire
        '.temp',      # Fichier temporaire
        '.bak',       # Fichier de sauvegarde
        '.swp',       # Fichier temporaire vim
        '.swo'        # Fichier temporaire vim
    ]
    
    # Retourne False si le nom de fichier contient l'un des modèles d'exclusion
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
    # Filtrage des fichiers temporaires
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    # Boucle externe : progression des fichiers modifiés
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # Boucle interne : progression de traduction par langue pour chaque fichier
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### Méthode d'utilisation des scripts Python
Basé sur un blog Jekyll, créez des sous-répertoires par code de langue [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) dans le répertoire `/_posts`{: .filepath} comme `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Puis placez le texte original en coréen dans le répertoire `/_posts/ko`{: .filepath} (ou après avoir modifié la variable `source_lang` dans le script Python selon vos besoins, placez le texte original dans la langue correspondante dans le répertoire correspondant), placez les scripts Python présentés ci-dessus et le fichier `hash.csv`{: .filepath} dans le répertoire `/tools`{: .filepath}, puis ouvrez le terminal à cet emplacement et exécutez la commande suivante.

```bash
python3 translate_changes.py
```

Alors le script s'exécutera et l'écran suivant s'affichera.  
![Capture d'écran d'exécution du script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Capture d'écran d'exécution du script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

## Retour d'expérience d'utilisation réelle
Comme mentionné précédemment, j'ai introduit la traduction automatique de posts utilisant l'API Claude Sonnet fin juin 12024 sur ce blog et je l'utilise de manière satisfaisante en l'améliorant continuellement. Dans la plupart des cas, je peux recevoir des traductions naturelles sans intervention humaine supplémentaire, et après avoir publié les posts traduits en plusieurs langues, j'ai confirmé qu'un trafic de recherche organique considérable provenant de régions autres que la Corée comme le Brésil, le Canada, les États-Unis, la France et le Japon était effectivement généré. De plus, en vérifiant les sessions enregistrées, on peut voir que parmi les visiteurs arrivés via les versions traduites, il n'est pas rare qu'ils restent longtemps, de quelques minutes à plusieurs dizaines de minutes. Considérant que généralement, lorsque le contenu d'une page web semble manifestement être une traduction automatique maladroite, les gens cliquent sur le bouton retour ou cherchent plutôt la version anglaise, cela suggère que la qualité des traductions n'est pas très maladroite même selon les critères des locuteurs natifs. De plus, il y a eu des avantages supplémentaires du point de vue de l'apprentissage pour moi, l'auteur du blog, au-delà de l'afflux de trafic sur le blog. Comme Claude rédige des textes assez fluides en anglais, lors du processus de révision avant de faire un Commit & Push des posts vers le dépôt GitHub Pages, j'ai l'occasion de vérifier comment certains termes ou expressions de mon texte original coréen peuvent être exprimés naturellement en anglais. Bien que cela ne soit pas suffisant pour constituer un apprentissage complet de l'anglais, le fait de pouvoir fréquemment rencontrer des expressions anglaises naturelles pour des expressions non seulement quotidiennes mais aussi académiques et des termes, en utilisant comme exemples les textes que j'ai moi-même rédigés et qui me sont les plus familiers, sans effort supplémentaire, semble également agir comme un avantage considérable pour un étudiant de premier cycle en ingénierie d'un pays non anglophone comme la Corée.
