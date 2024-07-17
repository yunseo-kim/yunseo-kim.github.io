---
title: Claude 3.5 Sonnet APIでポストを自動翻訳する方法 (1)
description: >-
  最近公開されたClaude 3.5 Sonnetモデルを簡単に紹介し、このブログポストの多言語翻訳作業に適用するためのプロンプトをデザインしたプロセスと完成したプロンプトの結果を共有する。
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## はじめに
最近、ブログポストの多言語翻訳のためにAnthropicのClaude 3.5 Sonnet APIを導入した。ここでは、Claude 3.5 Sonnet APIを選択した理由とプロンプトのデザイン方法、そしてPythonスクリプトを通じたAPI連携と自動化の実装方法について扱う。記事で扱う内容がかなり広範囲にわたるため、1つのポストではなくシリーズになる予定であり、この記事はシリーズの最初の記事である。

## Claude 3.5 Sonnetについて
Claude 3シリーズモデルは、モデルサイズに応じてHaiku、Sonnet、そしてOpusバージョンが提供される。  
![Claude 3モデルティア区分](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> 画像出典: [Anthropic Claude API公式ウェブページ](https://www.anthropic.com/api)

そして韓国時間2024年6月21日、Anthropicは最新の言語モデルである[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)を公開した。Anthropicの発表によると、既存のClaude 3 Sonnetと同じコストと速度でClaude 3 Opusを上回る推論性能を示すとのことで、概して作文と言語推論、多言語理解および翻訳分野で競合モデルであるGPT-4に比べて強みを持つという評価が支配的である。  
![Claude 3.5 Sonnet紹介画像](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet性能ベンチマーク結果](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> 画像出典: [Anthropicホームページ](https://www.anthropic.com/news/claude-3-5-sonnet)

## ポスト翻訳のためにClaude 3.5を導入した理由
あえてClaude 3.5やGPT-4のような言語モデルでなくても、Google翻訳やDeepLのような既存の商用翻訳APIが存在する。それにもかかわらず、翻訳目的でLLMを使用することにした理由は、他の商用翻訳サービスとは異なり、ユーザーがプロンプトデザインを通じてモデルに文章の作成目的や主要テーマなど本文以外にも追加的な文脈情報や要求事項を提供でき、モデルはそれに合わせて文脈を考慮した翻訳を提供できるからである。DeepLやGoogle翻訳も概して優れた翻訳品質を示す傾向があるが、文章のテーマや全体的な文脈をよく把握できない限界のため、日常的な会話ではなく専門的なテーマの長い文章を翻訳するよう要求した場合、相対的に翻訳結果が不自然な場合があった。特にClaudeは前述したように、競合モデルであるGPT-4に比べて作文、言語推論、多言語理解および翻訳分野で相対的により優れているという評価が多いため、このブログに記載する工学関連の文章を複数の言語に翻訳する作業に適していると判断した。

## プロンプトデザイン
### プロンプトデザインの基本原則
言語モデルから目的に合致する満足のいく結果物を得るためには、それに合った適切なプロンプトを提供する必要がある。プロンプトデザインというと何か漠然と感じられるかもしれないが、実際には「何かをうまく要求する方法」という点で、相手が言語モデルであれ人間であれ大きく変わらないので、このような観点からアプローチすれば特に難しくない。5W1Hに従って現状況および要請事項を明確に説明し、必要であれば具体的な例をいくつか添えるのも良い。プロンプトデザインに関する数多くのヒントやテクニックが存在するが、ほとんどは上述の基本原則から派生したものである。

### 役割付与および状況説明（誰が、なぜ）
まず最初にClaude 3.5に*「技術分野専門翻訳者（professional technical translator）」*という役割を付与し、*「主に数学や物理学、データサイエンスに関する記事を寄稿する工学ブロガー」*というユーザーに関する文脈情報を提供した。
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### 大枠での要請事項伝達（何を）
次に、ユーザーから提供されたマークダウン形式の文章を{source_lang}から{target_lang}に形式を維持しながら翻訳するよう要請した。
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Claude API呼び出し時、プロンプトの{source_lang}と{target_lang}の位置には、Pythonスクリプトのf-string機能を通じて翻訳元言語と翻訳先言語変数がそれぞれ入る。
{: .prompt-info }

### 要求事項の具体化および例示（どのように）
前段階までで十分に望む結果を得る場合もあるが、複雑な作業を要求する場合には追加的な説明が必要な場合がある。この場合は以下のような条件を追加した。

#### 提供された原文が出発言語以外の言語を含む場合の処理
韓国語で原文を作成する際、ある概念の定義を初めて紹介したり、いくつかの専門用語を使用する場合に*「中性子減衰（Neutron Attenuation）」*のように括弧内に英語表現を一緒に記載することがしばしばある。このような表現を翻訳する場合、ある時は括弧を残し、またある時は括弧内に記載された英語を省略するなど、翻訳方式が一貫していない問題があったため、以下の文をプロンプトに追加した。
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### 他のポストにリンクする処理
いくつかのポストは他のポストへのリンクを含んでおり、URLのパス部分まで翻訳すべき対象として解釈して変更してしまったため、内部リンクが壊れる問題が頻繁に発生した。該当問題はプロンプトにこの文を追加して解決した。
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### 翻訳結果のみを応答として出力すること
最後に、応答時に他の言葉を付け加えず、翻訳結果のみを出力するよう次の文を提示する。
> The output should only contain the translated text.

### 完成したプロンプト
上記の段階を経たプロンプトデザインの結果物は次の通りである。
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.
