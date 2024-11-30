---
title: Comment traduire automatiquement des articles avec l'API Claude 3.5 Sonnet (2) - Rédaction et application d'un script d'automatisation
description: >-
  Cet article traite de la conception d'un prompt pour la traduction multilingue de fichiers texte en markdown, et du processus d'automatisation en Python en utilisant la clé API fournie par Anthropic et le prompt rédigé. Ce post est le deuxième de la série, présentant la méthode d'obtention et d'intégration de l'API ainsi que la rédaction du script Python.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introduction
J'ai récemment adopté l'API Claude 3.5 Sonnet d'Anthropic pour la traduction multilingue des articles de blog. Dans cette série, nous aborderons les raisons du choix de l'API Claude 3.5 Sonnet, la méthode de conception des prompts, ainsi que l'implémentation de l'intégration API et de l'automatisation via des scripts Python.  
La série se compose de deux articles, et celui-ci est le second.
- Partie 1 : [Présentation du modèle Claude 3.5 Sonnet, raisons de la sélection et prompt engineering](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Partie 2 : Création et application du script d'automatisation Python utilisant l'API (cet article)

## Avant de commencer
Cet article fait suite à la [Partie 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1), il est donc recommandé de lire d'abord l'article précédent si vous ne l'avez pas encore fait.

## Intégration de l'API Claude
### Obtention de la clé API Claude

> Cette section explique comment obtenir une nouvelle clé API Claude. Si vous disposez déjà d'une clé API à utiliser, vous pouvez passer cette étape.
{: .prompt-tip }

Connectez-vous à <https://console.anthropic.com>. Si vous n'avez pas encore de compte, vous devrez d'abord vous inscrire. Une fois connecté, vous verrez un tableau de bord comme ci-dessous.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

En cliquant sur le bouton 'Get API keys' sur cet écran, vous verrez l'écran suivant.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Comme j'ai déjà créé une clé, une clé nommée `yunseo-secret-key` est affichée, mais si vous venez de créer votre compte et n'avez pas encore obtenu de clé API, vous n'aurez probablement aucune clé listée. Cliquez sur le bouton 'Create Key' en haut à droite pour obtenir une nouvelle clé.

> Une fois la clé générée, elle s'affichera à l'écran, mais vous ne pourrez plus la consulter ultérieurement, alors assurez-vous de la noter dans un endroit sûr.
{: .prompt-warning }

### (Recommandé) Enregistrement de la clé API Claude dans les variables d'environnement
Pour utiliser l'API Claude dans Python ou des scripts Shell, vous devez charger la clé API. Bien qu'il soit possible d'enregistrer la clé API directement dans le script, cette méthode n'est pas utilisable si vous devez partager le script avec d'autres personnes via GitHub ou d'autres moyens. De plus, même si vous n'aviez pas l'intention de partager le fichier de script, il existe un risque que la clé API soit divulguée en cas de fuite accidentelle du fichier de script. Il est donc recommandé d'enregistrer la clé API dans les variables d'environnement de votre système et de la charger depuis le script. Voici comment enregistrer la clé API dans les variables d'environnement système sous UNIX. Pour Windows, veuillez consulter d'autres ressources en ligne.

1. Dans le terminal, lancez l'éditeur en tapant `nano ~/.bashrc` ou `nano ~/.zshrc` selon votre shell.
2. Ajoutez `export ANTHROPIC_API_KEY='your-api-key-here'` au contenu du fichier. Remplacez 'your-api-key-here' par votre clé API et notez qu'elle doit être entourée de guillemets simples.
3. Sauvegardez les modifications et quittez l'éditeur.
4. Exécutez `source ~/.bashrc` ou `source ~/.zshrc` dans le terminal pour appliquer les changements.

### Installation des packages Python nécessaires
Si le package anthropic n'est pas installé dans votre environnement Python, installez-le avec la commande suivante :
```bash
pip3 install anthropic
```
De plus, les packages suivants sont nécessaires pour utiliser le script de traduction des articles que nous présenterons plus tard, alors installez-les ou mettez-les à jour avec cette commande :
```bash
pip3 install -U argparse tqdm
```

### Écriture des scripts Python
Le script de traduction des articles que nous allons présenter se compose de trois fichiers Python et d'un fichier CSV.

- `compare_hash.py` : Calcule les valeurs de hachage SHA256 des articles originaux en coréen dans le répertoire `_posts/ko`{: .filepath} et renvoie une liste des noms de fichiers modifiés ou nouvellement ajoutés en comparant avec les valeurs de hachage existantes enregistrées dans le fichier `hash.csv`
- `hash.csv` : Fichier CSV enregistrant les valeurs de hachage SHA256 des fichiers d'articles existants
- `prompt.py` : Reçoit les valeurs filepath, source_lang, target_lang et charge la valeur de la clé API Claude depuis les variables d'environnement système, puis appelle l'API en utilisant le prompt créé précédemment comme prompt système et le contenu de l'article à traduire comme prompt utilisateur. Reçoit ensuite la réponse (résultat de traduction) du modèle Claude 3.5 Sonnet et l'écrit dans un fichier texte au chemin `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py` : Contient la variable chaîne source_lang et la liste target_langs, appelle la fonction `changed_files()` de `compare_hash.py` pour obtenir la liste changed_files. S'il y a des fichiers modifiés, exécute une double boucle sur tous les fichiers de la liste changed_files et tous les éléments de la liste target_langs, et dans cette boucle, appelle la fonction `translate(filepath, source_lang, target_lang)` de `prompt.py` pour effectuer la traduction.

Le contenu des scripts complets est également disponible sur le dépôt GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
Comme le fichier contient le contenu du prompt créé précédemment et est assez long, nous le remplaçons par un lien vers le fichier source sur le dépôt GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> Dans le fichier `prompt.py` du lien ci-dessus, `max_tokens` est une variable qui spécifie la longueur maximale de sortie indépendamment de la taille de la fenêtre de contexte. Bien que la taille de la fenêtre de contexte que vous pouvez entrer en une fois lors de l'utilisation de l'API Claude soit de 200k tokens (environ 680 000 caractères), chaque modèle a un nombre maximum de tokens de sortie défini séparément, il est donc recommandé de vérifier à l'avance dans la [documentation officielle d'Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) avant d'utiliser l'API. Les modèles Claude 3 précédents pouvaient produire jusqu'à 4096 tokens, et bien que cela n'ait pas posé de problème pour la majorité des articles de ce blog lors des tests, certains articles plus longs (plus de 8000 caractères en coréen) ont rencontré des problèmes de troncature de la fin de la traduction dans certaines langues de sortie en dépassant les 4096 tokens. Dans le cas de Claude 3.5 Sonnet, le nombre maximum de tokens de sortie a doublé à 8192, donc il n'y a généralement pas eu de problèmes de dépassement de cette limite, et dans le fichier `prompt.py` du dépôt GitHub ci-dessus, `max_tokens=8192` est spécifié.
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

### Comment utiliser les scripts Python
Pour un blog Jekyll, créez des sous-répertoires par code de langue [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) comme `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath} dans le répertoire `/_posts`{: .filepath} où se trouvent les articles. Placez ensuite les scripts Python et le fichier CSV présentés ci-dessus dans le répertoire `/tools`{: .filepath}, ouvrez un terminal à cet emplacement et exécutez la commande suivante.

```bash
python3 translate_changes.py
```

Le script s'exécutera alors et affichera un écran comme celui-ci.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Retour d'expérience
Comme mentionné ci-dessus, j'utilise la traduction automatique des articles via l'API Claude 3.5 sur ce blog depuis environ 2 mois. Dans la plupart des cas, on peut obtenir des traductions de haute qualité sans nécessiter d'intervention humaine supplémentaire, et après avoir traduit et publié les articles en plusieurs langues, j'ai constaté un trafic organique réel provenant de recherches depuis des régions autres que la Corée, comme le Brésil, le Canada, les États-Unis et la France. En plus d'augmenter le trafic du blog, il y avait aussi des avantages secondaires en termes d'apprentissage pour l'auteur des articles, car Claude produit des textes très fluides en anglais, ce qui me permet, lors de la révision avant de pousser les articles vers le dépôt GitHub Pages, de voir comment certains termes ou expressions de mon texte original en coréen peuvent être exprimés naturellement en anglais. Bien que cela seul ne soit pas suffisant pour un apprentissage complet de l'anglais, le fait de pouvoir fréquemment rencontrer des expressions naturelles en anglais, tant quotidiennes qu'académiques, en utilisant comme exemple mon propre texte qui m'est plus familier que tout autre, sans effort supplémentaire particulier, semble être un avantage non négligeable pour un étudiant en ingénierie de premier cycle dans un pays non anglophone comme la Corée.
