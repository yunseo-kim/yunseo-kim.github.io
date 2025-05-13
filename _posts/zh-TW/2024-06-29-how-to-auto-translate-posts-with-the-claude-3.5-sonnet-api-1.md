---
title: 如何使用Claude 3.5 Sonnet API自動翻譯文章 (1) - 提示詞設計
description: 本文介紹如何設計用於多語言翻譯Markdown文本文件的提示詞,以及如何使用從Anthropic獲得的API密鑰和設計的提示詞,通過Python實現工作自動化的過程。這是該系列的第一篇文章，主要介紹提示詞的設計方法和過程。
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## 前言
最近我引入了 Anthropic 的 Claude 3.5 Sonnet API 來進行部落格文章的多語言翻譯。在這個系列中，我將分享選擇 Claude 3.5 Sonnet API 的原因、提示詞設計方法，以及如何透過 Python 腳本連接 API 並實現自動化。  
本系列共有兩篇文章，您正在閱讀的是第一篇。
- 第一篇：Claude 3.5 Sonnet模型介紹及選擇理由、提示詞工程（本文）
- 第二篇：[使用API編寫和應用Python自動化腳本](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## 關於 Claude 3.5 Sonnet
Claude 3 系列模型根據模型大小分為 Haiku、Sonnet 和 Opus 版本。  
![Claude 3 模型層級區分](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> 圖片來源：[Anthropic Claude API 官方網頁](https://www.anthropic.com/api)

在台灣時間 [人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 12024年6月21日，Anthropic 發布了最新的語言模型 [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)。根據 Anthropic 的公告，這個模型以與 Claude 3 Sonnet 相同的成本和速度提供超越 Claude 3 Opus 的推理能力，並且在寫作、語言推理、多語言理解和翻譯領域普遍被認為比競爭對手 GPT-4 更具優勢。  
![Claude 3.5 Sonnet 介紹圖片](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet 性能基準測試結果](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> 圖片來源：[Anthropic 官網](https://www.anthropic.com/news/claude-3-5-sonnet)

（12024.10.31. 補充）12024年10月22日，Anthropic 發布了 Claude 3.5 Sonnet 的升級版 API（"claude-3-5-sonnet-20241022"）和 Claude 3.5 Haiku。但由於[後文將提到的問題](#防止偷懶-120241031-萬聖節更新)，本部落格目前仍使用原有的 "claude-3-5-sonnet-20240620" API。

## 為何選擇 Claude 3.5 進行文章翻譯
即使不使用 Claude 3.5 或 GPT-4 等語言模型，也有 Google 翻譯或 DeepL 等現有的商業翻譯 API。我之所以決定使用 LLM 進行翻譯，是因為與其他商業翻譯服務不同，用戶可以通過提示詞設計向模型提供文章的寫作目的或主要主題等額外的上下文信息或要求，而模型能夠據此提供考慮到上下文的翻譯。雖然 DeepL 或 Google 翻譯通常也提供優質的翻譯，但由於它們在把握文章主題或整體上下文方面的局限性，當要求翻譯非日常對話的專業主題長文時，翻譯結果相對可能顯得不自然。特別是如前所述，Claude 在寫作、語言推理、多語言理解和翻譯領域被認為比競爭對手 GPT-4 更出色，我自己簡單測試後也發現它比 GPT-4o 提供更流暢的翻譯質量，因此我認為它適合翻譯本部落格上的工程相關文章。

## 提示詞設計
### 提出請求的基本原則
要從語言模型獲得符合目的的滿意結果，需要提供適當的提示詞。提示詞設計可能看起來很複雜，但實際上「如何有效提出請求」這一點，無論對象是語言模型還是人類，原則都大同小異，從這個角度出發就不會太困難。按照六何原則清楚說明當前情況和請求事項，必要時附上一些具體例子也很有幫助。雖然有許多關於提示詞設計的技巧和方法，但大多數都源自於以下基本原則。

#### 整體語氣
有許多報告表明，使用禮貌請求的語氣而非高壓命令式的語氣撰寫提示詞時，語言模型會輸出更高質量的回應。在社會中，當我們向他人請求某事時，禮貌請求比高壓命令更可能讓對方認真完成任務，語言模型似乎也學習並模仿了這種人類回應模式。

#### 角色賦予和情境說明（誰，為什麼）
首先，我給 Claude 3.5 賦予了「技術領域專業翻譯者（professional technical translator）」的角色，並提供了關於用戶的上下文信息：「主要撰寫數學、物理學和數據科學相關文章的工程部落客」。

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### 傳達整體請求事項（什麼）
接下來，我請求將用戶提供的 Markdown 格式文本從 {source_lang} 翻譯成 {target_lang}，同時保持格式不變。

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> 在調用 Claude API 時，提示詞中的 {source_lang} 和 {target_lang} 位置會通過 Python 腳本的 f-string 功能分別填入翻譯源語言和目標語言變數。
{: .prompt-info }

#### 具體化需求和提供範例（如何）
對於簡單的任務，前面的步驟可能已經足夠獲得想要的結果，但對於複雜的任務，可能需要額外的說明。

當需求複雜且有多項時，將每項條件列成清單比逐一敘述更有助於提高可讀性，無論是對人類還是語言模型來說都更容易理解。此外，必要時提供範例也很有幫助。
在這種情況下，我添加了以下條件：

##### YAML front matter 的處理
Jekyll 部落格中用 Markdown 撰寫的文章開頭的 YAML front matter 包含「title」、「description」、「categories」和「tags」信息。例如，本文的 YAML front matter 如下：

```yaml
---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법
description: \>-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
  그리고 Anthropic으로부터 발급받은 API 키와 앞서 작성한 프롬프트를 적용하여 Python으로 번역 자동화 스크립트를 작성하고 활용하는 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

在翻譯文章時，標題（title）和描述（description）標籤需要翻譯成多種語言，但為了保持文章 URL 的一致性，類別（categories）和標籤（tags）名稱應保持英文原樣，這有利於維護管理。因此，我添加了以下指示，確保只翻譯「title」和「description」：

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> 我添加了「under any circumstances, regardless of the language you are translating to」這一短語，強調**無一例外地**不得隨意修改 YAML front matter 中的其他標籤。
{: .prompt-tip }

##### 處理原文中包含非源語言的情況
在用韓文撰寫原文時，當首次介紹某個概念定義或使用某些專業術語時，常會以「中性子減衰（Neutron Attenuation）」這樣的形式在括號內附上英文表達。在翻譯這類表達時，有時會保留括號，有時又會省略括號內的英文，導致翻譯方式不一致，因此我制定了以下詳細指南：
- 對於專業術語：
  - 翻譯成日文等非羅馬字母基礎的語言時，保持「翻譯表達（英文表達）」的格式。
  - 翻譯成西班牙文、葡萄牙文、法文等羅馬字母基礎的語言時，允許「翻譯表達」單獨標記和「翻譯表達（英文表達）」並行標記，由 Claude 自行選擇更適合的方式。
- 對於專有名詞，無論以何種形式，原文拼寫都必須在翻譯結果中保留。

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
  2. it may be a proper noun such as a person's name or a place name. \n\
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
  <if>it is the first case, and the target language is not a Roman alphabet-based language, \
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
      You can choose whichever you think is more appropriate.</example>\n\
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### 處理連結到其他文章的鏈接
一些文章包含連結到其他文章的鏈接，在測試階段，當沒有提供關於這方面的具體指導時，模型會將 URL 的路徑部分也視為需要翻譯的對象，導致內部鏈接失效。我通過添加以下指示解決了這個問題：

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### 僅輸出翻譯結果
最後，我要求回應中不要添加其他文字，只輸出翻譯結果：

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### 額外的提示詞設計技巧
與向人類請求任務不同，使用語言模型時有一些特別適用的額外技巧。
網上有許多有用的資源，但以下是一些普遍有用的代表性技巧：  
[主要參考了 Anthropic 官方文檔的提示詞工程指南](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)。

#### 使用 XML 標籤進行結構化
實際上，這是我們一直在使用的技巧。對於包含多種上下文、指示、格式和範例的複雜提示詞，適當使用 `<instructions>`、`<example>`、`<format>` 等 XML 標籤可以幫助語言模型準確解釋提示詞並產生高質量的符合意圖的輸出。[GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub 倉庫中有很好的提示詞編寫時有用的 XML 標籤整理，推薦參考。

#### 思維鏈（CoT, chain of thinking）技巧
對於需要相當程度推理的任務，如數學問題解決或複雜文檔編寫，引導語言模型分步思考可以大幅提升性能。但這可能會延長回應時間，且並非所有任務都適用此技巧。

#### 提示詞鏈接（prompt chaining）技巧
處理複雜任務時，單一提示詞可能有局限性。這時可以考慮將整個工作流程分為多個階段，為每個階段提供專門的提示詞，並將前一階段的回應作為下一階段的輸入。這種技巧稱為提示詞鏈接（prompt chaining）。

#### 預填回應的開頭部分
輸入提示詞時，可以預先提供回應的開頭部分，讓模型繼續完成，這樣可以跳過不必要的問候語等開場白，或強制模型以特定格式（如 XML、JSON）回應。[使用 Claude API 時，可以在調用時同時提交 `User` 消息和 `Assistant` 消息來使用此技巧。](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### 防止偷懶 (12024.10.31. 萬聖節更新)
雖然在最初撰寫這篇文章後進行了一兩次輕微的提示詞改進和指示具體化，但在過去四個月應用這個自動化系統時基本沒有遇到重大問題。

然而，在台灣時間 12024.10.31. 晚上 6 點左右，當我嘗試翻譯新撰寫的文章時，系統開始出現異常：它只翻譯文章開頭的「TL;DR」部分後就自行中斷翻譯。

關於這個問題的可能原因和解決方法，我已在[另一篇文章](/posts/does-ai-hate-to-work-on-halloween)中詳細討論，請參考該文。

### 完成的提示詞
經過上述步驟設計的提示詞結果如下：

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role> The customer's request is as follows:\n\n \
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task> \
In the provided markdown format text, \n\
  - <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
  - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
    1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
    2. it may be a proper noun such as a person's name or a place name. \n\
    After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
    <if>it is the first case, and the target language is not a Roman alphabet-based language, \
    please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
      - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
      - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
    <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
      - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
        You can choose whichever you think is more appropriate.</example>\n\
      - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
        French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
    <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
      - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
        In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
        redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
    </condition>\n\n\
  - <condition><if>the provided text contains links in markdown format, \
    please translate the link text and the fragment part of the URL into {target_lang}, \
    but keep the path part of the URL intact.</if> \n\
    - <example> the German translation of '[중성자 상호작용과 반응단면적]\
      (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
      would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
      #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

## 延伸閱讀
繼續閱讀[第二部分](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
