---
title: 撰寫好程式碼的原則
description: "說明為何要寫好程式碼，並整理常見原則與實務：KISS、DRY、標準函式庫、清楚命名、資料正規化、邏輯與資料分離；兼論在PS/CP與實務中的取捨。"
categories: [Dev, Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Principles-for-Writing-Clean-Code/
---

## 寫好程式碼的必要性
若只顧著為了眼前的實作而快速敲出程式碼，[技術債](/posts/Technical-debt/)可能會膨脹到無法承擔的程度，導致後續維護出問題。因此在開發專案時，儘量從一開始就寫出可讀性高、易於維護的好程式碼，這點不言而喻地重要。

在演算法問題解決（PS, Problem Solving）或競技程式設計（CP, Competitive Programming）的情境中，通常題目的程式在題解或比賽結束後幾乎不會再重用；尤其在 CP 有時間限制時，也有人認為和寫「好程式碼」相比，快速實作更重要。要回答這個問題，需要思考自己做 PS/CP 的目的，以及想追求的方向。

就我個人看法，若撇開培養通用的問題解決能力，僅從與程式設計相關的面向來看，透過 PS/CP 能學到的事情包括：
- 在既定的執行時間與記憶體限制內解題，能嘗試並熟悉各種演算法與資料結構，進而在實際專案中也更有感覺地選用合適的工具
- 提交後能立刻得到正確/錯誤與執行時間、記憶體用量等客觀回饋，可練習快速且熟練地寫出正確無遺漏的程式碼
- 透過閱讀高手的程式碼，和自己的實作相互比較，找出可改進之處
- 相較於真實開發專案，PS/CP 多半是小規模、功能相似的程式重複撰寫，（尤其獨自練習 PS 時）不受截止期限綁定，能更專注於細節，練習寫出簡潔且良好的程式碼

當然也可能只是把 PS/CP 當作單純的嗜好；但若是為了提升程式能力而進行 PS/CP，那麼最後一點「練習寫好程式碼」同樣是很大的優勢，絲毫不遜於前面三點。寫好程式碼並非自然而然會發生，而是需要反覆練習才能持續精進。而且複雜難讀的程式碼很難除錯，連作者自己也不易一次就正確寫完；結果可能反而把時間浪費在低效率的除錯上，最後也未必寫得比較快。PS/CP 與業界實務確實有差異，但因此就完全不在乎寫好程式碼、只求眼前能跑起來，依我之見是本末倒置。即使在 PS/CP，我也傾向寫出簡潔且高效的程式碼。 

> 12024.12 新增評論:  
> 以目前的趨勢來看，為了寫出高效率程式所需的背景知識（如演算法與資料結構）與解題能力，未來仍具意義；但在把想法落成可運行的程式碼這一步，未必要堅持全都親手撰寫，不如積極運用 GitHub Copilot、Cursor、Windsurf 等 AI 來節省時間，把省下的時間投入其他工作或學習。若是為了通用問題解決能力或演算法/資料結構學習，或純粹當作興趣而做 PS/CP，當然無可厚非；但若只是為了練打字寫程式本身而在 PS/CP 上投入大量時間與心力，現在看來成本效益已大幅降低。甚至在開發職缺上，至少做為入職考試的程式測驗，其重要性很可能會比以往明顯下降。
{: .prompt-warning }

## 撰寫好程式碼的原則
無論是比賽中的程式碼，或是實務開發的程式碼，「好程式碼」的要件並沒有太大差異。本文整理了一般撰寫好程式碼的主要原則。不過在 PS/CP 為了快速實作，與實務相比可能會有相對的取捨，這類情況會在文中另行說明。

### 撰寫簡潔的程式碼
> "KISS（Keep It Simple, Stupid）"

- 程式碼越短越簡潔，當然越不容易出現打字錯或低級錯誤，除錯也更容易
- 盡量讓程式碼即使沒有額外註解也能容易理解；只有在確有必要時才補上註解。與其依賴註解，不如讓結構本身保持簡潔，較為理想
- 需要寫註解時，務必明確且精簡
- 單一函式的參數以不超過 3 個為佳；若需要傳遞更多參數，應封裝成一個物件再傳入
- 條件式的巢狀深度（depth）若一層層加深，會降低可讀性；應儘量避免加深條件式。  
  例如，相較於上面的寫法，利用守衛子句（Guard Clause）的下面版本在可讀性上更有優勢。  

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
- 不過，在 PS/CP 中，為了進一步縮短程式碼、加快撰寫速度，偶爾會使用 C/C++ 巨集這類取巧手法。在時間緊迫的比賽中偶爾用用有其效益，但這只在 PS/CP 場景較吃香；一般而言在 C++ 中仍應避免過度使用巨集。  
  例如：  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### 模組化程式碼
> "DRY（Don't Repeat Yourself）"

- 若有重複使用的程式片段，應抽取為函式或類別以利重用
- 積極透過模組化來重用程式碼，能提升可讀性；未來若需要修改，只要調整對應的函式或類別即可，維護更容易
- 原則上，一個函式不要做兩件以上的事，只執行單一功能。不過 PS/CP 的程式多為小規模且功能單純，可重用性有限，加上時間受限，較難像實務一樣嚴格遵循原則

### 善用標準函式庫
> "Don't reinvent the wheel"

- 在學習演算法或資料結構的階段，親手實作佇列、堆疊、排序等確實有助於理解原理；但除此之外，應積極善用標準函式庫
- 標準函式庫已被大量使用並充分驗證，且多半經過良好最佳化，通常比自行重寫更有效率
- 直接使用現成函式庫可避免重複造輪子，不必浪費時間實作相同功能；且在協作時，也更容易讓其他成員理解你的程式碼

### 使用一致且明確的命名
> "Follow standard conventions"

- 使用不含糊的變數名與函式名
- 各種程式語言通常都有相應的命名規範（naming convention）；請熟悉該語言標準函式庫所採用的命名規範，並在宣告類別、函式、變數時一以貫之
- 讓每個變數、函式、類別的功能一目了然；若為布林（boolean）型別，命名要能清楚表達在何種條件下會回傳 True

### 所有資料皆應正規化後儲存
- 將所有資料以一致的格式正規化處理
- 相同資料若同時存在兩種以上格式，容易因字串表示略有差異、或雜湊值不同等，產生難以發現的細微錯誤
- 處理像是時區、字串等資料時，應在輸入或計算後立即轉換為單一標準格式，如 UTC、UTF-8 編碼等。最好在代表該資料的類別建構子就先做正規化，或於接收輸入的函式中立刻進行

### 將程式邏輯與資料分離
- 與程式邏輯無關的資料，不要直接硬寫在條件式中，應分離成獨立的表格  
  例如，與其寫上面的程式，不如像下面這樣比較理想。

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ~~~c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ~~~
