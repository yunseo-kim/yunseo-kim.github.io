---
title: 使用 Claude Sonnet 4 API 自動翻譯文章的方法 (1) - 提示詞設計
description: "設計用於 Markdown 文字檔案多語言翻譯的提示詞，並運用從 Anthropic 取得的 API 金鑰和撰寫的提示詞，透過 Python 自動化作業流程。本文是該系列的第一篇文章，介紹提示詞設計的方法和過程。"
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---

## 前言
自 12024 年 6 月導入 Anthropic 的 Claude 3.5 Sonnet API 用於部落格文章的多語言翻譯以來，經過數次提示詞及自動化腳本改進，以及模型版本升級，在將近一年的期間內滿意地運用該翻譯系統。因此在這個系列中，將探討導入過程中選擇 Claude Sonnet 模型的原因、提示詞設計方法，以及透過 Python 腳本進行 API 整合及自動化實作的方法。  
系列共由 2 篇文章組成，您正在閱讀的這篇是該系列的第一篇文章。
- 第 1 篇：Claude Sonnet 模型介紹及選定理由、提示詞工程（本文）
- 第 2 篇：[運用 API 撰寫 Python 自動化腳本及應用](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## 關於 Claude Sonnet
Claude 系列模型根據模型大小提供 Haiku、Sonnet 和 Opus 版本。  
![Claude 3 模型層級區分](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)  
> 圖片來源：[Anthropic Claude API 官方網頁](https://www.anthropic.com/api)

> （12025.05.29. 補充）  
> 由於是一年前擷取的圖片，所以 token 費用是以舊版本 Claude 3 為基準，但根據模型大小區分的 Haiku、Sonnet、Opus 分類仍然有效。截至 12025 年 5 月底，Anthropic 提供的各模型價格設定如下。
>
> | Model | Base Input <br>Tokens | 5m Cache <br>Writes | 1h Cache <br>Writes | Cache Hits &<br> Refreshes | Output <br>Tokens |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | Claude Opus 4 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Sonnet 4 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.7 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.5 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Haiku 3.5 | $0.80 / MTok | $1 / MTok | $1.6 / MTok | $0.08 / MTok | $4 / MTok |
> | Claude Opus 3 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Haiku 3 | $0.25 / MTok | $0.30 / MTok | $0.50 / MTok | $0.03 / MTok | $1.25 / MTok |
>
> 來源：[Anthropic developer docs](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

而在韓國時間[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 12024 年 6 月 21 日，Anthropic 公開的語言模型 [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) 以與既有 Claude 3 Sonnet 相同的成本和速度，展現超越 Claude 3 Opus 的推理性能，普遍評價認為在寫作、語言推理、多語言理解及翻譯領域相較於競爭模型 GPT-4 具有優勢。  
![Claude 3.5 Sonnet 介紹圖片](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet 性能基準測試結果](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)  
> 圖片來源：[Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## 為文章翻譯導入 Claude 3.5 的原因
即使不使用 Claude 3.5 或 GPT-4 等語言模型，也存在 Google 翻譯或 DeepL 等既有的商用翻譯 API。儘管如此，決定使用 LLM 進行翻譯的原因是，與其他商用翻譯服務不同，使用者可以透過提示詞設計向模型提供文章的撰寫目的或主要主題等本文以外的額外脈絡資訊或需求，模型可以據此提供考慮文脈的翻譯。

DeepL 或 Google 翻譯雖然大致展現優秀的翻譯品質，但由於無法很好地掌握文章主題或整體脈絡，也無法另外傳達複雜的需求，因此當要求翻譯非日常對話而是專業主題的長文時，相對來說翻譯結果有時會不自然，且難以準確配合所需的特定格式（Markdown、YAML frontmatter 等）輸出。

特別是如前所述，Claude 相較於競爭模型 GPT-4，在寫作、語言推理、多語言理解及翻譯領域普遍評價更為優秀，直接進行簡單測試時也比 GPT-4 展現更流暢的翻譯品質，因此在考慮導入的 12024 年 6 月當時，判斷適合將這個部落格記載的工程相關文章翻譯成多種語言的作業。

## 模型採用歷程及現況
### 12024.07.01.
如[另一篇文章](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/)所整理，[完成了應用 Polyglot 外掛並配合修改 `_config.yml`{: .filepath}、html 標頭、sitemap 的初期作業。](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) 接著[採用 Claude 3.5 Sonnet 模型作為翻譯用途，完成本系列探討的 API 整合 Python 腳本的初期實作及驗證後予以應用。](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
12024 年 10 月 22 日，Anthropic 發表了 Claude 3.5 Sonnet 的升級版本 API（"claude-3-5-sonnet-20241022"）和 Claude 3.5 Haiku。不過由於[後述問題](#防止偷懶120241031-萬聖節補丁)，目前本部落格仍應用既有的 "claude-3-5-sonnet-20240620" API。

### 12025.04.02.
[將應用模型從 "claude-3-5-sonnet-20240620" 轉換為 "claude-3-7-sonnet-20250219"。](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[將應用模型從 "claude-3-7-sonnet-20250219" 轉換為 "claude-sonnet-4-20250514"。](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Claude 4 性能基準測試結果](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)  
> 圖片來源：[Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

雖然根據使用條件可能有所差異，但大致上自 Claude 3.7 Sonnet 模型推出以來，在編程方面 Claude 是最強大的模型這一點幾乎沒有異議。Anthropic 也積極將相較於 OpenAI 或 Google 等競爭模型的優秀編程性能作為自家模型的主要優勢來宣傳。在這次 Claude Opus 4 和 Claude Sonnet 4 的發表中，也可以確認延續強調編程性能、以開發者為主要客群的基調。

當然從公開的基準測試結果來看，編程以外的項目也整體有所改善，對於本文探討的翻譯作業而言，多語言問答（MMMLU）或數學解題（AIME 2025）部門的性能提升預期將特別有效。直接進行簡單測試的結果，確認 Claude Sonnet 4 相較於前一個模型 Claude 3.7 Sonnet，在表達的自然性、專業性、術語使用的一致性等方面的翻譯結果更為優秀。

> 在現階段，至少對於像這個部落格探討的技術性質韓文文章的多語言翻譯作業，我認為 Claude 模型仍然是最優秀的。不過最近 Google 的 Gemini 模型性能顯著提升，今年 5 月甚至公開了雖然還在 Preview 階段但已達 Gemini 2.5 模型的情況。  
> 比較 Gemini 2.0 Flash 模型與 Claude 3.7 Sonnet、Claude Sonnet 4 模型時，判斷 Claude 的翻譯性能更優秀，但 Gemini 的多語言性能也相當優秀，數學、物理解題及敘述能力甚至 Gemini 2.5 Preview 05-06 比 Claude Opus 4 更為優秀，因此該模型正式公開後再次比較會如何還無法斷言。  
> 考慮到相較於 Claude 稍微便宜的 API 費用，Gemini 的價格競爭力卓越，因此只要達到某種程度的對等性能，Gemini 就可能成為合理的替代方案。Gemini 2.5 還在 Preview 階段，因此判斷現在應用於實際自動化還為時過早，暫不考慮，但未來正式版本公開後計劃進行測試。
{: .prompt-tip }

## 提示詞設計
### 請求某事時的基本原則
為了從語言模型獲得符合目的的滿意結果，必須提供相應的適當提示詞。提示詞設計聽起來可能感覺很困難，但實際上「很好地請求某事的方法」無論對方是語言模型還是人類都沒有太大差異，因此從這種觀點接近就不會太困難。根據六何原則明確說明現況及請求事項，必要時也可以附加幾個具體例子。關於提示詞設計存在無數的技巧和技法，但大部分都是從後述基本原則衍生出來的。

#### 整體語調
有許多報告指出，以禮貌請求的語調而非高壓命令調撰寫並輸入提示詞時，語言模型會輸出更高品質的回應。通常在社會上向他人請求某事時，禮貌請求比高壓命令更能提高對方認真執行委託作業的機率，語言模型似乎也學習並模仿了人們的這種回應模式。

#### 角色賦予及情況說明（誰、為什麼）
首先給 Claude 4 賦予*「技術領域專業翻譯家（professional technical translator）」*的角色，並提供*「主要撰寫數學、物理學、資料科學相關文章的工程部落客」*這樣的使用者脈絡資訊。

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### 大框架的請求事項傳達（什麼）
接下來，要求將使用者提供的 Markdown 格式文章從 {source_lang} 翻譯為 {target_lang}，同時保持格式。

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> 呼叫 Claude API 時，提示詞的 {source_lang} 和 {target_lang} 位置會透過 Python 腳本的 f-string 功能分別填入翻譯出發語言和到達語言變數。
{: .prompt-info }

#### 需求具體化及例子（如何）
如果是簡單的作業，到前面的步驟就足以獲得想要的結果，但如果要求複雜的作業，可能需要額外的說明。

當需求條件複雜且有多項時，比起逐一敘述各項事項，採用條列式傳達可以提升可讀性，對閱讀方（無論是人類還是語言模型）來說更容易理解。此外，必要時也一起提供例子會有幫助。
在這種情況下，添加了以下條件。

##### YAML front matter 的處理
為了上傳到 Jekyll 部落格而以 Markdown 撰寫的文章開頭部分的 YAML front matter 記錄了 'title'、'description'、'categories' 和 'tags' 資訊。例如，現在這篇文章的 YAML front matter 如下。

```yaml
---
title: 使用 Claude Sonnet 4 API 自動翻譯文章的方法 (1) - 提示詞設計
description: >-
  設計用於 Markdown 文字檔案多語言翻譯的提示詞，並運用從 Anthropic 取得的
  API 金鑰和撰寫的提示詞，透過 Python 自動化作業流程。
  本文是該系列的第一篇文章，介紹提示詞設計的方法和過程。
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

但是翻譯文章時，標題（title）和說明（description）標籤需要翻譯成多語言，但為了文章 URL 的一致性，類別（categories）和標籤（tags）名稱不翻譯而保持英文原樣在維護管理上更為便利。因此下達以下指示，使 'title' 和 'description' 以外的標籤不被翻譯。Claude 應該已經學習並知道關於 YAML front matter 的資訊，因此這種程度的說明在大部分情況下就足夠了。

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> 添加了 "under any circumstances, regardless of the language you are translating to" 這個句子，強調**無例外地**不要隨意修改 YAML front matter 的其他標籤。
{: .prompt-tip }

（12025.04.02. 更新）  
此外，指示 description 標籤的內容考慮 SEO 以適當分量撰寫，如下所示。

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### 提供的原文包含出發語言以外其他語言時的處理
用韓文撰寫原文時，首次介紹某個概念的定義或使用某些專業術語時，經常會像「*중성자 감쇠（Neutron Attenuation）*」這樣在括號內一起記載英文表達。翻譯這種表達時，有時保留括號，有時遺漏括號內記載的英文等，翻譯方式不一致的問題，因此制定了以下細部指針。
- 專業術語的情況，
  - 翻譯成日文等非羅馬字基礎語言時，維持「翻譯表達（英語表達）」的格式。
  - 翻譯成西班牙文、葡萄牙文、法文等羅馬字基礎語言時，允許「翻譯表達」單獨標記和「翻譯表達（英語表達）」並行標記兩種，讓 Claude 自主選擇其中更適當的。
- 專有名詞的情況，無論何種形式，原文拼字都必須在翻譯結果中保存。

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases.
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it.
  2. it may be a proper noun such as a person's name or a place name.
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language,
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'.
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### 連結到其他文章的連結處理
有些文章包含連結到其他文章的連結，在測試階段沒有另外提示相關指針時，經常發生將 URL 的路徑部分也解釋為需要翻譯的對象而改變，導致內部連結損壞的問題。該問題透過在提示詞中添加這個句子得到解決。

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

（12025.04.06. 更新）  
提供上述指針後，翻譯時會正確處理連結的路徑部分，連結損壞的頻率大幅減少，但對於包含部分識別符（Fragment identifier）的連結，由於不知道連結目標文章的內容，部分識別符部分仍然需要語言模型大致推測填入，存在根本問題無法解決的限制。因此改善了 Python 腳本及提示詞，將連結到的其他文章的脈絡資訊包含在使用者提示詞的 `<reference_context>` XML 標籤內一起提供，並根據該脈絡處理連結翻譯。應用該更新後，大部分可以預防連結損壞問題，對於緊密連結的系列文章，也可以期待在多篇文章中提供更一致翻譯的效果。

在系統提示詞中提示以下指針。
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

而使用者提示詞的 `<reference_context>` 部分以下列格式和內容構成，在要翻譯的本文內容後額外提供。
```xml
<reference_context>
The following are contents of posts linked with hash fragments in the original post. 
Use these for context when translating links and references:

<referenced_post path="{post_1_path}" hash="{hash_fragment_1}">
{post_content}
</referenced_post>

<referenced_post path="{post__2_path}" hash="{hash_fragment_2}">
{post_content}
</referenced_post>

...

</reference_context>
```

> 關於具體如何實作，請參考本系列的[第 2 篇](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)和 GitHub 儲存庫中的 [Python 腳本](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py)內容。
{: .prompt-tip }

##### 僅輸出翻譯結果作為回應
最後，提示回應時不要添加其他話語，只輸出翻譯結果，如下句所示。

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### 額外的提示詞設計技法
不過，與向人類請求作業不同，對於語言模型還存在特別適用的額外技法。
關於這方面，網路上有許多有用的資料，但整理幾個可以廣泛有用活用的代表性技巧如下。  
主要參考了 [Anthropic 官方文件的提示詞工程指南](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)。

#### 運用 XML 標籤進行結構化
實際上這在前面已經一直使用了。對於包含多種脈絡、指示事項、格式、例子的複雜提示詞，適當運用 `<instructions>`、`<example>`、`<format>` 等 XML 標籤，有助於語言模型正確解釋提示詞並產出符合意圖的高品質輸出。[GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub 儲存庫中整理了撰寫提示詞時有用的 XML 標籤，建議參考。

#### 逐步推理（CoT, chain of thinking）技法
對於數學解題或複雜文件撰寫等需要相當程度推理的作業，誘導語言模型逐步分割問題思考可以大幅提升性能。不過這種情況下回應延遲時間可能會變長，且並非對所有作業都總是有用，需要注意。

#### 提示詞鏈接（prompt chaining）技法
需要執行複雜作業時，單一提示詞可能有應對限制。這種情況下可以考慮從一開始就將整體作業流程分為多個階段，各階段提示特化的提示詞，並將前一階段獲得的回應作為下一階段的輸入傳遞的方式。這種技法稱為提示詞鏈接（prompt chaining）。

#### 預先填入回應開頭部分
輸入提示詞時，預先提示回應內容的開頭部分，讓其撰寫後續答案，藉此跳過不必要的寒暄等開場白，或強制以 XML、JSON 等特定格式回應。[Claude API 的情況，呼叫時不僅提交 `User` 訊息，同時提交 `Assistant` 訊息就可以使用這種技法。](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### 防止偷懶（12024.10.31. 萬聖節補丁）
在首次撰寫這篇文章後，中間雖然經過一兩次稍微的提示詞改善及指示事項具體化的追加，但無論如何，4 個月間應用本自動化系統沒有什麼大問題。

但是從韓國時間 12024.10.31. 晚上 6 點左右開始，委託新撰寫文章的翻譯作業時，持續發生只翻譯文章開頭的 'TL;DR' 部分後任意中斷翻譯的異常現象。

關於該問題的預想原因及解決方法已在[另一篇文章](/posts/does-ai-hate-to-work-on-halloween)中探討，請參考該文章。

### 完成的系統提示詞
經過上述步驟的提示詞設計結果可以在[下一篇](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)中確認。

## 延伸閱讀
在[第 2 篇](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)中繼續
