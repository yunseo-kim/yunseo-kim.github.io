---
title: "Technical Debt"
description: >-
  Let's explore the concept of technical debt, why it occurs, and how to minimize it.
categories: [Programming]
tags: [Coding]
---

## Technical Debt
Technical debt: The cost that must be paid later by choosing shortcuts that can complete the project at hand faster to meet immediate requirements during the development process.

Just as taking on financial debt allows for quick investment in urgent needs but leads to financial pressure and repayment with interest, quickly developing to solve immediate requirements with slightly messy code results in increased complexity and duplication, making it difficult to implement or expand new features later.

Taking on technical debt to quickly implement new features is not necessarily bad, similar to how companies use debt to invest in new product development and increase market share, or individuals take out loans to buy houses. However, it's desirable to reduce the accumulation of technical debt and manage it at a sustainable level.

## Reasons for Technical Debt
Even if a developer's capabilities are sufficient, technical debt inevitably occurs in the software development process and cannot be completely prevented.
As a service evolves, existing code design may reach its limits, requiring modifications even to previously readable and well-functioning code.
Also, as technology itself advances, libraries/frameworks that were once mainstream may fall out of use, leading to decisions to change the tech stack to different libraries/frameworks, in which case the existing code becomes a kind of technical debt.

Technical debt can also occur for the following reasons:
- Failing to document designs in a timely manner during project progress, making it difficult for others or even oneself to interpret the code later
- Not removing variables or database items that are no longer in use
- Not automating repetitive tasks (deployment/build, etc.), requiring additional time and effort each time
- Urgent specification changes

## Methods to Minimize Technical Debt
### Establishing Conventions Between Developers
- When not developing alone, agreement is needed on languages, tech stacks, project directory structures, development styles, etc., for smooth collaboration
- Decide how much to unify methods and where to allow individual autonomy
- Code reviews are necessary to check each other's development styles and exchange opinions

### Writing Clean Code & Refactoring
- If existing code is messy and hinders development, technical debt can be cleared through refactoring to improve code structure
- Naturally, the messier the existing spaghetti code, the more difficult refactoring becomes
- Effort should be made to write readable and easily maintainable code from the start