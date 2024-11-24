---
title: Comment utiliser Polyglot pour prendre en charge plusieurs langues sur un blog Jekyll
description: >-
  Présentation du processus d'implémentation du support multilingue en appliquant le plugin Polyglot à un blog Jekyll basé sur 'jekyll-theme-chirpy'.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
- RegExp
---
## Introduction
Il y a environ 4 mois, début juillet 2024, j'ai ajouté la prise en charge multilingue à ce blog, hébergé via Github Pages et basé sur Jekyll, en appliquant le plugin [Polyglot](https://github.com/untra/polyglot).
Dans cet article, je partage les bugs rencontrés lors de l'application du plugin Polyglot au thème Chirpy et leur processus de résolution, ainsi que la méthode de rédaction de l'en-tête html et du sitemap.xml en tenant compte du SEO.

## Exigences
- [x] Le résultat de la construction (pages web) doit pouvoir être fourni en distinguant les chemins par langue (ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Pour minimiser le temps et les efforts supplémentaires nécessaires à la prise en charge multilingue, la langue doit pouvoir être automatiquement reconnue lors de la construction en fonction du chemin local où se trouve le fichier markdown original (ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}), sans avoir à spécifier manuellement les balises 'lang' et 'permalink' dans le YAML front matter du fichier original.
- [x] La partie en-tête de chaque page du site doit inclure des balises méta Content-Language appropriées et des balises alternatives hreflang pour répondre aux directives SEO pour la recherche multilingue de Google.
- [x] Tous les liens des pages prenant en charge chaque langue sur le site doivent pouvoir être fournis sans omission dans `sitemap.xml`, et `sitemap.xml` lui-même ne doit exister qu'une seule fois dans le chemin racine sans duplication.
- [ ] Toutes les fonctionnalités fournies par le [thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) doivent fonctionner normalement sur chaque page de langue, et si ce n'est pas le cas, elles doivent être modifiées pour fonctionner correctement.
  - [x] Fonctionnement normal des fonctionnalités telles que 'Recently Updated', 'Trending Tags', etc.
  - [x] Pas de faux positifs (False Positive) lors de la vérification des erreurs de liens internes du site pendant le processus de construction utilisant GitHub Actions
  - [ ] Fonctionnement normal de la fonction de recherche de posts en haut à droite du blog

## Application du plugin Polyglot
Comme Jekyll ne prend pas en charge nativement les blogs multilingues, il faut utiliser un plugin externe pour implémenter un blog multilingue répondant aux exigences ci-dessus. Après recherche, j'ai constaté que [Polyglot](https://github.com/untra/polyglot) est largement utilisé pour implémenter des sites web multilingues et peut satisfaire la plupart des exigences ci-dessus, j'ai donc choisi ce plugin.

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

- languages : liste des langues à prendre en charge
- default_lang : langue par défaut pour le fallback
- exclude_from_localization : spécifie les expressions régulières des chemins de fichiers/dossiers racine à exclure de la localisation
- parallel_localization : valeur booléenne indiquant s'il faut paralléliser le traitement multilingue pendant le processus de construction
- lang_from_path : valeur booléenne, si définie sur 'true', elle reconnaîtra et utilisera automatiquement le code de langue inclus dans la chaîne de chemin du fichier Markdown correspondant, même si l'attribut 'lang' n'est pas spécifié explicitement dans le YAML front matter du fichier Markdown

> Le [document officiel du protocole Sitemap](https://www.sitemaps.org/protocol.html#location) stipule ce qui suit :
>
>> "L'emplacement d'un fichier Sitemap détermine l'ensemble des URL qui peuvent être incluses dans ce Sitemap. Un fichier Sitemap situé à http://example.com/catalog/sitemap.xml peut inclure toutes les URL commençant par http://example.com/catalog/ mais ne peut pas inclure les URL commençant par http://example.com/images/."
>
>> "Il est fortement recommandé de placer votre Sitemap dans le répertoire racine de votre serveur web."
>
> Pour se conformer à cela, il faut ajouter 'sitemap' à la liste 'exclude_from_localization' afin qu'un seul fichier `sitemap.xml` avec le même contenu existe dans le répertoire racine, et non pas un pour chaque langue, comme dans le mauvais exemple ci-dessous.
>
> Mauvais exemple (le contenu de chaque fichier n'est pas différent par langue, tous sont identiques) :
> - https://www.yunseo.kim/sitemap.xml
> - https://www.yunseo.kim/ko/sitemap.xml
> - https://www.yunseo.kim/es/sitemap.xml
> - https://www.yunseo.kim/pt-BR/sitemap.xml
> - https://www.yunseo.kim/ja/sitemap.xml
> - https://www.yunseo.kim/fr/sitemap.xml
> - https://www.yunseo.kim/de/sitemap.xml
{: .prompt-tip }

> Définir 'parallel_localization' sur 'true' présente l'avantage de réduire considérablement le temps de construction, mais à partir de juillet 2024, lorsque cette fonctionnalité était activée pour ce blog, il y avait un bug où les titres des liens dans les sections 'Recently Updated' et 'Trending Tags' de la barre latérale droite de la page n'étaient pas traités correctement et étaient mélangés avec d'autres langues. Cela semble encore instable, donc il est nécessaire de tester à l'avance si cela fonctionne normalement avant de l'appliquer au site. De plus, [cette fonctionnalité n'est pas prise en charge sous Windows, elle doit donc être désactivée](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

De plus, [dans Jekyll 4.0, vous devez désactiver la génération de sourcemaps CSS comme suit](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # Dans Jekyll 4.0, les sourcemaps SCSS seront générées incorrectement en raison du fonctionnement de Polyglot
```
{: file='_config.yml'}

### Points à noter lors de la rédaction d'articles
Voici les points à noter lors de la rédaction d'articles multilingues :
- Spécification du code de langue approprié : Il faut spécifier le code de langue ISO approprié en utilisant le chemin du fichier (ex. `/_posts/ko/example-post.md`{: .filepath}) ou l'attribut 'lang' dans le YAML front matter (ex. `lang: ko`). Référez-vous aux exemples de la [documentation pour développeurs Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Cependant, bien que la [documentation pour développeurs Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) indique le code de région sous la forme 'pt_BR', il faut en réalité utiliser '-' au lieu de '_' comme dans 'pt-BR' pour que cela fonctionne correctement lors de l'ajout ultérieur de balises hreflang alternatives dans l'en-tête html.

- Le chemin et le nom du fichier doivent être cohérents.

Pour plus de détails, veuillez vous référer au [README du dépôt GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Dépannage ('relative_url_regex': target of repeat operator is not specified)
Après avoir terminé les étapes précédentes, j'ai exécuté la commande `bundle exec jekyll serve` pour tester la construction, mais la construction a échoué avec l'erreur `'relative_url_regex': target of repeat operator is not specified`.

```shell
...(début omis)
                    ------------------------------------------------
      Jekyll 4.3.4   Veuillez ajouter `--trace` à la commande `serve` 
                     pour toute information supplémentaire ou backtrace. 
                    ------------------------------------------------
/Users/yunseo/.gem/ruby/3.2.2/gems/jekyll-polyglot-1.8.1/lib/jekyll/polyglot/
patches/jekyll/site.rb:234:in `relative_url_regex': target of repeat operator 
is not specified: /href="?\/((?:(?!*.gem)(?!*.gemspec)(?!tools)(?!README.md)(
?!LICENSE)(?!*.config.js)(?!rollup.config.js)(?!package*.json)(?!.sass-cache)
(?!.jekyll-cache)(?!gemfiles)(?!Gemfile)(?!Gemfile.lock)(?!node_modules)(?!ve
ndor\/bundle\/)(?!vendor\/cache\/)(?!vendor\/gems\/)(?!vendor\/ruby\/)(?!en\/
)(?!ko\/)(?!es\/)(?!pt-BR\/)(?!ja\/)(?!fr\/)(?!de\/)[^,'"\s\/?.]+\.?)*(?:\/[^
\]\[)("'\s]*)?)"/ (RegexpError)

...(fin omise)
```

Après avoir recherché si un problème similaire avait déjà été signalé, j'ai trouvé [exactement le même problème](https://github.com/untra/polyglot/issues/204) déjà enregistré dans le dépôt Polyglot, avec une solution existante.

Le fichier `_config.yml` du [thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml) appliqué à ce blog contient la clause suivante :

```yml
exclude:
  - "*.gem"
  - "*.gemspec"
  - docs
  - tools
  - README.md
  - LICENSE
  - "*.config.js"
  - package*.json
```
{: file='_config.yml'}

La cause du problème réside dans le fait que les expressions régulières des deux fonctions suivantes incluses dans le fichier [`site.rb` de Polyglot](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb) ne traitent pas correctement les modèles de globbing contenant des caractères génériques comme `"*.gem"`, `"*.gemspec"`, `"*.config.js"` ci-dessus.

{% raw %}
```ruby
    # une regex qui correspond aux urls relatives dans un document html
    # correspond à href="baseurl/foo/bar-baz" href="/foo/bar-baz" et autres similaires
    # évite de correspondre aux fichiers exclus. prepare s'assure
    # que tous les répertoires @exclude ont un slash final.
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    # une regex qui correspond aux urls absolues dans un document html
    # correspond à href="http://baseurl/foo/bar-baz" et autres similaires
    # évite de correspondre aux fichiers exclus. prepare s'assure
    # que tous les répertoires @exclude ont un slash final.
    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(chemin racine de polyglot)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

Il y a deux façons de résoudre ce problème.

### 1. Forker Polyglot, modifier la partie problématique et l'utiliser
Au moment de la rédaction de cet article (novembre 2024), la [documentation officielle de Jekyll](https://jekyllrb.com/docs/configuration/options/#global-configuration) indique que le paramètre `exclude` prend en charge l'utilisation de modèles de globbing.

>"Cette option de configuration prend en charge les modèles de globbing de noms de fichiers de Ruby's File.fnmatch pour faire correspondre plusieurs entrées à exclure."

En d'autres termes, la cause du problème ne réside pas dans le thème Chirpy mais dans les deux fonctions `relative_url_regex()` et `absolute_url_regex()` de Polyglot, donc la solution fondamentale est de les modifier pour qu'elles ne posent pas de problème.

Comme ce bug n'a pas encore été résolu dans Polyglot, vous pouvez forker le dépôt Polyglot en vous référant à [cet article de blog](https://hionpu.com/en/posts/github_blog_4#4-polyglot-dependency-issue) et à [la réponse donnée au problème GitHub précédent](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322), puis modifier la partie problématique comme suit et l'utiliser à la place du Polyglot original.

{% raw %}
```ruby
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(chemin racine de polyglot)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

### 2. Remplacer les modèles de globbing par des noms de fichiers exacts dans le fichier de configuration `_config.yml` du thème Chirpy
En réalité, la méthode orthodoxe et idéale serait que le patch ci-dessus soit reflété dans le courant principal de Polyglot. Cependant, en attendant, il faudrait utiliser la version forkée à la place, mais dans ce cas, il serait fastidieux de suivre et de refléter chaque mise à jour du flux amont de Polyglot à chaque fois qu'il est mis à jour, j'ai donc utilisé une autre méthode.

Si vous vérifiez les fichiers situés dans le chemin racine du projet dans le [dépôt du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) correspondant aux modèles `"*.gem"`, `"*.gemspec"`, `"*.config.js"`, il n'y a de toute façon que les 3 suivants :
- `jekyll-theme-chirpy.gemspec`
- `purgecss.config.js`
- `rollup.config.js`

Par conséquent, si vous supprimez les modèles de globbing de la clause `exclude` dans le fichier `_config.yml` et les remplacez comme suit, Polyglot pourra les traiter sans problème.

```yml
exclude: # Modifié en référence au problème https://github.com/untra/polyglot/issues/204.
  # - "*.gem"
  - jekyll-theme-chirpy.gemspec # - "*.gemspec"
  - tools
  - README.md
  - LICENSE
  - purgecss.config.js # - "*.config.js"
  - rollup.config.js
  - package*.json
```

## Modification de l'en-tête html et du sitemap
Maintenant, pour le SEO, nous devons insérer les balises méta Content-Language et les balises alternatives hreflang dans l'en-tête html de chaque page du blog.

### En-tête html
À partir de la version 1.8.1, la dernière version en novembre 2024, Polyglot dispose d'une fonctionnalité qui effectue automatiquement cette tâche lorsque la balise Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} est appelée dans la partie en-tête de la page.
Cependant, cela suppose que la balise d'attribut 'permalink' a été spécifiée explicitement pour cette page, et ne fonctionnera pas correctement si ce n'est pas le cas.

J'ai donc récupéré le [head.html du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) puis j'ai directement ajouté le contenu suivant.
J'ai travaillé en me référant à [la page SEO Recipes du blog officiel de Polyglot](https://polyglot.untra.io/seo/), mais j'ai modifié pour utiliser l'attribut `page.url` à la place si `page.permalink` n'existe pas.
De plus, en me référant à [la documentation officielle de Google Search Central](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault), j'ai spécifié `x-default` au lieu de `site.default_lang` comme valeur d'attribut hreflang pour la page en langue par défaut du site, afin que le lien de cette page soit reconnu comme fallback si la langue préférée du visiteur n'est pas dans la liste des langues prises en charge par le site ou si la langue préférée du visiteur ne peut pas être reconnue.

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
J'ai créé un fichier `_includes/lang-selector.html` et entré le contenu suivant :

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

Ensuite, j'ai ajouté les trois lignes suivantes à la partie de classe "sidebar-bottom" du [`_includes/sidebar.html` du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) pour que Jekyll charge le contenu de `_includes/lang-selector.html` précédemment écrit lors de la construction de la page :

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Problème d'indexation incorrecte des pages multilingues lors de l'utilisation de la fonction de recherche
Après avoir terminé les étapes précédentes, presque toutes les fonctionnalités du site fonctionnaient de manière satisfaisante comme prévu. Cependant, j'ai découvert tardivement qu'il y avait un problème : la barre de recherche située en haut à droite de la page appliquant le thème Chirpy n'indexait pas les pages dans des langues autres que `site.default_lang` (dans le cas de ce blog, l'anglais), et lors d'une recherche dans une langue autre que l'anglais, elle affichait des pages en anglais comme résultats de recherche.

Cela est dû au fait que la bibliothèque JavaScript [Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search) utilisée par le thème Chirpy dépend de la variable `site.posts` fournie par Jekyll pour effectuer l'indexation, et ne reconnaît donc pas les pages multilingues autres que la langue par défaut construites à l'aide de Polyglot.

La structure simple de Simple-Jekyll-Search, qui effectue l'indexation en s'appuyant uniquement sur les variables fournies par défaut par Jekyll avec un seul modèle liquid appelé [`search.json`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/assets/js/data/search.json), est un avantage, mais dans ce cas, c'est un inconvénient et une limitation fatals, et donc inadaptés à l'application à ce blog. À moins que Jekyll ne prenne en charge nativement les pages multilingues et que Polyglot ne fournisse une autre variable pouvant remplacer `site.posts`, je pense que Simple-Jekyll-Search ne pourra pas effectuer correctement l'indexation des pages multilingues requise par ce blog. Il est donc nécessaire de rechercher et d'appliquer une alternative pouvant remplacer Simple-Jekyll-Search, ce qui reste un défi et un sujet de post ultérieur.
