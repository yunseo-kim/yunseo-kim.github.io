---
title: 良いコードを書くための原則
description: 良いコードを書く必要性と、一般的に良いコードを書くための主要な原則について学ぶ。
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
---
## 良いコードを書く必要性
目の前の実装のために急いでコードを書くことだけに集中していると、[技術的負債](/posts/Technical-debt/)が手に負えないレベルまで膨らみ、後の保守に問題が生じる可能性がある。したがって、開発プロジェクトを進める際には、最初から可読性が高く保守が容易な良いコードを書くことが言うまでもなく重要である。

アルゴリズム問題解決（PS, Problem Solving）やプログラミングコンテスト（CP, Competitive Programming）の場合、通常は問題解決に使用したコードを問題解決やコンテストが終わった後に再利用することはなく、特にCPの場合は時間制限があるため、良いコードを書くことよりも速い実装の方が重要ではないかという意見もある。この質問に答えるためには、自分が何のためにPS/CPを行い、どのような方向性を追求しているのかを考える必要がある。

個人的に考えると、PS/CPを通じて学べる点は以下の通りである：
- 与えられた実行時間制限とメモリ制限などの条件内で問題を解決する過程で、様々なアルゴリズムとデータ構造を使用して習得することができ、これにより実際のプロジェクトを進める際にも特定の状況でどのアルゴリズムとデータ構造を使用すれば良いかの感覚を養うことができる
- コードを書いて提出すると、即座に正解/不正解の判定と実行時間、メモリ使用量に関する客観的なフィードバックを受けることができるため、見落としなく正確なコードを速く熟練して書く練習ができる
- 他の上級者が書いたコードを見て自分が書いたコードと比較し、改善点を見つけることができる
- 実際の開発プロジェクトに比べて小規模の、似たような機能を持つコードを繰り返し書くため、（特に一人でPSを練習する場合）締め切りなどに縛られず、細部に気を配りながら簡潔で良いコードを書く練習ができる

PS/CPを単に趣味として楽しむ場合ももちろんあるかもしれないが、PS/CPを間接的にプログラミングスキルを高めるために行う場合、最後の「良いコードを書く練習」も前の3つに劣らず大きな利点である。良いコードを書くことも最初から自然にできるわけではなく、繰り返しの練習を通じて着実に習得する必要があるからだ。また、複雑で読みにくいコードはデバッグが難しく、自分自身も一度で正確に書くことが容易ではないため、非効率的なデバッグに時間を取られると、結局そんなに速く実装できないこともある。PS/CPはもちろん実務とは大きな違いがあるだろうが、だからといって良いコードを書くことを全く気にせず、目の前の実装に急いでいるのは上記の理由で本末転倒であるため、個人的にはPS/CPでも簡潔で効率的なコードを書くことが良いのではないかと考えている。

> 12024.12 コメント追加：  
> 現時点での流れを見ると、コンピュータサイエンスを専攻し開発自体を職業とするならともかく、プログラミングを数値解析や実験データ解析などの手段として活用しようとする場合は、GitHub CopilotやCursor、WindsurfなどのAIを積極的に活用して時間を節約し、その節約した時間に他のことをもっと勉強した方が良いのではないかと思う。PS/CP自体を趣味として楽しむのであれば止める人はいないだろうが、コード作成の練習のためにPS/CPに時間と労力を費やすことは、今ではコストに対する効用が非常に低いように思える。さらには、開発職種の場合でも、少なくとも入社試験としてのコーディングテストはその重要度が恐らく従来よりもかなり低くなると予想する。
{: .prompt-warning }

## 良いコードを書くための原則
コンテストで書くコードであれ実務で書くコードであれ、良いコードと言えるための条件は大きく変わらない。この記事では、一般的に良いコードを書くための主要な原則について扱う。ただし、PS/CPでは速い実装のために実務に比べて相対的に妥協する部分があるかもしれないが、そのような場合は記事内で別途言及する。

### 簡潔なコードの作成
> "KISS（Keep It Simple, Stupid）"

- コードが短く簡潔であるほど、当然ながらタイプミスや単純なバグが発生する恐れが減り、デバッグも容易になる
- できるだけ別途のコメントなしでも簡単に解釈できるように書き、本当に必要な場合にのみコメントを追加して詳細説明を加える。コメントに依存するよりもコード構造自体を簡潔に保つことが望ましい
- コメントを書く場合は、明確かつ簡潔に書く
- 一つの関数に渡す引数は3つ以下にし、それ以上の引数を一緒に渡す必要がある場合は、一つのオブジェクトにまとめて渡す
- 条件文の深さ（depth）が二重、三重と深くなると可読性が低下するため、条件文の深さを増やすことはできるだけ避けるべき  
  例）以下のコードよりもガードクローズ（Guard Clause）を活用した下のコードの方が可読性の面で有利

  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if user:
          token = await user_service.get_token(user)
  
          if token :
              if token.purpose == 'reset':
                  return True
      return False
  ```
  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if not user:
          return False
    
      token = await user_service.get_token(user)
  
      if not token or token.purpose != 'reset':
          return False
    
    return True
  ```
- ただし、PS/CPではさらに進んでコードの長さを短縮して速く書くために、時にC/C++のマクロを活用する裏技を使うことがある。時間が限られたコンテストに限って時々使用すると便利だが、PS/CPに限って通用する方法であり、一般的にC++でのマクロ使用は避けるべき  
  例）

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### コードのモジュール化
> "DRY（Don't Repeat Yourself）"

- 同じコードを繰り返し使用する場合、該当部分を関数やクラスに分離して再利用する
- モジュール化を通じてコードを積極的に再利用すると可読性が向上し、後にコードを修正する必要が生じた場合、該当関数やクラスを一度だけ修正すれば良いため、保守が容易になる
- 原則的には、一つの関数が二つ以上の仕事をせず、一つの機能のみを実行することが理想的。ただし、PS/CPで書くコードは大抵単純な機能を実行する小規模のプログラムであるため再利用に限界があり、時間が限られているため実務のように厳格に原則に従うのは難しいかもしれない

### 標準ライブラリの活用
> "Don't reinvent the wheel"

- アルゴリズムやデータ構造を学ぶ段階では、キューやスタックのようなデータ構造、ソートアルゴリズムなどを直接実装して原理を理解することが有用だが、そうでなければ標準ライブラリを積極的に活用するのが良い
- 標準ライブラリはすでに数え切れないほど多く使用され検証されており、最適化も十分になされているため、直接再実装するよりも効率的
- すでにあるライブラリを使用すれば良いため、不必要に同じ機能をするコードを直接実装するために時間を無駄にする必要がなく、協業時に書いたコードを他のチームメンバーが理解しやすい

### 一貫性のある明確な命名法の使用
> "Follow standard conventions"

- 曖昧でない変数名と関数名を使用する
- 通常、使用するプログラミング言語ごとにそれに合った命名規約（naming convention）があるので、使用する言語の標準ライブラリで使用されている命名規約を学び、クラス、関数、変数などを宣言する際に一貫して適用する
- それぞれの変数と関数、クラスがどのような機能を持つのか、そしてブール（boolean）型であればどのような条件で真（True）を返すのかが明確に表れるように命名する

### すべてのデータは正規化して保存
- すべてのデータは一つの一貫した形式に正規化して処理する
- 同じデータが二つ以上の形式を持つと、文字列表現が微妙に異なったり、ハッシュ値が異なったりするなど、捉えにくい微妙なバグが発生する可能性がある
- タイムゾーン、文字列などのデータを保存して処理する際は、入力を受け取ったり計算したりするとすぐにUTC、UTF-8エンコーディングなど一つの標準形式に変換する必要がある。該当データを表現するクラスのコンストラクタで最初から正規化を行うか、データを入力として受け取る関数ですぐに正規化を行うのが良い

### コードのロジックとデータを分離
- コードのロジックと関係のないデータは条件文の中に直接入れず、別のテーブルに分離する  
  例）上のコードよりも下のコードのように書く方が望ましい

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ```c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ```
