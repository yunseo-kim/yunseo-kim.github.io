---
title: "የGitHub ማርክዳውን ሰነድ ህጎች ማጠቃለያ"
description: "Markdown ምን እንደሆነ በመመልከት፣ ለGitHub Pages ብሎግ ሆስቲንግ በGitHub Flavored Markdown መሠረት ዋና ዋና የMarkdown ሰነድ ህጎችን አጠቃለልሁ።"
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

GitHub Pagesን ለመጠቀም **markdown** ሰነድ ህጎችን ማወቅ ያስፈልጋል።
ይህ ጽሑፍ የGitHub ኦፊሴላዊ ሰነዶች [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) እና [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)ን በመጠቀም ተዘጋጅቷል።

## 1. Markdown ምንድን ነው
> **ማርክዳውን(markdown)** በተራ ጽሑፍ ላይ የተመሠረተ ቀላል የማርክአፕ ቋንቋ ነው። በተራ ጽሑፍ የቅርጸት ያላቸውን ሰነዶች ለመጻፍ ይጠቅማል፣ እና ከተለመዱ የማርክአፕ ቋንቋዎች ጋር ሲነጻጸር ሰነድ ህጎቹ ቀላልና አጭር መሆናቸው ዋና ባህሪው ነው። HTML እና ሪች ቴክስት(RTF) ያሉ የቅርጸት ሰነዶች ወደ እነሱ በቀላሉ ሊቀየር ስለሚችል፣ ከመተግበሪያ ሶፍትዌሮች ጋር የሚሰራጩ README ፋይሎች ወይም የመስመር ላይ ልጥፎች ላይ ብዙ ጊዜ ይጠቀማሉ།  
> ጆን ግሩበር(John Gruber) በ[የሆሎሲን ዘመን](https://en.wikipedia.org/wiki/Holocene_calendar) 12004 ዓመት የMarkdown ቋንቋን ከኤረን ሽዋርትዝ(Aaron Swartz) ጋር በሰነድ ህግ አወጣጥ ላይ በአስፈላጊ ትብብር ፈጠረው፣ ዓላማውም ሰዎች ለማንበብና ለመጻፍ ቀላል በሆነ ፕሌይን ቴክስት ፎርማት(plain text format) እንዲጽፉ ማስቻል ሲሆን እንዲሁም ወደ መዋቅራዊ ትክክለኛ XHTML(ወይም HTML) በአማራጭ እንዲቀየር ማድረግ ነበር።

\- [ዊኪፔዲያ, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. የMarkdown ሰነድ ህጎች
Markdown ቋሚ የተወሰነ መመዘኛ ስለሌለው ዝርዝር ሰነድ ህጎች እንደ አጠቃቀሙ ቦታ ትንሽ ትንሽ ሊለያዩ ይችላሉ። እዚህ የተደረገው ዝርዝር በ [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) ላይ የተመሠረተ ነው።

### 2.1. የመስመር መቆራረጥ እና የአንቀጽ መለያየት
Markdown ውስጥ አንድ ጊዜ Enter መጫን እንደ የመስመር መቆራረጥ አይቆጠርም።
~~~
የመጀመሪያ ዓረፍተ ነገር።
ሁለተኛ ዓረፍተ ነገር።
ሦስተኛ ዓረፍተ ነገር።
~~~
የመጀመሪያ ዓረፍተ ነገር።
ሁለተኛ ዓረፍተ ነገር።
ሦስተኛ ዓረፍተ ነገር።

የመስመር መቆራረጥ በተከታታይ ሁለት ወይም ከዚያ በላይ ክፍተቶችን በማስገባት ይተገበራል።
~~~
የመጀመሪያ ዓረፍተ ነገር።  
ሁለተኛ ዓረፍተ ነገር።  
ሦስተኛ ዓረፍተ ነገር።
~~~
የመጀመሪያ ዓረፍተ ነገር።  
ሁለተኛ ዓረፍተ ነገር።  
ሦስተኛ ዓረፍተ ነገር።

አንቀጽ እና አንቀጽ መካከል በባዶ መስመር(Enter ሁለት ጊዜ) ይለያሉ።
~~~
አንድ አንቀጽ።

ሌላ አንቀጽ።
~~~
አንድ አንቀጽ።

ሌላ አንቀጽ።

### 2.2. ራስጌዎች(Headers)
ጠቅላላ 6 ደረጃዎች አሉ።
```
# ይህ H1 ነው
## ይህ H2 ነው
### ይህ H3 ነው
#### ይህ H4 ነው
##### ይህ H5 ነው
###### ይህ H6 ነው
```
H1 መለያ(tag) በመሠረቱ በአንድ ገጽ ላይ አንድ ብቻ መኖር ስላለበት፣ ብዙ ጊዜ ልጥፍ ወይም ሰነድ ሲጻፍ በቀጥታ መጠቀሙ አይኖርም።

### 2.3. ማጉላት
```
*ይህ ጽሑፍ ተዘንብሏል*
_ይህም እንዲሁ ተዘንብሏል_

**ይህ ደማቅ ጽሑፍ ነው**
__ይህም እንዲሁ ደማቅ ጽሑፍ ነው__

~~ይህ የተሳሳተ ጽሑፍ ነበር~~

_እነሱን **ማዋሃድ** ትችላለህ_

***ይህ ሁሉ ጽሑፍ አስፈላጊ ነው***
```
*ይህ ጽሑፍ ተዘንብሏል*  
_ይህም እንዲሁ ተዘንብሏል_

**ይህ ደማቅ ጽሑፍ ነው**  
__ይህም እንዲሁ ደማቅ ጽሑፍ ነው__

~~ይህ የተሳሳተ ጽሑፍ ነበር~~

_እነሱን **ማዋሃድ** ትችላለህ_

***ይህ ሁሉ ጽሑፍ አስፈላጊ ነው***

### 2.4. የጽሑፍ ጥቅስ
\>ን ይጠቀማል።
```
> ይህ የመጀመሪያው የጥቅስ ብሎክ ነው።
>> ይህ ሁለተኛው የጥቅስ ብሎክ ነው።
>>> ይህ ሦስተኛው የጥቅስ ብሎክ ነው።
```
> ይህ የመጀመሪያው የጥቅስ ብሎክ ነው።
>> ይህ ሁለተኛው የጥቅስ ብሎክ ነው።
>>> ይህ ሦስተኛው የጥቅስ ብሎክ ነው።

### 2.5. የኮድ ጥቅስ
\``` ወይም \~~~ን ይጠቀማል።
~~~
```
git status
git add
git commit
```
~~~
```
git status
git add
git commit
```

የፕሮግራሚንግ ቋንቋውን በመግለጽ የሰነድ አቀራረብ ማጉላት(syntax highlighting) ማስነሳትም ይቻላል።
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

### 2.6. አገናኞች
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

በሪፖዚቶሪ ውስጥ ያሉ ሌሎች ፋይሎችን የሚያመለክቱ አንፃራዊ ዱካ አገናኞችም መጠቀም ይቻላል። አጠቃቀሙም በተርሚናል ውስጥ ካለው ጋር ተመሳሳይ ነው።
```
[README](../README.md)
```

### 2.7. ያልተደረደረ ዝርዝር
\- ወይም \*ን ይጠቀማል።
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. የተደረደረ ዝርዝር
ቁጥሮችን ይጠቀማል።
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. የተደራረበ ዝርዝር
```
1. የመጀመሪያ ዝርዝር ንጥል
   - የመጀመሪያ ውስጣዊ ዝርዝር ንጥል
     - ሁለተኛ ውስጣዊ ዝርዝር ንጥል
```
1. የመጀመሪያ ዝርዝር ንጥል
   - የመጀመሪያ ውስጣዊ ዝርዝር ንጥል
     - ሁለተኛ ውስጣዊ ዝርዝር ንጥል

### 2.10. የሚሠሩ ሥራዎች ዝርዝር
የሥራ ዝርዝር ለመፍጠር በእያንዳንዱ ንጥል ፊት \[ ] ይጨምራል።
የተጠናቀቀ ሥራ ለማመልከት \[x]ን ይጠቀማል።
```
- [x] ለውጦቼን ማጠናቀቅ
- [ ] commit ዎቼን ወደ GitHub መግፋት
- [ ] pull request መክፈት
```
- [x] ለውጦቼን ማጠናቀቅ
- [ ] commit ዎቼን ወደ GitHub መግፋት
- [ ] pull request መክፈት

### 2.11. ምስል ማከል
```
መንገድ: ![(አማራጭ, የሚመከር)የምስል መግለጫ](url){(አማራጭ)ተጨማሪ አማራጮች}
![የGitHub አርማ](/images/logo.png)
![የGitHub አርማ](/images/logo.png){: .align-center}
![የGitHub አርማ](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. ሰንጠረዥ መፍጠር
| እና -ን በመጠቀም ሰንጠረዥ መፍጠር ይቻላል።
ከሰንጠረዡ በፊት አንድ ባዶ መስመር መተው አለበት እንዲሁ በትክክል ይታያል።
ቢያንስ 3 ወይም ከዚያ በላይ - መጠቀም አለበት እንዲሁ በትክክል ይለያል።
```
 
| በግራ የተሰለፈ | በመካከል የተሰለፈ | በቀኝ የተሰለፈ |
| :---           |      :---:       |            ---: |
| git status     | git status       | git status      |
| git diff       | git diff         | git diff        |
```

| በግራ የተሰለፈ | በመካከል የተሰለፈ | በቀኝ የተሰለፈ |
| :---           |      :---:       |            ---: |
| git status     | git status       | git status      |
| git diff       | git diff         | git diff        |
