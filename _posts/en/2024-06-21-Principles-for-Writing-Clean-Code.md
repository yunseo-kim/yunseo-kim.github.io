---
title: "Principles for Writing Good Code"
description: >-
  Explore the necessity of writing good code and the main principles generally used to write good code.
categories:
  - Programming
tags:
  - Coding
  - PS/CP
---
## The Necessity of Writing Good Code
If we focus only on quickly writing code for immediate implementation, [technical debt](/posts/Technical-debt/) can accumulate to an unmanageable level, causing problems with future maintenance. Therefore, it goes without saying that writing good, readable, and easily maintainable code from the start is crucial when conducting a development project.

In the case of Problem Solving (PS) or Competitive Programming (CP), there's an argument that since the code used to solve problems is usually not reused after the problem-solving session or competition ends, and especially in CP where there are time constraints, quick implementation is more important than writing good code. To answer this question, it's necessary to consider what you're doing PS/CP for and what direction you're pursuing.

Personally, I think the points that can be learned through PS/CP are as follows:
- You can use and become familiar with various algorithms and data structures in the process of solving problems within given execution time and memory limits, which can help you develop a sense of which algorithms and data structures to use in specific situations when working on actual projects
- After writing and submitting code, you can immediately receive objective feedback on correctness, execution time, and memory usage, allowing you to practice writing accurate code quickly and proficiently without missing any parts
- You can compare your code with that of other experts and find areas for improvement
- Compared to actual development projects, you repeatedly write smaller-scale code with similar functionality, so (especially when practicing PS alone) you can practice writing concise and good code while paying attention to details without being constrained by deadlines

While some people may enjoy PS/CP simply as a hobby, for those like me who do PS/CP indirectly to improve programming skills, the last point of 'practicing writing good code' is just as significant as the first three. This is because writing good code doesn't come naturally from the start but requires consistent practice through repetition. Moreover, complex and hard-to-read code is difficult to debug and not easy to write accurately in one go, so if you spend time on inefficient debugging, you may not even implement it quickly. Although PS/CP is quite different from real-world work, for these reasons, I personally try to write concise and efficient code even in PS/CP, rather than focusing solely on immediate implementation without any regard for writing good code.

## Principles for Writing Good Code
Whether it's code written for competitions or for practical work, the conditions for good code are not significantly different. This article covers the main principles for writing generally good code. However, in PS/CP, there may be areas where compromises are made relative to practical work for quick implementation, which will be mentioned separately in the article.

### Writing Concise Code
> "KISS (Keep It Simple, Stupid)"
- The shorter and more concise the code, the less likely it is to have typos or simple bugs, and the easier it is to debug
- Write in a way that can be easily interpreted without separate comments if possible, and add detailed explanations with comments only when absolutely necessary. It's preferable to maintain a concise code structure rather than relying on comments.
- If you write comments, make them clear and concise
- Limit the number of arguments passed to a function to three or fewer, and if more arguments need to be passed together, group them into a single object
- As the depth of conditional statements deepens to double or triple, it reduces readability, so increasing the depth of conditional statements should be avoided as much as possible.
  e.g., The code below using the Guard Clause idiom is more advantageous in terms of readability than the code above

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
- However, in PS/CP, to further reduce the length of code and write it quickly, there are cases where tricks like using macros in C/C++ are used. This can be useful if used occasionally for time-pressed competitions, but it's a method that only works for PS/CP and should generally be avoided in C++.
  e.g.,

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Code Modularization
> "DRY (Don't Repeat Yourself)"
- If the same code is used repeatedly, separate that part into functions or classes for reuse
- Active reuse of code through modularization improves readability, and when code needs to be modified later, only the relevant function or class needs to be modified once, making maintenance easier
- In principle, it's ideal for one function to perform only one task and not do two or more things. However, the code written in PS/CP is usually a small-scale program that performs simple functions, so there are limitations to reuse, and due to time constraints, it may be difficult to strictly follow the principles as in practical work.

### Utilizing Standard Libraries
> "Don't reinvent the wheel"
- While it's useful to implement data structures like queues and stacks or sorting algorithms directly to understand the principles when studying algorithms or data structures, otherwise, it's better to actively use standard libraries
- Standard libraries have already been used and verified countless times, and are well-optimized, making them more efficient than implementing them again yourself
- Using existing libraries saves time that would be wasted implementing the same functionality unnecessarily, and makes it easier for other team members to understand your code during collaboration

### Using Consistent and Clear Naming Conventions
> "Follow standard conventions"
- Use unambiguous variable and function names
- Usually, each programming language has its own naming conventions, so learn the naming conventions used in the standard library of the language you're using and consistently apply them when declaring classes, functions, variables, etc.
- Name variables, functions, and classes in a way that clearly shows what they do, and for boolean types, under what conditions they return True

### Normalize All Data for Storage
- Process all data in one consistent, normalized format
- If the same data has two or more formats, subtle bugs that are hard to catch can occur, such as slight differences in string representations or different hash values
- When storing and processing data such as time zones and strings, they should be converted to a single standard format like UTC or UTF-8 encoding as soon as they are received or calculated. It's good to perform normalization from the start in the constructor of the class representing that data, or to perform normalization immediately in the function receiving the data.

### Separate Code Logic and Data
- Data unrelated to the code's logic should not be directly inserted into conditional statements but separated into a separate table
  e.g., It's preferable to write like the code below rather than the code above.

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