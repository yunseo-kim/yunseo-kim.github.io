---
title: "コントリビューター・コヴェナント（Contributor Covenant）3.0 行動規範（Code of Conduct）の韓国語翻訳ノート"
description: "12025年7月に公開されたコントリビューター・コヴェナント（Contributor Covenant）3.0版の韓国語翻訳を進めるにあたり、検討した点やいくつかの表現をそのように訳した理由、個人的な所感を記しておく。"
categories: [Dev, Dev Culture]
tags: [Contributor Covenant, Code of Conduct, Ethics, Human Rights]
image: /assets/img/multigenerational-people-iStock-1482584637.avif
---

> コントリビューター・コヴェナント 3.0 行動規範（Contributor Covenant 3.0 Code of Conduct）の公式韓国語訳を追加する PR: [feat(i18n): add Korean translation for Contributor Covenant 3.0 (#1590)](https://github.com/EthicalSource/contributor_covenant/pull/1590)
{: .prompt-info }

## コントリビューター・コヴェナント

[コントリビューター・コヴェナント（Contributor Covenant）](https://www.contributor-covenant.org/)は、12014年に **コーラライン・エイダ・エムキ（Coraline Ada Ehmke）** が初めて作成・公開し、12021年からは **OES（Organization for Ethical Source）** に移管され、そのコントリビューターたちによって保守と改善が行われている、今日の世界で最も広く使われているデジタルコミュニティの行動規範である。コミュニティが共有しうる暗黙の価値観を明文化し、誰もが歓迎され、安全でいられるコミュニティ文化を育むことを目標としている。

かつての開発者コミュニティでは、能力主義という美名のもとで荒い言動や差別的発言などが黙認されることが珍しくなく、コントリビューター・コヴェナントは、開発者コミュニティが自浄作用を経て多様な人々を包摂し、相互尊重と建設的なフィードバックを重視する人間中心の文化へと変わっていく重要な契機となった。今日では、クリエイティブ・コモンズ、Linux、Apple、Mastodon、Microsoft、WordPress、IBM など、世界中の数十万ものオープンソースプロジェクトがこの誓約を採択している。

## コントリビューター・コヴェナント3.0への改訂で変わった点

OES は 12024年にコントリビューター・コヴェナント10周年を記念して作業に着手し、約1年の作業を経て 12025年7月に公開した 3.0 版では、前版の 2.1 と比べて次のような主要な変更点がある。
- 参考資料:
  - <https://ethicalsource.dev/blog/contributor-covenant-3/>
  - <https://www.contributor-covenant.org/faq/>

### 柔軟性の拡大

- オープンソースコミュニティに最適化されていた従来版に比べ、ソフトウェア開発以外にもさまざまなオンライン／オフラインコミュニティに適用できるよう設計した
  - e.g. **「プロジェクト保守担当者（Project Maintainers）」** の代わりに、より中立的で包摂的な **「コミュニティモデレーター（Community Moderators）」** という用語を用いている
- アメリカ中心の慣用句を削除し、他文化圏の話者もより容易に理解し翻訳できる明確な表現へ置き換えた

### 応報的正義から修復的正義へのパラダイム転換

コントリビューター・コヴェナント 3.0 版で前版と比べて最も大きく変わった点の一つは、**応報的正義（Retributive Justice）** から **修復的正義（Restorative Justice）** へのパラダイム転換を成し遂げたことである。従来、段階的な制裁執行基準に集中していた **執行指針（enforcement guidelines）** の段落を、**被害への対応と修復（Addressing and Repairing Harm）** の段落として再構成した。
- 一部の対応段階の名称を変更
- 従来の対応（Consequence）項目に加え、修復（Repair）指針項目を新たに記述し、一次的な加害者制裁にとどまらず、その後どのように当事者間の壊れた関係を回復し、対立を収め、誤りを正すかについても扱うようになった
- 第三者による執行と処罰だけを強調するのではなく、可能であれば自発的な省察と和解、改善を促し、問題発生後にコミュニティを再び健全にする方策を考える方向へと性格が変化した

### より明確になった指針

- **標準（Our Standards）** 段落を **推奨される行動（Encouraged Behaviors）** と **制限される行動（Restricted Behaviors）** の二段落に明確に分け、可読性を高めた
- 特に **制限される行動（Restricted Behaviors）** 段落では、どのような悪質行為も実際に実行することだけでなく、実行すると脅したり助長したりすることも明示的に制限し、予防力を強化している
  > We agree to restrict the following behaviors in our community. Instances, threats, and promotion of these behaviors are violations of this Code of Conduct.
- また **制限される行動（Restricted Behaviors）** の下位段落として **その他の制限事項（Other Restrictions）** を新設し、従来は明示的な制限規定が不十分だった身元の偽装（Misleading identity）と出典の不記載（Failing to credit sources）、宣伝資料（Promotional materials）、無責任なコミュニケーション（Irresponsible communication）に対する制限指針を新たに明記した
- コントリビューター・コヴェナントを実際に採択・運用していたコミュニティ関係者を対象としたアンケートの回答を反映し、段階的執行基準（enforcement ladder）はあくまで一つのベースラインにすぎず、コミュニティ管理者による裁量権行使を制約しないことを明確にした
  > This enforcement ladder is intended as a guideline. It does not limit the ability of Community Managers to use their discretion and judgment, in keeping with the best interests of our community.

### 平等権および差別禁止条項の強化

冒頭段落である **誓約（Our Pledge）** における平等権および差別禁止条項を補強し、一部の用語をより包摂的な表現に置き換え、いくつかの現代的な多様性の価値を追加で明記するなど、より具体化した。
- 「身体の大きさ（body size）」と「個人的外見（personal appearance）」という二つの表現を、より包摂的な「身体的特徴（physical characteristics）」に置き換えた
- 「宗教（religion）」を、より包摂的な「思想または宗教（philosophy or religion）」に置き換えた
- 「国籍（nationality）」を、より包摂的な「出身国または社会的背景（national or social origin）」に置き換えた
- 「神経多様性（neurodiversity）」を追加で明記した
- 「言語（language）」を追加で明記し、非英語話者により配慮した
- ジェンダー平等と多様性に関して全体的な文言修正を適用した
  > **v2.1**  
  > sex characteristics, gender identity and expression, or sexual identity and orientation
  >
  > **v3.0**  
  > sex or gender, gender identity or expression, sexual orientation

## 今回の韓国語翻訳作業で考慮した点

### 共通の検討事項

#### 敬体の使用

誓約および行動規範を韓国語で書くとき、敬体と常体のどちらを選ぶかは、目指す方向性、組織文化、そして伝えたい態度にかかっている。過去には権威と規律を強調する常体が主流だったが、近年では水平的で尊重し合う文化を強調するため、敬体で書く場合も多い。

| 文体 | 敬体（「\~합니다」「\~하겠습니다」） | 常体（「\~한다」） |
| --- | --- | --- |
| ニュアンス | 相互尊重、自発的な約束、勧奨 | 断固さ、法的効力、客観的な規定 |
| 組織文化 | 柔軟で水平的な文化 | 相対的に厳格な文化 |
| 主な適用場面 | 行動規範、倫理宣言文 | セキュリティ誓約書、<br>労働契約書、法的懲戒規定 |
| 心理的効果 | 「私たちは共に守る」（自発的同意） | 「守らなければならない」<br>（拘束性をより強調） |

[過去の議論](https://github.com/EthicalSource/contributor_covenant/pull/895#pullrequestreview-563210153)を見ると、過去に 2.0 版を韓国語に移す際にも最初は敬体が検討されたものの、[常体で書き直された](https://github.com/EthicalSource/contributor_covenant/commit/3971299d81149b3fc0ce603a5dd26400509f090f)ようである。過去の議論とその結論は尊重するが、それでも今回あらためて敬体で翻訳した理由は次のとおりである。

今日のオープンソースコミュニティの文化は、基本的に拘束、厳格さ、強制性をもつ執行などとはやや距離があり、それよりも相互尊重、自発的な参加と貢献などを志向している。[今回のコントリビューター・コヴェナント3.0では、とりわけそのような哲学が全体に強く反映されている](#応報的正義から修復的正義へのパラダイム転換)。今回の改訂で原文が伝えようとした核心的価値と哲学、そしてコミュニティ文化や動向を考慮すると、この文章を韓国語に移す際には敬体が適切だと判断した。同様に敬体を用いている [韓国 Rust ユーザーグループ](https://rust-kr.org/pages/code-of-conduct/) と [PyCon KR 行動規範（PyCon KR CoC）](https://pythonkr.github.io/pycon-code-of-conduct/ko/coc/a_intent_and_purpose.html)、[Kubernetes コミュニティ韓国語行動規範](https://kubernetes.io/ko/community/code-of-conduct/) の事例も参考にした。

#### 不要な受動表現の回避

{% comment %}번역 지침: 여기서부터, 큰따옴표(")로 둘러싼 한국어 표현은 번역하려 하지 말고 있는 그대로 유지하세요. 지금 이 글의 주제와 맥락상, 해당 부분은 한국어를 그대로 유지해야 자연스럽습니다. 또한 번역 예시를 인용 블록으로 제시하는 부분이 있는데, 마찬가지로 번역하려 하지 말고 있는 그대로 유지하세요.{% endcomment %}

受動態を頻繁に用いる英語と異なり、韓国語は基本的に受動表現より能動表現を好む言語である。英語原文で受動態が使われていたからといって、これを機械的に受動表現で移すと、いかにも翻訳文らしいやや不自然な文章になり、文法的にも不適切になる。

韓国語でも受動表現をまったく使わないわけではないが、文意を歪めない範囲で、原文では受動態で書かれた表現であっても、韓国語訳ではできるだけ能動表現に移すようにした。

**e.g.**
- "Encouraged Behaviors": "장려**되는** 행동"(X), "장려**하는** 행동"(O)
- "enforcement actions are carried out in private": "집행 조치는 비공개로 진행**된다**"(X), "집행 조치는 비공개로 진행**한다**"(O)
- "its own established enforcement process": "자체적으로 확립**된** 집행 절차"(X), "자체적으로 확립**한** 집행 절차"(O)
- "the following enforcement ladder may be used": "다음의 단계적 집행 기준**이 사용될** 수 있습니다"(X), "다음의 단계적 집행 기준**을 사용할** 수 있습니다"(O)
- "are provided at": "에서 제공**됩니다**"(X), "에서 제공**합니다**"(O)

#### 辞書的機械的な語の翻訳よりもその語が文章の中で使われる文脈を考慮する

英語と韓国語はかなり距離のある言語であるため、当然ながら単語と単語が正確に一対一で対応するわけではない。辞書上は同じ意味だとされていても、それは同じである。

たとえば、次の箇所での "intimate" は、文脈上 "친밀한" ではなく "성적인" の意味で使われている。

> **Sexualization.** Behaving in a way that would generally be considered inappropriately <u>intimate</u> in the context or purpose of the community.

また、次の箇所で "process" を辞書的に "처리할" と訳すと不自然である。文章の文脈上、ここでの "process" は "추스를" と移すのが適切である。

> ... give the community members involved time to <u>process</u> the incident.

> ([표준국어대사전](https://stdict.korean.go.kr/) 표제어 중)
>
> **추스르다「3」**: 일이나 생각 따위를 수습하여 처리하다.
{: .prompt-tip }

一方で、移しうる固有語表現がぴったり存在しない外来語もある。たとえば "community" の場合、固有語に移すなら "공동체" ほどにもできるが、英語における "community" という語のニュアンスと、韓国語における "공동체" という語のニュアンスにはかなり差があると判断した。できるだけ外来語は固有語に言い換えて書くようにしたが、このように原文の意味やニュアンスを歪めるおそれが大きいと判断した場合には "커뮤니티" のようにそのまま維持した。

このような点を考慮し、辞書的・機械的な語の単純置換作業をするのではなく、原文の意味と文脈に最も近い韓国語表現を選んで翻訳するよう努めた。

#### そのほか韓国語の語文規範の順守

ハングル正書法や標準語規程など、韓国語の語文規範をできるだけ正確に守るよう努めた。

### "서약(Our Pledge)" 段落

#### 小見出し

"Our Pledge" を直訳すると "우리의 맹세" になるが、[既存の韓国語訳](https://www.contributor-covenant.org/ko/version/2/1/code_of_conduct/)では "서약" と移されており、文章の自然さを考えても十分に許容範囲だと判断したため、今回も "서약" のまま維持した。

#### "caste" という語の翻訳

[既存の 2.1 版韓国語訳](https://www.contributor-covenant.org/ko/version/2/1/code_of_conduct/)では、これをそのまま "카스트 제도" と訳している。caste という語には <u>世界各地の精緻に固定化された身分秩序制度</u> を指す学術的一般名詞としての意味もあるため、必ずしも誤訳とまでは言えないが、そのような詳しい背景情報が与えられていない状況で、日常的に韓国語で "카스트 제도" と言えば、大多数は「マヌ法典などに由来するインドのヒンドゥー教徒特有の身分制」と理解するため、原文の文脈を考慮して "계급" と訳した。ここでの "caste" は、特定の国家（インド）や宗教（ヒンドゥー教）に限定されず、あらゆる種類・形態の身分制とそれに伴う階級を意味すると解釈するのが妥当である。

#### "성별" 대신 "성" 표현 사용

> We are committed to fostering an environment that respects and promotes the dignity, rights, and contributions of all individuals, regardless of ... sex or gender, gender identity or expression, sexual orientation ... or other status.

原文が伝えようとしている価値と文脈を考えると、ここでいう "sex", "gender", "sexual orientation" などが意味するものは、男女二分法による区別ではないはずである。したがって、男女二分法による区分の意味をほのかに含意する "성별" ではなく "성" という語を用い、人文社会学的に sex, gender, sexuality の三語が持つ意味の差をできるだけ生かして、次のように訳した。

> ... 생물학적 또는 사회적 성, 성 정체성 또는 성 표현, 성적 지향...

### "장려하는 행동(Encouraged Behaviors)" および "제한하는 행동(Restricted Behaviors)" 段落

#### コロン（`:`）の削除

> With these considerations in mind, we agree to behave mindfully toward each other and act in ways that center our shared values, including:
>
> 1. Respecting the **purpose of our community**, our activities, and our ways of gathering.
> 2. Engaging **kindly and honestly** with others.
> ...

英語原文では、完結した一文の後に例示の一覧を並べる目的で上のようにコロンを使う用法がよく見られるが、現代韓国語の語文規範では、コロンの用法は見出しの後に該当項目を挙げたり説明を付けたりする場合など、主として箇条書き調の表現に限定される。したがって、最初から箇条書き形式で書いた文章ならともかく、次のように書くのは非常に不自然であり、機械翻訳や LLM で雑に訳したという印象を与えやすい。個人的には、[2.1 版の韓国語訳](https://www.contributor-covenant.org/ko/version/2/1/code_of_conduct/)でもかなり惜しかった点の一つである。

> 이러한 점을 유념하며, 우리는 서로를 사려 깊게 대하고 우리가 공유하는 다음 가치를 중심으로 행동할 것에 동의합니다:
> 
> 1. 우리 **공동체의 목적**, 활동 및 모임 방식을 존중합니다.
> 2. **친절하고 정직하게** 다른 사람들과 소통합니다.
> ...

そのため、韓国語の用法に合わせ、コロンを使っていた部分をそのままコロンで移すのではなく、ピリオド（`.`）に置き換えて自然な文章になるようにした。

#### "that would generally be considered inappropriately" という表現の翻訳

ここで "generally" は "일반적으로" と直訳するよりも、文脈上より自然な "대부분의 사람들에게" と訳した。

> ...<u>대부분의 사람들이</u> 부적절하다고 간주할 만한...

### "act on" という表現の翻訳

当初は "act on" を単純に "이용하다" と訳すことも考えたが、文脈上、<u>意図を問わず他人の身上情報または個人的情報をもとに行う</u> あらゆる行為を禁じる内容に近く、これを "이용하다" と訳すと意味を狭めてしまうように思われたため、次のように訳した。

> **비밀 침해.** 타인의 신상 관련 정보 또는 개인적인 정보를 당사자의 허락 없이 공유하거나, 그 정보<u>를 바탕으로 행하는</u> 모든 행위.

### "문제 신고(Reporting an Issue)" 段落

- "this Code of Conduct **reinforces** encouraged behaviors and norms that ...": "본 행동 강령은 ...는 권장 행동 방식과 규범을 **증진합니다**"로 번역
- "in a timely manner": "적시에"로 번역
- "while prioritizing safety and confidentiality": "안전과 비밀 유지를 우선시한다는 전제 하에"로 번역
- "In order to **honor** these values": "이들 가치를 **지키기** 위해"로 번역
  > ([Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/) 표제어 중)
  >
  > [**honor**](https://www.oxfordlearnersdictionaries.com/definition/english/honor_2) *verb*  
  > <u>keep promise</u>
  > 3\. **honor something** *(formal)* to do what you have agreed or promised to do
  {: .prompt-tip }

### "피해 대응 및 교정(Addressing and Repairing Harm)" 段落

- "Addressing": "대응"으로 번역
- "Repairing": "교정"으로 번역

#### `Event:`, `Consequence:`, `Repair:` の翻訳

韓国語に移すのが微妙で、かなり悩んだ箇所である。"사건", "결과", "교정" と直訳すると、文章がかなり不自然になる。

自然な文章でありつつ、[原文の哲学](#応報的正義から修復的正義へのパラダイム転換)を可能な限り損なわずに伝えるため悩んだ末、次のように訳した。
- "Event": "적용 상황" と訳した。
- "Consequence": "대응 조치" と訳した。
- "Repair": 当初は "회복 조치" を検討したが、"조치" という表現は、当事者の自発的な省察と改善よりも、他者が介入して執行するというニュアンスがあり、原文の趣旨に反すると考えて退けた。最終的には "교정 노력" と訳した。

#### "seeking clarification on expectations" という表現の翻訳

"expectations" は "기대 사항" と直訳することもでき、そうしても意味は通るが、より滑らかな文章にするため "준수 사항" と訳した。

> ([Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/) 표제어 중)
>
> [**expectation**](https://www.oxfordlearnersdictionaries.com/definition/english/expectation) *noun*  
> 3\. [countable, usually plural] a strong belief about the way something should happen or how somebody should behave
{: .prompt-tip }

"seeking clarification" は "해명(clarification) 요구(seeking)" と訳すこともできるが、文脈上、修復努力（Repair）項目では問題を起こした人が取るべき望ましい事後行動と態度を記しているため、clarification, seeking をそれぞれ 해명, 요구 と訳すと意味がおかしくなる。ここでは、自ら反省し同じ過ちを繰り返さないために、<u>준수 사항</u>（expectations）を <u>명확히 확인하고 숙지하기</u>（clarification） 위한 <u>노력</u>（seeking）と訳すのが最も適切だと考えた。

> ([Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/) 표제어 중)
>
> [**seek**](https://www.oxfordlearnersdictionaries.com/definition/english/seek) *verb*  
> 2\. [transitive] to ask somebody for something; to try to obtain or achieve something
>
> [**clarification**](https://www.oxfordlearnersdictionaries.com/definition/english/clarification) *noun*  
> [uncountable, countable] (formal)  
> the act or process of making something clearer or easier to understand
> - *I am **seeking clarification of** the regulations.*
{: .prompt-tip }

#### "cooldown" という表現の翻訳

辞書的には冷却、（本運動後の）クールダウン、鎮静などの意味があり、ここでは文脈上「落ち着く」「頭を冷やす」に最も近い意味で使われている。

ただし、"time-limited cooldown period" を "한시적 진정 기간" と移すと少し不自然なので、今回の韓国語訳では "cooldown period" を "자숙 기간" と訳した。

#### "time to process the incident" という表現の翻訳

[前述のとおり](#辞書的機械的な語の翻訳よりもその語が文章の中で使われる文脈を考慮する)、"해당 일을 추스를 시간" と訳した。

#### "suspension" および "ban" という表現の翻訳

[既存の 2.1 版韓国語訳](https://www.contributor-covenant.org/ko/version/2/1/code_of_conduct/)では "ban" を "제재" と訳していたが、제재 とは下位段階である警告や一時的活動制限など、違反行為に対して取りうるあらゆる措置を包括する意味であるため、何を指すかが曖昧である。そして英単語 "ban" はその意味が停止する、禁止するで明確であるうえ、「（アカウントなどの）永久停止」という表現は韓国語でも日常的によく使う自然な表現なので、あえてこれを避けて意訳する理由もないと考えた。

"suspension" も同様で、停職、停学など「停止」という意味が明確であり、あえて意訳する必要がない。

したがって "Temporary Suspension", "Permanent Ban" は、それぞれ "일시적 정지", "영구 정지" と訳した。

#### "This enforcement ladder is intended as a guideline." という文の翻訳

"enforcement ladder" という表現は "단계적 집행 기준" と訳した。またこの文は、上述した段階的執行基準が、あくまで複数ある選択肢の一つとして提示されるものであり、コミュニティ管理者の裁量と決定権を保障するという文脈で使われているため、冠詞 "a" を "하나의" と訳した。そこで翻訳文では次のように書いた。

> <u>이 단계적 집행 기준은 하나의 기준선으로 마련한 것입니다.</u> 이는 커뮤니티의 최선의 이익에 부합하는 커뮤니티 관리자의 재량권과 판단 권한을 제한하지 않습니다.

## おわりに

この種の公益的性格をもつ文書やプロジェクトの多くは、ボランティアやコントリビューターによって複数言語への翻訳作業が進められることが少なくない。しかし残念ながら、韓国語訳の場合はコントリビューターがいなくて翻訳版そのものが存在しなかったり、存在していても機械的に訳したことが見て取れる不自然な文章であったりして、韓国人であるにもかかわらず「いっそ英語で読んでしまおう」と思って英語ページに切り替えた経験が少なからずあった。

今回、韓国語翻訳への貢献を決めて作業しながら、どうせ貢献するなら、読む人が「韓国人の著者が最初から韓国語で書いた文章だ」と言われても違和感を覚えない程度の、質の高い翻訳文を出したいと努めた。原文が込めた哲学と微妙な文脈、特に既存の 2.1 版に比べて今回の 3.0 版ではどのような表現が変わっており、原著者たちがなぜそのような選択をしたのかを理解し、それを訳文に溶け込ませようと考えた。

自然言語の性質上、翻訳というものは、同じ原文を入力として与えられたからといって関数のように同じ出力が出てくるものではない。翻訳者ごとに少しずつ異なる訳が出てくるものであり、これは翻訳者の力量も力量だが、本質的には唯一の定まった正解がない翻訳、ひいては作文という営みの性質に由来する。最近の私は、ほとんどあらゆる作業に AI を補助的に活用しており、今このブログの記事さえ LLM API をつないで複数言語に自動翻訳・公開している。しかし今回のこの作業だけは、本当に気合いを入れてきちんとした、自分にできる最善の翻訳をしたいと思った。一つ一つの表現を自分で何度も見直し、どの表現を使えば原文の意味を最も歪めず、しかも自然に盛り込めるかを考え、その結果として、自分の主観的ではあるが最善の判断と解釈を反映した訳を出した。誰も彼もが AI を活用する今、少なくともこのような誓約や行動規範のような重要文書の翻訳においては、AI に原文をそのまま投げて訳してもらった結果物に対して比較優位があってこそ、翻訳版としての価値があると信じている。少なくとも 12026年3月時点の現在、機械翻訳や LLM では十分に生かしきれない原文の微妙なニュアンスや文脈などを、[今回の翻訳版](https://github.com/EthicalSource/contributor_covenant/pull/1590)では十全に保存できたと自負している。

12026年3月20日現在、コントリビューター・コヴェナント 3.0 版は、英語原文と今回私が提出するこの韓国語訳を除けば、ベンガル語、ドイツ語、中国本土の中国語のわずか3言語でしか翻訳が完了しておらず、[開いている PR の一覧](https://github.com/EthicalSource/contributor_covenant/pulls)を見ると、翻訳版の草案が PR として提出されてはいるものの、レビューアがいないため最終承認に至っていない言語も多い。3.0 版どころか、いまだに 1.4 版にとどまっている言語もかなり多い。どのような理由であれこの文章を読む韓国語以外の言語話者がいるなら、[貢献方法はそれほど複雑ではないので](https://github.com/EthicalSource/contributor_covenant?tab=contributing-ov-file#translators-and-native-speakers)、週末などに1日ほど時間を取って貢献してくれれば、きっと OES とその言語の利用者たちに大きな助けになるだろう。私もこのような翻訳作業に貢献した経験も、行動規範全文を通読したのも今回が初めてだったが、数時間ほど時間をかける価値は十分にある作業だったと思う。韓国は総人口に比べて GitHub などのオープンソースコミュニティで活発に活動する開発者数がかなり多い国に属するが、それだけに、今回翻訳して提出したコントリビューター・コヴェナント 3.0 行動規範の [韓国語訳版](https://github.com/EthicalSource/contributor_covenant/pull/1590) についても、ほかの韓国の方々がレビューに参加し、さらにできれば多くの方々にさまざまな場所で有用に採択・活用してもらえればうれしい。

[OES のブログ記事](https://ethicalsource.dev/blog/contributor-covenant-3/)で引用されている **ネイサン・シュナイダー（Nathan Schneider）教授** の言葉のとおり、コントリビューター・コヴェナント（Contributor Covenant）は、責任ある透明なコミュニティを構築するうえで不可欠な土台として機能し、実際に対立の解消にも寄与してきた。慣例的に GitHub などで "Add a code of conduct" ボタンを押してテンプレートを貼り付けることが多いだろうが、GitHub が自動提供するテンプレートは、なぜか 2.0 版を最後に更新されていない。3.0 版は、従来の 2.0、2.1 版に比べて大きな変化と改善があったので、せっかくなら [公式ページ](https://www.contributor-covenant.org/adopt/) を通じて最新版本を採択してみてはどうかと勧めたい。内容も実際にはそれほど長くないので、その過程で一度くらい全文をじっくり読んでみれば、なおさら意味があると思う。コントリビューター・コヴェナント 3.0 行動規範と、今回作業した [韓国語訳版](https://github.com/EthicalSource/contributor_covenant/pull/1590) に多くの関心を寄せてもらえることを願い、ここで筆を置く。
