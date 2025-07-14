---
title: "Claude Sonnet 4 APIを使った投稿自動翻訳の方法 (1) - プロンプトデザイン"
description: "マークダウンテキストファイルの多言語翻訳のためのプロンプトをデザインし、Anthropic/Gemini APIキーと作成したプロンプトを適用してPythonで作業を自動化する過程を扱う。この投稿は該当シリーズの最初の記事として、プロンプトデザイン方法と過程を紹介する。"
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1/
---

## はじめに
12024年6月にブログ投稿の多言語翻訳のためにAnthropicのClaude 3.5 Sonnet APIを導入して以来、数回のプロンプトおよび自動化スクリプトの改善、そしてモデルバージョンのアップグレードを経て約1年近い期間にわたって該当翻訳システムを満足に運用している。そこでこのシリーズでは、導入過程でClaude Sonnetモデルを選択し、その後Gemini 2.5 Proを追加導入した理由とプロンプトデザイン方法、そしてPythonスクリプトを通じたAPI連携および自動化実装方法を扱いたい。  
シリーズは2つの記事で構成されており、読んでいるこの記事は該当シリーズの最初の記事である。
- 1編：Claude Sonnet/Gemini 2.5モデル紹介および選定理由、プロンプトエンジニアリング（本文）
- 2編：[APIを活用したPython自動化スクリプト作成および適用](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## About Claude Sonnet
Claudeシリーズモデルは、モデルサイズに応じてHaiku、Sonnet、そしてOpusバージョンが提供される。  
![Claude 3モデルティア区分](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)  
> 画像出典：[Anthropic Claude API公式ウェブページ](https://www.anthropic.com/api)

> （12025.05.29. 追加）  
> 1年前にキャプチャした画像のため、トークン当たりの料金が旧バージョンのClaude 3基準で表示されているが、モデルサイズによるHaiku、Sonnet、Opus区分はまだ有効である。12025年5月末基準でAnthropicが提供する各モデル別価格設定は以下の通りである。
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
> 出典：[Anthropic developer docs](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

そして韓国時間で[人類紀](https://en.wikipedia.org/wiki/Holocene_calendar)12024年6月21日にAnthropicが公開した言語モデル[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)は、既存のClaude 3 Sonnetと同じコストと速度でClaude 3 Opusを上回る推論性能を示し、概して作文と言語推論、多言語理解および翻訳分野で競合モデルであるGPT-4に比べて強みを見せるという評価が支配的である。  
![Claude 3.5 Sonnet紹介画像](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet性能ベンチマーク結果](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)  
> 画像出典：[Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## 投稿翻訳のためにClaude 3.5を導入した理由
あえてClaude 3.5やGPT-4のような言語モデルでなくても、Google翻訳やDeepLのような既存の商用翻訳APIが存在する。それでも翻訳目的でLLMを使用することにした理由は、他の商用翻訳サービスとは異なり、ユーザーがプロンプトデザインを通じてモデルに文章の作成目的や主要テーマなど本文以外にも追加的な文脈情報や要求事項を提供でき、モデルはこれに合わせて文脈を考慮した翻訳を提供できるからである。

DeepLやGoogle翻訳も概して優れた翻訳品質を示す方だが、文章のテーマや全体的な文脈をよく把握できず、別途複雑な要求事項を伝えることはできないという限界のため、日常的な会話ではない専門的なテーマの長い文章を翻訳するよう要求した時は、相対的に翻訳結果物が不自然な場合があり、必要とする特定の形式（マークダウン、YAML frontmatterなど）に正確に合わせて出力することが困難だという問題がある。

特にClaudeは前述したように競合モデルであるGPT-4に比べて作文、言語推論、多言語理解および翻訳分野では相対的により優れているという評価が多く、直接簡単にテストしてみた時もGPT-4よりもう少し滑らかな翻訳品質を示したため、導入を検討していた12024年6月当時、このブログに記載する工学関連記事を複数の言語に翻訳する作業に適していると判断した。

## アップデート履歴
### 12024.07.01.
[別の記事](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/)で整理したように、[Polyglotプラグインを適用し、それに合わせて`_config.yml`{: .filepath}とhtmlヘッダー、sitemapを修正する初期作業を完了した。](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7)続いて[Claude 3.5 Sonnetモデルを翻訳目的で採択し、このシリーズで扱っているAPI連携Pythonスクリプトの初期実装および検証を終えた後に適用した。](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
12024年10月22日、AnthropicがClaude 3.5 SonnetのアップグレードバージョンAPI（"claude-3-5-sonnet-20241022"）とClaude 3.5 Haikuを発表した。ただし[後述する問題](#怠け防止120241031-ハロウィンパッチ)により、まだ本ブログには既存の"claude-3-5-sonnet-20240620" APIを適用している。

### 12025.04.02.
[適用モデルを"claude-3-5-sonnet-20240620"から"claude-3-7-sonnet-20250219"に転換した。](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[適用モデルを"claude-3-7-sonnet-20250219"から"claude-sonnet-4-20250514"に転換した。](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Claude 4性能ベンチマーク結果](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)  
> 画像出典：[Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

使用条件によって差があるかもしれないが、概してClaude 3.7 Sonnetモデルが出て以来、コーディングにおいてはClaudeが最も強力なモデルだということに異論があまりない雰囲気である。AnthropicもOpenAIやGoogleなどの競合モデルに比べて優秀なコーディング性能を自社モデルの主要強みとして積極的に打ち出している状況である。今回のClaude Opus 4とClaude Sonnet 4発表でもコーディング性能を強調し、開発者を主要顧客層として狙う基調を続けていることが確認できる。

もちろん公開したベンチマーク結果を見ると、コーディング以外の項目でも全般的に改善が行われており、この記事で扱う翻訳作業の場合には多言語質疑応答（MMMLU）や数学問題解決（AIME 2025）部門の性能向上が特に有効に作用すると思われる。直接簡単にテストした結果、以前のモデルであるClaude 3.7 Sonnetに比べてClaude Sonnet 4の翻訳結果物が表現の自然さや専門性、用語使用の一貫性などでより優れていることを確認できた。

> 現時点で、少なくともこのブログで扱うような技術的な性格の韓国語で書かれた文章を多言語に翻訳する作業では、Claudeモデルが依然として最も優れていると思う。ただし最近GoogleのGeminiモデルの性能が目に見えて良くなっており、今年5月に入ってはまだPreview段階ではあるがGemini 2.5モデルまで公開した状況である。  
> Gemini 2.0 FlashモデルとClaude 3.7 Sonnet、Claude Sonnet 4モデルを比較した時はClaudeの翻訳性能がより優秀だと判断したが、Geminiの多言語性能もかなり優秀な方である上、Preview段階にもかかわらずGemini 2.5 Preview 05-06の数学、物理問題解決および記述能力はむしろClaude Opus 4よりも優れている状況なので、該当モデルが正式公開されて再び比較してみればどうなるかは断言できない。  
> 一定使用量までは[無料等級（Free Tier）](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits)として使用可能である上、有料等級（Paid Tier）基準でもClaude比較で安価なAPI料金を考慮すると、Gemini側の価格競争力が圧倒的であるため、ある程度対等な性能さえ出ればGeminiが合理的な代案になり得る。Gemini 2.5はまだPreview段階であるため、実際の自動化に適用するには早いと判断して当面は考慮していないが、今後正式バージョンが公開されればテストしてみる計画である。
{: .prompt-tip }

### 12025.07.04.
- [増分翻訳機能追加](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/978032f52c7d85ecb6b213233d5404d844402965)
- 翻訳到着言語による適用モデル二元化（[Commit 3890c82](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3890c820c1f3df34f8e4686b8903ca4ee770ba15)、[Commit fe0fc63](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/fe0fc63ae4e2764f3dfe24ff259b4477f120b9ed)）
  - 英語、台湾中国語、ドイツ語への翻訳時"gemini-2.5-pro"使用
  - 日本語、スペイン語、ポルトガル語、フランス語への翻訳時既存の"claude-sonnet-4-20250514"を継続使用
- `temperature`値を`0.0`から`0.2`に上向き調整する案を検討したが、元通りロールバック

12025年7月4日、ついにGemini 2.5 ProおよびGemini 2.5 FlashモデルがPreview段階を脱して正式公開された。使用した例文数が限定的ではあるが、個人的にテストしてみると英文翻訳基準ではGemini 2.5 Flashだけでも既存のClaude Sonnet 4よりもより自然に処理する部分もかなりあった。Gemini 2.5 ProとFlashモデルの出力トークン当たり料金が有料等級基準でもClaude Sonnet 4よりもそれぞれ1.5倍、6倍安いという点を考慮すると、英文基準では事実上12025年7月現時点で最も競争力のあるモデルだと言える。ただしGemini 2.5 Flashモデルの場合、小型モデルの限界なのか出力結果物が概して優れてはいるが、一部マークダウン文書形式や内部リンクが壊れるなどの問題があって複雑な文書翻訳および加工作業には適していなかった。また英文に対してはGemini 2.5 Proが確実に優れた性能を示すが、**大部分のポルトガル語（pt-BR）投稿**、そして一部のスペイン語投稿に対する処理は学習されたデータの量が不足しているのか困難を示した。発生したエラーを見ると、大部分が'í'と'i'、'ó'と'o'、'ç'と'c'、そして'ã'と'a'など似た文字を混同して発生した問題だった。またフランス語に対しては前述したような問題はなかったが、しばしば文章が過度に冗長でClaude Sonnet 4に比べて可読性が落ちる場合があった。

私は英語以外の言語はよく分からないので詳細で正確な比較は困難だが、概略的な言語別応答品質を比較してみると以下の通りだった。
- 英語、ドイツ語、台湾中国語：Geminiが優秀
- 日本語、フランス語、スペイン語、ポルトガル語：Claudeが優秀

また投稿翻訳スクリプトに増分翻訳（Incremental Translation）機能を追加した。文章を最初に作成する時に細かく検討しようと努力するが、それでも文章を上げてから後になって誤字脱字など些細なエラーを発見したり、あるいは追加/修正すれば良い内容が思い浮かぶ時がある。ところがこのような場合に全体文章中修正した分量は限定的にもかかわらず、既存のスクリプトは全体文章を最初から最後まで再び翻訳して出力しなければならず、API使用量の面でやや非効率的な問題があった。そこでgitと連動して韓国語原文のバージョン比較を実行し、原文の変更された部分をdiff形式で抽出して変更以前の翻訳文全文と共にプロンプトに入力した後、翻訳文に対するdiffパッチを出力として受けて必要な部分だけ選択的に修正する機能を追加した。入力トークン当たり料金が出力トークン当たり料金より大幅に安いため、有意味なコスト削減効果を期待でき、したがって今後は文章を一部分だけ修正した場合にも各言語別翻訳文を直接修正せず、負担なく自動翻訳スクリプトを適用できるだろう。

一方、`temperature`とは言語モデルが応答を出力する過程で各単語に対してその次に来る単語を選択する時、どの程度の無作為性を付与するかを調整するパラメータである。非負の実数（\*後述するが通常$[0,1]$ないし$[0,2]$の範囲）の値を持つが、0に近い小さい値ほどより決定論的で一貫した応答を生成し、値が大きくなるほどより多様で創造的な応答を生成する。  
翻訳の目的は原文の意味、語調を他の言語に最大限正確で一貫して伝えることであり、創造的に新しい内容を作り出すことではないので、翻訳の正確性、一貫性、そして予測可能性を確保するためには低い`temperature`値を使用すべきである。ただし`temperature`を`0.0`に設定すると、モデルが常に最も確率の高い単語だけを選択するようになるが、場合によっては翻訳を過度に直訳に近くしたり、不自然で硬い文章を生成する可能性があって応答が過度に硬直するのを防ぎ、ある程度は柔軟性を付与するために`temperature`値を`0.2`に若干上向き調整する案を検討したが、部分識別子（Fragment identifier）を含む複雑なリンクに対する処理精度が急減する問題があって適用しないことにした。

> \* 大部分の場合実用的に使用される`temperature`値は0以上1以下の範囲であり、Anthropic APIでの許容範囲も$[0,1]$である。OpenAI APIやGemini APIではより広い$[0,2]$の`temperature`値を許容するが、`temperature`範囲が$[0,2]$に拡張されたからといってスケールも2倍になるわけではなく、$T=1$の意味は$[0,1]$範囲を使うモデルと同じである。
>
> 言語モデルが出力を生成する時、内部的にはプロンプトおよび以前までの出力トークンを入力として受けて次に来るトークンの確率分布を応答として出す一種の関数として動作し、その確率分布による試行の結果が次のトークンとして決定されて出力される。該当確率分布をそのまま使用する基準値が$T=1$で、$T<1$の場合には確率分布を狭く尖らせて最も確率の高い単語中心により一貫した選択をするようになる一方、$T>1$の場合は反対に確率分布を平坦化して出る確率が低い、本来ならほとんど選択しない単語の選択確率を人為的に引き上げる方式で動作する。
>
> $T>1$領域では応答に文脈を外れたトークンが含まれたり、意味をなさない文法的に間違った文章を生成するなど出力品質が低下し予測不可能になる可能性がある。大部分の作業、特に現業（production）環境では$[0,1]$範囲内で`temperature`値を設定するのが良く、1より大きい値はブレインストーミング、創作補助（シナリオ草案生成など）のような目的で多彩な出力を望む時に実験的に使用するが、幻覚（hallucination）や文法的、論理的エラーのリスクも高くなるので自動化よりは人間の介入と検収を前提とするのが望ましい。
>
> 言語モデルの`temperature`に関するより詳しい内容は以下の記事を参考すると良い。
> - [Tamanna, *Understanding LLM Temperature* (2025).](https://medium.com/@tam.tamanna18/understanding-llm-temperature-7d838277a7d9)
> - [Tickr Data, *The Impact of Temperature on LLM Performance* (2023).](https://www.tickr.com/blog/posts/impact-of-temperature-on-llms/)
> - [Anik Das, *Temperature in Prompt Engineering* (2025).](https://peerlist.io/anikdas/articles/temperature-in-prompt-engineering)
> - [Peeperkorn et al., *Is Temperature the Creativity Parameter of LLMs?*, arXiv:2405.00492 (2024).](https://arxiv.org/abs/2405.00492)
> - [Colt Steele, *Understanding OpenAI's Temperature Parameter* (2023).](https://www.coltsteele.com/tips/understanding-openai-s-temperature-parameter)
> - [Damon Garn, *Understanding the role of temperature settings in AI output*, TechTarget (2025).](https://www.techtarget.com/searchenterpriseai/tip/Understanding-the-role-of-temperature-settings-in-AI-output)
{: .prompt-info }

## プロンプトデザイン
### 何かを要求する時の基本原則
言語モデルから目的に合致する満足のいく結果物を得るためには、それに合った適切なプロンプトを提供しなければならない。プロンプトデザインというと何か途方もなく感じられるかもしれないが、実際「何かをうまく要求する方法」というのは相手が言語モデルであれ人間であれ大きく変わらないので、このような観点からアプローチすればそれほど難しくない。六何原則に従って現状況および要求事項を明確に説明し、必要であればいくつかの具体的な例を付け加えるのも良い。プロンプトデザインに関する数多くのティップスと技法が存在するが、大部分は後述する基本原則から派生するものである。

#### 全体的な語調
高圧的な命令調よりは丁寧に要求する語調でプロンプトを作成して入力した時、言語モデルがより高い品質の応答を出力するという報告が多くある。普通社会で他の人に何かを要求する時も高圧的に命令するよりは丁寧に要求した時、相手がより誠意を持って頼まれた作業を実行する確率が高くなるが、言語モデルもこのような人々の応答パターンを学習して模倣するものと思われる。

#### 役割付与および状況説明（誰が、なぜ）
まず最初に*「技術分野専門翻訳家（professional technical translator）」*という役割を付与し、*「主に数学や物理学、データサイエンスに関する記事を寄稿する工学ブロガー」*というユーザーに関する文脈情報を提供した。

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### 大きな枠での要求事項伝達（何を）
次に、ユーザーから提供されたマークダウン形式の文章を{source_lang}から{target_lang}に形式を維持しながら翻訳するよう要求した。

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> Claude API呼び出し時、プロンプトの{source_lang}と{target_lang}の場所にはPythonスクリプトのf-string機能を通じて翻訳出発言語と到着言語変数がそれぞれ入る。
{: .prompt-info }

#### 要求事項具体化および例示（どのように）
簡単な作業であれば前段階までだけでも十分に望む結果を得る場合もあるが、複雑な作業を要求する場合には追加的な説明が必要な場合がある。

要求条件が複雑で複数ある場合、それぞれの事項を展開して叙述するよりも頭括式にリスト化して伝えれば可読性が向上し、読む立場（人間であれ言語モデルであれ）で理解しやすい。また必要であれば例示も一緒に提供するのが助けになる。
この場合には以下のような条件を追加した。

##### YAML front matterの処理
JekyllブログにアップロードするためにMarkdownで作成した投稿の最初の部分に位置するYAML front matterには'title'と'description'、'categories'、そして'tags'情報を記録する。例えば、今この記事のYAML front matterは以下の通りである。

```yaml
---
title: "Claude Sonnet 4 APIを使った投稿自動翻訳の方法 (1) - プロンプトデザイン"
description: "マークダウンテキストファイルの多言語翻訳のためのプロンプトをデザインし、Anthropic/Gemini APIキーと作成したプロンプトを適用してPythonで作業を自動化する過程を扱う。この投稿は該当シリーズの最初の記事として、プロンプトデザイン方法と過程を紹介する。"
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

ところが投稿を翻訳する時、タイトル（title）と説明（description）タグは多言語に翻訳すべきだが、投稿URLの一貫性のためにはカテゴリ（categories）とタグ（tags）名は翻訳せず英文のまま置いておくのが維持管理に有利である。したがって以下のような指示を下して'title'と'description'以外のタグは翻訳しないようにした。モデルがYAML front matterに関する情報は既に学習して知っているだろうから、この程度だけ説明しても大部分の場合十分である。

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> "under any circumstances, regardless of the language you are translating to"という文句を付け加えて**例外なく**YAML front matterの他のタグは勝手に修正しないよう強調した。
{: .prompt-tip }

（12025.04.02. アップデート）  
また、descriptionタグの内容はSEOを考慮して適切な分量で作成するよう以下のように指示した。

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### 提供された原文が出発言語でない他の言語を含む場合の処理
韓国語で原文を作成する時、ある概念の定義を初めて紹介したり、いくつかの専門用語を使用する場合「*中性子減衰（Neutron Attenuation）*」のように括弧内に英文表現を一緒に記載する場合がしばしばある。このような表現を翻訳する場合、ある時は括弧を活かし、またある時は括弧内に記載された英文を漏らすなど翻訳方式が一貫していない問題があって、以下のような細部指針を定めた。
- 専門用語の場合、
  - 日本語のようにローマ字ベースでない言語に翻訳する時は「翻訳表現（英語表現）」の形式を維持する。
  - スペイン語、ポルトガル語、フランス語のようなローマ字ベースの言語に翻訳する時には「翻訳表現」単独表記と「翻訳表現（英語表現）」併行表記を両方許容し、モデルが二つのうちより適切なものを自律的に選択するようにする。
- 固有名詞の場合、いかなる形態であれ原文のスペルが翻訳結果物にも保存されなければならない。

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

##### 他の投稿に接続されるリンクの処理
いくつかの投稿は他の投稿に接続されるリンクを含むが、テスト段階でこれに関する指針を別途提示しなかった時、URLのパス部分まで翻訳すべき対象として解釈して変えてしまい、内部リンクが壊れる問題がしばしば発生した。該当問題はプロンプトにこの句を追加して解決した。

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

（12025.04.06. アップデート）  
上記の指針を提供すれば翻訳時リンクのパス部分を正しく処理するようになってリンクが壊れる頻度がかなり減るが、部分識別子（Fragment identifier）を含むリンクの場合、リンクが掛けられた対象記事の内容を知らない以上、部分識別子部分は依然として言語モデルが大体推測して埋めなければならない限界があって根本的な問題解決は不可能だった。そこでリンクで接続された他の投稿に対する文脈情報をユーザープロンプトの`<reference_context>` XMLタグ内に込めて一緒に提供し、該当文脈に合わせてリンク翻訳を処理するようPythonスクリプトおよびプロンプトを改善した。該当アップデートを適用した結果、リンク破損問題を大部分予防でき、密接に接続されたシリーズ記事の場合には複数の投稿にわたってより一貫した翻訳を提供する効果も期待できるようになった。

システムプロンプトに以下の指針を提示する。
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

そしてユーザープロンプトの`<reference_context>`部分は以下のような形式と内容で構成され、翻訳しようとする本文の内容の後に追加的に提供される。
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

> これを具体的にどのように実装したかは、このシリーズの[2編](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)とGitHubリポジトリにある[Pythonスクリプト](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py)の内容を参考されたい。
{: .prompt-tip }

##### 翻訳結果物のみを応答として出力すること
最後に、応答時他の言葉を付け加えず、ただ翻訳結果物のみを出力するよう以下の文章を提示する。

```xml
<important>In any case, without exception, the output should contain only the translation results, \
without any text such as "Here is the translation of the text provided, preserving the markdown format:" \
or "```markdown" or something of that nature!!</important>
```

### 追加的なプロンプトデザイン技法
ただし、人間に作業を要求する時とは異なり、言語モデルの場合に特別に適用される追加的な技法も存在する。
これに関してはウェブ上に複数の有用な資料が多いが、汎用的に有用に活用できるいくつかの代表的なティップスを整理してみると以下の通りである。  
[Anthropic公式文書のプロンプトエンジニアリングガイド](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)を主に参考した。

#### XMLタグを活用した構造化
実際これは今まで前で既に使用してきていた。複数の文脈と指示事項、形式、例示を含む複雑なプロンプトの場合、`<instructions>`、`<example>`、`<format>`などのXMLタグを適切に活用すれば言語モデルがプロンプトを正確に解釈し、意図に符合する高い品質の出力を出すのに役立つ。[GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHubリポジトリにプロンプト作成時有用なXMLタグがよく整理されているので参考することを推奨する。

#### 段階別推論（CoT、Chain-of-Thought）技法
数学問題解決や複雑な文書作成のようにかなりのレベルの推論を必要とする作業の場合、言語モデルが問題を段階別に分けて考えるよう誘導すれば性能を大きく引き上げることができる。ただしこの場合応答遅延時間が長くなる可能性があり、すべての作業に対して常にこのような技法が有用なわけではないので注意する。

#### プロンプトチェーニング（prompt chaining）技法
複雑な作業を実行しなければならない場合、単一プロンプトでは対応に限界がある場合がある。この場合最初から全体作業フローを複数段階に分けて段階別にそれに特化したプロンプトを提示し、前段階で得た応答をその次段階の入力として伝達する方式を使用することも考慮できる。このような技法をプロンプトチェーニング（prompt chaining）という。

#### 応答最初部分を予め埋めておく
プロンプトを入力する時、応答する内容の最初部分を予め提示し、その後に続く答弁を作成するようにすることで不要な挨拶などの前置きを飛ばしたり、XML、JSONのような特定形式で応答するよう強制できる。[Anthropic APIの場合、呼び出し時に`User`メッセージだけでなく`Assistant`メッセージを一緒に提出すればこの技法を使用できる。](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### 怠け防止（12024.10.31. ハロウィンパッチ）
この記事を最初に作成した後、中間に一、二回程度若干のプロンプト改善および指示事項具体化を追加で経たが、とにかく4ヶ月間本自動化システムを適用しながら別段大きな問題はなかった。

ところが韓国時間で12024.10.31. 夕方6時頃から、新しく作成した投稿の翻訳作業を任せた時、投稿の最初の'TL;DR'部分だけを翻訳した後、翻訳を任意に中断する異常現象が持続発生した。

該当問題の予想原因および解決方法について[別の投稿](/posts/does-ai-hate-to-work-on-halloween)で扱ったので、該当記事を参考されたい。

### 完成したシステムプロンプト
上記の段階を経たプロンプトデザイン結果物は[次編](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)で確認できる。

## Further Reading
Continued in [Part 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
