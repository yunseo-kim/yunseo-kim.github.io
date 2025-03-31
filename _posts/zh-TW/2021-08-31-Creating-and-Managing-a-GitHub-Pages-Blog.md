---
title: 建立和管理 GitHub Pages 部落格
description: 了解靜態網頁和動態網頁的特點與差異,探討靜態網站生成器(Static Site Generator),並嘗試將 Jekyll 部落格託管在 GitHub Pages 上。
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---

從[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 12021年初開始,我使用Jekyll在GitHub Pages上託管部落格。但是在建立部落格時沒有好好整理安裝過程,導致後續維護時遇到一些困難,所以決定簡單記錄一下安裝過程和維護方法。

(+ 12024.12 內容更新)

## 1. 靜態網站生成器 & 網頁託管

### 1-1. 靜態網頁 vs 動態網頁

#### 靜態網頁(Static Web Page)
- 將伺服器上儲存的資料直接傳送給使用者的網頁
- 網頁伺服器會傳送預先儲存的頁面來回應使用者的請求
- 除非伺服器上的資料被更改,否則使用者每次看到的都是相同的網頁
- 只需傳送對應的檔案,無需額外處理,所以回應通常較快
- 僅由簡單的檔案組成,只需建立網頁伺服器,因此建置成本較低
- 只能顯示預先儲存的資訊,所以服務有限
- 資料的新增、修改、刪除需要管理員手動操作
- 結構便於搜尋引擎爬蟲,相對更有利於搜尋引擎最佳化(SEO)

#### 動態網頁(Dynamic Web Page)
- 將伺服器上儲存的資料經過腳本處理後傳送給使用者的網頁
- 網頁伺服器會解析使用者的請求,處理資料後生成網頁再傳送
- 使用者看到的網頁會根據情況、時間、請求等因素而變化
- 需要處理腳本才能傳送網頁,所以回應相對較慢
- 除了網頁伺服器外還需要應用程式伺服器,因此建置時會產生額外成本
- 可以動態組合各種資訊,所以能提供多樣化的服務
- 根據網頁結構,使用者可以在瀏覽器中新增、修改、刪除資料
 
### 1-2. 靜態網站生成器(SSG, Static Site Generator)
- 基於原始資料(通常是markdown格式的文字檔)和預定義的模板生成靜態網頁的工具
- 無需直接編寫個別HTML頁面,只要用markdown撰寫文章,就能自動化建置網頁並發布到網路上的過程
- 例如: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- GitHub提供的免費靜態網頁託管服務
- 每個帳號可以託管1個個人代表網頁,以及無限量的專案文件頁面
- 建立名為'{username}.github.io'的儲存庫,然後可以直接推送建置好的HTML頁面,或使用GitHub Actions進行建置和部署
- 如果擁有自己的網域,可以在設定中連結,用其他網域地址取代預設的'{username}.github.io'格式

## 2. 選擇SSG和主題

### 2-1. 選擇Jekyll的原因
雖然有Jekyll、Hugo、Gatsby等多種SSG可選,但我決定使用Jekyll。以下是選擇SSG時考慮的標準,以及選擇Jekyll的原因:
- 是否能最小化不必要的嘗試錯誤,專注於寫作和經營部落格?
  - Jekyll是GitHub Pages官方支援的靜態網站生成器。雖然Hugo、Gatsby等其他SSG也可以在GitHub Pages上託管,甚至可以選擇使用Netlify等完全不同的託管服務,但實際上對於這種規模的個人部落格來說,使用哪種SSG建置、建置速度和性能等技術細節並不是很重要,所以我判斷選擇維護更簡單、參考文件更多的方案會更好。
  - Jekyll相比Hugo、Gatsby等競爭對手,開發時間最長。因此相關文件更完善,實際遇到問題時可參考的資料量也壓倒性地多。
- 可用的主題和外掛是否多樣?
  - 即使使用SSG而不是直接編寫HTML,自己製作各種模板也很麻煩、耗時,而且沒有必要。網上已經有很多優秀的公開主題,選擇喜歡的來使用就可以了。
  - 而且我原本主要使用C和Python,對Jekyll的Ruby或Hugo的Go語言不太熟悉,所以更想積極利用現有的主題和外掛。
  - 在Jekyll中很快就找到了看起來就很喜歡的主題,相比之下Hugo和Gatsby適合個人部落格用途的主題數量似乎不是很多。這可能也是受到上述GitHub Pages的相容性和開發時間長度的影響。

### 2-2. 主題選擇

#### Minimal Mistakes (12021.01 - 12022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- 建立部落格初期使用了約1年3個月的主題
- 支援通過Disqus、Discourse、utterances等的評論功能
- 支援分類和標籤功能
- 內建支援Google Analytics
- 可選擇預定義的外觀
- 雖然後來發現了設計更優雅、更喜歡的Chirpy主題而轉移過去,但考慮到這是個工程師風格的部落格,即使不是很漂亮,這個主題的設計也算乾淨整潔,使用起來還算不錯。

#### Chirpy Jekyll Theme (12022.04 - 現在)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- 從12022年4月轉換部落格主題後至今一直在使用的主題
- 支援多層分類、標籤功能
- 基於MathJax,內建支援LaTex語法的數學公式表示
- 基於Mermaid,內建支援圖表功能
- 支援通過Disqus、Giscus等的評論功能
- 支援Google Analytics、GoatCounter
- 支援淺色主題和深色主題
- 在主題轉換時,MathJax和Mermaid在Minimal Mistakes主題中並不內建支援,需要自行客製化添加,而Chirpy主題則內建支援。雖然說是客製化,其實也沒什麼大不了的,但這還是個小優點。
- 最重要的是,設計很漂亮。Minimal Mistakes主題雖然乾淨,但有種特有的僵硬感,感覺更適合專案官方技術文件或作品集頁面,而不是部落格。相比之下,Chirpy主題的設計即使與Tistory、Medium、velog等商業部落格平台相比也毫不遜色。

## 3. 建立GitHub儲存庫、建置和部署

以目前(12024.06)使用的Chirpy Jekyll Theme為基準說明,並假設已經安裝了Git。  
參考[Jekyll官方安裝指南](https://jekyllrb.com/docs/installation/)和[Chirpy Jekyll Theme官方頁面](https://github.com/cotes2020/jekyll-theme-chirpy/wiki)。

### 3-1. 安裝Ruby & Jekyll
按照[Jekyll官方安裝指南](https://jekyllrb.com/docs/installation/)根據自己的作業系統環境安裝Ruby和Jekyll。

### 3-2. 建立GitHub儲存庫
[Chirpy Jekyll Theme官方頁面](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site)介紹了以下兩種方法:
1. 使用"jekyll-theme-chirpy" gem載入核心檔案,其餘資源從[Chirpy Starter](https://github.com/cotes2020/chirpy-starter)模板獲取
  - 優點:如後所述,版本升級應用較容易。
  - 缺點:客製化受限。
2. 將[jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy)儲存庫fork到自己的部落格儲存庫
  - 優點:直接在儲存庫中管理所有檔案,可以自由修改程式碼來客製化主題不支援的功能。
  - 缺點:要應用版本升級時需要合併[原始儲存庫的最新上游標籤](https://github.com/cotes2020/jekyll-theme-chirpy/tags),有時自行客製化的程式碼可能與升級版本的程式碼衝突。這種情況下需要自行解決衝突。

我選擇了第1種方法。Chirpy主題本身完成度很高,大多數使用者不太需要客製化,而且截至12024年仍在積極開發和改進功能,除非要大幅修改,否則及時跟進原始上游的優點超過了自行客製化的優點。Chirpy主題官方指南也建議大多數使用者採用第1種方法。

### 3-3. 主要設定
在根目錄的`_config.yml`{: .filepath}檔案和`_data/contact.yml`{: .filepath}、`_data/share.yml`{: .filepath}檔案中應用必要的設定。註解寫得很清楚,設定也很直觀,可以輕鬆應用。比較需要外部額外操作的設定有Google Search Console連結的驗證碼註冊,以及Google Analytics或GoatCounter等網站管理工具的連結,但這些程序其實也不複雜,而且不是本文要討論的核心主題,所以省略詳細說明。

### 3-4. 在本機建置
雖然不是必要步驟,但在撰寫新文章或修改網站時,可能想預先確認是否能在網頁上正常顯示。這時可以在本機儲存庫的根目錄開啟終端機,執行以下命令:
```console
$ bundle exec jekyll s
```
等待幾秒後,網站就會在本機建置完成,可以在<http://127.0.0.1:4000>地址查看結果。

### 3-5. 部署
有兩種方法:
1. 使用GitHub Actions (在GitHub Pages上託管的情況)
  - 如果使用GitHub Free Plan,需要將儲存庫保持為public
  - 在GitHub網頁上選擇儲存庫的*Settings*標籤,然後在左側導航欄選擇*Code and automation > Pages*,在**Source**部分選擇**GitHub Actions**選項
  - 設定完成後,每次推送新的commit時都會自動執行*Build and Deploy*工作流程
2. 直接建置後部署 (使用其他託管服務或自行託管的情況)
  - 執行以下命令直接建置網站
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - 將`_site`目錄中的建置結果上傳到伺服器

## 4. 撰寫文章
Chirpy主題的[文章撰寫指南](https://chirpy.cotes.page/posts/write-a-new-post/)詳細說明了文章撰寫方法和可用選項。除了本文描述的內容外,還提供了多種功能,是值得參考的內容,有需要時可以查看官方文件。這裡整理了每次發文時都需要注意的主要事項。

### 建立Markdown檔案
- 名稱格式: `YYYY-MM-DD-TITLE.md`{: .filepath}
- 位置: `_posts`{: .filepath}目錄

### 撰寫Front Matter
Markdown檔案的開頭需要適當撰寫Front Matter。
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
- **description**: 摘要。如果不填寫,會自動使用正文內容的前面部分,但為了搜尋引擎最佳化(SEO),建議直接適當撰寫description meta標籤。羅馬字135~160字,中文80~110字左右的長度較為適合。
- **date**: 精確的文章撰寫日期時間和時區(可省略,省略時會自動識別使用檔案的建立日期或修改日期資訊)
- **categories**: 文章的分類
- **tags**: 文章的標籤
- **image**: 在文章頂部插入預覽圖片
  - **path**: 圖片檔案路徑
  - **alt**: 替代文字(可省略)
- **toc**: 是否使用右側側邊欄的目錄功能,預設值為`true`
- **comments**: 如果想明確指定個別文章的評論使用與否,可以使用此選項覆蓋網站的預設設定
- **math**: 啟用內建的[MathJax](https://www.mathjax.org/)數學公式表示功能,為了頁面效能預設為停用(`false`)
- **mermaid**: 啟用內建的[Mermaid](https://github.com/mermaid-js/mermaid)圖表表示功能,預設為停用(`false`)

## 5. 升級

假設採用了[3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-建立github儲存庫)中的第1種方法。如果採用第2種方法,如前所述需要直接合併最新的上游標籤。

1. 編輯`Gemfile`{: .filepath},指定"jekyll-theme-chirpy" gem的新版本。
2. 對於主要升級,不包含在"jekyll-theme-chirpy" gem中的核心檔案和設定選項也可能有變更。這時需要使用以下GitHub API確認變更後手動反映:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
