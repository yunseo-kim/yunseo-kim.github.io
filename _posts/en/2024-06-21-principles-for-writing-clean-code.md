---
title: Principles for Writing Clean Code
description: "Why writing good code matters, and core principles for clean, readable, maintainable software—plus PS/CP trade‑offs and practical examples."
categories: [Dev, Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Principles-for-Writing-Clean-Code/
---

## Why Writing Good Code Matters
If you only rush to write code for immediate implementation, [technical debt](/posts/Technical-debt/) can grow to an unmanageable level and cause maintenance problems later. Therefore, when undertaking a development project, it goes without saying that writing good code—readable and maintainable from the outset—is important.

In algorithmic problem solving (PS, Problem Solving) or competitive programming (CP, Competitive Programming), you usually won’t reuse the code after the problem set or contest ends; with CP in particular, time limits can make fast implementation more important than writing good code—so the argument goes. To answer this, you should reflect on why you do PS/CP and what you aim to get out of it.

From a programming-focused perspective (setting aside general problem-solving skill development), I think PS/CP can teach you the following:
- While solving problems within time and memory constraints, you can try and become familiar with various algorithms and data structures, which helps you develop an intuition for which ones to use in specific situations during real projects.
- Submitting code yields immediate, objective feedback on correctness, runtime, and memory usage, helping you practice writing accurate code quickly and proficiently without missing edge cases.
- You can study solutions written by strong competitors, compare them with your own, and find areas to improve.
- Compared to real-world projects, you write small programs with similar functionality repeatedly; especially when practicing PS alone, you can focus on details and practice writing concise, high-quality code without being tied to deadlines.

Enjoying PS/CP purely as a hobby is perfectly fine, of course. But if you do PS/CP to improve your programming skills, the last point—“practice writing good code”—is as valuable as the three above. Writing good code doesn’t come naturally; you need consistent practice and repetition. Moreover, convoluted code is hard to debug and even for the author is harder to get right the first time; you may end up wasting time on inefficient debugging and not actually implementing faster. While PS/CP differs greatly from industry work, neglecting code quality for the sake of speed is, for these reasons, putting the cart before the horse. Personally, I think it’s better even in PS/CP to write concise, efficient code.

> 12024.12 Additional comment:  
> Given the current trends, building background knowledge in algorithms and data structures and honing problem-solving skills will remain meaningful. But when it comes to turning that into working code, rather than insisting on writing every line yourself, it’s probably better to use AI tools like GitHub Copilot, Cursor, or Windsurf to save time and spend the saved time on other work or study. If you do PS/CP to study algorithms/data structures or simply as a hobby, no one will stop you; however, investing time and effort in PS/CP solely to practice coding now seems to yield much lower returns. I even expect that, in development roles, the importance of coding tests as hiring filters will likely drop quite a bit compared to before.
{: .prompt-warning }

## Principles for Writing Good Code
The criteria for good code are largely similar whether it’s for contests or production. This post covers core principles for writing good code in general. For PS/CP, there may be places where we compromise for speed compared to production; I’ll note those explicitly.

### Write Simple, Concise Code
> "KISS (Keep It Simple, Stupid)"

- The shorter and simpler the code, the fewer typos and trivial bugs, and the easier it is to debug.
- Aim to make code self-explanatory with minimal comments; add comments only when truly necessary. Prefer relying on simple structure over comments.
- When you do write comments, make them clear and concise.
- Keep a function’s parameters to three or fewer; if you need more, bundle them into an object.
- Avoid deep nesting in conditionals, which hurts readability. Prefer guard clauses.  
  e.g., using guard clauses below is more readable than the nested version above

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
- In PS/CP, some people take this further to shorten code for speed by using C/C++ macros. Under tight contest time limits that can be handy, but it’s a PS/CP-specific trick; in general-purpose C++, macro use should be avoided.  
  e.g.,

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularize Your Code
> "DRY (Don't Repeat Yourself)"

- When you repeat the same code, extract it into a function or class for reuse.
- Reuse via modularization improves readability and makes maintenance easier—future changes require modifying only the shared function or class.
- Ideally, a function should do one thing (single responsibility). In PS/CP, programs are small and simple, reuse is limited, and time is constrained, so strictly following this principle can be difficult.

### Use the Standard Library
> "Don't reinvent the wheel"

- When learning algorithms/data structures, implementing queues, stacks, sorting, etc. yourself is useful to understand the principles. Otherwise, prefer the standard library.
- Standard libraries are widely used, well-tested, and optimized—more efficient than reimplementing yourself.
- Using existing libraries avoids wasting time on duplicate implementations and makes your code easier for teammates to understand.

### Use Consistent, Clear Naming
> "Follow standard conventions"

- Use unambiguous variable and function names.
- Each language typically has its own naming conventions; learn those used by its standard library and apply them consistently to classes, functions, and variables.
- Name things so it’s clear what each variable, function, or class does; for booleans, make it obvious under what conditions they are true.

### Normalize All Data Before Storing
- Process all data in a single, consistent format.
- If the same data exists in multiple formats, subtle, hard-to-catch bugs can arise (e.g., slightly different string representations, different hash values).
- For time zones, strings, etc., convert inputs or computed values immediately to a single standard such as UTC and UTF-8. Perform normalization in the constructor of the class representing the data, or directly in the function that accepts it.

### Separate Code Logic from Data
- Don’t hard-code data unrelated to logic inside conditionals; move it into a separate table.  
  e.g., the version below is preferable to the one above

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
