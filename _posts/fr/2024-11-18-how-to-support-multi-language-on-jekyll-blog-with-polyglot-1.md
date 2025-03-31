---
title: Comment supporter le multilinguisme sur un blog Jekyll avec Polyglot (1) - Application du plugin Polyglot & implémentation des balises hreflang alt, du sitemap et du bouton de sélection de langue
description: 'Cet article présente le processus d''implémentation du support multilingue sur un blog Jekyll basé sur le thème ''jekyll-theme-chirpy'' en utilisant le plugin Polyglot. C''est le premier article de la série, couvrant l''application du plugin Polyglot et la modification de l''en-tête HTML et du sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## Aperçu
Il y a environ 4 mois, au début du mois de juillet de l'an 12024 du [calendrier holocène](https://en.wikipedia.org/wiki/Holocene_calendar), j'ai ajouté le support multilingue à ce blog basé sur Jekyll et hébergé via GitHub Pages en appliquant le plugin [Polyglot](https://github.com/untra/polyglot).
Cette série partage les bugs rencontrés lors de l'application du plugin Polyglot au thème Chirpy, leur processus de résolution, ainsi que la méthode pour écrire l'en-tête HTML et le sitemap.xml en tenant compte du SEO.
La série se compose de deux articles, et celui que vous lisez est le premier de la série.
- Partie 1 : Application du plugin Polyglot & implémentation des balises hreflang alt, du sitemap et du bouton de sélection de langue (cet article)
- Partie 2 : [Dépannage de l'échec de construction du thème Chirpy et des erreurs de fonction de recherche](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Exigences
- [x] Le résultat de la construction (pages web) doit pouvoir être fourni en distinguant les chemins par langue (ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Pour minimiser le temps et l'effort supplémentaires nécessaires au support multilingue, le système doit pouvoir reconnaître automatiquement la langue en fonction du chemin local où se trouve le fichier (ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) lors de la construction, sans avoir à spécifier manuellement les balises 'lang' et 'permalink' dans le YAML front matter du fichier Markdown original.
- [x] L'en-tête de chaque page du site doit inclure les balises méta Content-Language appropriées et les balises alternatives hreflang pour répondre aux directives SEO de Google pour la recherche multilingue.
- [x] Le `sitemap.xml`{: .filepath} doit pouvoir fournir tous les liens des pages supportant chaque langue sur le site sans omission, et le `sitemap.xml`{: .filepath} lui-même ne doit exister qu'une seule fois dans le chemin racine sans duplication.
- [x] Toutes les fonctionnalités fournies par le [thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) doivent fonctionner normalement sur chaque page de langue, et si ce n'est pas le cas, elles doivent être modifiées pour fonctionner correctement.
  - [x] Fonctionnement normal des fonctions 'Recently Updated' et 'Trending Tags'
  - [x] Pas d'erreur lors du processus de construction utilisant GitHub Actions
  - [x] Fonctionnement normal de la fonction de recherche de posts en haut à droite du blog

## Application du plugin Polyglot
Comme Jekyll ne prend pas en charge nativement les blogs multilingues, il est nécessaire d'utiliser un plugin externe pour implémenter un blog multilingue répondant aux exigences ci-dessus. Après recherche, j'ai constaté que [Polyglot](https://github.com/untra/polyglot) est largement utilisé pour l'implémentation de sites web multilingues et peut satisfaire la plupart des exigences ci-dessus, j'ai donc adopté ce plugin.

### Installation du plugin
Comme j'utilise Bundler, j'ai ajouté le contenu suivant à `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Ensuite, exécuter `bundle update` dans le terminal terminera automatiquement l'installation.

Si vous n'utilisez pas Bundler, vous pouvez installer directement la gem avec la commande `gem install jekyll-polyglot` dans le terminal, puis ajouter le plugin à `_config.yml`{: .filepath} comme suit :

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuration
Ensuite, ouvrez le fichier `_config.yml`{: .filepath} et ajoutez le contenu suivant :

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages : Liste des langues à prendre en charge
- default_lang : Langue de repli par défaut
- exclude_from_localization : Spécifie les expressions régulières des chemins de fichiers/dossiers racine à exclure de la localisation
- parallel_localization : Valeur booléenne indiquant s'il faut paralléliser le traitement multilingue lors de la construction
- lang_from_path : Valeur booléenne, si définie sur 'true', reconnaît et utilise automatiquement le code de langue inclus dans la chaîne de chemin du fichier Markdown sans avoir à spécifier explicitement l'attribut 'lang' dans le YAML front matter du fichier Markdown

> La [documentation officielle du protocole Sitemap](https://www.sitemaps.org/protocol.html#location) stipule ce qui suit :
>
>> "L'emplacement d'un fichier Sitemap détermine l'ensemble des URL qui peuvent être incluses dans ce Sitemap. Un fichier Sitemap situé à http://example.com/catalog/sitemap.xml peut inclure toutes les URL commençant par http://example.com/catalog/ mais ne peut pas inclure les URL commençant par http://example.com/images/."
>
>> "Il est fortement recommandé de placer votre Sitemap dans le répertoire racine de votre serveur web."
>
> Pour se conformer à cela, il faut ajouter 'sitemap.xml' à la liste 'exclude_from_localization' afin qu'un seul fichier `sitemap.xml`{: .filepath} avec le même contenu existe dans le répertoire racine, et non pas un pour chaque langue comme dans le mauvais exemple ci-dessous.
>
> Mauvais exemple (le contenu de chaque fichier n'est pas différent selon la langue, tous sont identiques) :
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Mise à jour du 14.01.12025) Suite à l'acceptation de [la Pull Request que j'ai soumise pour renforcer le contenu mentionné ci-dessus dans le README](https://github.com/untra/polyglot/pull/230), les mêmes instructions peuvent désormais être trouvées dans la [documentation officielle de Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Définir 'parallel_localization' sur 'true' présente l'avantage de réduire considérablement le temps de construction, mais en juillet 12024, lorsque cette fonctionnalité était activée pour ce blog, il y avait un bug où les titres des liens dans les sections 'Recently Updated' et 'Trending Tags' de la barre latérale droite de la page n'étaient pas traités correctement et étaient mélangés avec d'autres langues. Cela semble encore instable, donc si vous voulez l'appliquer à votre site, il est nécessaire de tester à l'avance pour vérifier son bon fonctionnement. De plus, [cette fonctionnalité n'est pas prise en charge sous Windows et doit être désactivée](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

De plus, [dans Jekyll 4.0, vous devez désactiver la génération de sourcemaps CSS comme suit](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # Dans Jekyll 4.0, les sourcemaps SCSS seront générées incorrectement en raison du fonctionnement de Polyglot
```
{: file='_config.yml'}

### Points à noter lors de la rédaction de posts
Voici les points à noter lors de la rédaction de posts multilingues :
- Spécification du code de langue approprié : Il faut spécifier le code de langue ISO approprié en utilisant le chemin du fichier (ex. `/_posts/ko/example-post.md`{: .filepath}) ou l'attribut 'lang' dans le YAML front matter (ex. `lang: ko`). Référez-vous aux exemples de la [documentation pour développeurs Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Cependant, bien que la [documentation pour développeurs Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) utilise le format 'pt_BR' pour les codes régionaux, il faut en réalité utiliser 'pt-BR' avec un - au lieu de _ pour que cela fonctionne correctement lors de l'ajout ultérieur de balises alternatives hreflang dans l'en-tête HTML.

- Les chemins et noms de fichiers doivent être cohérents.

Pour plus de détails, veuillez consulter le [README du dépôt GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modification de l'en-tête HTML et du sitemap
Maintenant, nous devons insérer la balise méta Content-Language et les balises alternatives hreflang dans l'en-tête HTML de chaque page du blog pour le SEO.

### En-tête HTML
À partir de la version 1.8.1, la plus récente en novembre 12024, Polyglot dispose d'une fonctionnalité qui effectue automatiquement cette tâche lorsque la balise Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} est appelée dans la partie en-tête de la page.
Cependant, cela suppose que l'attribut 'permalink' a été spécifié explicitement pour cette page, et ne fonctionne pas correctement si ce n'est pas le cas.

J'ai donc récupéré le [head.html du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) puis ajouté directement le contenu suivant.
J'ai travaillé en me référant à [la page SEO Recipes du blog officiel de Polyglot](https://polyglot.untra.io/seo/), mais j'ai modifié pour utiliser l'attribut `page.url` à la place si `page.permalink` n'existe pas.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">

  {% if site.default_lang %}<link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />{% endif %}
  {% for lang in site.languages %}{% if lang == site.default_lang %}{% continue %}{% endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {% endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

### Sitemap
Comme le sitemap généré automatiquement par Jekyll lors de la construction ne prend pas correctement en charge les pages multilingues, créez un fichier `sitemap.xml`{: .filepath} dans le répertoire racine et entrez le contenu suivant :

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
(Mise à jour du 05.02.12025) J'ai amélioré le bouton de sélection de langue en le transformant en une liste déroulante.  
Créez un fichier `_includes/lang-selector.html`{: .filepath} et entrez le contenu suivant :

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Sélectionner la langue">
    {%- for lang in site.languages -%}
        <option value="{% if lang == site.default_lang %}{{ page.url }}{% else %}/{{ lang }}{{ page.url }}{% endif %}"
                {% if lang == site.active_lang %}selected{% endif %}>
            {% case lang %}
            {% when 'ko' %}🇰🇷 한국어
            {% when 'en' %}🇺🇸 English
            {% when 'ja' %}🇯🇵 日本語
            {% when 'zh-TW' %}🇹🇼 正體中文
            {% when 'es' %}🇪🇸 Español
            {% when 'pt-BR' %}🇧🇷 Português
            {% when 'fr' %}🇫🇷 Français
            {% when 'de' %}🇩🇪 Deutsch
            {% else %}{{ lang }}
            {% endcase %}
        </option>
    {%- endfor -%}
    </select>
</div>

<script>
function changeLang(url) {
    window.location.href = url;
}
</script>
```
{: file='_includes/lang-selector.html'}
{% endraw %}

De plus, créez un fichier `assets/css/lang-selector.css`{: .filepath} et entrez le contenu suivant :

```css
/**
 * Style du sélecteur de langue
 * 
 * Définit le style de la liste déroulante de sélection de langue située dans la barre latérale.
 * Prend en charge le mode sombre du thème et est optimisé pour l'environnement mobile.
 */

/* Conteneur du sélecteur de langue */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Conteneur de la liste déroulante */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* Élément de sélection */
.lang-select {
    /* Style de base */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Police et couleur */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Forme et interaction */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Ajout de l'icône de flèche */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Style des emojis de drapeaux */
.lang-select option {
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
    padding: 0.35rem;
    font-size: 1rem;
}

.lang-flag {
    display: inline-block;
    margin-right: 0.5rem;
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
}

/* État de survol */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* État de focus */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Prise en charge du navigateur Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Prise en charge du navigateur IE */
.lang-select::-ms-expand {
    display: none;
}

/* Prise en charge du mode sombre */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Optimisation pour l'environnement mobile */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Zone de toucher plus grande */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Zone de sélection plus large sur mobile */
    }
}
```
{: file='assets/css/lang-selector.css'}

Ensuite, j'ai ajouté les trois lignes suivantes juste avant la classe "sidebar-bottom" dans [`_includes/sidebar.html`{: .filepath} du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) pour que Jekyll charge le contenu de `_includes/lang-selector.html`{: .filepath} créé précédemment lors de la construction de la page :

{% raw %}
```liquid
  (début)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(fin)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Pour aller plus loin
Suite dans la [Partie 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
