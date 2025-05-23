---
title: 技術債務(Technical debt)
description: 探討技術債務的概念、產生原因，以及如何最小化技術債務。
categories: [Programming]
tags: [Coding]
image: /assets/img/technology.webp
---
## 技術債務(Technical debt)
技術債務：在開發過程中，為了滿足即時需求而選擇捷徑以更快完成眼前的專案，從而在未來必須付出的代價。

就像在會計上承擔債務（debt）借錢可以快速投資於當前需要的地方，但會面臨財務壓力並需要支付本金加利息一樣，為了解決當前面臨的需求而快速進行開發（即使代碼稍微凌亂），會導致代碼變得複雜和重複，從而在未來實現新功能或擴展時遇到困難。

就像企業通過債務及時執行更多投資以開發新產品並提高市場佔有率，或個人通過貸款購買房屋一樣，承擔技術債務並快速實現新功能並不總是壞事。然而，減少技術債務的積累並在可控範圍內管理它是理想的做法。

## 技術債務產生的原因
即使開發人員的能力足夠，在軟體製作過程中技術債務也不可避免地會產生，完全阻止它是不可能的。
在服務發展過程中，當原有的代碼設計遇到瓶頸時，即使原本是可讀性好且運作良好的代碼，也可能需要修改原有設計。
此外，隨著技術本身的發展，當以前流行的庫/框架不再常用時，可能會決定將技術棧更改為其他庫/框架，在這種情況下，原先編寫的代碼也會成為一種技術債務。

除此之外，技術債務還可能由以下原因產生：
- 在專案進行過程中未及時記錄設計，導致其他人或時間過後自己再次查看該代碼時難以解讀
- 未刪除不再使用的變數或數據庫項目
- 未自動化重複性工作（部署/構建等），每次都需要額外的時間和精力
- 緊急的規格變更

## 最小化技術債務的方法
### 設定開發人員之間的規則（Convention）
- 如果不是單獨開發，為了順暢的協作，需要就使用的語言或技術棧、專案的目錄結構、開發風格等達成共識
- 需要決定在多大程度上統一開發方式，以及從哪裡開始保留個人自主權
- 通過代碼審查來確認彼此的開發風格並交換意見是必要的

### 編寫乾淨代碼（Clean Code）& 重構（Refactoring）
- 如果現有代碼凌亂妨礙開發，可以通過重構來清理技術債務，使代碼結構更加整潔
- 當然，現有代碼越是凌亂的意大利麵條式代碼，重構的難度就越高
- 應該盡可能從一開始就努力編寫可讀性好、易於維護的代碼
