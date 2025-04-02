---
title: Principles for Writing Good Code
description: Exploring the necessity of writing good code and the key principles for writing good code in general.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.jpg
---
## The Necessity of Writing Good Code
If you focus only on writing code quickly for immediate implementation, [technical debt](/posts/Technical-debt/) can grow to an unmanageable level, causing maintenance problems later. Therefore, it goes without saying that writing readable and maintainable code from the beginning is important when working on development projects.

In the case of Problem Solving (PS) or Competitive Programming (CP), there's an argument that since the code used to solve problems is typically not reused after the problem-solving session or competition ends, and especially in CP where time constraints exist, quick implementation might be more important than writing good code. To answer this question, you need to consider why you're doing PS/CP and what direction you're pursuing.

In my opinion, here are the things you can learn through PS/CP:
- You can use and become familiar with various algorithms and data structures while solving problems within given execution time and memory limits, which helps develop intuition about which algorithms and data structures to use in specific situations in real projects
- You receive immediate objective feedback on correctness, execution time, and memory usage after writing and submitting code, allowing you to practice writing accurate code quickly and proficiently without missing anything
- You can compare your code with that of more skilled programmers and find areas for improvement
- You repeatedly write code of smaller scale compared to actual development projects, with similar functionality, so (especially when practicing PS alone) you can practice writing concise and good code with attention to detail without being constrained by deadlines

While some may enjoy PS/CP simply as a hobby, if you're doing PS/CP indirectly to improve your programming skills, the last point about 'practicing writing good code' is just as significant as the first three. Writing good code doesn't come naturally from the beginning but requires consistent practice through repetition. Additionally, complex and difficult-to-read code is hard to debug and even difficult for you to write correctly the first time, so inefficient debugging can often prevent quick implementation. Although PS/CP is certainly different from professional work, completely ignoring good code practices and focusing only on immediate implementation is, for the reasons mentioned above, putting the cart before the horse. Therefore, I personally think it's better to write concise and efficient code even in PS/CP.

> 12024.12 additional comment:  
> Given the current trends, unless you're majoring in computer science and planning to make development your profession, if you're using programming as a means for numerical analysis or experimental data interpretation, it might be better to actively use AI tools like GitHub Copilot, Cursor, or Windsurf to save time and use that saved time to study other things. If you enjoy PS/CP as a hobby, no one will stop you, but spending time and effort on PS/CP for code writing practice now seems to have a low cost-benefit ratio. Even for development positions, I expect that coding tests as part of the hiring process will likely become significantly less important than before.
{: .prompt-warning }

## Principles for Writing Good Code
Whether it's code written for competitions or for professional work, the conditions for good code aren't very different. This article covers the main principles for writing good code in general. However, in PS/CP, there may be some compromises made for quick implementation compared to professional work, which I'll mention separately in the article.

### Writing Concise Code
> "KISS (Keep It Simple, Stupid)"

- The shorter and more concise the code, the less likely it is to have typos or simple bugs, and debugging becomes easier
- Write code that can be easily interpreted without additional comments, and add comments only when really necessary for detailed explanations. It's better to maintain a concise code structure rather than relying on comments.
- If you do write comments, make them clear and concise
- Keep the number of parameters passed to a function to three or fewer, and if more parameters need to be passed together, group them into a single object
- Deeply nested conditional statements (double, triple depth) reduce readability, so increasing the depth of conditional statements should be avoided if possible.  
  e.g.) The code below using Guard Clauses is more readable than the code above

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
- However, in PS/CP, there are occasionally tricks used to further reduce code length for quick writing, such as using macros in C/C++. This can be useful in time-constrained competitions, but it's a technique that only works in PS/CP, and generally, the use of macros in C++ should be avoided.  
  e.g.)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Code Modularization
> "DRY (Don't Repeat Yourself)"

- When the same code is used repeatedly, separate that part into functions or classes for reuse
- Active reuse of code through modularization improves readability, and when code needs to be modified later, you only need to modify the function or class once, making maintenance easier
- In principle, it's ideal for a function to perform only one task rather than two or more. However, code written in PS/CP is usually a small-scale program performing simple functions, so there are limitations to reuse, and with time constraints, it may be difficult to follow principles as strictly as in professional work.

### Utilizing Standard Libraries
> "Don't reinvent the wheel"

- While it's useful to implement data structures like queues and stacks or sorting algorithms yourself to understand the principles when studying algorithms or data structures, otherwise, it's better to actively use standard libraries
- Standard libraries have been used and verified countless times, and are well-optimized, making them more efficient than implementing them yourself
- Using existing libraries saves time that would be wasted implementing the same functionality, and makes it easier for other team members to understand your code during collaboration

### Using Consistent and Clear Naming Conventions
> "Follow standard conventions"

- Use unambiguous variable and function names
- Each programming language typically has its own naming conventions, so learn the naming conventions used in the standard library of the language you're using and apply them consistently when declaring classes, functions, variables, etc.
- Name variables, functions, and classes to clearly indicate what they do, and for boolean types, what conditions return True

### Normalize All Data for Storage
- Process all data in one consistent, normalized format
- If the same data has two or more formats, subtle bugs that are difficult to catch can occur, such as slightly different string representations or different hash values
- When storing and processing data such as time zones and strings, convert them to a single standard format such as UTC or UTF-8 encoding as soon as they are received or calculated. It's good to perform normalization from the beginning in the constructor of the class representing the data, or to perform normalization immediately in the function receiving the data.

### Separate Code Logic and Data
- Data unrelated to code logic should not be directly included in conditional statements but separated into separate tables  
  e.g.) Writing code like the example below is preferable to the one above.

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
