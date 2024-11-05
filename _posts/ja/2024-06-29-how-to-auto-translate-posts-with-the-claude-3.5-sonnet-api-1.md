---
title: Claude 3.5 Sonnet APIで投稿を自動翻訳する方法 (1) - プロンプトデザイン
description: >-
  本ブログ投稿の多言語翻訳作業に適用するためにプロンプトをデザインし、Anthropicから発行されたAPIキーと作成したプロンプトを適用してPythonで作業を自動化するプロセスを扱う。この投稿はシリーズの最初の記事で、プロンプトデザインの方法とプロセスを紹介する。
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## はじめに
最近、ブログ投稿の多言語翻訳のためにAnthropic社のClaude 3.5 Sonnet APIを導入した。このシリーズでは、導入過程でClaude 3.5 Sonnet APIを選択した理由とプロンプトデザインの方法、そしてPythonスクリプトを通じたAPI連携と自動化の実装方法を扱う。  
シリーズは2つの記事で構成されており、現在読んでいるこの記事はそのシリーズの第1回目である。
- 第1回：Claude 3.5 Sonnetモデルの紹介と選定理由、プロンプトエンジニアリング（本文）
- 第2回：[APIを活用したPython自動化スクリプトの作成と適用](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## About Claude 3.5 Sonnet
Claude 3シリーズモデルは、モデルサイズによってHaiku、Sonnet、そしてOpusバージョンが提供される。  
![Claude 3モデルティア区分](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> 画像出典：[Anthropic Claude API公式ウェブページ](https://www.anthropic.com/api)

そして日本時間2024年6月21日、Anthropicが最新言語モデルである[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)を公開した。Anthropicの発表によると、既存のClaude 3 Sonnetと同じコストと速度でClaude 3 Opusを上回る推論性能を示すとのことで、全般的に作文と言語推論、多言語理解および翻訳分野において競合モデルであるGPT-4に比べて優位性を示すという評価が支配的である。  
![Claude 3.5 Sonnet紹介画像](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet性能ベンチマーク結果](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> 画像出典：[Anthropicホームページ](https://www.anthropic.com/news/claude-3-5-sonnet)

（2024.10.31.追加）2024年10月22日、AnthropicはClaude 3.5 Sonnetのアップグレード版API（"claude-3-5-sonnet-20241022"）とClaude 3.5 Haikuを発表した。ただし、[後述する問題](#怠け者防止20241031ハロウィンパッチ)により、現在本ブログでは既存の"claude-3-5-sonnet-20240620" APIを適用している。

## 投稿翻訳のためにClaude 3.5を導入した理由
あえてClaude 3.5やGPT-4のような言語モデルでなくても、Google翻訳やDeepLなどの既存の商用翻訳APIが存在する。それにもかかわらず翻訳目的でLLMを使用することにした理由は、他の商用翻訳サービスとは異なり、ユーザーがプロンプトデザインを通じてモデルに文章の作成目的や主要テーマなど本文以外にも追加的な文脈情報や要求事項を提供でき、モデルはそれに合わせて文脈を考慮した翻訳を提供できるためである。DeepLやGoogle翻訳も概ね優れた翻訳品質を示す傾向にあるが、文章のテーマや全体的な文脈をよく把握できないという限界のため、日常的な会話ではなく専門的なテーマの長い文章を翻訳するよう要請した場合は、相対的に翻訳結果が不自然な場合があった。特にClaudeは前述したように競合モデルであるGPT-4に比べて作文、言語推論、多言語理解および翻訳分野では相対的により優れているという評価が多く、実際に簡単にテストしてみた時もGPT-4よりもより滑らかな翻訳品質を示したため、このブログに記載する工学関連の文章を様々な言語に翻訳する作業に適していると判断した。

## プロンプトデザイン
### 何かを要請する際の基本原則
言語モデルから目的に合う満足のいく結果物を得るためには、それに合った適切なプロンプトを提供する必要がある。プロンプトデザインというと何か漠然と感じられるかもしれないが、実際には「何かをうまく要請する方法」という点で、相手が言語モデルであれ人間であれ大きく変わらないため、このような観点からアプローチすれば特に難しくない。5W1Hに従って現状況および要請事項を明確に説明し、必要であれば具体的な例をいくつか添えるのも良い。プロンプトデザインに関する数多くのヒントと技法が存在するが、ほとんどは後述する基本原則から派生するものである。

#### 全体的なトーン
高圧的な命令調よりも丁寧に要請する調子でプロンプトを作成して入力した時、言語モデルがより高品質の応答を出力するという報告が多くある。通常、社会で他人に何かを要請する時も前者よりは後者のような話し方で要請した時の方が、相手がより誠意を持って依頼された作業を遂行する確率が高くなるが、言語モデルもこのような人々の応答パターンを学習して模倣しているものと思われる。

#### 役割付与および状況説明（誰が、なぜ）
まず最初にClaude 3.5に*「技術分野専門翻訳者（professional technical translator）」*という役割を付与し、*「主に数学や物理学、データサイエンスに関する記事を寄稿する工学ブロガー」*というユーザーに関する文脈情報を提供した。

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### 大枠での要請事項伝達（何を）
次に、ユーザーから提供されたマークダウン形式の文章を{source_lang}から{target_lang}に形式を維持しながら翻訳するよう要請した。

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Claude API呼び出し時、プロンプトの{source_lang}と{target_lang}の位置には、Pythonスクリプトのf-string機能を通じて翻訳元言語と翻訳先言語変数がそれぞれ入る。
{: .prompt-info }

#### 要求事項の具体化および例示（どのように）
簡単な作業であれば前段階までで十分に望む結果を得られる場合もあるが、複雑な作業を要求する場合には追加的な説明が必要な場合がある。

要求条件が複雑で多岐にわたる場合、それぞれの事項を詳しく説明するよりも、要点を箇条書きにして伝えると可読性が向上し、読む立場（人間であれ言語モデルであれ）で理解しやすい。また必要であれば例も一緒に提供すると役立つ。
この場合は以下のような条件を追加した。

##### YAML front matterの処理
Jekyll ブログにアップロードするためにmarkdownで作成した投稿の冒頭に位置するYAML front matterには「title」と「description」、「categories」、そして「tags」情報を記録する。例えば、この記事のYAML front matterは以下の通りである。

```yaml
---
title: Claude 3.5 Sonnet APIで投稿を自動翻訳する方法
description: \>-
  最近公開されたClaude 3.5 Sonnetモデルを簡単に紹介し、本ブログ投稿の多言語翻訳作業に適用するためにプロンプトをデザインしたプロセスと完成したプロンプト結果物を共有する。
  そしてAnthropicから発行されたAPIキーと先に作成したプロンプトを適用してPythonで翻訳自動化スクリプトを作成し活用する方法を紹介する。
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

しかし投稿を翻訳する際、タイトル（title）と説明（description）タグは多言語に翻訳する必要があるが、投稿URLの一貫性のためにはカテゴリー（categories）とタグ（tags）名は翻訳せずに英文のまま残しておく方が維持管理に有利である。したがって以下のような指示を出して「title」と「description」以外のタグは翻訳しないようにした。Claudeは YAML front matterに関する情報をすでに学習して知っているはずなので、この程度の説明でほとんどの場合十分である。

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> "under any circumstances, regardless of the language you are translating to"という文句を添えて、**例外なく**YAML front matterの他のタグは勝手に修正しないよう強調した。
{: .prompt-tip }

##### 提供された原文が出発言語以外の言語を含む場合の処理
韓国語で原文を作成する際、ある概念の定義を初めて紹介したり、いくつかの専門用語を使用する場合に*「中性子減衰（Neutron Attenuation）」*のように括弧内に英語表現を一緒に記載する場合がしばしばある。このような表現を翻訳する場合、時には括弧を生かし、また時には括弧内に記載された英文を省略するなど翻訳方式が一貫していない問題があり、以下のような詳細指針を定めた。
- 専門用語の場合、
  - 日本語のようにローマ字ベースでない言語に翻訳する時は「翻訳表現（英語表現）」の形式を維持する。
  - スペイン語、ポルトガル語、フランス語のようなローマ字ベースの言語に翻訳する時は「翻訳表現」単独表記と「翻訳表現（英語表現）」併記表記の両方を許容し、Claudeが二つのうちより適切なものを自律的に選択するようにする。
- 固有名詞の場合、何らかの形で原文の綴りが翻訳結果物にも保存されなければならない。

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

##### 他の投稿へのリンクの処理
いくつかの投稿は他の投稿へのリンクを含むが、テスト段階でこれに関する指針を別途提示しなかった時、URLのパス部分まで翻訳すべき対象として解釈して変更してしまい、内部リンクが壊れる問題が頻繁に発生した。該当問題はプロンプトにこの文句を追加して解決した。

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### 翻訳結果物のみを応答として出力すること
最後に、応答時に他の言葉を添えず、翻訳結果物のみを出力するよう以下の文章を提示する。

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### 追加的なプロンプトデザイン技法
ただし、人間に作業を要請する時とは異なり、言語モデルの場合に特別に適用される追加的な技法も存在する。
これに関してはウェブ上に様々な有用な資料が多いが、汎用的に有用に活用できる代表的なヒントをいくつかまとめると以下のようになる。  
[Anthropic公式文書のプロンプトエンジニアリングガイド](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)を主に参考にした。

#### XMLタグを活用して構造化
実はこれは今まで前から既に使用してきた。様々な文脈と指示事項、形式、例を含む複雑なプロンプトの場合、`<instructions>`、`<example>`、`<format>`などのXMLタグを適切に活用すると、言語モデルがプロンプトを正確に解釈し、高品質の意図に合った出力を提供するのに大きな助けとなる。[GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHubリポジトリにプロンプト作成時に有用なXMLタグがよく整理されているので参考にすることをお勧めする。

#### 段階別推論（CoT、chain of thinking）技法
数学問題解決や複雑な文書作成のように相当なレベルの推論を必要とする作業の場合、言語モデルが問題を段階別に分けて考えるよう誘導すると性能を大きく引き上げることができる。ただしこの場合、応答遅延時間が長くなる可能性があり、すべての作業に対して常にこのような技法が有用なわけではないので注意する。

#### プロンプトチェーニング（prompt chaining）技法
複雑な作業を遂行する必要がある場合、単一プロンプトでは対応に限界がある可能性がある。この場合、最初から全体作業の流れを複数の段階に分けて段階別にそれに特化したプロンプトを提示し、前段階で得た応答を次の段階の入力として伝達する方式を使用することも考慮できる。このような技法をプロンプトチェーニング（prompt chaining）という。

#### 応答の最初の部分を事前に埋めておく
プロンプトを入力する際、応答内容の最初の部分を事前に提示してその後に続く回答を作成するようにすることで、不要な挨拶などの前置きを飛ばしたり、XML、JSONなどの特定の形式で応答するよう強制することができる。[Claude APIの場合、呼び出し時に`User`メッセージだけでなく`Assistant`メッセージも一緒に提出するとこの技法を使用できる。](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### 怠け者防止（2024.10.31.ハロウィンパッチ）
この記事を最初に作成して以来、途中で1、2回のプロンプトの改善および指示事項の具体化を追加で行ったが、とにかく4ヶ月間本自動化システムを適用しながら特に大きな問題はなかった。

ところが日本時間2024.10.31.午後6時頃から、新しく作成した投稿の翻訳作業を依頼した時に投稿の最初の「TL;DR」部分のみを翻訳した後、翻訳を任意に中断する異常現象が継続発生した。

該当問題の予想原因および解決方法について[別途の投稿](/posts/does-ai-hate-to-work-on-halloween)で扱ったので、該当記事を参考にしていただきたい。

### 完成したプロンプト
上記の段階を経たプロンプトデザインの結果物は以下の通りである。

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
[第2回](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)に続く
