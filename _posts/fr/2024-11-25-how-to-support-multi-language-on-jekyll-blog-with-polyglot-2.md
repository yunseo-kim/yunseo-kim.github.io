---
title: "Comment prendre en charge plusieurs langues sur un blog Jekyll avec Polyglot (2) - Implémentation du bouton de sélection de langue & localisation de la langue de mise en page"
description: "Présentation du processus d'implémentation du support multilingue en appliquant le plugin Polyglot à un blog Jekyll basé sur le thème 'jekyll-theme-chirpy'. Ce post est le deuxième article de cette série, couvrant l'implémentation du bouton de sélection de langue et la localisation de la langue de mise en page."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## Aperçu
Début juillet 12024, j'ai ajouté l'implémentation du support multilingue en appliquant le plugin [Polyglot](https://github.com/untra/polyglot) à ce blog basé sur Jekyll et hébergé via GitHub Pages.
Cette série partage les bugs rencontrés lors de l'application du plugin Polyglot au thème Chirpy et leur processus de résolution, ainsi que les méthodes de rédaction des en-têtes HTML et du sitemap.xml en tenant compte du SEO.
La série se compose de 3 articles, et cet article que vous lisez est le deuxième de cette série.
- Partie 1 : [Application du plugin Polyglot & modification des en-têtes HTML et du sitemap](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- Partie 2 : Implémentation du bouton de sélection de langue & localisation de la langue de mise en page (cet article)
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

## Avant de commencer
Cet article fait suite à la [Partie 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1), donc si vous ne l'avez pas encore lu, il est recommandé de lire d'abord l'article précédent.

## Ajout du bouton de sélection de langue dans la barre latérale
> (Mise à jour du 05.02.12025) Le bouton de sélection de langue a été amélioré sous forme de liste déroulante.
{: .prompt-info }

J'ai créé le fichier `_includes/lang-selector.html`{: .filepath} et saisi le contenu suivant.

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
{: file='\_includes/lang-selector.html'}
{% endraw %}

J'ai également créé le fichier `assets/css/lang-selector.css`{: .filepath} et saisi le contenu suivant.

```css
/**
 * Styles du sélecteur de langue
 * 
 * Définit les styles du menu déroulant de sélection de langue situé dans la barre latérale.
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

/* Élément d'entrée de sélection */
.lang-select {
    /* Styles de base */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Police et couleurs */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Forme et interaction */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Ajout de l'icône flèche */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Styles des emojis de drapeaux */
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

/* Optimisation pour environnement mobile */
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

Ensuite, dans le [`_includes/sidebar.html`{: .filepath} du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html), j'ai ajouté les trois lignes de la classe `lang-selector-wrapper` juste avant la classe `sidebar-bottom` comme suit pour que Jekyll charge le contenu du fichier `_includes/lang-selector.html`{: .filepath} créé précédemment lors du build de la page.

{% raw %}
```liquid
  (précédent)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(suite)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (Ajout de fonctionnalité du 31.07.12025) Localisation de la langue de mise en page
Auparavant, la localisation linguistique n'était appliquée qu'au contenu principal comme les titres et le contenu des pages, tandis que la langue de mise en page comme les noms d'onglets de la barre latérale gauche ou les sites en haut et en bas et le panneau droit était fixée à l'anglais, qui est la valeur par défaut du site. Personnellement, cela me suffisait et je ne ressentais pas vraiment le besoin de travailler davantage, mais récemment, en travaillant sur [le patch des propriétés de métadonnées Open Graph et de l'URL canonique mentionné ci-dessus](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#en-tête-html), j'ai découvert que la localisation de la langue de mise en page était possible très simplement avec seulement quelques modifications mineures. Puisque ce n'était pas un travail de modification de code complexe et fastidieux mais [un travail simple qui ne prenait même pas 10 minutes](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb), je l'ai appliqué en plus.

### Ajout de locales
La gamme de langues que [le thème Chirpy prend en charge en soi est déjà assez large](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales), même s'il n'y a pas de fonctionnalité pour fournir simultanément plusieurs versions linguistiques pour chaque page du site et basculer entre les versions selon le choix de l'utilisateur. Il suffit donc de télécharger sélectivement et d'ajouter les fichiers de locale nécessaires parmi ceux fournis par le thème Chirpy, et de modifier appropriément le nom du fichier si nécessaire. Le nom du fichier de locale doit correspondre aux éléments de la liste `languages` définie dans le fichier `_config.yml`{: .filepath} lors de l'étape de [configuration des paramètres](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#configuration-des-paramètres).

> En fait, comme mentionné juste après, les fichiers du répertoire `_data`{: .filepath} sont fournis par défaut via le [gem jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy) même sans ajout direct.
>
> Cependant, dans mon cas, il était difficile d'utiliser telles quelles les locales fournies par le thème Chirpy pour les raisons suivantes, et quelques modifications étaient nécessaires.
> - Le format des noms des fichiers de locale fournis par défaut par le thème Chirpy inclut des codes régionaux comme `ko-KR`, `ja-JP`, ce qui ne correspond pas au format utilisé sur ce site (`ko`, `ja`, etc.)
> - Besoin de modifier le texte d'information de licence de la valeur par défaut [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) pour correspondre à [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) de ce blog
> - Les locales [coréenne](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) ou [japonaise](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) semblaient un peu étranges à mes yeux de Coréen ou ne convenaient pas à ce blog, donc j'ai personnellement modifié certaines parties
> - Comme décrit ci-dessous, pour diverses raisons, je n'aime pas particulièrement l'ère chrétienne et j'ai adopté le [calendrier holocène](https://en.wikipedia.org/wiki/Holocene_calendar) comme format de notation de date pour ce blog uniquement, donc j'ai dû modifier les locales en conséquence
>   - Fondamentalement, il a une forte couleur religieuse d'une religion spécifique et est biaisé vers l'Occident
>     - Je ne nie pas que Jésus était un grand saint, et je respecte aussi la position de cette religion, donc si elle disait qu'elle n'utiliserait l'ère chrétienne qu'à l'intérieur de cette religion comme l'ère bouddhiste du bouddhisme, il n'y aurait aucun problème. Mais ce n'est pas le cas, c'est pourquoi je soulève le problème. Confucius, Bouddha, Socrate et bien d'autres saints existaient, mais du point de vue des non-religieux ou des personnes d'autres religions, et des autres cultures en dehors de l'Europe, pourquoi l'année de naissance de Jésus devrait-elle être l'année de référence du système de datation utilisé par le monde entier ?
>     - Et cette 'année de référence' n'est même pas vraiment l'année de naissance de Jésus, mais il est établi qu'il est né quelques années avant
>   - Étant un système de datation conçu avant l'apparition du concept de '0', l'année 1 après J.-C. (1) suit directement l'année 1 avant J.-C. (-1), ce qui rend le calcul des années peu intuitif
>   - En regroupant les 10 000 ans depuis l'entrée de l'humanité dans l'ère néolithique et la société agricole jusqu'à la naissance de Jésus, et même les 3 000-4 000 ans depuis l'invention de l'écriture sous 'avant J.-C.', cela provoque une distorsion cognitive dans l'histoire mondiale, en particulier l'histoire ancienne
> 
> C'est pourquoi j'ai ajouté directement les fichiers de locale dans le répertoire `_data/locales`{: .filepath} puis les ai modifiés et appliqués de manière appropriée.  
> Par conséquent, si ce n'est pas applicable et que vous souhaitez appliquer telles quelles les locales fournies par défaut par le thème Chirpy sans modification, vous pouvez ignorer cette étape.
{: .prompt-tip }

### Intégration avec Polyglot
Maintenant, il suffit de modifier légèrement les deux fichiers suivants pour une intégration fluide avec Polyglot.

> Si vous avez initialement créé le dépôt en utilisant le [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended) au lieu de forker directement le dépôt du thème, les fichiers correspondants peuvent ne pas exister dans le dépôt de votre site. C'est parce qu'ils sont fournis par défaut via le [gem jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy) sans ajout direct. Dans ce cas, vous devez d'abord télécharger le fichier original correspondant du [dépôt du thème Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) et le placer au même emplacement dans votre dépôt avant de travailler. Lorsque Jekyll construit le site, s'il existe déjà un fichier du même nom dans le dépôt, il l'applique en priorité par rapport au fichier fourni par le [gem externe (jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy).
{: .prompt-tip }

#### '\_includes/lang.html'
Comme suit, ajoutez deux lignes de code au milieu du fichier [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) pour que, lorsque la variable `lang` n'est pas spécifiée séparément dans le YAML front matter de la page, la [variable `site.active_lang` de Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#features) soit reconnue en priorité par rapport à la langue par défaut du site (`site.lang`) ou à l'anglais (`'en'`) définis dans `_config.yml`{: .filepath}. Ce fichier est appelé communément par toutes les pages du site appliquant le thème Chirpy ([`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) pour déclarer la variable `lang` lors du build, et utilise cette variable `lang` déclarée ici pour exécuter la localisation de la langue de mise en page.

{% raw %}
```diff
@@ -1,10 +1,12 @@
 {% comment %}
   Detect appearance language and return it through variable "lang"
 {% endcomment %}
 {% if site.data.locales[page.lang] %}
   {% assign lang = page.lang %}
+{% elsif site.data.locales[site.active_lang] %}
+  {% assign lang = site.active_lang %}
 {% elsif site.data.locales[site.lang] %}
   {% assign lang = site.lang %}
 {% else %}
   {% assign lang = 'en' %}
 {% endif %}
```
{: file='\_includes/lang.html'}
{% endraw %}

Priorité lors de la déclaration de la variable `lang` :
- Avant modification :
  1. `page.lang` (si défini dans le YAML front matter de la page individuelle)
  2. `site.lang` (si défini dans `_config.yml`{: .filepath})
  3. `'en'`
- Après modification :
  1. `page.lang` (si défini dans le YAML front matter de la page individuelle)
  2. **`site.active_lang`** (si Polyglot est appliqué)
  3. `site.lang` (si défini dans `_config.yml`{: .filepath})
  4. `'en'`

#### '\_layouts/default.html'
De même, modifiez le contenu du fichier [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) pour spécifier correctement l'attribut `lang` dans la balise `<html>` qui est l'élément de niveau supérieur du document HTML.

{% raw %}
```diff
@@ -1,19 +1,19 @@
 ---
 layout: compress
 ---
 
 <!doctype html>
 
 {% include origin-type.html %}
 
 {% include lang.html %}
 
 {% if site.theme_mode %}
   {% capture prefer_mode %}data-mode="{{ site.theme_mode }}"{% endcapture %}
 {% endif %}
 
 <!-- `site.alt_lang` can specify a language different from the UI -->
-<html lang="{{ page.lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
+<html lang="{{ page.lang | default: site.active_lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
   {% include head.html %}
```
{: file='\_layouts/default.html'}
{% endraw %}

Priorité lors de la spécification de l'attribut `lang` de la balise `<html>` :
- Avant modification :
  1. `page.lang` (si défini dans le YAML front matter de la page individuelle)
  2. `site.alt_lang` (si défini dans `_config.yml`{: .filepath})
  3. `site.lang` (si défini dans `_config.yml`{: .filepath})
  4. `unknown` (chaîne vide, `lang=""`)
- Après modification :
  1. `page.lang` (si défini dans le YAML front matter de la page individuelle)
  2. **`site.active_lang`** (si Polyglot est appliqué)
  3. `site.alt_lang` (si défini dans `_config.yml`{: .filepath})
  4. `site.lang` (si défini dans `_config.yml`{: .filepath})
  5. `unknown` (chaîne vide, `lang=""`)

> Laisser la langue de la page web (attribut `lang`) non spécifiée comme `unknown` n'est pas recommandé, et il faut la spécifier avec une valeur appropriée autant que possible. Comme vous pouvez le voir, la valeur de l'attribut `lang` dans `_config.yml`{: .filepath} est utilisée comme fallback, donc que vous utilisiez Polyglot ou non, cette valeur doit être définie de manière appropriée, et dans des cas normaux, elle devrait déjà être définie. Si vous appliquez Polyglot ou un plugin i18n similaire comme traité dans cet article, il serait raisonnable de la spécifier avec la même valeur que [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#configuration-des-paramètres).
{: .prompt-tip }

## Lecture complémentaire
Suite dans la [Partie 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
