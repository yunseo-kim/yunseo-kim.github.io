---
title: Comment traduire automatiquement des articles avec l'API Claude 3.5 Sonnet
description: >-
  Présentation succincte du modèle Claude 3.5 Sonnet récemment publié, partage du processus de conception du prompt et du résultat final pour l'appliquer à la traduction multilingue des articles de ce blog.
  Introduction à la méthode d'écriture et d'utilisation d'un script Python d'automatisation de la traduction en utilisant la clé API obtenue d'Anthropic et le prompt précédemment rédigé.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introduction
J'ai récemment adopté l'API Claude 3.5 Sonnet d'Anthropic pour la traduction multilingue des articles de blog. Je souhaite aborder les raisons du choix de l'API Claude 3.5 Sonnet, la méthode de conception du prompt, ainsi que la méthode d'implémentation de l'automatisation via l'intégration de l'API et un script Python.

## À propos de Claude 3.5 Sonnet
Les modèles de la série Claude 3 sont proposés en versions Haiku, Sonnet et Opus selon la taille du modèle.  
![Distinction des niveaux de modèles Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Source de l'image : [Page officielle de l'API Claude d'Anthropic](https://www.anthropic.com/api)

Et le 21 juin 2024 (heure coréenne), Anthropic a dévoilé son dernier modèle de langage, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Selon l'annonce d'Anthropic, il offre des performances d'inférence supérieures à celles de Claude 3 Opus avec le même coût et la même vitesse que Claude 3 Sonnet existant. Il est généralement considéré comme ayant un avantage par rapport à son concurrent GPT-4 dans les domaines de la rédaction, du raisonnement linguistique, de la compréhension multilingue et de la traduction.  
![Image de présentation de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Résultats des tests de performance de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Source des images : [Site web d'Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

## Raisons de l'adoption de Claude 3.5 pour la traduction d'articles
Il existe déjà des API de traduction commerciales comme Google Translate ou DeepL, sans nécessairement recourir à des modèles de langage comme Claude 3.5 ou GPT-4. Cependant, j'ai décidé d'utiliser un LLM pour la traduction car, contrairement aux autres services de traduction commerciaux, l'utilisateur peut fournir des informations contextuelles supplémentaires ou des exigences au-delà du texte principal, comme le but de la rédaction ou les principaux sujets, grâce à la conception du prompt. Le modèle peut alors fournir une traduction qui tient compte du contexte en conséquence. Bien que DeepL et Google Translate offrent généralement une excellente qualité de traduction, ils ont tendance à produire des résultats relativement peu naturels lorsqu'on leur demande de traduire de longs textes sur des sujets spécialisés plutôt que des conversations quotidiennes, en raison de leur limitation à bien saisir le sujet et le contexte global du texte. En particulier, comme mentionné précédemment, Claude est considéré comme supérieur à son concurrent GPT-4 dans les domaines de la rédaction, du raisonnement linguistique, de la compréhension multilingue et de la traduction, j'ai donc jugé qu'il était approprié pour traduire les articles d'ingénierie publiés sur ce blog dans plusieurs langues.

## Conception du prompt
### Principes de base de la conception du prompt
Pour obtenir des résultats satisfaisants et conformes à l'objectif d'un modèle de langage, il faut lui fournir un prompt approprié. La conception de prompt peut sembler intimidante, mais en réalité, "la façon de bien demander quelque chose" n'est pas très différente, que l'interlocuteur soit un modèle de langage ou un être humain, donc ce n'est pas si difficile si on l'aborde sous cet angle. Il est bon d'expliquer clairement la situation actuelle et les demandes selon les six questions de base (qui, quoi, où, quand, pourquoi, comment), et d'ajouter quelques exemples concrets si nécessaire. Il existe de nombreux conseils et techniques pour la conception de prompt, mais la plupart découlent des principes de base mentionnés ci-dessus.

### Attribution d'un rôle et explication de la situation (qui, pourquoi)
Tout d'abord, j'ai attribué à Claude 3.5 le rôle de *"traducteur technique professionnel"* et fourni des informations contextuelles sur l'utilisateur en tant que *"blogueur en ingénierie qui écrit principalement sur les mathématiques, la physique et la science des données"*.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Transmission des demandes générales (quoi)
Ensuite, j'ai demandé de traduire le texte au format markdown fourni par l'utilisateur de {source_lang} vers {target_lang} tout en préservant le format.
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Lors de l'appel à l'API Claude, les variables de langue source et cible sont respectivement insérées à la place de {source_lang} et {target_lang} dans le prompt via la fonctionnalité f-string du script Python.
{: .prompt-info }

### Spécification des exigences et exemples (comment)
Pour des tâches simples, les étapes précédentes peuvent suffire pour obtenir les résultats souhaités, mais pour des tâches plus complexes, des explications supplémentaires peuvent être nécessaires. Dans ce cas, j'ai ajouté les conditions suivantes.

#### Traitement du YAML front matter
Le YAML front matter situé au début des articles rédigés en markdown pour être téléchargés sur le blog Jekyll contient les informations 'title', 'description', 'categories' et 'tags'. Par exemple, le YAML front matter de cet article est le suivant :

```YAML
---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법
description: >-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
  그리고 Anthropic으로부터 발급받은 API 키와 앞서 작성한 프롬프트를 적용하여 Python으로 번역 자동화 스크립트를 작성하고 활용하는 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

Cependant, lors de la traduction des articles, les balises titre (title) et description (description) doivent être traduites dans plusieurs langues, mais pour la cohérence des URL des articles, il est plus facile de maintenir les noms des catégories (categories) et des tags (tags) en anglais sans les traduire. J'ai donc donné l'instruction suivante pour ne pas traduire les balises autres que 'title' et 'description'. Comme Claude a probablement déjà appris les informations sur le YAML front matter, cette explication devrait suffire dans la plupart des cas.
> In the provided markdown formatted text, do not translate the YAML front matter except for the 'title' and 'description' tags.

#### Traitement lorsque le texte source contient une langue autre que la langue de départ
Lors de la rédaction du texte original en coréen, il arrive souvent d'inclure l'expression anglaise entre parenthèses lorsqu'on introduit pour la première fois la définition d'un concept ou qu'on utilise certains termes techniques, comme '*중성자 감쇠 (Neutron Attenuation)*'. Lors de la traduction de telles expressions, il y avait un problème de manque de cohérence dans la méthode de traduction, parfois en conservant les parenthèses, parfois en omettant l'anglais entre parenthèses. J'ai donc ajouté la phrase suivante au prompt :
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Traitement des liens vers d'autres articles
Certains articles contiennent des liens vers d'autres articles, et il y avait souvent un problème où les liens internes étaient cassés parce que la partie du chemin de l'URL était interprétée comme devant être traduite. Ce problème a été résolu en ajoutant cette phrase au prompt :
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Ne produire que le résultat de la traduction comme réponse
Enfin, on présente la phrase suivante pour ne produire que le résultat de la traduction sans ajouter d'autres commentaires dans la réponse.
> The output should only contain the translated text.

### Prompt finalisé
Le résultat de la conception du prompt après ces étapes est le suivant :
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.

## Intégration de l'API Claude
### Obtention de la clé API Claude

> Cette section explique comment obtenir une nouvelle clé API Claude. Si vous avez déjà une clé API à utiliser, vous pouvez passer cette étape.
{: .prompt-tip }

Connectez-vous à <https://console.anthropic.com>. Si vous n'avez pas encore de compte, vous devez d'abord vous inscrire. Une fois connecté, vous verrez un écran de tableau de bord comme ci-dessous.  
![Tableau de bord de la console Anthropic](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

En cliquant sur le bouton 'Get API keys' sur cet écran, vous verrez l'écran suivant.  
![Clés API](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Comme j'ai déjà créé une clé, une clé nommée `yunseo-secret-key` est affichée, mais si vous venez de créer votre compte et n'avez pas encore obtenu de clé API, vous n'aurez probablement aucune clé. Vous pouvez obtenir une nouvelle clé en cliquant sur le bouton 'Create Key' en haut à droite.

> Une fois l'obtention de la clé terminée, votre clé API s'affichera à l'écran. Comme cette clé ne pourra plus être consultée ultérieurement, assurez-vous de la noter séparément dans un endroit sûr.
{: .prompt-warning }

### (Recommandé) Enregistrement de la clé API Claude dans les variables d'environnement
Pour utiliser l'API Claude dans des scripts Python ou Shell, il faut charger la clé API. Bien qu'il soit possible d'enregistrer la clé API dans le script lui-même, cette méthode ne peut pas être utilisée si le script doit être partagé avec d'autres personnes, par exemple en le téléchargeant sur GitHub. De plus, même si vous n'aviez pas l'intention de partager le fichier de script, il existe un risque que la clé API soit également divulguée en cas de fuite accidentelle du fichier de script si la clé API y est enregistrée. Il est donc recommandé d'enregistrer la clé API dans les variables d'environnement du système que vous seul utilisez, et d'utiliser cette variable d'environnement dans le script. Voici comment enregistrer la clé API dans les variables d'environnement du système, basé sur un système UNIX. Pour Windows, veuillez consulter d'autres articles sur le web.

1. Dans le terminal, exécutez `nano ~/.bashrc` ou `nano ~/.zshrc` selon le type de shell que vous utilisez pour lancer l'éditeur.
2. Ajoutez `export ANTHROPIC_API_KEY='your-api-key-here'` au contenu du fichier. Remplacez 'your-api-key-here' par votre propre clé API, en veillant à l'entourer de guillemets simples.
3. Sauvegardez les modifications et quittez l'éditeur.
4. Exécutez `source ~/.bashrc` ou `source ~/.zshrc` dans le terminal pour appliquer les modifications.

### Installation des packages Python nécessaires
Si le package anthropic n'est pas installé dans votre environnement Python, installez-le avec la commande suivante :
```bash
pip3 install anthropic
```
De plus, les packages suivants sont nécessaires pour utiliser le script de traduction d'articles que nous présenterons plus tard, alors installez-les ou mettez-les à jour avec la commande suivante :
```bash
pip3 install -U argparse tqdm
```

### Écriture du script Python
Le script de traduction d'articles que nous allons présenter dans cet article se compose de 3 fichiers de script Python et 1 fichier CSV.

- `compare_hash.py` : Calcule les valeurs de hachage SHA256 des articles originaux en coréen dans le répertoire `_posts/ko`{: .filepath}, les compare aux valeurs de hachage existantes enregistrées dans le fichier `hash.csv`, et renvoie une liste des noms de fichiers modifiés ou nouvellement ajoutés
- `hash.csv` : Fichier CSV enregistrant les valeurs de hachage SHA256 des fichiers d'articles existants
- `prompt.py` : Reçoit les valeurs filepath, source_lang, target_lang, charge la valeur de la clé API Claude depuis les variables d'environnement du système, puis appelle l'API en soumettant le prompt écrit précédemment comme prompt système et le contenu de l'article à traduire dans 'filepath' comme prompt utilisateur. Ensuite, il reçoit la réponse (résultat de la traduction) du modèle Claude 3.5 Sonnet et l'écrit dans un fichier texte au chemin `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py` : Contient la variable chaîne source_lang et la liste 'target_langs', appelle la fonction `changed_files()` dans `compare_hash.py` pour obtenir la liste changed_files. S'il y a des fichiers modifiés, il exécute une double boucle pour tous les fichiers de la liste changed_files et tous les éléments de la liste target_langs, et dans cette boucle, il appelle la fonction `translate(filepath, source_lang, target_lang)` dans `prompt.py` pour effectuer la traduction.

Le contenu des fichiers de script complétés peut également être consulté sur le dépôt GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, hash_value in file_hashes.items():
            writer.writerow([file_path, hash_value])

def changed_files():
    posts_dir = '../_posts/ko/'
    hash_csv_path = './hash.csv'
    
    existing_hashes = load_existing_hashes(hash_csv_path)
    current_hashes = {}
    changed_files = []

    for root, _, files in os.walk(posts_dir):
        for file in files:
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

    if __name__ == "__main__":
        if changed_files:
            print("Changed files:")
            for file in changed_files:
                print(f"- {file}")
        else:
            print("No files have changed.")

    return changed_files
```

#### prompt.py
Comme il contient le contenu du prompt écrit précédemment et que le contenu du fichier est assez long, nous le remplaçons par le lien vers le fichier source dans le dépôt GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> Dans le fichier `prompt.py` du lien ci-dessus, `max_tokens` est une variable qui spécifie la longueur maximale de sortie, indépendamment de la taille de la fenêtre de contexte. Lors de l'utilisation de l'API Claude, la taille de la fenêtre de contexte pouvant être saisie en une fois est de 200k tokens (environ 680 000 caractères), mais indépendamment de cela, chaque modèle a un nombre maximum de tokens de sortie défini, il est donc recommandé de vérifier à l'avance dans la [documentation officielle d'Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) avant d'utiliser l'API. Les modèles de la série Claude 3 existants pouvaient produire jusqu'à 4096 tokens maximum, et bien que cela n'ait pas posé de problème pour la plupart des articles de ce blog lors des tests, pour certains articles assez longs de plus de 8000 caractères en coréen, il y avait un problème où la partie arrière de la traduction était coupée dans certaines langues de sortie car elle dépassait 4096 tokens. Dans le cas de Claude 3.5 Sonnet, le nombre maximum de tokens de sortie a doublé à 8192, donc il n'y a généralement pas eu de problème de dépassement de ce nombre maximum de tokens de sortie, et dans le `prompt.py` du dépôt GitHub ci-dessus, `max_tokens=8192` a été spécifié.
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
```

### Comment utiliser le script Python
Pour un blog Jekyll, placez des sous-répertoires par code de langue [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) comme `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath} dans le répertoire `/_posts`{: .filepath} où se trouvent les articles. Ensuite, placez les scripts Python et le fichier CSV présentés ci-dessus dans le répertoire `/tools`{: .filepath}, ouvrez un terminal à cet emplacement et exécutez la commande suivante.

```bash
python3 translate_changes.py
```

Le script s'exécutera alors et un écran comme celui-ci s'affichera.  
![Capture d'écran de l'exécution du script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Capture d'écran de l'exécution du script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Retour d'expérience
Comme mentionné ci-dessus, j'utilise la traduction automatique des articles via l'API Claude 3.5 sur ce blog depuis environ 2 mois. Dans la plupart des cas, on peut obtenir des traductions de haute qualité sans nécessiter d'intervention humaine supplémentaire, et j'ai constaté qu'après avoir traduit et publié les articles en plusieurs langues, il y a effectivement un trafic Organic Search provenant de recherches depuis des régions autres que la Corée, comme le Brésil, le Canada, les États-Unis ou la France. De plus, outre l'augmentation du trafic du blog, il y avait aussi des avantages supplémentaires en termes d'apprentissage pour l'auteur des articles. Comme Claude produit des textes très fluides en anglais, lors du processus de révision avant de pousser les articles vers le dépôt GitHub Pages, j'ai l'opportunité de vérifier comment certains termes ou expressions que j'ai écrits en coréen dans le texte original peuvent être exprimés naturellement en anglais. Bien que cela seul ne suffise pas pour un apprentissage complet de l'anglais, le fait de pouvoir fréquemment rencontrer des expressions anglaises naturelles, non seulement pour le langage quotidien mais aussi pour les expressions et termes académiques, en utilisant comme exemple le texte que j'ai écrit moi-même et qui m'est le plus familier, sans effort supplémentaire particulier, semble être un avantage assez important pour un étudiant de premier cycle en ingénierie dans un pays non anglophone comme la Corée.
