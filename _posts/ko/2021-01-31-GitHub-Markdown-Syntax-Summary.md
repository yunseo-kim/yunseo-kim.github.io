---
title: GitHub 마크다운 문법 정리
description: Markdown이 무엇인지 알아보고, GitHub Pages 블로그 호스팅을 위해 GitHub Flavored Markdown
  기준으로 주요 Markdown 문법을 정리하였다.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
---
GitHub Pages 활용을 위해서는 **markdown** 문법에 대해 알 필요가 있다.
GitHub 공식 문서의 [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)과 [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)를 참고하여 작성하였다.

## 1. 마크다운이란
> **마크다운(markdown)**은 일반 텍스트 기반의 경량 마크업 언어다. 일반 텍스트로 서식이 있는 문서를 작성하는 데 사용되며, 일반 마크업 언어에 비해 문법이 쉽고 간단한 것이 특징이다. HTML과 리치 텍스트(RTF) 등 서식 문서로 쉽게 변환되기 때문에 응용 소프트웨어와 함께 배포되는 README 파일이나 온라인 게시물 등에 많이 사용된다.  
> 존 그루버는 [인류력](https://en.wikipedia.org/wiki/Holocene_calendar) 12004년에 문법 면에서 에런 스워츠와 중대한 협업을 통해 마크다운 언어를 만들었으며, 사람들이 읽기 쉽고 쓰기 쉬운 플레인 텍스트 포맷을 사용하여 쓸 수 있으면서 구조적으로 유효한 XHTML(또는 HTML)로 선택적 변환이 가능하게 하는 것이 목표이다.

-[위키백과, 마크다운](https://en.wikipedia.org/wiki/Markdown)

## 2. 마크다운 문법
마크다운은 정해진 표준이 없기 때문에 세부 문법은 사용처마다 조금씩 다를 수 있다. 여기서 정리한 마크다운 문법은 [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 기준이다.

### 2.1. 줄바꿈, 문단 구분
마크다운에서는 엔터키 한 번은 줄바꿈으로 인식하지 않는다.
~~~
첫째 문장.
둘째 문장.
셋째 문장.
~~~
첫째 문장.
둘째 문장.
셋째 문장.

줄바꿈은 공백을 연속하여 두 칸 이상 입력하면 적용된다.
~~~
첫째 문장.  
둘째 문장.  
셋째 문장.
~~~
첫째 문장.  
둘째 문장.  
셋째 문장.

문단과 문단 사이는 빈 줄(엔터키 두 번)로 구분한다.
~~~
하나의 문단.

다른 문단.
~~~
하나의 문단.

다른 문단.

### 2.2. 글머리(Headers)
총 6단계가 있다.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
H1 태그는 원칙적으로 한 페이지에 하나만 있어야 하므로, 보통 포스트나 문서 작성 시에는 직접 쓸 일은 잘 없다.

### 2.3. 강조
```
*This text is italicized*
_This is italicized too_

**This is bold text**
__This is bold text too__

~~This was mistaken text~~

_You **can** combine them_

***All this text is important***
```
*This text is italicized*  
_This is italicized too_

**This is bold text**  
__This is bold text too__

~~This was mistaken text~~

_You **can** combine them_

***All this text is important***

### 2.4. 텍스트 인용
\>을 이용한다.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. 코드 인용
\``` 또는 \~~~을 이용한다.
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

프로그래밍 언어를 지정하여 문법 강조 표시를 활성화할 수도 있다.
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

### 2.6. 링크
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

리퍼지토리 내의 다른 파일을 가리키는 상대경로 링크도 사용할 수 있다. 사용법은 터미널에서와 동일하다.
```
[README](../README.md)
```

### 2.7. 비정렬 목록
\-나 \*을 이용한다.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. 정렬 목록
숫자를 이용한다.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. 중첩 목록
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. 할 일 목록
할 일 목록을 만드려면 각 항목 앞에 \[ ]을 추가한다.
완료된 일을 표시하려면 \[x]을 이용한다.
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. 이미지 첨부
```
방법: ![(선택)이미지 설명](url){(선택)추가옵션}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. 표 생성
|와 -을 이용해 표를 생성할 수 있다.
표 앞에 한줄을 비워 놓아야 정상적으로 표시된다.
적어도 3개 이상의 -을 사용해야 정상적으로 인식한다.
```

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
