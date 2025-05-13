---
title: Creating and Managing a GitHub Pages Blog
description: Learn about the characteristics and differences between static and dynamic web pages, explore Static Site Generators, and host a Jekyll blog on GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
---
I started hosting a blog on GitHub Pages using Jekyll from early 12021 in the [Holocene calendar](https://en.wikipedia.org/wiki/Holocene_calendar). However, I didn't properly document the installation process at the time, which caused some difficulties with maintenance later on. So I decided to briefly document the installation process and maintenance methods.

(+ Updated 12024.12)

## 1. Static Site Generator & Web Hosting
### 1-1. Static Web Page vs Dynamic Web Page
#### Static Web Page
- Web pages that deliver data stored on the server directly to users
- The web server delivers pre-stored pages corresponding to user requests
- Users see the same web page unless the data stored on the server is changed
- Generally faster response times as it only needs to transfer the requested file without additional processing
- Consists of simple files, so only a web server needs to be set up, making it cost-effective
- Limited service as it only shows pre-stored information
- Data addition, modification, and deletion must be done manually by the administrator
- Structure is easier for search engines to crawl, making it relatively more advantageous for Search Engine Optimization (SEO)

#### Dynamic Web Page
- Web pages that process and deliver data stored on the server through scripts
- The web server interprets user requests, processes the data, and delivers the generated web page
- Users see web pages that change according to situation, time, requests, etc.
- Relatively slower response as scripts need to be processed to deliver the web page
- Additional costs incurred during setup as it requires an application server in addition to a web server
- Various services possible as it can dynamically provide combinations of different information
- Users can add, modify, and delete data from the browser depending on the web page structure

### 1-2. Static Site Generator (SSG)
- A tool that generates static web pages based on raw data (usually markdown text files) and predefined templates
- Automates the process of building and deploying web pages without having to write individual HTML pages directly
- Examples: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- A free static web page hosting service provided by GitHub
- Each account can host one personal representative web page and an unlimited number of project documentation pages per repository
- After creating a repository with the name format '{username}.github.io' matching your GitHub username, you can either directly push built HTML pages to the repository or use GitHub Actions to build and deploy
- If you own a domain, you can connect it in the settings to use a different domain address instead of the default '{username}.github.io' format

## 2. Choosing an SSG and Theme

### 2-1. Why I Chose Jekyll
There are several SSGs like Jekyll, Hugo, Gatsby, etc., but I decided to use Jekyll. The criteria I considered when choosing an SSG and the reasons for choosing Jekyll are as follows:
- Can I minimize unnecessary trial and error and focus on writing and blog operation?
  - Jekyll is the officially supported static website generator for GitHub Pages. Of course, other SSGs like Hugo and Gatsby can also be hosted on GitHub Pages, and there's also the option of using other hosting services like Netlify, but for a personal blog of this scale, the technical aspects of which SSG was used for construction, build speed, and performance aren't that important, so I decided it would be better to use something that's simpler to maintain and has more reference documentation.
  - Jekyll also has the longest development period compared to competitors like Hugo and Gatsby. This means it has well-documented resources, and there's an overwhelming amount of reference material available when problems arise.
- Are there a variety of themes and plugins available?
  - Even if you're using an SSG instead of writing HTML directly, creating various templates yourself is cumbersome, time-consuming, and unnecessary. There are many excellent themes already available online, so you can just adopt and use one you like.
  - Moreover, since I mainly use C and Python, I'm not very familiar with Ruby (Jekyll) or Go (Hugo), so I wanted to actively utilize existing themes and plugins.
  - With Jekyll, I could quickly find a theme that I liked at first glance, whereas Hugo and Gatsby seemed to have relatively fewer themes suitable for personal blog purposes. As mentioned above, the compatibility with GitHub Pages, which many developers use for personal blog hosting, and the development period seem to have had a significant impact here as well.

### 2-2. Theme Selection
#### Minimal Mistakes (12021.01 - 12022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- The theme I used for about 1 year and 3 months after first creating the blog
- Supports comment functionality through Disqus, Discourse, utterances, etc.
- Supports category and tag classification
- Built-in Google Analytics support
- Ability to choose from predefined skins
- I later discovered the Chirpy theme, which has a more elegant design that I preferred, but considering it's an engineering-focused blog, Minimal Mistakes had a clean design that was decent enough to use, even if it wasn't particularly pretty.

#### Chirpy Jekyll Theme (12022.04 - Present)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- The theme I've been using since switching in April 12022
- Supports multi-category classification and tag functionality
- Built-in support for LaTeX syntax mathematical expressions based on MathJax
- Built-in support for diagram functionality based on Mermaid
- Supports comment functionality through Disqus, Giscus, etc.
- Supports Google Analytics, GoatCounter
- Supports light and dark themes
- At the time of the theme transition, MathJax and Mermaid weren't natively supported by the Minimal Mistakes theme and had to be added through customization, but the Chirpy theme supports them by default. Although the customization wasn't particularly complex, it's still a minor advantage.
- Above all, the design is beautiful. While the Minimal Mistakes theme is clean, it has a certain stiffness that seems more suitable for official technical documentation or portfolio pages rather than blogs. The Chirpy theme, on the other hand, has a design that doesn't fall short compared to commercial blog platforms like Tistory, Medium, or velog.

## 3. Creating a GitHub Repository, Building, and Deploying
This is based on the Chirpy Jekyll Theme currently (12024.06) in use, and assumes Git is already installed.  
Refer to the [Jekyll official installation guide](https://jekyllrb.com/docs/installation/) and [Chirpy Jekyll Theme official page](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Installing Ruby & Jekyll
Install Ruby and Jekyll according to the [Jekyll official installation guide](https://jekyllrb.com/docs/installation/) for your operating system environment.

### 3-2. Creating a GitHub Repository
The [Chirpy Jekyll Theme official page](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) introduces the following two methods:
1. Using the "jekyll-theme-chirpy" gem to import core files and getting the rest of the resources from the [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) template
  - Advantage: Easy to apply version upgrades, as will be explained later.
  - Disadvantage: Customization is limited.
2. Forking the [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) repository as your blog repository
  - Advantage: You can freely customize by directly modifying the code, even for features not supported by the theme, as you manage all files directly within the repository.
  - Disadvantage: To apply version upgrades, you need to merge the [latest upstream tag from the original repository](https://github.com/cotes2020/jekyll-theme-chirpy/tags), which may conflict with your custom code. In this case, you need to resolve the conflicts yourself.

I chose method 1. The Chirpy theme is already highly complete, so most users don't have much to customize, and as of 12024, development and feature improvements are still quite active, so unless you're planning significant modifications, the benefits of keeping up with the original upstream outweigh the benefits of applying direct customization. The official Chirpy theme guide also recommends method 1 for most users.

### 3-3. Key Configuration
Apply the necessary settings in the `_config.yml`{: .filepath} file in the root directory and the `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath} files. The comments are well-written and the settings are intuitive, so they can be applied without much difficulty. The settings that might require separate work from external sources include registering authentication codes for Google Search Console integration and connecting webmaster tools like Google Analytics or GoatCounter, but these procedures aren't particularly complex and aren't the core topic of this article, so detailed descriptions are omitted.

### 3-4. Building Locally
This isn't a mandatory procedure, but you might want to check in advance whether a new post or site modification will display correctly on the web. In this case, open a terminal in the root directory of the local repository and run the following command:
```console
$ bundle exec jekyll s
```
After waiting a few seconds, the site will be built locally and you can check the result at <http://127.0.0.1:4000>.

### 3-5. Deploying
There are two methods:
1. Using GitHub Actions (when hosting on GitHub Pages)
  - If you're using the GitHub Free Plan, you need to keep the repository public
  - On the GitHub webpage, select the *Settings* tab of the repository, click *Code and automation > Pages* in the left navigation bar, and select the **GitHub Actions** option in the **Source** section
  - After setup is complete, the *Build and Deploy* workflow will automatically run whenever a new commit is pushed
2. Building and deploying directly (when using other hosting services or self-hosting)
  - Run the following command to build the site directly
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Upload the build results in the `_site` directory to the server

## 4. Writing Posts
The Chirpy theme's [post writing guide](https://chirpy.cotes.page/posts/write-a-new-post/) well documents how to write posts and the options available. It provides various features beyond what is described in this article, and it's good reference material, so refer to the official documentation if needed. Here, I'll summarize the key points to keep in mind every time you post.

### Creating a Markdown File
- Name format: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Location: `_posts`{: .filepath} directory

### Writing Front Matter
The front matter should be properly written at the beginning of the markdown file.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: Post title
- **description**: Summary. If not written, it automatically uses part of the beginning of the content, but it's recommended to write the description meta tag directly for search engine optimization (SEO). A length of about 135-160 characters for Roman alphabet-based languages or 80-110 characters for Korean is appropriate.
- **date**: Exact post creation time and timezone (optional, if omitted, it automatically uses the file creation date or modification date)
- **categories**: Post category classification
- **tags**: Tag classification to apply to the post
- **image**: Insert a preview image at the top of the post
  - **path**: Image file path
  - **alt**: Alternative text (optional)
- **toc**: Whether to use the table of contents feature in the right sidebar, default is `true`
- **comments**: Used to explicitly specify whether to use comments for individual posts, separate from the site's default settings
- **math**: Activate the built-in [MathJax](https://www.mathjax.org/) based mathematical expression feature, default is deactivated (`false`) for page performance
- **mermaid**: Activate the built-in [Mermaid](https://github.com/mermaid-js/mermaid) based diagram expression feature, default is deactivated (`false`)

## 5. Upgrading

This is described assuming method 1 was chosen in [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-creating-a-github-repository). If method 2 was chosen, as mentioned above, you need to directly merge the latest upstream tag.

1. Edit the `Gemfile`{: .filepath} to specify a new version of the "jekyll-theme-chirpy" gem.
2. For major upgrades, core files not included in the "jekyll-theme-chirpy" gem and configuration options may have changed. In this case, you need to check the changes using the GitHub API below and apply them directly.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
