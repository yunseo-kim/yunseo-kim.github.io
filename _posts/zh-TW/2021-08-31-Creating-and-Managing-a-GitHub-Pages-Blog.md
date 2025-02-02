---
title: 建立和管理 GitHub Pages 部落格
description: 了解靜態網頁和動態網頁的特點與差異,探討靜態網站生成器(Static Site Generator),並將 Jekyll 部落格託管到 GitHub Pages。
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---

從2021年初開始,我就使用 Jekyll 在 GitHub Pages 上託管部落格。但是在建立部落格時,我沒有好好整理安裝過程,導致後續維護時遇到一些困難,所以我決定簡單地整理一下安裝過程和維護方法。

(+ 2024.12 內容更新)

## 1. 靜態網站生成器 & 網頁託管

### 1-1. 靜態網頁 vs 動態網頁

#### 靜態網頁(Static Web Page)
- 將儲存在伺服器上的資料直接傳送給使用者的網頁
- 網頁伺服器會將對應使用者請求的預先儲存的頁面傳送
- 除非管理員更改伺服器上儲存的資料,否則使用者會看到相同的網頁
- 只需傳送對應請求的檔案,無需額外處理,因此通常回應較快
- 僅由簡單的檔案組成,只需建立網頁伺服器,因此建置成本較低
- 只能顯示儲存的資訊,因此服務有限
- 資料的新增、修改、刪除需要管理員手動操作
- 結構便於搜尋引擎爬蟲,相對更有利於搜尋引擎最佳化(SEO)

#### 動態網頁(Dynamic Web Page)
- 將儲存在伺服器上的資料經過腳本處理後傳送給使用者的網頁
- 網頁伺服器會解析使用者的請求,處理資料後生成網頁並傳送
- 使用者會看到根據情況、時間、請求等而變化的網頁
- 需要處理腳本才能傳送網頁,因此相對回應較慢
- 除了網頁伺服器外還需要應用程式伺服器,因此建置時會產生額外成本
- 可以動態組合各種資訊提供,因此可以實現多樣化的服務
- 根據網頁結構,使用者可以在瀏覽器中新增、修改、刪除資料
 
### 1-2. 靜態網站生成器(SSG, Static Site Generator)
- 基於原始資料(通常是 markdown 格式的文字檔)和預定義的模板生成靜態網頁的工具
- 無需直接編寫個別 HTML 頁面,只需用 markdown 撰寫文章,就能自動化建立網頁並部署到網路上的過程
- 例如: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- GitHub 提供的免費靜態網頁託管服務
- 每個帳戶可以託管1個個人代表網頁,以及無限數量的儲存庫專案文件頁面
- 建立名為 '{username}.github.io' 格式的儲存庫,然後可以直接將建立的 HTML 頁面推送到該儲存庫,或使用 GitHub Actions 進行建立和部署
- 如果擁有自己的網域,可以在設定中連結,使用其他網域地址代替 '{username}.github.io' 格式的預設網域

## 2. 選擇要使用的 SSG 和主題

### 2-1. 選擇 Jekyll 的原因
雖然有 Jekyll、Hugo、Gatsby 等多種 SSG,但我決定使用 Jekyll。以下是我在選擇 SSG 時考慮的標準,以及選擇 Jekyll 的原因:
- 是否能最小化不必要的試錯,專注於寫作和經營部落格?
  - Jekyll 是 Github Pages 官方支援的靜態網站生成器。雖然 Hugo、Gatsby 等其他 SSG 也可以在 Github Pages 上託管,甚至可以選擇使用 Netlify 等完全不同的託管服務,但實際上,對於這種規模的個人部落格來說,使用哪種 SSG 建立以及建立速度、性能等技術細節並不是很重要,所以我認為選擇維護更簡單且參考文件更多的方案會更好。
  - Jekyll 也是相比 Hugo、Gatsby 等競爭對手開發時間最長的。因此,相關文件化做得很好,實際遇到問題時可以參考的資料量也壓倒性地多。
- 可用的主題和外掛是否多樣?
  - 即使使用 SSG 而不是直接編寫 HTML,自己製作各種模板也很麻煩,而且耗時,也沒有必要。網上已經有很多優秀的公開主題,選擇喜歡的使用就可以了。
  - 而且我原本主要使用 C 或 Python,對 Jekyll 的 Ruby 或 Hugo 的 Go 語言不太熟悉,所以更想積極利用現有的主題和外掛。
  - 在 Jekyll 中我很快就找到了一眼就喜歡的主題,而 Hugo 或 Gatsby 相對來說適合個人部落格用途的主題數量並不是很多。這可能也是因為上面提到的與 Github Pages 的相容性以及開發時間長度的影響。

### 2-2. 主題選擇

#### Minimal Mistakes (2021.01 ~ 2022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- 建立部落格後使用了約1年3個月的主題
- 支援通過 Disqus、Discourse、utterances 等的評論功能
- 支援分類和標籤分類功能
- 基本支援 Google Analytics
- 可選擇預定義的外觀
- 雖然後來發現了設計更優雅且更喜歡的 Chirpy 主題並轉移過去,但考慮到這是一個工程師風格的部落格,雖然不漂亮但也算是乾淨的設計,感覺還是可以適當使用的。

#### Chirpy Jekyll Theme (2022.04~)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- 從2022年4月轉移部落格主題後至今仍在使用的主題
- 支援多重分類、標籤功能
- 基於 MathJax 基本支援 LaTex 語法的數學公式表達
- 基於 Mermaid 基本支援圖表功能
- 支援通過 Disqus、Giscus 等的評論功能
- 支援 Google Analytics、GoatCounter
- 支援亮色主題和暗色主題
- 在主題轉換時點,MathJax 或 Mermaid 在 Minimal Mistakes 主題中並不自行支援,需要自己通過客製化來添加,而 Chirpy 主題則基本自行支援。雖然說是客製化,其實也沒什麼大不了的,但還是可以說是一個小優點。
- 最重要的是,設計很漂亮。Minimal Mistakes 主題雖然乾淨,但有一種特有的僵硬感,感覺更適合專案官方技術文件或作品集頁面,而不是部落格。相比之下,Chirpy 主題的設計即使與 Tistory、Medium、velog 等商業部落格平台相比也毫不遜色。

## 3. 建立 GitHub 儲存庫、建置和部署

以目前(2024.06)使用中的 Chirpy Jekyll Theme 為基準來說明,並假設已經安裝了 Git 的情況下進行。  
參考 [Jekyll 官方安裝指南](https://jekyllrb.com/docs/installation/)和 [Chirpy Jekyll Theme 官方頁面](https://github.com/cotes2020/jekyll-theme-chirpy/wiki)。

### 3-1. 安裝 Ruby & Jekyll
按照 [Jekyll 官方安裝指南](https://jekyllrb.com/docs/installation/)根據自己的作業系統環境安裝 Ruby 和 Jekyll。

### 3-2. 建立 GitHub 儲存庫
[Chirpy Jekyll Theme 官方頁面](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site)介紹了以下兩種方法:
1. 使用 "jekyll-theme-chirpy" gem 引入核心檔案,其餘資源從 [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) 模板獲取
  - 優點: 如後所述,版本升級應用較容易。
  - 缺點: 客製化受限。
2. 將 [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) 儲存庫 fork 到自己的部落格儲存庫
  - 優點: 直接在儲存庫中管理所有檔案,可以自由修改程式碼來客製化主題不支援的功能。
  - 缺點: 要應用版本升級時需要合併[原始儲存庫的最新上游標籤](https://github.com/cotes2020/jekyll-theme-chirpy/tags),有時自己客製化的程式碼可能會與升級版本的程式碼衝突。這種情況下需要自己解決衝突。

我選擇了第1種方法。Chirpy 主題本身完成度很高,大多數使用者角度來看並沒有太多需要客製化的地方,而且截至2024年仍在積極開發和改進功能中,除非要大幅修改,否則及時跟隨原始上游的優點超過了直接客製化的優點。Chirpy 主題官方指南也建議大多數使用者採用第1種方法。

### 3-3. 主要設定
在根目錄的 `_config.yml`{: .filepath} 檔案和 `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath} 檔案中應用必要的設定。註解寫得很清楚,設定也很直觀,可以輕鬆應用。比較需要外部額外工作的設定有 Google Search Console 連結的認證碼註冊,以及 Google Analytics 或 GoatCounter 等網站管理工具的連結,但這些其實也不是很複雜的程序,而且不是這篇文章要討論的核心主題,所以省略詳細說明。

### 3-4. 在本機建置
雖然不是必要步驟,但在寫新文章或對網站進行修改時,可能想預先確認是否能在網頁上正常顯示。這時可以在本機儲存庫的根目錄開啟終端機,執行以下命令:
```console
$ bundle exec jekyll s
```
等待幾秒鐘後,網站就會在本機建置完成,可以在 <http://127.0.0.1:4000> 地址查看結果。

### 3-5. 部署
有兩種方法:
1. 使用 GitHub Actions (在 GitHub Pages 上託管的情況)
  - 如果使用 GitHub Free Plan,需要將儲存庫保持為 public
  - 在 GitHub 網頁上選擇儲存庫的 *Settings* 標籤,然後在左側導航欄中點擊 *Code and automation > Pages*,在 **Source** 部分選擇 **GitHub Actions** 選項
  - 設定完成後,每次推送新的提交時都會自動執行 *Build and Deploy* 工作流程
2. 直接建置後部署 (使用其他託管服務或自行託管的情況)
  - 執行以下命令直接建置網站
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - 將 `_site` 目錄中的建置結果上傳到伺服器

## 4. 撰寫文章
Chirpy 主題的[文章撰寫指南](https://chirpy.cotes.page/posts/write-a-new-post/)詳細說明了文章撰寫方法和可以使用的選項。除了本文描述的內容外,還提供了各種功能,有需要時可以參考官方文件。這裡整理了每次發文時都需要注意的主要事項。

### 建立 Markdown 檔案
- 名稱格式: `YYYY-MM-DD-TITLE.md`{: .filepath}
- 位置: `_posts`{: .filepath} 目錄

### 撰寫 Front Matter
Markdown 檔案的開頭部分需要適當地撰寫 Front Matter。
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
- **title**: 文章標題
- **description**: 摘要。如果不寫,會自動使用正文內容的前面部分,但為了搜尋引擎最佳化(SEO),建議直接適當撰寫 description 元標籤。羅馬字基準 135~160 字,中文基準 80~110 字左右的篇幅較為適當。
- **date**: 精確的文章撰寫日期時間和時區(可省略,省略時會自動識別並使用檔案的建立日期或修改日期資訊)
- **categories**: 文章的分類
- **tags**: 要應用於文章的標籤分類
- **image**: 在文章頂部插入預覽圖片
  - **path**: 圖片檔案路徑
  - **alt**: 替代文字(可省略)
- **toc**: 右側側邊欄的目錄功能使用與否,預設值為 `true`
- **comments**: 如果想明確指定個別文章的評論使用與否,可以使用此選項(與網站基本設定分開)
- **math**: 啟用內建的基於 [MathJax](https://www.mathjax.org/) 的數學公式表達功能,預設值為停用(`false`)以提高頁面性能
- **mermaid**: 啟用內建的基於 [Mermaid](https://github.com/mermaid-js/mermaid) 的圖表表達功能,預設值為停用(`false`)

## 5. 升級

假設採用了 [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-建立-github-儲存庫) 中的第1種方法。如果採用了第2種方法,如上所述,需要直接合併最新的上游標籤。

1. 編輯 `Gemfile`{: .filepath} 來指定 "jekyll-theme-chirpy" gem 的新版本。
2. 對於主要升級,不包含在 "jekyll-theme-chirpy" gem 中的核心檔案和設定選項也可能有變更。這時需要通過以下 GitHub API 確認變更後直接反映:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
