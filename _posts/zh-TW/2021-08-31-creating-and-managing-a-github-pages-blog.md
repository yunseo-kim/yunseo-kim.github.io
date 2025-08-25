---
title: 建立與管理 GitHub Pages 部落格
description: 比較靜態網頁與動態網頁的差異，介紹靜態網站產生器（Static Site Generator），並示範使用 Jekyll 在 GitHub Pages 部署部落格。
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

自 12021 年初起，我開始用 Jekyll 將部落格代管到 GitHub Pages。當時沒有把建置流程好好整理，後續維護時遇到一些不便，所以決定至少把安裝流程與維護方式簡要整理一下。  

(+ 12024.12 內容更新)

## 1. 靜態網站產生器與網站代管
### 1-1. 靜態網頁 vs 動態網頁
#### 靜態網頁（Static Web Page）
- 將伺服器中已儲存的資料原封不動傳給使用者的網頁
- 由網頁伺服器傳回對應使用者請求、事先儲存好的頁面
- 除非變更伺服器上的資料，否則使用者看到的頁面相同
- 只需傳送對應檔案，不需額外處理，通常回應速度較快
- 由簡單檔案組成，只需架設網頁伺服器即可，建置成本低
- 只能展示既有資訊，服務內容受限
- 新增、修改、刪除資料需由管理者手動處理
- 結構便於搜尋引擎爬取，對搜尋引擎最佳化（SEO）相對有利

#### 動態網頁（Dynamic Web Page）
- 將伺服器內的資料以腳本處理後再傳遞的網頁
- 網頁伺服器解析使用者請求，處理資料後生成頁面再回傳
- 依情境、時間、請求等不同，顯示內容會改變
- 因需執行腳本產生頁面，相對回應較慢
- 除網頁伺服器外，還需要應用程式伺服器，建置成本較高
- 能動態組合多種資訊，提供多樣化服務
- 依頁面結構，使用者可在瀏覽器中新增、修改、刪除資料

### 1-2. 靜態網站產生器（SSG, Static Site Generator）
- 基於原始資料（通常為 Markdown 文字檔）與預先定義的模板，生成靜態網頁的工具
- 無需逐頁撰寫 HTML，只要用 Markdown 撰寫文章，即可自動建置並發佈到網路上
- 例：Jekyll、Hugo、Gatsby、Eleventy

### 1-3. GitHub Pages
- GitHub 免費提供的靜態網頁代管服務
- 每個帳號可有 1 個個人主頁，並可為無限個儲存庫建立與代管專案文件頁面
- 以 '{username}.github.io' 命名、依你的 GitHub 使用者名稱建立儲存庫後，可直接將建置好的 HTML 頁面 Push 到該儲存庫，或用 GitHub Actions 進行建置與部署
- 若有自有網域，可在設定中綁定，改用自訂網域取代預設的 '{username}.github.io'

## 2. 選擇要使用的 SSG 與主題

### 2-1. 為何選擇 Jekyll
雖然有 Jekyll、Hugo、Gatsby 等多種 SSG，但我最後決定用 Jekyll。選擇時的考量與理由如下。
- 能否把不必要的踩雷降到最低，專注在寫作與經營？
  - Jekyll 是 GitHub Pages 官方支援的靜態網站產生器。當然，用 Hugo、Gatsby 等一樣可以在 GitHub Pages 或 Netlify 等其他服務代管。但對這種規模的個人部落格而言，使用哪個 SSG、建置速度與效能並不是關鍵，因此我更看重維護簡單、文件資源多。
  - 相較 Hugo、Gatsby，Jekyll 的歷史更長，相關文件更完整，遇到問題時可參考的資料量也壓倒性地多。
- 可用的主題與外掛是否多元？
  - 即便使用 SSG，不一定要自己從零做各種模板。網路上已有許多優秀的主題，挑一個順眼的直接用即可。
  - 我主要寫 C 或 Python，對 Jekyll 的 Ruby 或 Hugo 的 Go 語言並不熟，因此更傾向於善用既有的主題與外掛。
  - 就我當時的觀察，Jekyll 很快就能找到一眼順眼的主題；而 Hugo 或 Gatsby 相對較少適合個人部落格的主題。這大概也與它與 GitHub Pages 的整合度、以及專案發展時間長短有關。

### 2-2. 主題選擇
#### Minimal Mistakes（12021.01 - 12022.04）
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- 剛建立部落格後約 1 年 3 個月使用的主題
- 支援 Disqus、Discourse、utterances 等留言功能
- 支援分類與標籤
- 內建 Google Analytics
- 可選用預先定義的樣式（skin）
- 後來發現設計更優雅、我更喜歡的 Chirpy 主題而轉用；不過考量這是工程取向的部落格，即使不華麗，Minimal Mistakes 也有相當清爽的設計，算是好用穩妥。

#### Chirpy Jekyll Theme（12022.04 - 現在）
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- 自 12022 年 4 月將主題切換後沿用至今
- 支援多重分類與標籤
- 內建以 MathJax 為基礎的 LaTeX 數學式支援
- 內建以 Mermaid 為基礎的圖表支援
- 支援 Disqus、Giscus 等留言功能
- 支援 Google Analytics、GoatCounter
- 支援淺色／深色主題
- 以我切換時點來說，Minimal Mistakes 未內建 MathJax 與 Mermaid，需要自行客製化加入；Chirpy 則內建支援。雖然那點客製化不算難，但能少做就少做，算小小優勢。
- 最重要的是，設計好看。Minimal Mistakes 乾淨但偏硬派，更像專案技術文件或作品集；Chirpy 的觀感與 Tistory、Medium、velog 等商用平台相比也不遜色，這是很大的加分。

## 3. 建立 GitHub 儲存庫、建置與部署
以下以我目前（12024.06）使用的 Chirpy Jekyll Theme 為基準，並假設已安裝 Git。  
參考 [Jekyll 官方安裝指南](https://jekyllrb.com/docs/installation/) 與 [Chirpy Jekyll Theme 官方頁面](https://github.com/cotes2020/jekyll-theme-chirpy/wiki)。

### 3-1. 安裝 Ruby 與 Jekyll
依照 [Jekyll 官方安裝指南](https://jekyllrb.com/docs/installation/)，依你的作業系統安裝 Ruby 與 Jekyll。

### 3-2. GitHub 儲存庫建立
[Chirpy Jekyll Theme 官方頁面](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) 提供兩種方式：
1. 以 "jekyll-theme-chirpy" gem 載入核心檔案，其餘資源從 [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) 範本取得
  - 優點：如後述，升級版本時較容易套用
  - 缺點：若要進行大規模客製化，可能反而不便
2. 將 [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) 儲存庫 fork 成自己的部落格儲存庫
  - 優點：所有檔案都在自己的儲存庫內管理，方便直接修改程式碼以新增主題未提供的功能等客製化
  - 缺點：若要套用新版本，需要將[上游原始儲存庫的最新標籤](https://github.com/cotes2020/jekyll-theme-chirpy/tags) merge；某些情況下你客製化的程式碼可能與新版衝突，需自行解決

我採用方法一。Chirpy 本身完成度高，多數使用者其實不太需要客製化；而且截至 12024 年仍持續活躍開發與改進，如果不是要大改，追上游更新的好處往往大於自行客製化。Chirpy 官方指南也建議多數使用者採用方法一。

### 3-3. 主要設定
在根目錄的 `_config.yml`{: .filepath} 與 `_data/contact.yml`{: .filepath}、`_data/share.yml`{: .filepath} 中套用所需設定。這些設定都有完善註解且直覺，調整起來不難。需要外部作業的大概只有 Google Search Console 驗證碼註冊，以及 Google Analytics 或 GoatCounter 等站長工具的串接；其實流程不複雜，且非本文重點，故不贅述。

### 3-4. 在本機建置
不是必經步驟，但當你撰寫新文章或修改網站時，可能想先在本機確認呈現是否正常。此時在本機儲存庫根目錄開啟終端機，執行下列指令：
```console
$ bundle exec jekyll s
```
稍候網站會在本機建置完成，可於 <http://127.0.0.1:4000> 檢視結果。

### 3-5. 部署
有兩種方式：
1. 使用 GitHub Actions（由 GitHub Pages 代管）
  - 若使用 GitHub Free Plan，儲存庫需為 public
  - 於 GitHub 網頁介面進入儲存庫的 *Settings* 分頁，左側導覽選擇 *Code and automation > Pages*，在 **Source** 區塊選擇 **GitHub Actions**
  - 設定完成後，每次推送新 commit 都會自動執行 *Build and Deploy* 工作流程
2. 自行建置後部署（使用其他代管服務或自架）
  - 執行以下指令自行建置網站
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - 將 `_site` 目錄中的建置成果上傳到伺服器

## 4. 撰寫文章
Chirpy 主題的[文章撰寫指南](https://chirpy.cotes.page/posts/write-a-new-post/)對寫文方式與可用選項有完善文件。除此之外還有許多功能可參考官方文件。另我也曾在[另一篇文章](/posts/github-markdown-syntax-summary/)整理 GitHub Flavored Markdown 的基本語法。以下僅整理每次發文時共同需要留意的重點。

### 建立 Markdown 檔案
- 檔名格式：`YYYY-MM-DD-TITLE.md`{: .filepath}
- 位置：`_posts`{: .filepath} 目錄

### 撰寫 Front Matter
Markdown 檔案開頭需撰寫適當的 Front Matter。
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
- **title**：文章標題
- **description**：摘要。不寫時會自動擷取內文前段，但為了搜尋引擎最佳化（SEO）建議手動撰寫合適的描述。以拉丁字母計約 135～160 字、以韓文計約 80～110 字較為適宜。
- **date**：文章精確撰寫時間與時區（可省略；省略時會自動取用檔案建立或修改時間）
- **categories**：文章分類
- **tags**：文章標籤
- **image**：於文章頂部插入預覽圖
  - **path**：圖片檔路徑
  - **alt**：替代文字（可省略）
- **toc**：是否使用右側側邊欄的目錄功能，預設為 `true`
- **comments**：若想針對單篇文章覆寫站台預設的留言設定，可在此指定
- **math**：啟用內建的 MathJax 數學式支援，為了頁面效能預設停用（`false`）
- **mermaid**：啟用內建的 Mermaid 圖表支援，預設停用（`false`）

## 5. 升級

以下假設你在[3-2](#3-2-github-儲存庫建立) 採用方法一。若採用方法二，如前述需自行 merge 最新上游標籤。

1. 編輯 `Gemfile`{: .filepath}，指定新的 "jekyll-theme-chirpy" gem 版本。
2. 若為重大升級，"jekyll-theme-chirpy" gem 未內含的核心檔案與設定選項也可能有變更。此時可用下列 GitHub API 比對差異後，手動套用：
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
