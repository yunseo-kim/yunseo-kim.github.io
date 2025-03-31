---
title: Creating and Managing a GitHub Pages Blog
description: Learn about the characteristics and differences between static and dynamic web pages, explore static site generators, and host a Jekyll blog on GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---
I started hosting a blog on GitHub Pages using Jekyll from early 12021 in the [Human Era](https://en.wikipedia.org/wiki/Holocene_calendar). However, since I didn't properly document the installation process when setting up the blog, I encountered some difficulties with maintenance later on. So, I decided to briefly outline the installation process and maintenance methods.

(+ Updated December 12024)

## 1. Static Site Generator & Web Hosting
### 1-1. Static Web Page vs Dynamic Web Page
#### Static Web Page
- A web page that delivers data stored on the server directly to the user
- The web server delivers a pre-stored page corresponding to the user's request
- Users see the same web page unless the data stored on the server is changed
- Generally faster response as it only needs to send the file corresponding to the request, without additional processing
- Consists of simple files, so only a web server needs to be set up, making it cost-effective
- Limited service as it only shows pre-stored information
- Data addition, modification, and deletion must be done manually by the administrator
- Structure is easier for search engines to crawl, making it relatively more advantageous for Search Engine Optimization (SEO)

#### Dynamic Web Page
- A web page that processes and delivers data stored on the server using scripts
- The web server interprets the user's request, processes the data, and delivers the generated web page
- Users see web pages that change according to situations, time, requests, etc.
- Relatively slower response as scripts need to be processed to deliver the web page
- Additional costs incurred during setup as it requires an application server in addition to a web server
- Enables various services by dynamically providing combinations of diverse information
- Depending on the web page structure, users can add, modify, and delete data from the browser

### 1-2. Static Site Generator (SSG)
- A tool that generates static web pages based on raw data (usually markdown format text files) and predefined templates
- Automates the process of building and deploying web pages by writing posts in markdown, without the need to directly write individual HTML pages
- Examples: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- A free static web page hosting service provided by GitHub
- Allows hosting of one personal representative web page per account, and unlimited project documentation pages per repository
- After creating a repository named '{username}.github.io' to match your GitHub username, you can directly push built HTML pages to the repository or use GitHub Actions to perform build and deployment
- If you own a domain, you can connect it in the settings to use a different domain address instead of the default '{username}.github.io' format

## 2. Choosing an SSG and Theme

### 2-1. Reasons for Choosing Jekyll
While there are several SSGs like Jekyll, Hugo, Gatsby, etc., I decided to use Jekyll. The criteria considered in the process of selecting an SSG and the reasons for choosing Jekyll are as follows:
- Can it minimize unnecessary trial and error and focus on writing and blog operation?
  - Jekyll is the officially supported static website generator for GitHub Pages. Of course, other SSGs like Hugo, Gatsby can also be hosted on GitHub Pages, and there's also the option of using other hosting services like Netlify. However, for operating a personal blog of this scale, the technical aspects of which SSG was used for construction, build speed, performance, etc., are not very important. So I decided it would be better to use something that's even slightly easier to maintain and has more reference documents.
  - Jekyll also has the longest development period compared to other competitors like Hugo and Gatsby. As a result, it is well-documented, and there is an overwhelming amount of reference material available when problems occur.
- Are there a variety of themes and plugins available?
  - Even if you're not writing HTML directly but using an SSG, creating various templates yourself is cumbersome, time-consuming, and unnecessary. There are many excellent themes already available on the web, so you can adopt and utilize one that you like.
  - Moreover, since I mainly use C or Python, I'm not very familiar with Ruby (used by Jekyll) or Go (used by Hugo), so I wanted to actively utilize existing themes and plugins.
  - With Jekyll, I could quickly find a theme that I liked at first glance, whereas Hugo and Gatsby seemed to have relatively fewer themes suitable for personal blog purposes. As mentioned above, the compatibility with GitHub Pages, which many developers use for personal blog hosting, and the development period seem to have had a significant impact here as well.

### 2-2. Theme Selection
#### Minimal Mistakes (January 12021 - April 12022)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- The theme I used for about 1 year and 3 months when I first created the blog
- Supports comment functionality through Disqus, Discourse, utterances, etc.
- Supports category and tag classification features
- Basic support for Google Analytics
- Ability to choose from predefined skins
- Although I later discovered the Chirpy theme, which has a more elegant design that I prefer, considering it's an engineering blog anyway, Minimal Mistakes had a clean design that was decent enough to use, even if not particularly pretty.

#### Chirpy Jekyll Theme (April 12022 - Present)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- The theme I've been using since switching blog themes in April 12022
- Supports multi-category classification and tag features
- Basic support for LaTeX syntax equation expression based on MathJax
- Basic support for diagram functionality based on Mermaid
- Supports comment functionality through Disqus, Giscus, etc.
- Supports Google Analytics, GoatCounter
- Supports light and dark themes
- At the time of theme transition, features like MathJax and Mermaid were not natively supported by the Minimal Mistakes theme and had to be added through customization, but the Chirpy theme supports them by default. Although the customization wasn't much, it's still a minor advantage.
- Above all, the design is beautiful. While the Minimal Mistakes theme is clean, it has a certain stiffness that seems more suitable for official project technical documentation or portfolio pages rather than blogs. The Chirpy theme, on the other hand, has a design that doesn't fall short compared to commercial blog platforms like Tistory, Medium, or velog.

## 3. Creating GitHub Repository, Building and Deploying
This is based on the currently (June 12024) used Chirpy Jekyll Theme, and assumes that Git is already installed.  
Refer to the [Jekyll official installation guide](https://jekyllrb.com/docs/installation/) and [Chirpy Jekyll Theme official page](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Installing Ruby & Jekyll
Install Ruby and Jekyll according to the [Jekyll official installation guide](https://jekyllrb.com/docs/installation/), tailored to your operating system environment.

### 3-2. Creating GitHub Repository
The [Chirpy Jekyll Theme official page](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) introduces the following two methods:
1. Using the "jekyll-theme-chirpy" gem to import core files and getting the rest of the resources from the [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) template
  - Advantage: Easy to apply version upgrades, as will be described later.
  - Disadvantage: Customization is limited.
2. Forking the [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) repository as your blog's repository
  - Advantage: As you directly manage all files within the repository, you can freely customize even features not supported by the theme by modifying the code directly.
  - Disadvantage: To apply version upgrades, you need to merge [the latest upstream tag of the original repository](https://github.com/cotes2020/jekyll-theme-chirpy/tags), which may sometimes conflict with your custom code. In this case, you need to resolve the conflict manually.

I chose method 1. The Chirpy theme is highly complete by default, so most users don't have much to customize. Moreover, as of 12024, it's still being actively developed and improved, so unless you're planning to heavily modify it, the benefits of keeping up with the original upstream outweigh the benefits of applying direct customization. The official Chirpy theme guide also recommends method 1 for most users.

### 3-3. Main Settings
Apply the necessary settings in the `_config.yml`{: .filepath} file in the root directory and the `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath} files. The comments are well-written and the settings are intuitive, so you can apply them without much difficulty. The settings that require separate work externally include registering an authentication code for Google Search Console integration and linking webmaster tools like Google Analytics or GoatCounter, but these procedures are not really complicated and are not the core topic I want to cover in this article, so I'll omit the detailed description.

### 3-4. Building Locally
This is not a mandatory procedure, but you might want to check in advance if a new post you've written or some modification you've made to the site will display correctly on the web. In this case, open a terminal in the root directory of your local repository and run the following command:
```console
$ bundle exec jekyll s
```
After waiting for a few seconds, the site will be built locally and you can check the result at <http://127.0.0.1:4000>.

### 3-5. Deploying
There are two methods:
1. Using GitHub Actions (when hosting on GitHub Pages)
  - If you're using the GitHub Free Plan, you need to keep the repository public
  - On the GitHub webpage, select the *Settings* tab of the repository, click on *Code and automation > Pages* in the left navigation bar, and select the **GitHub Actions** option in the **Source** section
  - After setup, the *Build and Deploy* workflow will automatically run every time you push a new commit
2. Building and deploying directly (when using other hosting services or self-hosting)
  - Run the following command to build the site directly
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Upload the build results in the `_site` directory to your server

## 4. Writing Posts
The Chirpy theme's [post writing guide](https://chirpy.cotes.page/posts/write-a-new-post/) well documents how to write posts and the options available. It provides various features beyond what is described in this article, and it contains useful information to refer to, so check the official documentation if needed. Here, we'll summarize the main points to keep in mind every time you post.

### Creating a Markdown File
- Name format: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Location: `_posts`{: .filepath} directory

### Writing Front Matter
At the beginning of the markdown file, you need to write the Front Matter appropriately.
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
- **description**: Summary. If not written, it automatically uses a part of the beginning of the main content, but it's recommended to write the description meta tag directly for search engine optimization (SEO). A length of about 135-160 characters for Roman alphabet or 80-110 characters for Korean is appropriate.
- **date**: Exact post creation date and time with timezone (optional, if omitted, it automatically uses the file creation date or modification date information)
- **categories**: Post category classification
- **tags**: Tag classification to apply to the post
- **image**: Insert preview image at the top of the post
  - **path**: Image file path
  - **alt**: Alternative text (optional)
- **toc**: Whether to use the table of contents feature in the right sidebar, default is `true`
- **comments**: Used when you want to explicitly specify whether to use comments for individual posts, separate from the site's default settings
- **math**: Activate the built-in [MathJax](https://www.mathjax.org/)-based equation expression feature, default is deactivated (`false`) for page performance
- **mermaid**: Activate the built-in [Mermaid](https://github.com/mermaid-js/mermaid)-based diagram expression feature, default is deactivated (`false`)

## 5. Upgrading

This description assumes that method 1 was chosen in [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-creating-github-repository). If method 2 was chosen, as mentioned earlier, you need to manually merge the latest upstream tag.

1. Edit `Gemfile`{: .filepath} to specify the new version of the "jekyll-theme-chirpy" gem.
2. For major upgrades, core files not included in the "jekyll-theme-chirpy" gem and configuration options may have changed. In this case, you need to check the changes using the GitHub API below and reflect them manually.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
