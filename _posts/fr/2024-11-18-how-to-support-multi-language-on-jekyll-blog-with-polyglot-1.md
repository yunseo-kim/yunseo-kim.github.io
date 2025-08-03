---
title: "Comment prendre en charge plusieurs langues sur un blog Jekyll avec Polyglot (1) - Application du plugin Polyglot & modification des en-têtes HTML et du sitemap"
description: "Présentation du processus d'implémentation du support multilingue en appliquant le plugin Polyglot à un blog Jekyll basé sur le thème 'jekyll-theme-chirpy'. Ce post est le premier article de cette série, couvrant l'application du plugin Polyglot et la modification des en-têtes HTML et du sitemap."
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## Aperçu
Début juillet 12024, j'ai ajouté l'implémentation du support multilingue en appliquant le plugin [Polyglot](https://github.com/untra/polyglot) à ce blog basé sur Jekyll et hébergé via GitHub Pages.
Cette série partage les bugs rencontrés lors de l'application du plugin Polyglot au thème Chirpy et leur processus de résolution, ainsi que les méthodes de rédaction des en-têtes HTML et du sitemap.xml en tenant compte du SEO.
La série se compose de 3 articles, et cet article que vous lisez est le premier de cette série.
- Partie 1 : Application du plugin Polyglot & modification des en-têtes HTML et du sitemap (cet article)
- Partie 2 : [Implémentation du bouton de sélection de langue & localisation de la langue de mise en page](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
- Partie 3 : [Résolution des problèmes de compilation du thème Chirpy et des erreurs de recherche](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> À l'origine composée de 2 parties au total, la série a été réorganisée en 3 parties suite à plusieurs enrichissements de contenu qui ont considérablement augmenté le volume.
{: .prompt-info }

## Exigences
- [x] Le résultat du build (page web) doit pouvoir être fourni en séparant les chemins par langue (ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Pour minimiser autant que possible le temps et les efforts supplémentaires requis pour le support multilingue, il doit être possible de reconnaître automatiquement la langue selon le chemin local où se trouve le fichier (ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) lors du build, sans avoir à spécifier manuellement les balises 'lang' et 'permalink' dans le YAML front matter du fichier markdown original écrit.
- [x] La partie en-tête de chaque page du site doit inclure les balises méta Content-Language appropriées, les balises alternatives hreflang et les liens canoniques pour répondre aux directives SEO Google pour la recherche multilingue.
- [x] Il doit être possible de fournir tous les liens de pages par version linguistique du site sans omission via `sitemap.xml`{: .filepath}, et `sitemap.xml`{: .filepath} lui-même ne doit exister qu'une seule fois dans le chemin racine sans duplication.
- [x] Toutes les fonctionnalités fournies par le [thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) doivent fonctionner normalement sur chaque page linguistique, sinon elles doivent être corrigées pour fonctionner normalement.
  - [x] Fonctionnement normal des fonctionnalités 'Recently Updated' et 'Trending Tags'
  - [x] Aucune erreur ne doit se produire lors du processus de build utilisant GitHub Actions
  - [x] Fonctionnement normal de la fonction de recherche de posts en haut à droite du blog

## Application du plugin Polyglot
Jekyll ne prend pas en charge nativement les blogs multilingues, donc pour implémenter un blog multilingue satisfaisant les exigences ci-dessus, il faut utiliser un plugin externe. Après recherche, j'ai trouvé que [Polyglot](https://github.com/untra/polyglot) est largement utilisé pour l'implémentation de sites web multilingues et peut satisfaire la plupart des exigences ci-dessus, j'ai donc adopté ce plugin.

### Installation du plugin
Comme j'utilise Bundler, j'ai ajouté le contenu suivant au `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Ensuite, exécuter `bundle update` dans le terminal complète automatiquement l'installation.

Si vous n'utilisez pas Bundler, vous pouvez également installer directement le gem avec la commande `gem install jekyll-polyglot` dans le terminal, puis ajouter le plugin dans `_config.yml`{: .filepath} comme suit.

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuration des paramètres
Ensuite, ouvrez le fichier `_config.yml`{: .filepath} et ajoutez le contenu ci-dessous.

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages` : Liste des langues à prendre en charge
- `default_lang` : Langue de fallback par défaut
- `exclude_from_localization` : Spécification des expressions régulières de chaînes de chemins de fichiers/dossiers racine à exclure de la localisation linguistique
- `parallel_localization` : Valeur booléenne spécifiant s'il faut paralléliser le traitement multilingue lors du processus de build
- `lang_from_path` : Valeur booléenne, si définie sur 'true', même sans spécifier séparément l'attribut 'lang' comme YAML front matter dans le fichier markdown du post, si la chaîne de chemin du fichier markdown contient un code de langue, elle sera automatiquement reconnue et utilisée

> La [documentation officielle du protocole Sitemap](https://www.sitemaps.org/protocol.html#location) stipule ce qui suit :
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> Pour respecter cela, il faut s'assurer qu'un seul fichier `sitemap.xml`{: .filepath} avec le même contenu existe dans le répertoire racine au lieu d'être créé séparément par langue, en l'ajoutant à la liste 'exclude_from_localization', pour éviter l'exemple incorrect suivant.
>
> Exemple incorrect (le contenu de chaque fichier n'est pas différent par langue mais identique) :
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Mise à jour du 14.01.12025) Suite à l'acceptation de [la Pull Request que j'ai soumise pour renforcer le contenu mentionné ci-dessus dans le README](https://github.com/untra/polyglot/pull/230), les mêmes conseils peuvent maintenant être consultés dans la [documentation officielle de Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Bien que spécifier 'parallel_localization' sur 'true' ait l'avantage de réduire considérablement le temps de build, au moment de juillet 12024, lorsque cette fonctionnalité était activée pour ce blog, il y avait un bug où les titres des liens dans les parties 'Recently Updated' et 'Trending Tags' de la barre latérale droite de la page n'étaient pas traités correctement et se mélangeaient avec d'autres langues. Comme cela semble encore instable, il faut tester si cela fonctionne normalement avant de l'appliquer au site. De plus, [cette fonctionnalité n'est pas prise en charge sur Windows et doit être désactivée](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

De plus, [dans Jekyll 4.0, il faut désactiver la génération de sourcemaps CSS comme suit](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Points à noter lors de la rédaction de posts
Les points à noter lors de la rédaction de posts multilingues sont les suivants :
- Spécification appropriée du code de langue : Il faut spécifier le code de langue ISO approprié en utilisant le chemin du fichier (ex. `/_posts/ko/example-post.md`{: .filepath}) ou l'attribut 'lang' du YAML front matter (ex. `lang: ko`). Référez-vous aux exemples de la [documentation Chrome Developer](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Cependant, bien que la [documentation Chrome Developer](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) indique les codes régionaux au format 'pt_BR', en réalité il faut utiliser - au lieu de _ comme 'pt-BR' pour que cela fonctionne normalement lors de l'ajout ultérieur de balises alternatives hreflang dans l'en-tête HTML.
{: .prompt-tip }

- Les chemins et noms de fichiers doivent être cohérents.

Pour plus de détails, veuillez consulter le [README du dépôt GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modification de l'en-tête HTML et du sitemap
Maintenant, pour le SEO, il faut insérer les balises méta Content-Language et les balises alternatives hreflang dans l'en-tête HTML de chaque page du blog, et spécifier appropriément l'URL canonique.

### En-tête HTML
Basé sur la version 1.8.1 qui est la dernière version au moment de novembre 12024, Polyglot a une fonctionnalité qui effectue automatiquement le travail ci-dessus lors de l'appel de la balise Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} dans la partie en-tête de la page.
Cependant, cela suppose que l'attribut 'permalink' a été spécifié pour cette page, et ne fonctionne pas normalement sinon.

J'ai donc récupéré le [head.html du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) puis ajouté directement le contenu comme suit.
J'ai travaillé en me référant à la [page SEO Recipes du blog officiel Polyglot](https://polyglot.untra.io/seo/), mais j'ai modifié pour utiliser l'attribut `page.url` au lieu de `page.permalink` pour correspondre à mon environnement d'utilisation et mes exigences.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">
  
  {% if site.default_lang -%}
  <link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />
  {%- endif -%}
  {% for lang in site.languages -%}
    {% if lang == site.default_lang -%}
      {%- continue -%}
    {%- endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {%- endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

(Ajout du 29.07.12025) De plus, le thème Chirpy intègre par défaut le plugin [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag), mais j'ai confirmé que les propriétés de métadonnées [Open Graph](https://ogp.me/) `og:locale`, `og:url` générées automatiquement par Jekyll SEO Tag et l'[URL canonique](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) (élément `link` `rel="canonical"`) sont basées sur la langue par défaut du site (`site.lang`, `site.default_lang`) et nécessitent un traitement supplémentaire.  
J'ai donc ajouté la déclaration suivante avant {% raw %}`{{ seo_tags }}`{% endraw %}.

{% raw %}
```liquid
(précédent)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(milieu)...

  {%- capture old_og_locale -%}
    <meta property="og:locale" content="{{site.lang}}" />
  {%- endcapture -%}
  {%- capture new_og_locale -%}
    <meta property="og:locale" content="{{site.active_lang}}" />
    {% for lang in site.languages -%}
      {%- if lang == site.active_lang -%}
        {%- continue -%}
      {%- endif %}
    <meta property="og:locale:alternate" content="{{lang}}" />
    {%- endfor %}
  {%- endcapture -%}
  {% assign seo_tags = seo_tags | replace: old_og_locale, new_og_locale %}
  
  {% unless site.active_lang == site.default_lang -%}
    {%- capture old_canonical_link -%}
      <link rel="canonical" href="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture old_og_url -%}
      <meta property="og:url" content="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_canonical_link -%}
      <link rel="canonical" href="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_og_url -%}
      <meta property="og:url" content="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {% assign seo_tags = seo_tags | replace: old_canonical_link, new_canonical_link %}
    {% assign seo_tags = seo_tags | replace: old_og_url, new_og_url %}
  {%- endunless %}

  {{ seo_tags }}

  ...(suite)
```
{: file='/_includes/head.html'}
{% endraw %}

> Selon la [documentation Google Developer](https://developers.google.com/search/docs/crawling-indexing/canonicalization), lorsqu'une page a plusieurs versions linguistiques, elles ne sont considérées comme des doublons que si la langue du contenu principal est la même, c'est-à-dire lorsque seuls les en-têtes, pieds de page et autres textes non importants sont traduits et que le corps du texte est identique. Par conséquent, dans le cas où le texte du corps est fourni en plusieurs langues comme ce blog actuellement, toutes les versions linguistiques sont considérées comme des pages indépendantes et non des doublons, il faut donc spécifier des URL canoniques différentes selon la langue.  
> Par exemple, pour la version coréenne de cette page, l'URL canonique n'est pas "{{site.url}}{{page.url}}" mais "{{site.url}}/ko{{page.url}}".
{: .prompt-tip }

### Sitemap
Si aucun modèle n'est spécifié séparément, le sitemap généré automatiquement par Jekyll lors du build ne prend pas en charge normalement les pages multilingues, donc créez un fichier `sitemap.xml`{: .filepath} dans le répertoire racine et saisissez le contenu comme suit.

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages -%}

  {% for node in site.pages %}
    {%- comment -%}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{%- endcomment -%}
    {%- comment -%}<!-- Exclude redirects from sitemap -->{%- endcomment -%}
    {%- if node.redirect.to -%}
      {%- continue -%}
    {%- endif -%}
    {%- unless site.exclude_from_localization contains node.path -%}
      {%- comment -%}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{%- endcomment -%}
      {% if node.layout %}
        <url>
          <loc>
            {%- if lang == site.default_lang -%}
              {{ node.url | absolute_url }}
            {%- else -%}
              {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
            {%- endif -%}
          </loc>
          {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {% endif -%}
          {% if site.default_lang -%}
          <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
          {%- endif -%}
          {% for lang in site.languages -%}
            {% if lang == site.default_lang -%}
              {%- continue -%}
            {%- endif %}
          <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
          {%- endfor %}
        </url>
      {% endif %}
    {%- elsif site.default_lang -%}
        <url>
          <loc>{{ node.url | absolute_url }}</loc>
      {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {% endif -%}
        </url>
    {%- endunless -%}
  {% endfor %}

  {%- comment -%}<!-- This loops through all site collections including posts -->{%- endcomment -%}
  {% for collection in site.collections %}
    {% for node in site[collection.label] %}
      <url>
        <loc>
          {%- if lang == site.default_lang -%}
            {{ node.url | absolute_url }}
          {%- else -%}
            {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
          {%- endif -%}
        </loc>
        {% if node.last_modified_at and node.last_modified_at != node.date -%}
        <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- elsif node.date -%}
        <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- endif %}
        {% if site.default_lang -%}
        <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
        {%- endif -%}
        {% for lang in site.languages -%}
          {% if lang == site.default_lang -%}
            {%- continue -%}
          {%- endif %}
        <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
        {%- endfor %}
      </url>
    {% endfor %}
  {% endfor %}

{%- endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## Lecture complémentaire
Suite dans la [Partie 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
