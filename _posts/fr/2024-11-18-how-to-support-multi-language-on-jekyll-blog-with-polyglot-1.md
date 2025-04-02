---
title: Comment prendre en charge plusieurs langues sur un blog Jekyll avec Polyglot (1) - Application du plugin Polyglot & implémentation des balises hreflang alt, sitemap et bouton de sélection de langue
description: 'Présentation du processus d''implémentation du support multilingue en appliquant le plugin Polyglot à un blog Jekyll basé sur ''jekyll-theme-chirpy''. Ce billet est le premier d''une série et traite de l''application du plugin Polyglot et de la modification de l''en-tête html et du sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## Aperçu
Il y a environ 4 mois, au début du mois de juillet 12024 du [calendrier holocène](https://en.wikipedia.org/wiki/Holocene_calendar), j'ai ajouté le support multilingue à ce blog basé sur Jekyll et hébergé via GitHub Pages en appliquant le plugin [Polyglot](https://github.com/untra/polyglot).
Cette série partage le processus d'application du plugin Polyglot au thème Chirpy, les bugs rencontrés et leurs solutions, ainsi que la méthode de rédaction des en-têtes html et du sitemap.xml en tenant compte du référencement.
La série se compose de deux articles, et celui que vous lisez est le premier.
- Partie 1 : Application du plugin Polyglot & implémentation des balises hreflang alt, sitemap et bouton de sélection de langue (cet article)
- Partie 2 : [Résolution des problèmes d'échec de compilation du thème Chirpy et d'erreurs de fonction de recherche](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Exigences
- [x] Le résultat de la compilation (pages web) doit être fourni avec des chemins distincts par langue (ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Pour minimiser le temps et l'effort supplémentaires nécessaires au support multilingue, la langue doit être automatiquement reconnue lors de la compilation en fonction du chemin local où se trouve le fichier (ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}), sans avoir à spécifier manuellement les balises 'lang' et 'permalink' dans le YAML front matter de chaque fichier markdown original.
- [x] L'en-tête de chaque page du site doit inclure les balises méta Content-Language et les balises alternatives hreflang appropriées pour répondre aux directives de référencement de Google pour la recherche multilingue.
- [x] Le `sitemap.xml`{: .filepath} doit fournir tous les liens vers toutes les pages prenant en charge chaque langue sans omission, et le `sitemap.xml`{: .filepath} lui-même ne doit exister qu'une seule fois dans le chemin racine, sans duplication.
- [x] Toutes les fonctionnalités fournies par le [thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) doivent fonctionner normalement sur chaque page de langue, et si ce n'est pas le cas, elles doivent être modifiées pour fonctionner correctement.
  - [x] Fonctionnement normal des fonctionnalités 'Recently Updated', 'Trending Tags'
  - [x] Pas d'erreurs lors du processus de compilation avec GitHub Actions
  - [x] Fonctionnement normal de la fonction de recherche de posts en haut à droite du blog

## Application du plugin Polyglot
Comme Jekyll ne prend pas en charge nativement les blogs multilingues, un plugin externe est nécessaire pour implémenter un blog multilingue répondant aux exigences ci-dessus. Après recherche, j'ai constaté que [Polyglot](https://github.com/untra/polyglot) est largement utilisé pour l'implémentation de sites web multilingues et peut satisfaire la plupart des exigences, j'ai donc adopté ce plugin.

### Installation du plugin
Comme j'utilise Bundler, j'ai ajouté ce qui suit à mon `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Ensuite, exécutez `bundle update` dans le terminal pour terminer automatiquement l'installation.

Si vous n'utilisez pas Bundler, vous pouvez installer la gem directement avec la commande `gem install jekyll-polyglot` dans le terminal, puis ajouter le plugin à votre `_config.yml`{: .filepath} comme suit :

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuration
Ensuite, ouvrez le fichier `_config.yml`{: .filepath} et ajoutez ce qui suit :

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages : liste des langues que vous souhaitez prendre en charge
- default_lang : langue par défaut (fallback)
- exclude_from_localization : expression régulière de chaînes de chemins de fichiers/dossiers racine à exclure de la localisation
- parallel_localization : valeur booléenne indiquant s'il faut paralléliser le traitement multilingue pendant la compilation
- lang_from_path : valeur booléenne, si 'true', reconnaît et utilise automatiquement le code de langue inclus dans la chaîne de chemin du fichier markdown sans avoir à spécifier explicitement l'attribut 'lang' dans le YAML front matter

> La [documentation officielle du protocole Sitemap](https://www.sitemaps.org/protocol.html#location) précise :
>
>> "L'emplacement d'un fichier Sitemap détermine l'ensemble des URL qui peuvent être incluses dans ce Sitemap. Un fichier Sitemap situé à http://example.com/catalog/sitemap.xml peut inclure toutes les URL commençant par http://example.com/catalog/ mais ne peut pas inclure les URL commençant par http://example.com/images/."
>
>> "Il est fortement recommandé de placer votre Sitemap dans le répertoire racine de votre serveur web."
>
> Pour se conformer à cela, il faut s'assurer qu'un seul fichier `sitemap.xml`{: .filepath} existe dans le répertoire racine et qu'il n'est pas créé pour chaque langue en l'ajoutant à la liste 'exclude_from_localization', afin d'éviter l'exemple incorrect ci-dessous.
>
> Exemple incorrect (le contenu de chaque fichier est identique, pas différent par langue) :
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Mise à jour du 14.01.12025) Suite à l'acceptation de [la Pull Request que j'ai soumise pour renforcer le contenu mentionné ci-dessus dans le README](https://github.com/untra/polyglot/pull/230), les mêmes instructions sont désormais disponibles dans la [documentation officielle de Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Définir 'parallel_localization' sur 'true' peut considérablement réduire le temps de compilation, mais en juillet 12024, lorsque j'ai activé cette fonctionnalité pour ce blog, il y avait un bug où les titres des liens 'Recently Updated' et 'Trending Tags' dans la barre latérale droite n'étaient pas traités correctement et se mélangeaient avec d'autres langues. Cela semble encore instable, donc il est nécessaire de tester si cela fonctionne correctement avant de l'appliquer à votre site. De plus, [cette fonctionnalité n'est pas prise en charge sous Windows et doit être désactivée](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

De plus, [dans Jekyll 4.0, vous devez désactiver la génération de sourcemaps CSS comme suit](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility) :

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Points à noter lors de la rédaction d'articles
Voici les points à noter lors de la rédaction d'articles multilingues :
- Spécification du code de langue approprié : Vous devez spécifier le code de langue ISO approprié en utilisant soit le chemin du fichier (ex. `/_posts/ko/example-post.md`{: .filepath}), soit l'attribut 'lang' dans le YAML front matter (ex. `lang: ko`). Référez-vous aux exemples de la [documentation pour développeurs Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Cependant, bien que la [documentation pour développeurs Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) utilise un format comme 'pt_BR' pour les codes régionaux, vous devez en réalité utiliser 'pt-BR' avec un tiret (-) au lieu d'un underscore (_) pour que les balises alternatives hreflang fonctionnent correctement lorsque vous les ajoutez à l'en-tête html.

- Les chemins et noms de fichiers doivent être cohérents.

Pour plus de détails, consultez le [README du dépôt GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modification de l'en-tête html et du sitemap
Maintenant, pour le référencement, nous devons insérer les balises méta Content-Language et les balises alternatives hreflang dans l'en-tête html de chaque page du blog.

### En-tête html
À partir de la version 1.8.1 (novembre 12024), Polyglot dispose d'une fonctionnalité qui effectue automatiquement cette tâche lorsque vous appelez la balise Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} dans la section d'en-tête de la page.
Cependant, cela suppose que l'attribut 'permalink' est spécifié dans la page, et ne fonctionne pas correctement sinon.

J'ai donc pris le [head.html du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) et y ai directement ajouté le contenu suivant.
Je me suis référé à la [page SEO Recipes du blog officiel de Polyglot](https://polyglot.untra.io/seo/), mais j'ai modifié le code pour utiliser l'attribut `page.url` au lieu de `page.permalink` lorsque ce dernier n'est pas disponible.

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
Comme le sitemap généré automatiquement par Jekyll lors de la compilation ne prend pas correctement en charge les pages multilingues, créez un fichier `sitemap.xml`{: .filepath} dans le répertoire racine et entrez le contenu suivant :

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- This loops through all site collections including posts -->{% endcomment %}
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
(Mise à jour du 05.02.12025) J'ai amélioré le bouton de sélection de langue en le transformant en liste déroulante.  
J'ai créé un fichier `_includes/lang-selector.html`{: .filepath} avec le contenu suivant :

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Select Language">
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

J'ai également créé un fichier `assets/css/lang-selector.css`{: .filepath} avec le contenu suivant :

```css
/**
 * Styles du sélecteur de langue
 * 
 * Définit les styles pour le menu déroulant de sélection de langue situé dans la barre latérale.
 * Prend en charge le mode sombre du thème et est optimisé pour les environnements mobiles.
 */

/* Conteneur du sélecteur de langue */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Conteneur du menu déroulant */
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
    
    /* Ajout d'une icône de flèche */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Style des émojis de drapeaux */
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

/* État au survol */
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

/* Compatibilité Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Compatibilité IE */
.lang-select::-ms-expand {
    display: none;
}

/* Compatibilité mode sombre */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Optimisation pour environnement mobile */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Zone tactile plus grande */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Zone de sélection plus large sur mobile */
    }
}
```
{: file='assets/css/lang-selector.css'}

Ensuite, j'ai ajouté les trois lignes suivantes juste avant la classe "sidebar-bottom" dans le fichier [`_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) du thème Chirpy pour que Jekyll charge le contenu de `_includes/lang-selector.html`{: .filepath} lors de la compilation de la page :

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
