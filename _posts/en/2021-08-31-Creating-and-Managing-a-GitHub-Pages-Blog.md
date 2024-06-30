---
title: "Creating and Managing a GitHub Pages Blog"
description: >-
  Learn about the characteristics and differences between static and dynamic web pages, static site generators, and how to host a Jekyll blog on GitHub Pages.
categories:
  - Blogging
tags:
  - Jekyll
---

I started hosting a blog on GitHub Pages using Jekyll in early 2021. However, I didn't properly document the installation process at the time, which led to some difficulties in maintenance later on. So I decided to briefly outline the installation process and maintenance methods.  
~~Actually, the main reason is that I'm still not very familiar with static site hosting.~~
(Content updated June 2024)

## 1. Static Site Generator & Web Hosting
### 1-1. Static Web Page vs Dynamic Web Page
#### Static Web Page
- A web page that delivers data stored on the server directly to the user
- The web server delivers a pre-stored page corresponding to the user's request
- Users see the same web page unless the data stored on the server is changed
- Generally faster response as it only needs to send the requested file without additional processing
- Cheaper to set up as it only requires a web server, consisting of simple files
- Limited service as it only shows pre-stored information
- Data addition, modification, and deletion must be done manually by the administrator
- Relatively more advantageous for search engine optimization (SEO) due to its structure that is easy for search engines to crawl

#### Dynamic Web Page
- A web page that delivers data stored on the server after processing it with scripts
- The web server interprets the user's request, processes the data, and delivers the generated web page
- Users see web pages that change according to situations, time, requests, etc.
- Relatively slower response as it needs to process scripts to deliver the web page
- Additional costs incurred during setup as it requires an application server in addition to a web server
- Enables various services by dynamically providing combinations of diverse information
- Users can add, modify, and delete data from the browser depending on the web page structure

### 1-2. Static Site Generator (SSG)
- A tool that generates static web pages based on raw data (usually markdown format text files) and predefined templates
- Automates the process of building and deploying web pages by writing posts in markdown, eliminating the need to write individual HTML pages
- Examples: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- A free static web page hosting service provided by GitHub
- Allows hosting of one personal representative web page per account and unlimited project documentation pages per repository
- After creating a repository named '{username}.github.io' to match your GitHub username, you can either directly push built HTML pages to the repository or use GitHub Actions for building and deployment
- If you own a domain, you can connect it in the settings to use a different domain address instead of the default '{username}.github.io' format

## 2. Choosing an SSG and Theme

### Reasons for Choosing Jekyll
While there are several SSGs like Jekyll, Hugo, and Gatsby, I decided to use Jekyll. The criteria considered in the selection process and the reasons for choosing Jekyll are as follows:
- Can it minimize unnecessary trial and error and allow focus on writing and blog operation?
  - Jekyll is the officially supported static website generator for GitHub Pages. Although other SSGs like Hugo and Gatsby can also be hosted on GitHub Pages, and there's the option of using other hosting services like Netlify, I decided that for a personal blog of this scale, the technical aspects of which SSG was used for construction and build speed, performance, etc., are not very important. So I thought it would be better to choose one that is simpler to maintain and has more reference documents.
  - Jekyll also has the longest development period compared to competitors like Hugo and Gatsby. This means it has well-documented resources, and there's an overwhelming amount of reference material available when problems occur.
- Are there a variety of themes and plugins available?
  - Even if you're not writing HTML directly but using an SSG, creating various templates yourself is cumbersome, time-consuming, and unnecessary. There are many excellent themes already available on the web, so you can just adopt and use one you like.
  - Moreover, since I mainly use C or Python, I'm not familiar with Ruby used by Jekyll or Go used by Hugo, so I wanted to actively utilize existing themes and plugins.
  - With Jekyll, I could quickly find a theme that I liked at first glance, whereas Hugo and Gatsby seemed to have relatively fewer themes suitable for personal blog purposes. This seems to be largely influenced by the connectivity with GitHub Pages, which is widely used by developers for personal blog hosting, and the longer development period as mentioned above.

### Theme Selection
#### Minimal Mistakes (Jan 2021 - Apr 2022)
- GitHub Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- The theme I used for about 1 year and 3 months when I first created the blog
- Supports comment functionality through Disqus, Discourse, utterances, etc.
- Supports category and tag classification features
- Built-in support for Google Analytics
- Ability to choose from predefined skins
- Although I later discovered the Chirpy theme with a more appealing design and switched to it, considering it's a rather technical blog anyway, the Minimal Mistakes theme had a clean design that was decent to use, even if not particularly pretty.

### Chirpy Jekyll Theme (Apr 2022~)
- GitHub Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- The theme I've been using since switching blog themes in April 2022
- Supports multi-category classification and tag features
- Built-in support for LaTeX syntax equation expressions based on MathJax
- Built-in support for diagram functionality based on Mermaid
- Supports comment functionality through Disqus, Giscus, etc.
- Supports Google Analytics, GoatCounter
- Supports light and dark themes
- At the time of theme transition, features like MathJax and Mermaid were not natively supported by the Minimal Mistakes theme and had to be added through customization, but the Chirpy theme supports these natively. Although the customization wasn't much, it's still a minor advantage.
- Above all, the design is beautiful. While the Minimal Mistakes theme is clean, it has a certain stiffness that seems more suitable for official project technical documentation or portfolio pages rather than blogs. The Chirpy theme, on the other hand, has a design that doesn't fall short compared to commercial blog platforms like Tistory, Medium, or velog.

## 3. Creating GitHub Repository, Building and Deploying
This is based on the currently (June 2024) used Chirpy Jekyll Theme, and assumes Git is already installed.  
Refer to the [Jekyll official installation guide](https://jekyllrb.com/docs/installation/) and [Chirpy Jekyll Theme official page](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Installing Ruby & Jekyll
Install Ruby and Jekyll according to the [Jekyll official installation guide](https://jekyllrb.com/docs/installation/) for your operating system environment.

### 3-2. Creating GitHub Repository
The [Chirpy Jekyll Theme official page](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) introduces two methods:
1. Using the "jekyll-theme-chirpy" gem to import core files and getting the rest of the resources from the [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) template
  - Advantage: Easy to apply version upgrades, as will be explained later.
  - Disadvantage: Customization is limited.
2. Forking the [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) repository as your blog repository
  - Advantage: You can freely customize by directly modifying the code, even for features not supported by the theme, as you manage all files directly in the repository.
  - Disadvantage: To apply version upgrades, you need to merge [the latest upstream tag of the original repository](https://github.com/cotes2020/jekyll-theme-chirpy/tags), which may conflict with your custom code in some cases. In such cases, you need to resolve the conflicts manually.

I chose method 1. The Chirpy theme is highly complete by default, so most users don't have much to customize. Moreover, as of 2024, it's still being actively developed and improved, so unless you're planning significant modifications, the benefits of keeping up with the original upstream outweigh the benefits of applying custom customizations. The official Chirpy theme guide also recommends method 1 for most users.

### 3-3. Main Settings
Apply necessary settings in the `_config.yml`{: .filepath} file in the root directory and the `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath} files. The comments are well-written and the settings are intuitive, so you can apply them without much difficulty. The only settings that require separate work externally are registering the authentication code for Google Search Console integration and linking webmaster tools like Google Analytics or GoatCounter, but these procedures are not very complicated and are not the core topic of this article, so detailed descriptions are omitted.

### 3-4. Building Locally
This is not a mandatory procedure, but you might want to check in advance if new posts or site modifications will display correctly on the web. In such cases, open a terminal in the root directory of the local repository and run the following command:
```console
$ bundle exec jekyll s
```
After waiting for a few seconds, the site will be built locally and you can check the result at <http://127.0.0.1:4000>.

### 3-5. Deploying
There are two methods:
1. Using GitHub Actions (when hosting on GitHub Pages)
  - If you're using the GitHub Free Plan, you need to keep the repository public
  - On the GitHub webpage, select the *Settings* tab of the repository, click *Code and automation > Pages* in the left navigation bar, and select the **GitHub Actions** option in the **Source** section
  - After setup, the *Build and Deploy* workflow will automatically run with each new commit push
2. Building and deploying directly (when using other hosting services or self-hosting)
  - Run the following command to build the site directly
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Upload the build results in the `_site` directory to the server

## 4. Writing Posts
The [post writing guide](https://chirpy.cotes.page/posts/write-a-new-post/) for the Chirpy theme well documents the post writing method and available options. It provides various features beyond what is described in this article, and it's good reference material, so refer to the official documentation if needed. Here, we summarize the main points to keep in mind every time you post.

### Creating a Markdown File
- Name format: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Location: `_posts`{: .filepath} directory

### Writing Front Matter
The front matter should be appropriately written at the beginning of the markdown file.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]     # TAG names should always be lowercase
---
```
- **title**: Post title
- **description**: Summary. If not written, it automatically uses a portion of the main content, but it's recommended to write the description meta tag directly for search engine optimization (SEO). An appropriate length is about 135-160 characters for Roman characters, or 80-110 characters for Korean.
- **date**: Exact post creation date and time with timezone (optional, if omitted, it automatically recognizes and uses the creation date information from the file name)
- **categories**: Category classification of the post
- **tags**: Tag classification to apply to the post

## 5. Upgrading

This is described assuming method 1 was chosen in [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-github-리포지터리-생성). If method 2 was chosen, as mentioned earlier, you need to manually merge the latest upstream tag.

1. Edit `Gemfile`{: .filepath} to specify the new version of the "jekyll-theme-chirpy" gem.
2. For major upgrades, core files not included in the "jekyll-theme-chirpy" gem and configuration options may have changed. In this case, you need to check the changes using the GitHub API below and reflect them manually:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```