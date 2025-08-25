---
title: Creating and Managing a GitHub Pages Blog
description: Compare static vs dynamic web pages, learn what a Static Site Generator is, and host a Jekyll blog on GitHub Pages—with setup, build, deploy, and upkeep tips.
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

I started hosting my blog on GitHub Pages with Jekyll in early 12021. Since I hadn’t properly documented the setup at the time, I ran into some friction during later maintenance. So here’s a concise write-up of the setup process and how I maintain it.  

(+ Updated in 12024.12)

## 1. Static Site Generators & Web Hosting
### 1-1. Static Web Page vs Dynamic Web Page
#### Static Web Page
- A web page that serves data exactly as stored on the server
- The web server returns pre-saved pages corresponding to user requests
- Users see the same page unless the data on the server is changed
- Because it only needs to transmit the requested file, no extra processing is required, so responses are generally fast
- Consists of simple files and only needs a web server, making it inexpensive to set up
- Shows only stored information, so the service is limited
- Data addition, modification, and deletion must be done manually by the administrator
- Typically easier for search engines to crawl, which is relatively advantageous for SEO

#### Dynamic Web Page
- A web page that processes server-stored data with scripts before serving it
- The web server interprets user requests, processes the data, and returns generated pages
- Users see pages that vary by situation, time, or request
- Slower response compared to static pages because scripts must be processed
- Requires an application server in addition to a web server, adding setup cost
- Can combine various information to provide rich, dynamic services
- Depending on page structure, users can add, modify, or delete data in the browser

### 1-2. Static Site Generator (SSG)
- A tool that generates static web pages from raw data (usually markdown-formatted text files) and predefined templates
- Automates building and deploying web pages: write posts in Markdown instead of hand-coding individual HTML files
- Examples: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- A free static web hosting service provided by GitHub
- You can host one personal homepage per account, and create/host unlimited project documentation sites per repository
- Create a repository named in the form '{username}.github.io' matching your GitHub username, then either push built HTML pages directly to that repo or use GitHub Actions to build and deploy
- If you own a domain, you can connect it in settings to use that instead of the default '{username}.github.io' domain

## 2. Choosing an SSG and Theme

### 2-1. Why I chose Jekyll
There are several SSGs—Jekyll, Hugo, Gatsby, etc.—but I decided on Jekyll. My criteria and reasons:
- Minimize unnecessary trial and error and focus on writing and running the blog.
  - Jekyll is officially supported by GitHub Pages. Sure, you can host Hugo or Gatsby on GitHub Pages, or use other hosts like Netlify. But for a personal blog at this scale, which SSG you use, build speed, and raw performance aren’t critical; I preferred something with simpler maintenance and abundant documentation.
  - Jekyll also has the longest development history compared to Hugo and Gatsby. Documentation is mature, and there’s an abundance of resources to consult when issues arise.
- Availability of themes and plugins.
  - Even with an SSG, hand-rolling templates is tedious and time-consuming—and unnecessary. There are many excellent themes available; just pick one you like and use it.
  - I primarily use C and Python, and I’m not fluent in Ruby (Jekyll) or Go (Hugo), so I wanted to lean on existing themes and plugins.
  - With Jekyll, I quickly found themes I liked. Hugo and Gatsby seemed to have fewer themes well-suited for personal blogs. As mentioned above, Jekyll’s integration with GitHub Pages—popular among developers for personal sites—and its longer history likely play a big role here.

### 2-2. Theme selection
#### Minimal Mistakes (12021.01 - 12022.04)
- GitHub Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- The theme I used for about 1 year and 3 months when I first built the blog
- Supports comments via Disqus, Discourse, utterances, etc.
- Supports category and tag taxonomy
- Built-in Google Analytics
- Selectable predefined skins
- I later moved to the Chirpy theme, which I found more elegant, but given the engineering-heavy nature of this blog, Minimal Mistakes’ clean—if not flashy—design worked just fine.

#### Chirpy Jekyll Theme (12022.04 - present)
- GitHub Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- The theme I switched to in 12022.04 and have used ever since
- Supports multi-category classification and tags
- Built-in math rendering with MathJax using LaTeX syntax
- Built-in diagram support with Mermaid
- Comments via Disqus, Giscus, etc.
- Supports Google Analytics and GoatCounter
- Light and dark themes
- At the time I switched, Minimal Mistakes didn’t natively support MathJax or Mermaid, so I had to add them via customization; Chirpy supports both out of the box. It’s a small convenience, but still a plus.
- Above all, it looks great. Minimal Mistakes is clean but feels better suited to official project docs or a portfolio site. Chirpy’s design holds its own even compared to commercial platforms like Tistory, Medium, or Velog.

## 3. Create a GitHub Repository, Build, and Deploy
The following assumes the Chirpy Jekyll Theme currently in use (as of 12024.06), and that Git is already installed.  
See the Jekyll official installation guide (https://jekyllrb.com/docs/installation/) and the Chirpy Jekyll Theme official page (https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Install Ruby & Jekyll
Follow the Jekyll official installation guide (https://jekyllrb.com/docs/installation/) to install Ruby and Jekyll for your OS.

### 3-2. Create a GitHub Repository
The Chirpy Jekyll Theme official page (https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) introduces two approaches:
1. Use the "jekyll-theme-chirpy" gem for core files and pull the rest from the Chirpy Starter template (https://github.com/cotes2020/chirpy-starter)
  - Pros: Easier to apply version upgrades (see below).
  - Cons: Can be inconvenient for large-scale customizations.
2. Fork the jekyll-theme-chirpy repository (https://github.com/cotes2020/jekyll-theme-chirpy) into your blog’s repository
  - Pros: You manage all files directly in your repo, making it convenient to modify code and add features the theme doesn’t support.
  - Cons: To apply upgrades, you need to merge the original repository’s latest upstream tags (https://github.com/cotes2020/jekyll-theme-chirpy/tags). Your custom changes may conflict with updates, and you’ll have to resolve those conflicts.

I chose option 1. Chirpy is already highly polished, so most users don’t need heavy customization. Development and improvements remain active as of 12024, so unless you’re doing major overhauls, staying current with upstream outweighs bespoke customizations. The official guide also recommends option 1 for most users.

### 3-3. Key settings
Configure the necessary options in the root `_config.yml`{: .filepath} and in `_data/contact.yml`{: .filepath} and `_data/share.yml`{: .filepath}. The comments are clear and the settings intuitive. External tasks like adding the verification code for Google Search Console and connecting Google Analytics or GoatCounter aren’t complicated and are outside this post’s scope.

### 3-4. Build locally
Not required, but you may want to preview changes before pushing. From the root of your local repository, run:
```console
$ bundle exec jekyll s
```
After a moment, the site will build locally and be available at <http://127.0.0.1:4000>.

### 3-5. Deploy
There are two ways:
1. Use GitHub Actions (when hosting on GitHub Pages)
  - If you’re on the GitHub Free plan, keep the repository public
  - In the GitHub web UI, open the repository’s Settings tab, then in the left nav click Code and automation > Pages, and in the Source section select the GitHub Actions option
  - After setup, every new push triggers the Build and Deploy workflow automatically
2. Build and deploy yourself (for other hosts or self-hosting)
  - Build the site with:
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Upload the build artifacts from the `_site` directory to your server

## 4. Writing Posts
Chirpy’s write-up guide (https://chirpy.cotes.page/posts/write-a-new-post/) documents how to write posts and available options. It offers more features than I cover here, so refer to the official docs as needed. I also summarized GitHub Flavored Markdown basics in a separate post (/posts/github-markdown-syntax-summary/). Below are key points to keep in mind each time you publish.

### Create the Markdown file
- Naming format: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Location: `_posts`{: .filepath} directory

### Write the Front Matter
Add appropriate Front Matter at the top of the Markdown file.
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
- title: Post title
- description: Summary. If omitted, the theme will use the beginning of the body, but for SEO it’s better to explicitly write a suitable description. About 135–160 characters in Roman letters or 80–110 in Korean works well.
- date: Exact posting datetime and timezone (optional; if omitted, the file’s creation or modified date is used)
- categories: Post categories
- tags: Tags to apply to the post
- image: Insert a hero/preview image at the top of the post
  - path: Image file path
  - alt: Alternative text (optional)
- toc: Whether to show the table of contents in the right sidebar; default is `true`
- comments: Override the site default to explicitly enable/disable comments for this post
- math: Enable built-in MathJax-based math rendering; disabled (`false`) by default for performance
- mermaid: Enable built-in Mermaid-based diagram rendering; disabled (`false`) by default

## 5. Upgrade

This assumes you chose option 1 in [3-2](#3-2-create-a-github-repository). If you chose option 2, as mentioned above, you’ll need to merge the latest upstream tag.

1. Edit `Gemfile`{: .filepath} to specify the new version of the "jekyll-theme-chirpy" gem.
2. For major upgrades, core files and settings not included in the gem may also change. Check the diff below via the GitHub API and apply changes manually as needed.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
