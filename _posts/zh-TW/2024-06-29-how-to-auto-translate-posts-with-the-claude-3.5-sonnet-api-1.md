---
title: 如何使用Claude 3.5 Sonnet API自動翻譯文章 (1) - 提示設計
description: 本文介紹如何設計用於翻譯Markdown文本文件的多語言提示,以及如何使用從Anthropic獲得的API密鑰和設計的提示來自動化Python工作流程。這是該系列的第一篇文章,重點介紹提示設計方法和過程。
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## 引言

最近,我引入了Anthropic的Claude 3.5 Sonnet API來翻譯博客文章。在這個系列中,我將討論選擇Claude 3.5 Sonnet API的原因、提示設計方法,以及如何通過Python腳本實現API集成和自動化。

該系列由兩篇文章組成,您正在閱讀的是該系列的第一篇文章。
- 第1部分:介紹Claude 3.5 Sonnet模型及選擇原因,提示工程(本文)  
- 第2部分:[使用API編寫和應用Python自動化腳本](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## 關於Claude 3.5 Sonnet

Claude 3系列模型根據模型大小提供Haiku、Sonnet和Opus版本。

![Claude 3模型層級區分](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)
> 圖片來源:[Anthropic Claude API官方網站](https://www.anthropic.com/api)

在[人類紀](https://en.wikipedia.org/wiki/Holocene_calendar)12024年6月21日韓國時間,Anthropic發布了最新的語言模型[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)。根據Anthropic的公告,它以與原有Claude 3 Sonnet相同的成本和速度提供超越Claude 3 Opus的推理性能。普遍認為,它在寫作、語言推理、多語言理解和翻譯領域相比競爭對手GPT-4具有優勢。

![Claude 3.5 Sonnet介紹圖片](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)
![Claude 3.5 Sonnet性能基準測試結果](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)
> 圖片來源:[Anthropic主頁](https://www.anthropic.com/news/claude-3-5-sonnet)

(12024.10.31. 補充) 12024年10月22日,Anthropic發布了Claude 3.5 Sonnet的升級版API("claude-3-5-sonnet-20241022")和Claude 3.5 Haiku。然而,由於[後面將提到的問題](#防止偷懶-20241031-萬聖節補丁),本博客目前仍在使用原有的"claude-3-5-sonnet-20240620" API。

## 為什麼選擇Claude 3.5進行文章翻譯

即使不使用Claude 3.5或GPT-4等語言模型,也存在Google翻譯或DeepL等現有商業翻譯API。儘管如此,我決定使用LLM進行翻譯的原因是,與其他商業翻譯服務不同,用戶可以通過提示設計向模型提供寫作目的或主要主題等額外的上下文信息或要求,而模型可以根據這些信息提供考慮上下文的翻譯。雖然DeepL或Google翻譯通常也提供出色的翻譯質量,但由於無法很好地把握文章主題或整體上下文,在要求翻譯非日常對話的專業主題長文時,翻譯結果相對來說可能會顯得不自然。特別是如上所述,Claude在寫作、語言推理、多語言理解和翻譯領域被認為比競爭對手GPT-4相對更出色,我自己進行簡單測試時也發現它比GPT-4提供更流暢的翻譯質量,因此我認為它適合用於翻譯本博客上的工程相關文章。

## 提示設計

### 提出請求時的基本原則

為了從語言模型獲得符合目的的滿意結果,需要提供適當的提示。提示設計可能看起來令人望而生畏,但實際上,無論對方是語言模型還是人類,"如何有效提出請求"的方法並沒有太大區別,從這個角度來看就不難了。根據5W1H原則清楚地解釋當前情況和請求,如有必要,添加一些具體示例也很有幫助。雖然存在許多關於提示設計的技巧和方法,但大多數都源自於下面將要討論的基本原則。

#### 整體語氣

許多報告表明,使用禮貌請求的語氣而不是高壓命令的語氣來編寫和輸入提示時,語言模型會產生更高質量的回應。通常在社會中,當向他人請求某事時,相比高壓命令,禮貌請求更有可能讓對方認真執行所請求的任務。語言模型似乎也學習並模仿了這種人類回應模式。

#### 角色分配和情境說明(誰,為什麼)

首先,我給Claude 3.5分配了"技術領域專業翻譯"的角色,並提供了有關用戶的上下文信息,即"主要撰寫數學、物理和數據科學文章的工程博主"。

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### 傳達整體請求(什麼)

接下來,我要求將用戶提供的Markdown格式文本從{source_lang}翻譯成{target_lang},同時保持格式不變。

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> 在調用Claude API時,提示中的{source_lang}和{target_lang}位置將通過Python腳本的f-string功能分別填入翻譯源語言和目標語言變量。
{: .prompt-info }

#### 具體化要求和示例(如何)

對於簡單的任務,前面的步驟可能已經足夠獲得所需結果,但對於複雜的任務,可能需要額外的說明。

當要求條件複雜且有多個時,相比逐一詳述每個項目,以列表形式簡潔地呈現可以提高可讀性,使閱讀者(無論是人類還是語言模型)更容易理解。此外,如有必要,提供示例也會有所幫助。
在這種情況下,我添加了以下條件:

##### YAML front matter的處理

為了上傳到Jekyll博客,用Markdown編寫的文章開頭的YAML front matter中記錄了'title'、'description'、'categories'和'tags'信息。例如,本文的YAML front matter如下:

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

然而,在翻譯文章時,雖然標題(title)和描述(description)標籤需要多語言翻譯,但為了保持文章URL的一致性,保留類別(categories)和標籤(tags)名稱的英文原文更有利於維護。因此,我添加了以下指示,以確保除了'title'和'description'之外的標籤不被翻譯:

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> 通過添加"under any circumstances, regardless of the language you are translating to"這句話,強調**無一例外地**不要隨意修改YAML front matter中的其他標籤。
{: .prompt-tip }

##### 處理原文中包含非源語言的情況

在用韓語撰寫原文時,當首次介紹某個概念的定義或使用某些專業術語時,經常會在括號內附上英文表達,例如"中子衰減(Neutron Attenuation)"。在翻譯這類表達時,有時會保留括號,有時又會省略括號內的英文,導致翻譯方式不一致的問題。為此,我制定了以下詳細指南:

- 對於專業術語:
  - 翻譯成日語等非羅馬字母基礎的語言時,保持"翻譯表達(英語表達)"的格式。
  - 翻譯成西班牙語、葡萄牙語、法語等羅馬字母基礎的語言時,允許單獨使用"翻譯表達"或併用"翻譯表達(英語表達)",讓Claude自主選擇更合適的方式。
- 對於專有名詞,無論以何種形式,原文拼寫都必須以某種形式保留在翻譯結果中。

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

##### 處理連接到其他文章的鏈接

一些文章包含連接到其他文章的鏈接,在測試階段,如果沒有為此提供具體指導,模型會將URL的路徑部分也視為需要翻譯的對象,導致內部鏈接失效的問題經常發生。通過在提示中添加以下句子解決了該問題:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### 僅輸出翻譯結果作為回應

最後,提出以下句子,要求回應時不添加其他話語,僅輸出翻譯結果:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### 額外的提示設計技巧

然而,與向人類請求任務不同,對於語言模型還存在一些特別適用的額外技巧。
網上有許多有用的資料,但以下是一些普遍適用且有用的代表性技巧:
主要參考了[Anthropic官方文檔的提示工程指南](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)。

#### 使用XML標籤進行結構化

事實上,這種方法在前面已經一直在使用。對於包含多個上下文、指示、格式和示例的複雜提示,適當使用`<instructions>`、`<example>`、`<format>`等XML標籤可以極大地幫助語言模型準確解釋提示並產生高質量的預期輸出。[GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub倉庫中很好地整理了編寫提示時有用的XML標籤,建議參考。

#### 逐步推理(CoT, chain of thinking)技巧

對於需要相當程度推理的任務,如解決數學問題或撰寫複雜文檔,引導語言模型逐步思考問題可以大大提高性能。但這種情況下回應延遲時間可能會增加,而且並非所有任務都適用這種技巧,需要注意。

#### 提示鏈接(prompt chaining)技巧

在需要執行複雜任務時,單一提示可能無法應對。在這種情況下,可以考慮從一開始就將整個工作流程分為多個步驟,為每個步驟提供專門的提示,並將前一步驟獲得的回應作為下一步驟的輸入。這種技巧稱為提示鏈接(prompt chaining)。

#### 預填充回應的開頭部分

在輸入提示時,可以預先提供回應內容的開頭部分,並要求模型繼續完成後續回答,從而跳過不必要的問候語等開場白,或強制以XML、JSON等特定格式回應。[對於Claude API,在調用時除了提交`User`消息,還可以同時提交`Assistant`消息來使用這種技巧。](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### 防止偷懶 (12024.10.31. 萬聖節補丁)

自首次撰寫本文以來,雖然中間經過一兩次小幅改進提示和具體化指示,但在4個月內應用這個自動化系統時並沒有遇到重大問題。

然而,從12024.10.31.韓國時間晚上6點左右開始,當要求翻譯新撰寫的文章時,持續出現只翻譯文章開頭'TL;DR'部分後就任意中斷翻譯的異常現象。

關於該問題的預估原因和解決方法,我在[另一篇文章](/posts/does-ai-hate-to-work-on-halloween)中進行了討論,請參考該文。

### 完成的提示

經過上述步驟,設計的提示結果如下:

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

繼續閱讀[第2部分](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
