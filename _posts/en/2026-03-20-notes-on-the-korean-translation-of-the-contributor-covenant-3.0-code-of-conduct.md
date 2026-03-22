---
title: "Notes on the Korean Translation of the Contributor Covenant 3.0 Code of Conduct"
description: "Notes on my Korean translation of Contributor Covenant 3.0, released in July 12025, including key wording choices, rationale, and personal reflections."
categories: [Dev, Dev Culture]
tags: [Contributor Covenant, Code of Conduct, Ethics, Human Rights]
image: /assets/img/multigenerational-people-iStock-1482584637.avif
---

> Official Korean translation PR for Contributor Covenant 3.0 Code of Conduct: [feat(i18n): add Korean translation for Contributor Covenant 3.0 (#1590)](https://github.com/EthicalSource/contributor_covenant/pull/1590)
{: .prompt-info }

## Contributor Covenant

[Contributor Covenant](https://www.contributor-covenant.org/) was first written and published in 12014 by **Coraline Ada Ehmke**, and since 12021 has been transferred to **OES (Organization for Ethical Source)**, where it has been maintained and improved by its contributors. Today, it is the most widely used code of conduct for digital communities in the world. Its goal is to make explicit the implicit values that communities may share, thereby fostering a community culture in which everyone can feel welcome and safe.

In the past, developer communities often tolerated harsh behavior or discriminatory remarks under the banner of meritocracy, and Contributor Covenant served as an important turning point in helping developer communities transform themselves into more human-centered cultures that embrace diverse people and value mutual respect and constructive feedback. Today, hundreds of thousands of open-source projects around the world—including Creative Commons, Linux, Apple, Mastodon, Microsoft, WordPress, and IBM—have adopted this covenant.

## What Changed in the Contributor Covenant 3.0 Update

To mark the 10th anniversary of Contributor Covenant, OES began work in 12024, and after about a year of effort, released version 3.0 in July 12025. Compared to the previous 2.1 version, the major changes are as follows.
- References:
  - <https://ethicalsource.dev/blog/contributor-covenant-3/>
  - <https://www.contributor-covenant.org/faq/>

### Expanded Flexibility

- Whereas previous versions were optimized for open-source communities, version 3.0 was designed to be applicable to a wider range of online and offline communities beyond software development
  - e.g. instead of **"Project Maintainers"**, it uses the more neutral and inclusive term **"Community Moderators"**
- It removes U.S.-centric idiomatic expressions and replaces them with clearer wording that speakers from other cultures can understand and translate more easily

### Paradigm Shift from Retributive Justice to Restorative Justice

One of the biggest changes in Contributor Covenant 3.0 is its paradigm shift from **Retributive Justice** to **Restorative Justice**. The previous **enforcement guidelines** section, which focused on standards for escalating sanctions, has been restructured into **Addressing and Repairing Harm**.
- Some response-stage names have been changed
- In addition to the existing consequence items, new repair guidance has been added, so the document now goes beyond sanctioning the initial offender and also addresses how broken relationships between parties can be restored, how conflicts can be resolved, and how wrongs can be made right afterward
- Rather than emphasizing only third-party enforcement and punishment, it shifts toward encouraging voluntary reflection, reconciliation, and improvement where possible, and toward thinking about how to make the community healthy again after a problem occurs

### Clearer Guidelines

- The **Our Standards** section has been clearly divided into two sections—**Encouraged Behaviors** and **Restricted Behaviors**—to improve readability
- In particular, the **Restricted Behaviors** section explicitly restricts not only actually carrying out harmful behavior, but also threatening or promoting it, thereby strengthening prevention
  > We agree to restrict the following behaviors in our community. Instances, threats, and promotion of these behaviors are violations of this Code of Conduct.
- It also adds a new subsection under **Restricted Behaviors** called **Other Restrictions**, explicitly providing guidance on misleading identity, failing to credit sources, promotional materials, and irresponsible communication, areas that previously lacked clear restrictions
- Reflecting survey responses from people involved in communities that had actually adopted and operated Contributor Covenant, it makes clear that the enforcement ladder is only a baseline and does not constrain the discretion of community managers
  > This enforcement ladder is intended as a guideline. It does not limit the ability of Community Managers to use their discretion and judgment, in keeping with the best interests of our community.

### Stronger Equality and Anti-Discrimination Provisions

The equality and anti-discrimination provisions addressed in the opening **Our Pledge** section have been reinforced and made more specific by replacing some terms with more inclusive expressions and explicitly adding several modern diversity values.
- The two expressions "body size" and "personal appearance" are replaced with the more inclusive "physical characteristics"
- "religion" is replaced with the more inclusive "philosophy or religion"
- "nationality" is replaced with the more inclusive "national or social origin"
- "neurodiversity" is newly added
- "language" is newly added, showing greater consideration for non-English speakers
- Wording related to gender equality and diversity has been revised more broadly
  > **v2.1**  
  > sex characteristics, gender identity and expression, or sexual identity and orientation
  >
  > **v3.0**  
  > sex or gender, gender identity or expression, sexual orientation

## Considerations in This Korean Translation Work

### General Considerations

#### Use of Honorific Style

When writing a pledge or code of conduct in Korean, whether to choose honorific style or plain style depends on one's orientation, organizational culture, and the attitude one wants to convey. In the past, plain style emphasizing authority and discipline was more common, but recently some texts have been written in honorific style to emphasize a more horizontal and respectful culture.

| Style | Honorific style(\~합니다, \~하겠습니다) | Plain style(\~한다) |
| --- | --- | --- |
| Nuance | Mutual respect, voluntary promise,<br> recommendation | Firmness, legal force, objective rule |
| Organizational culture | Flexible and horizontal culture | Relatively stricter culture |
| Main use cases | Codes of conduct,<br> ethical declarations | Security pledges, employment contracts,<br> legal disciplinary rules |
| Psychological effect | "We uphold this together"<br> (voluntary agreement) | "This must be followed" (more strongly<br> emphasizing a binding nature) |

Looking at the [discussion at the time](https://github.com/EthicalSource/contributor_covenant/pull/895#pullrequestreview-563210153), it appears that when version 2.0 was translated into Korean, honorific style was initially considered, but the text was later [rewritten in plain style](https://github.com/EthicalSource/contributor_covenant/commit/3971299d81149b3fc0ce603a5dd26400509f090f). I respect that earlier discussion and its conclusion, but even so, I chose once again to translate this version in honorific style for the following reasons.

Today, the culture of open-source communities is, by nature, somewhat distant from constraint, rigidity, and coercive enforcement, and instead aims more toward mutual respect, voluntary participation, and contribution. [Contributor Covenant 3.0 in particular reflects that philosophy strongly throughout](#paradigm-shift-from-retributive-justice-to-restorative-justice). Considering the core values and philosophy the original text seeks to convey in this update, as well as broader community culture and trends, I judged that honorific style was the appropriate choice for the Korean translation. I also referred to examples such as the [Rust Korea User Group](https://rust-kr.org/pages/code-of-conduct/), the [PyCon KR Code of Conduct](https://pythonkr.github.io/pycon-code-of-conduct/ko/coc/a_intent_and_purpose.html), and the [Kubernetes Community Code of Conduct in Korean](https://kubernetes.io/ko/community/code-of-conduct/), all of which use honorific style.

#### Avoiding Unnecessary Passive Expressions

{% comment %}번역 지침: 여기서부터, 큰따옴표(")로 둘러싼 한국어 표현은 번역하려 하지 말고 있는 그대로 유지하세요. 지금 이 글의 주제와 맥락상, 해당 부분은 한국어를 그대로 유지해야 자연스럽습니다. 또한 번역 예시를 인용 블록으로 제시하는 부분이 있는데, 마찬가지로 번역하려 하지 말고 있는 그대로 유지하세요.{% endcomment %}

Unlike English, which frequently uses the passive voice, Korean is a language that generally prefers active constructions over passive expressions. If one mechanically renders English passive constructions into Korean passive expressions just because the English original used the passive voice, the result tends to sound unnaturally like a translation, and may even be grammatically inappropriate.

That is not to say Korean never uses passive expressions, but as long as the meaning was not distorted, I tried to render even passively written phrases in the original into active constructions in the Korean translation wherever possible.

**e.g.**
- "Encouraged Behaviors": "장려**되는** 행동"(X), "장려**하는** 행동"(O)
- "enforcement actions are carried out in private": "집행 조치는 비공개로 진행**된다**"(X), "집행 조치는 비공개로 진행**한다**"(O)
- "its own established enforcement process": "자체적으로 확립**된** 집행 절차"(X), "자체적으로 확립**한** 집행 절차"(O)
- "the following enforcement ladder may be used": "다음의 단계적 집행 기준**이 사용될** 수 있습니다"(X), "다음의 단계적 집행 기준**을 사용할** 수 있습니다"(O)
- "are provided at": "에서 제공**됩니다**"(X), "에서 제공**합니다**"(O)

#### Considering the Context in Which a Word Is Used Rather Than Relying on Dictionary-Style, Mechanical Translation

Because English and Korean are fairly distant languages, words in the two languages do not, of course, correspond exactly one-to-one. Even if a dictionary lists them as having the same meaning, that does not make them interchangeable in every context.

For example, in the following passage, "intimate" is used in the sense of something "sexual," not "친밀한."

> **Sexualization.** Behaving in a way that would generally be considered inappropriately <u>intimate</u> in the context or purpose of the community.

Likewise, in the next example, translating "process" mechanically into a dictionary equivalent would sound awkward. In context, it is more appropriate to render it as "추스를."

> ... give the community members involved time to <u>process</u> the incident.

> ([표준국어대사전](https://stdict.korean.go.kr/) 표제어 중)
>
> **추스르다「3」**: 일이나 생각 따위를 수습하여 처리하다.
{: .prompt-tip }

On the other hand, some loanwords do not have a particularly good native Korean equivalent. For instance, "community" could perhaps be rendered in native Korean as "공동체," but I judged that the nuance carried by the English word "community" differs considerably from that of the Korean word "공동체." So although I generally preferred to replace loanwords with native Korean expressions where possible, when I thought doing so would seriously distort the meaning or nuance of the original, I kept forms such as "커뮤니티."

With such considerations in mind, I aimed not to perform a simple, dictionary-like mechanical substitution of words, but to choose Korean expressions that came closest to the meaning and context of the original text.

#### Compliance with Korean Orthographic and Language Norms

I also tried to follow Korean orthographic and language norms—such as standard spelling and standard language conventions—as accurately as possible.

### The "서약(Our Pledge)" Section

#### Subheading

If translated literally, "Our Pledge" would become "우리의 맹세," but since the [existing Korean translation](https://www.contributor-covenant.org/ko/version/2/1/code_of_conduct/) had already rendered it as "서약," and since that wording falls well within the range of natural Korean, I kept "서약" again this time.

#### Translating the term "caste"

In the [existing Korean translation of version 2.1](https://www.contributor-covenant.org/ko/version/2/1/code_of_conduct/), this was translated directly as "카스트 제도." Since the word caste can also function as an academic common noun referring to <u>rigidly stratified status-order systems in various parts of the world</u>, I would not call that rendering simply mistranslated. However, without such detailed background information, most Korean speakers encountering "카스트 제도" in everyday usage would understand it as "the Hindu status system in India derived from sources such as the Manusmriti." Taking the context of the original into account, I therefore translated it as "계급." Here, it is more reasonable to interpret "caste" as referring not to a specific country (India) or religion (Hinduism), but to all kinds and forms of status systems and the classes that follow from them.

#### Using "성" instead of "성별"

> We are committed to fostering an environment that respects and promotes the dignity, rights, and contributions of all individuals, regardless of ... sex or gender, gender identity or expression, sexual orientation ... or other status.

Considering the values and context the original seeks to convey, what is meant here by "sex," "gender," and "sexual orientation" is clearly not distinction according to a simple male/female binary. Therefore, instead of "성별," which subtly implies categorization along that binary, I used the word "성," and tried to preserve as much as possible the distinctions that the three terms sex, gender, and sexuality carry in the humanities and social sciences, translating them as follows.

> ... 생물학적 또는 사회적 성, 성 정체성 또는 성 표현, 성적 지향...

### The "장려하는 행동(Encouraged Behaviors)" and "제한하는 행동(Restricted Behaviors)" Sections

#### Removing the colon(`:`)

> With these considerations in mind, we agree to behave mindfully toward each other and act in ways that center our shared values, including:
>
> 1. Respecting the **purpose of our community**, our activities, and our ways of gathering.
> 2. Engaging **kindly and honestly** with others.
> ...

In English, it is common to use a colon after a complete sentence to introduce a list of examples, as above. In contemporary Korean orthographic norms, however, the use of the colon is largely limited to itemized expressions such as listing entries after a heading or adding explanations. Unless the text is written entirely in itemized form, writing it as follows is very awkward, and can easily give the impression of something hastily translated by machine translation or an LLM. Personally, this was also one of the aspects I found most disappointing in the [Korean translation of version 2.1](https://www.contributor-covenant.org/ko/version/2/1/code_of_conduct/).

> 이러한 점을 유념하며, 우리는 서로를 사려 깊게 대하고 우리가 공유하는 다음 가치를 중심으로 행동할 것에 동의합니다:
> 
> 1. 우리 **공동체의 목적**, 활동 및 모임 방식을 존중합니다.
> 2. **친절하고 정직하게** 다른 사람들과 소통합니다.
> ...

Therefore, instead of mechanically carrying over the colon into Korean, I replaced it with a period(`.`) so that the result would read naturally in Korean usage.

#### Translating the expression "that would generally be considered inappropriately"

Here, rather than translating "generally" literally as "일반적으로," I rendered it more naturally in context as "대부분의 사람들에게."

> ...<u>대부분의 사람들이</u> 부적절하다고 간주할 만한...

### Translating the expression "act on"

At first, I considered translating "act on" simply as "이용하다," but in context the phrase is closer to prohibiting <u>any conduct undertaken on the basis of another person's identifying or personal information, regardless of intent</u>. Rendering it as "이용하다" seemed to narrow the meaning too much, so I translated it as follows.

> **비밀 침해.** 타인의 신상 관련 정보 또는 개인적인 정보를 당사자의 허락 없이 공유하거나, 그 정보<u>를 바탕으로 행하는</u> 모든 행위.

### The "문제 신고(Reporting an Issue)" Section

- "this Code of Conduct **reinforces** encouraged behaviors and norms that ...": translated as "본 행동 강령은 ...는 권장 행동 방식과 규범을 **증진합니다**"
- "in a timely manner": translated as "적시에"
- "while prioritizing safety and confidentiality": translated as "안전과 비밀 유지를 우선시한다는 전제 하에"
- "In order to **honor** these values": translated as "이들 가치를 **지키기** 위해"
  > ([Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/) 표제어 중)
  >
  > [**honor**](https://www.oxfordlearnersdictionaries.com/definition/english/honor_2) *verb*  
  > <u>keep promise</u>
  > 3\. **honor something** *(formal)* to do what you have agreed or promised to do
  {: .prompt-tip }

### The "피해 대응 및 교정(Addressing and Repairing Harm)" Section

- "Addressing": translated as "대응"
- "Repairing": translated as "교정"

#### Translating `Event:`, `Consequence:`, `Repair:`

This was a part I wrestled with quite a bit, because it is awkward to render these directly into Korean. Literal translations such as "사건," "결과," and "교정" make the text sound quite unnatural.

After much thought about how to preserve a natural Korean reading while conveying [the philosophy of the original](#paradigm-shift-from-retributive-justice-to-restorative-justice) as fully as possible, I settled on the following.
- "Event": translated as "적용 상황"
- "Consequence": translated as "대응 조치"
- "Repair": at first I considered "회복 조치," but rejected it because the word "조치" carries a nuance of action imposed by another party rather than voluntary reflection and improvement by the person involved, which runs against the intent of the original. I ultimately translated it as "교정 노력"

#### Translating the expression "seeking clarification on expectations"

"Expectations" could be translated literally as "기대 사항," and that would still be intelligible, but for a smoother Korean sentence I translated it as "준수 사항."

> ([Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/) 표제어 중)
>
> [**expectation**](https://www.oxfordlearnersdictionaries.com/definition/english/expectation) *noun*  
> 3\. [countable, usually plural] a strong belief about the way something should happen or how somebody should behave
{: .prompt-tip }

"Seeking clarification" could be translated as a "해명(clarification) 요구(seeking)," but in context the Repair item is describing desirable post-incident attitudes and actions that should be taken by the person who caused the problem. Translating clarification and seeking as "해명" and "요구" would therefore distort the meaning. Here, I judged it most appropriate to render it as an <u>effort</u>(seeking) to <u>clearly confirm and understand</u>(clarification) the <u>expectations to be followed</u>(expectations), so that one may reflect and avoid repeating the same mistake.

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

#### Translating the expression "cooldown"

In the dictionary, it can mean cooling, cool-down exercise after a workout, calming down, and so on; here, in context, it is closest to the sense of calming down—the same sense as in the Korean expression meaning "cool your head a bit."

That said, rendering "time-limited cooldown period" as "한시적 진정 기간" sounded awkward, so in this Korean translation I rendered "cooldown period" as "자숙 기간."

#### Translating the expression "time to process the incident"

As [mentioned above](#considering-the-context-in-which-a-word-is-used-rather-than-relying-on-dictionary-style-mechanical-translation), I translated it as "해당 일을 추스를 시간."

#### Translating "suspension" and "ban"

In the [existing Korean translation of version 2.1](https://www.contributor-covenant.org/ko/version/2/1/code_of_conduct/), "ban" was translated as "제재." But "제재" is an umbrella term that can encompass all kinds of actions taken in response to misconduct, including lower-level measures such as warnings or temporary restrictions on activity, so its meaning is ambiguous. Moreover, the English word "ban" clearly means prohibition or suspension, and expressions like "permanent suspension" of an account are also common and natural in Korean, so I see no reason to avoid a more direct rendering here.

The same applies to "suspension," which also clearly means something like suspension or stoppage, so there is no need to paraphrase it unnecessarily.

Accordingly, I translated "Temporary Suspension" and "Permanent Ban" as "일시적 정지" and "영구 정지," respectively.

#### Translating the sentence "This enforcement ladder is intended as a guideline."

I translated "enforcement ladder" as "단계적 집행 기준." Also, this sentence is used in the context of clarifying that the enforcement ladder described above is only being presented as one possible option among several, and that the discretion and decision-making authority of community managers are preserved. For that reason, I translated the article "a" as "하나의." The Korean translation was therefore written as follows.

> <u>이 단계적 집행 기준은 하나의 기준선으로 마련한 것입니다.</u> 이는 커뮤니티의 최선의 이익에 부합하는 커뮤니티 관리자의 재량권과 판단 권한을 제한하지 않습니다.

## Closing Thoughts

Many documents and projects of this public-interest kind are translated into multiple languages by volunteers and contributors. Unfortunately, when it comes to Korean translations, I have often encountered cases where no contributor existed and thus no translation was available at all, or where a translation did exist but read so awkwardly and mechanically that, despite being Korean, I found myself thinking, “I’d rather just read the English,” and switching back to the English page.

As I decided to contribute a Korean translation this time, I felt that if I was going to contribute at all, I should try to produce a high-quality translation that would not feel out of place even if readers assumed it had been written in Korean by a Korean author from the start. I tried to understand and capture the philosophy and subtle context of the original text, especially what expressions had changed in version 3.0 compared to version 2.1 and why the original authors might have made those choices.

By the nature of natural language, translation is not something where identical input produces identical output like a mathematical function. Different translators will inevitably produce somewhat different translations, and that has to do not only with skill, but also with the fact that translation—and writing more broadly—has no single fixed correct answer. These days I use AI as an aid in almost all of my work, and I even connect LLM APIs to this very blog to automatically translate and publish posts in multiple languages. But this particular project was one I genuinely wanted to do properly, to the very best of my ability. I reviewed each expression multiple times myself and thought carefully about which wording would preserve the original meaning as fully and naturally as possible with minimal distortion, and the result reflects my own subjective yet best judgment and interpretation. Now that everyone is using AI, I believe that at least for translations of important documents such as pledges and codes of conduct, a translation is valuable only if it has a comparative advantage over what you would get by simply feeding the original text to an AI and asking for a translation. At least as of March 12026, I can say with confidence that in [this translation](https://github.com/EthicalSource/contributor_covenant/pull/1590), I have fully preserved subtle nuances and contextual elements of the original that machine translation or LLMs still cannot completely capture.

As of March 20, 12026, aside from the English original and the Korean translation I am submitting this time, Contributor Covenant version 3.0 has been fully translated into only three other languages: Bengali, German, and Simplified Chinese, and if you look at the [list of open PRs](https://github.com/EthicalSource/contributor_covenant/pulls), there are also many languages whose draft translations have been submitted as PRs but have not received final approval because no reviewer is available. In fact, many languages have not even reached version 3.0 and are still on version 1.4. If any speaker of a language other than Korean happens to be reading this for whatever reason, [the contribution process is not that complicated](https://github.com/EthicalSource/contributor_covenant?tab=contributing-ov-file#translators-and-native-speakers), so if you can spare even a day on a weekend to contribute, it would surely be a great help both to OES and to speakers of your language. This was also my first time contributing to a translation project like this and my first time reading a full code of conduct closely from beginning to end, and I think it was more than worth the few hours it took. Korea has a fairly large number of developers active in open-source communities such as GitHub relative to its population, and for that reason I would be delighted if other Korean speakers would join the review process for the [Korean translation](https://github.com/EthicalSource/contributor_covenant/pull/1590) of Contributor Covenant 3.0 that I translated and submitted this time, and if many people could also adopt and use it widely in many places.

As **Professor Nathan Schneider** says in [the OES blog post](https://ethicalsource.dev/blog/contributor-covenant-3/), Contributor Covenant functions as an essential foundation for building responsible and transparent communities, and has in fact helped resolve conflicts. Conventionally, it is common on GitHub and similar platforms to click the “Add a code of conduct” button and paste in a template, but for some reason the template automatically provided by GitHub has not been updated past version 2.0. Since version 3.0 includes major changes and improvements compared with versions 2.0 and 2.1, I would encourage people to consider adopting the latest version through the [official page](https://www.contributor-covenant.org/adopt/). The text is not actually that long, so I think it would be even more meaningful if, in the process, you took the opportunity to read through the full text carefully at least once. I hope many people will take an interest in Contributor Covenant 3.0 and in the [Korean translation](https://github.com/EthicalSource/contributor_covenant/pull/1590) I worked on this time.
