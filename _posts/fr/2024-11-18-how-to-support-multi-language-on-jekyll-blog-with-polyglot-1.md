---
title: Comment supporter le multilinguisme sur un blog Jekyll avec Polyglot (1) - Application du plugin Polyglot & implémentation des balises hreflang alt, du sitemap et du bouton de sélection de langue
description: >-
  Présentation du processus d'implémentation du support multilingue sur un blog Jekyll basé sur 'jekyll-theme-chirpy' en utilisant le plugin Polyglot.
  Ce billet est le premier d'une série et traite de l'application du plugin Polyglot ainsi que de la modification de l'en-tête HTML et du sitemap.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
---
## Aperçu
Il y a environ 4 mois, début juillet 2024, j'ai ajouté le support multilingue à ce blog basé sur Jekyll et hébergé via Github Pages en appliquant le plugin [Polyglot](https://github.com/untra/polyglot).
Cette série partage le processus d'application du plugin Polyglot au thème Chirpy, les bugs rencontrés et leur résolution, ainsi que la méthode pour écrire l'en-tête HTML et le sitemap.xml en tenant compte du SEO.
La série se compose de deux articles, et celui-ci est le premier de la série.
- Partie 1 : Application du plugin Polyglot & implémentation des balises hreflang alt, du sitemap et du bouton de sélection de langue (cet article)
- Partie 2 : [Dépannage des échecs de construction du thème Chirpy et des erreurs de fonction de recherche](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Exigences
- [x] Le résultat de la construction (pages web) doit pouvoir être fourni avec des chemins distincts par langue (ex. `/posts/fr/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Pour minimiser le temps et l'effort supplémentaires nécessaires au support multilingue, le système doit pouvoir reconnaître automatiquement la langue en fonction du chemin local où se trouve le fichier original markdown (ex. `/_posts/fr/`{: .filepath}, `/_posts/ja/`{: .filepath}) lors de la construction, sans avoir à spécifier manuellement les balises 'lang' et 'permalink' dans le YAML front matter de chaque fichier markdown écrit.
- [x] L'en-tête de chaque page du site doit inclure les balises meta Content-Language appropriées et les balises alternatives hreflang pour répondre aux directives SEO de Google pour la recherche multilingue.
- [x] Le `sitemap.xml` doit pouvoir fournir tous les liens de pages supportant chaque langue sur le site sans omission, et le `sitemap.xml` lui-même ne doit exister qu'une seule fois dans le chemin racine sans duplication.
- [x] Toutes les fonctionnalités fournies par le [thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) doivent fonctionner normalement sur chaque page de langue, sinon elles doivent être modifiées pour fonctionner correctement.
  - [x] Fonctionnement normal des fonctions 'Recently Updated', 'Trending Tags'
  - [x] Pas d'erreur lors du processus de construction utilisant GitHub Actions
  - [x] Fonctionnement normal de la fonction de recherche de posts en haut à droite du blog

## Application du plugin Polyglot
Comme Jekyll ne prend pas en charge nativement les blogs multilingues, un plugin externe doit être utilisé pour implémenter un blog multilingue répondant aux exigences ci-dessus. Après recherche, j'ai constaté que [Polyglot](https://github.com/untra/polyglot) est largement utilisé pour l'implémentation de sites web multilingues et peut satisfaire la plupart des exigences ci-dessus, j'ai donc choisi ce plugin.

### Installation du plugin
Comme j'utilise Bundler, j'ai ajouté le contenu suivant à `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Ensuite, exécuter `bundle update` dans le terminal terminera automatiquement l'installation.

Si vous n'utilisez pas Bundler, vous pouvez installer directement la gem avec la commande `gem install jekyll-polyglot` dans le terminal, puis ajouter le plugin à `_config.yml` comme suit :

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuration
Ensuite, ouvrez le fichier `_config.yml` et ajoutez le contenu suivant :

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages : Liste des langues à prendre en charge
- default_lang : Langue par défaut pour le fallback
- exclude_from_localization : Spécifie les expressions régulières des chemins de fichiers/dossiers racine à exclure de la localisation
- parallel_localization : Valeur booléenne indiquant s'il faut paralléliser le traitement multilingue pendant le processus de construction
- lang_from_path : Valeur booléenne, si définie sur 'true', reconnaît et utilise automatiquement le code de langue inclus dans le chemin du fichier markdown sans avoir à spécifier explicitement l'attribut 'lang' dans le YAML front matter du fichier markdown

> La [documentation officielle du protocole Sitemap](https://www.sitemaps.org/protocol.html#location) stipule ce qui suit :
>
>> "L'emplacement d'un fichier Sitemap détermine l'ensemble des URL qui peuvent être incluses dans ce Sitemap. Un fichier Sitemap situé à http://example.com/catalog/sitemap.xml peut inclure toutes les URL commençant par http://example.com/catalog/ mais ne peut pas inclure les URL commençant par http://example.com/images/."
>
>> "Il est fortement recommandé de placer votre Sitemap dans le répertoire racine de votre serveur web."
>
> Pour se conformer à cela, il faut ajouter 'sitemap.xml' à la liste 'exclude_from_localization' pour s'assurer qu'un seul fichier `sitemap.xml` existe dans le répertoire racine, et non des fichiers identiques créés pour chaque langue, comme dans le mauvais exemple ci-dessous.
>
> Mauvais exemple (le contenu de chaque fichier est identique, pas différent par langue) :
> - /sitemap.xml
> - /fr/sitemap.xml
> - /es/sitemap.xml
> - /pt-BR/sitemap.xml
> - /ja/sitemap.xml
> - /ko/sitemap.xml
> - /de/sitemap.xml
{: .prompt-tip }

> Définir 'parallel_localization' sur 'true' présente l'avantage de réduire considérablement le temps de construction, mais en juillet 2024, lorsque cette fonctionnalité était activée pour ce blog, il y avait un bug où les titres des liens dans les sections 'Recently Updated' et 'Trending Tags' de la barre latérale droite de la page n'étaient pas traités correctement et se mélangeaient avec d'autres langues. Cela semble encore instable, donc il est nécessaire de tester à l'avance si cela fonctionne correctement avant de l'appliquer au site. De plus, [cette fonctionnalité n'est pas prise en charge sous Windows et doit être désactivée](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

De plus, [dans Jekyll 4.0, vous devez désactiver la génération de sourcemaps CSS comme suit](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # Dans Jekyll 4.0, les sourcemaps SCSS seront générées incorrectement en raison du fonctionnement de Polyglot
```
{: file='_config.yml'}

### Points à noter lors de la rédaction de posts
Voici les points à noter lors de la rédaction de posts multilingues :
- Spécification du code de langue approprié : Il faut spécifier le code de langue ISO approprié en utilisant soit le chemin du fichier (ex. `/_posts/fr/example-post.md`{: .filepath}) soit l'attribut 'lang' dans le YAML front matter (ex. `lang: fr`). Référez-vous aux exemples de la [documentation pour développeurs Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Cependant, bien que la [documentation pour développeurs Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) utilise le format 'pt_BR' pour les codes régionaux, il faut en réalité utiliser 'pt-BR' avec un tiret (-) au lieu d'un underscore (_) pour que cela fonctionne correctement lors de l'ajout ultérieur des balises alternatives hreflang dans l'en-tête HTML.

- Les chemins et noms de fichiers doivent être cohérents.

Pour plus de détails, veuillez consulter le [README du dépôt GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modification de l'en-tête HTML et du sitemap
Maintenant, nous devons insérer les balises meta Content-Language et les balises alternatives hreflang dans l'en-tête HTML de chaque page du blog pour le SEO.

### En-tête HTML
Dans la version 1.8.1, la plus récente en novembre 2024, Polyglot dispose d'une fonctionnalité qui effectue automatiquement cette tâche lorsque la balise Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} est appelée dans la partie en-tête de la page.
Cependant, cela suppose que la balise d'attribut 'permalink' a été spécifiée explicitement pour cette page, et ne fonctionne pas correctement si ce n'est pas le cas.

J'ai donc récupéré le [head.html du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) et y ai directement ajouté le contenu suivant.
J'ai travaillé en me référant à la [page SEO Recipes du blog officiel de Polyglot](https://polyglot.untra.io/seo/), mais j'ai modifié pour utiliser l'attribut `page.url` à la place si `page.permalink` n'existe pas.
De plus, en me référant à la [documentation officielle de Google Search Central](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault), j'ai spécifié `x-default` au lieu de `site.default_lang` comme valeur d'attribut hreflang pour la page de langue par défaut du site, afin que le lien de cette page soit reconnu comme fallback si la langue préférée du visiteur n'est pas dans la liste des langues prises en charge par le site ou si la langue préférée du visiteur ne peut pas être identifiée.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">

  {% if site.default_lang %}<link rel="alternate" hreflang="x-default" href="{{site.url}}{{page.url}}" />{% endif %}
  {% for lang in site.languages %}{% if lang == site.default_lang %}{% continue %}{% endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {% endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

### Sitemap
Comme le sitemap généré automatiquement par Jekyll lors de la construction ne prend pas correctement en charge les pages multilingues, créez un fichier `sitemap.xml` dans le répertoire racine et entrez le contenu suivant :

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- vérification très paresseuse pour voir si la page est dans la liste d'exclusion - cela signifie que les pages exclues ne seront pas du tout dans le sitemap, écrivez des exceptions si nécessaire -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- en supposant que s'il n'y a pas de mise en page attribuée, alors n'incluez pas la page dans le sitemap, vous voudrez peut-être changer cela -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- Ceci parcourt toutes les collections du site, y compris les posts -->{% endcomment %}
    {% for collection in site.collections %}
        {% for node in site[collection.label] %}
            <url>
                <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
            </url>
        {% endfor %}
    {% endfor %}

{% endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## Ajout d'un bouton de sélection de langue dans la barre latérale
J'ai créé un fichier `_includes/lang-selector.html` et y ai entré le contenu suivant :

{% raw %}
```liquid
<p>
{%- for lang in site.languages -%}
  {%- if lang == site.default_lang -%}
<a ferh="{{ page.url }}" style="display:inline-block; white-space:nowrap;">
    {%- if lang == site.active_lang -%}
      <b>{{ lang }}</b>
    {%- else -%}
      {{ lang }}
    {%- endif -%}
</a>
  {%- else -%}
<a href="/{{ lang }}{{ page.url }}" style="display:inline-block; white-space:nowrap;">
  {%- if lang == site.active_lang -%}
      <b>{{ lang }}</b>
    {%- else -%}
      {{ lang }}
    {%- endif -%}
</a>
  {%- endif -%}
{%- endfor -%}
</p>
```
{: file='_includes/lang-selector.html'}
{% endraw %}

Ensuite, j'ai ajouté les trois lignes suivantes à la partie de classe "sidebar-bottom" du [`_includes/sidebar.html` du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) pour que Jekyll charge le contenu de `_includes/lang-selector.html` précédemment créé lors de la construction de la page :

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Pour aller plus loin
Suite dans la [Partie 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
