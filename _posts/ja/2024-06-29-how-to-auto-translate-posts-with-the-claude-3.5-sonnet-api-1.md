---
title: Claude 3.5 Sonnet APIでポストを自動翻訳する方法 (1) - プロンプトデザイン
description: マークダウンテキストファイルの多言語翻訳のためのプロンプトをデザインし、Anthropicから発行されたAPIキーと作成したプロンプトを適用してPythonで作業を自動化するプロセスを扱います。このポストはシリーズの最初の記事で、プロンプトデザインの方法とプロセスを紹介します。
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## はじめに
最近、ブログポストの多言語翻訳のためにAnthropic社のClaude 3.5 Sonnet APIを導入しました。このシリーズでは、導入過程でClaude 3.5 Sonnet APIを選択した理由とプロンプトデザインの方法、そしてPythonスクリプトを通じたAPI連携および自動化実装方法を扱います。  
シリーズは2つの記事で構成されており、現在読んでいるこの記事はシリーズの最初の記事です。
- 第1回：Claude 3.5 Sonnetモデルの紹介と選定理由、プロンプトエンジニアリング（本文）
- 第2回：[APIを活用したPython自動化スクリプトの作成と適用](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## About Claude 3.5 Sonnet
Claude 3シリーズモデルは、モデルサイズによってHaiku、Sonnet、そしてOpusバージョンが提供されています。  
![Claude 3モデルティア区分](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> 画像出典：[Anthropic Claude API公式ウェブページ](https://www.anthropic.com/api)

そして韓国時間で[人類暦](https://en.wikipedia.org/wiki/Holocene_calendar) 12024年6月21日、Anthropicは最新の言語モデル[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)を公開しました。Anthropicの発表によると、既存のClaude 3 Sonnetと同じコストと速度でClaude 3 Opusを上回る推論性能を示すとのことで、全般的に作文と言語推論、多言語理解および翻訳分野において競合モデルであるGPT-4と比較して強みを持つという評価が支配的です。  
![Claude 3.5 Sonnet紹介画像](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnetパフォーマンスベンチマーク結果](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> 画像出典：[Anthropicホームページ](https://www.anthropic.com/news/claude-3-5-sonnet)

（12024.10.31. 追加）12024年10月22日、AnthropicはClaude 3.5 Sonnetのアップグレード版API（"claude-3-5-sonnet-20241022"）とClaude 3.5 Haikuを発表しました。ただし[後述する問題](#怠け防止120241031-ハロウィンパッチ)により、現在のところ本ブログには既存の"claude-3-5-sonnet-20240620" APIを適用しています。

## ポスト翻訳のためにClaude 3.5を導入した理由
必ずしもClaude 3.5やGPT-4のような言語モデルでなくても、Google翻訳やDeepLなどの既存の商用翻訳APIが存在します。それにもかかわらず翻訳目的でLLMを使用することにした理由は、他の商用翻訳サービスとは異なり、ユーザーがプロンプトデザインを通じてモデルに文章の作成目的や主要テーマなど本文以外にも追加的な文脈情報や要件を提供でき、モデルはそれに合わせて文脈を考慮した翻訳を提供できるからです。DeepLやGoogle翻訳も概ね優れた翻訳品質を示す傾向がありますが、文章のテーマや全体的な文脈をうまく把握できない限界のため、日常的な会話ではなく専門的なテーマの長い文章を翻訳するよう依頼した場合、相対的に翻訳結果が不自然になることがありました。特にClaudeは前述したように競合モデルであるGPT-4と比較して作文、言語推論、多言語理解および翻訳分野では相対的により優れているという評価が多く、実際に簡単にテストしてみたところGPT-4oよりもさらに滑らかな翻訳品質を示したため、このブログに掲載する工学関連の記事を様々な言語に翻訳する作業に適していると判断しました。

## プロンプトデザイン
### 何かをリクエストする際の基本原則
言語モデルから目的に合った満足のいく結果を得るためには、それに合った適切なプロンプトを提供する必要があります。プロンプトデザインというと何か漠然と感じられるかもしれませんが、実際には「何かをうまくリクエストする方法」という点では相手が言語モデルであれ人間であれ大きく変わらないので、このような観点からアプローチすれば特に難しくありません。5W1Hに従って現状況およびリクエスト事項を明確に説明し、必要であれば具体的な例をいくつか添えるのも良いでしょう。プロンプトデザインに関する数多くのヒントやテクニックが存在しますが、ほとんどは後述する基本原則から派生するものです。

#### 全体的なトーン
高圧的な命令調よりも丁寧にリクエストするトーンでプロンプトを作成して入力すると、言語モデルがより高品質の応答を出力するという報告が多くあります。通常、社会で他の人に何かをリクエストする際も高圧的に命令するよりも丁寧にリクエストした方が、相手がより誠意をもって依頼された作業を遂行する確率が高まりますが、言語モデルもこのような人々の応答パターンを学習して模倣しているようです。

#### 役割付与および状況説明（誰が、なぜ）
まず最初にClaude 3.5に*「技術分野専門翻訳者（professional technical translator）」*という役割を与え、*「主に数学や物理学、データサイエンスに関する記事を寄稿する工学ブロガー」*というユーザーに関する文脈情報を提供しました。

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### 大枠でのリクエスト事項伝達（何を）
次に、ユーザーから提供されたマークダウン形式の文章を{source_lang}から{target_lang}へ形式を維持しながら翻訳するようリクエストしました。

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Claude API呼び出し時、プロンプトの{source_lang}と{target_lang}の位置にはPythonスクリプトのf-string機能を通じて翻訳元言語と翻訳先言語変数がそれぞれ入ります。
{: .prompt-info }

#### 要件の具体化および例示（どのように）
簡単な作業であれば前段階までで十分に望む結果を得られる場合もありますが、複雑な作業を要求する場合には追加的な説明が必要な場合があります。

要求条件が複雑で複数ある場合、それぞれの事項を詳細に説明するよりも、箇条書きにして伝えると可読性が向上し、読む立場（人間であれ言語モデルであれ）で理解しやすくなります。また必要であれば例も一緒に提供すると役立ちます。
この場合は次のような条件を追加しました。

##### YAML front matterの処理
Jekyllブログにアップロードするためにmarkdownで作成したポストの最初の部分に位置するYAML front matterには「title」と「description」、「categories」、そして「tags」情報を記録します。例えば、この記事のYAML front matterは次のとおりです。

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

しかし、ポストを翻訳する際にタイトル（title）と説明（description）タグは多言語に翻訳する必要がありますが、ポストURLの一貫性のためにカテゴリー（categories）とタグ（tags）名は翻訳せず英文のままにしておくと維持管理に有利です。したがって、以下のような指示を出して「title」と「description」以外のタグは翻訳しないようにしました。Claudeは既にYAML front matterに関する情報を学習して知っているはずなので、この程度の説明でほとんどの場合十分です。

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> "under any circumstances, regardless of the language you are translating to"という文句を添えて**例外なく**YAML front matterの他のタグは勝手に修正しないよう強調しました。
{: .prompt-tip }

##### 提供された原文が出発言語以外の言語を含む場合の処理
韓国語で原文を作成する際、ある概念の定義を初めて紹介したり、いくつかの専門用語を使用する場合に「*中性子減衰（Neutron Attenuation）*」のように括弧内に英語表現を一緒に記載することがよくあります。このような表現を翻訳する場合、時には括弧を残し、また時には括弧内に記載された英文を省略するなど翻訳方式が一貫していない問題があり、以下のような詳細指針を定めました。
- 専門用語の場合、
  - 日本語のようにローマ字ベースではない言語に翻訳する場合は「翻訳表現（英語表現）」の形式を維持する。
  - スペイン語、ポルトガル語、フランス語のようなローマ字ベースの言語に翻訳する場合は「翻訳表現」単独表記と「翻訳表現（英語表現）」併記表記の両方を許容し、Claudeが二つのうちより適切なものを自律的に選択するようにする。
- 固有名詞の場合、何らかの形で原文の綴りが翻訳結果にも保存されなければならない。

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

##### 他のポストへのリンクの処理
いくつかのポストは他のポストへのリンクを含みますが、テスト段階でこれに関する指針を別途提示しなかった場合、URLのパス部分まで翻訳すべき対象として解釈して変更してしまったため、内部リンクが壊れる問題がよく発生しました。その問題はプロンプトにこのフレーズを追加して解決しました。

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### 翻訳結果のみを応答として出力すること
最後に、応答時に他の言葉を付け加えず、翻訳結果のみを出力するよう次の文を提示します。

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### 追加的なプロンプトデザイン技法
ただし、人間に作業をリクエストする場合と異なり、言語モデルの場合に特別に適用される追加的な技法も存在します。
これに関してはウェブ上に様々な有用な資料が多くありますが、汎用的に有用に活用できるいくつかの代表的なヒントをまとめると次のようになります。  
[Anthropic公式ドキュメントのプロンプトエンジニアリングガイド](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)を主に参考にしました。

#### XMLタグを活用して構造化
実はこれは今までの前述の部分ですでに使用してきました。様々な文脈と指示事項、形式、例を含む複雑なプロンプトの場合、`<instructions>`、`<example>`、`<format>`などのXMLタグを適切に活用すると、言語モデルがプロンプトを正確に解釈し、高品質の意図に合った出力を提供するのに大いに役立ちます。[GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHubリポジトリにプロンプト作成時に有用なXMLタグがよくまとめられているので参考にすることをお勧めします。

#### 段階的推論（CoT、chain of thinking）技法
数学問題解決や複雑な文書作成など、かなりのレベルの推論を必要とする作業の場合、言語モデルが問題を段階的に分けて考えるよう誘導すると性能を大きく向上させることができます。ただしこの場合、応答遅延時間が長くなる可能性があり、すべての作業に対して常にこのような技法が有用なわけではないので注意が必要です。

#### プロンプトチェーニング（prompt chaining）技法
複雑な作業を遂行する必要がある場合、単一のプロンプトでは対応に限界がある場合があります。この場合、最初から全体の作業フローを複数のステップに分けて、ステップごとにそれに特化したプロンプトを提示し、前のステップで得た応答を次のステップの入力として伝達する方式を使用することも検討できます。このような技法をプロンプトチェーニング（prompt chaining）と呼びます。

#### 応答の最初の部分を事前に埋めておく
プロンプトを入力する際、応答内容の最初の部分をあらかじめ提示し、その後に続く回答を作成するようにすることで、不要な挨拶などの前置きをスキップさせたり、XML、JSONなどの特定の形式で応答するよう強制することができます。[Claude APIの場合、呼び出し時に`User`メッセージだけでなく`Assistant`メッセージも一緒に提出するとこの技法を使用できます。](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### 怠け防止（12024.10.31. ハロウィンパッチ）
この記事を最初に作成した後、途中で1、2回のプロンプト改善および指示事項の具体化を追加で行いましたが、とにかく4ヶ月間この自動化システムを適用しながら特に大きな問題はありませんでした。

しかし韓国時間で12024.10.31.夕方6時頃から、新しく作成したポストの翻訳作業を依頼した際に、ポストの最初の「TL;DR」部分だけを翻訳した後、翻訳を任意に中断する異常現象が継続的に発生しました。

この問題の予想原因および解決方法については[別途のポスト](/posts/does-ai-hate-to-work-on-halloween)で扱っていますので、そちらの記事を参考にしてください。

### 完成したプロンプト
上記のステップを経たプロンプトデザインの結果物は次のとおりです。

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

## Further Reading
[パート2に続く](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
