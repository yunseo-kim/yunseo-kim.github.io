---
title: "Technical debt"
description: >-
  Let's explore the concept of technical debt, reasons for its occurrence, and methods to minimize it.
categories: [Programming]
tags: [Coding]
---

## Technical debt
Technical debt: The cost that must be paid later by choosing shortcuts that can complete the immediate project faster to meet immediate requirements during the development process.

Just as taking on financial debt allows for quick investment in immediate needs but leads to financial pressure and repayment with interest, quickly developing to solve immediate requirements with slightly messy code results in code becoming complex and redundant, making it difficult to implement or expand new features later.

Taking on technical debt to quickly implement new features is not necessarily bad, similar to how companies use debt to invest in new product development and increase market share, or individuals take out loans to buy houses. However, it is desirable to reduce the accumulation of technical debt and manage it at a manageable level.

## Reasons for technical debt occurrence
Even if a developer's capabilities are sufficient, technical debt inevitably occurs in the software development process and cannot be completely prevented.
As a service evolves, existing code design may reach its limits, and even originally readable and well-functioning code may need to be modified.
Also, as technology itself advances, when libraries/frameworks that were once mainstream are no longer widely used, one might decide to change the technology stack to different libraries/frameworks, in which case the previously written code becomes a kind of technical debt.

Technical debt can also occur for the following reasons:
- Difficulty in interpreting code when others or oneself revisit it later due to not documenting designs in a timely manner during project progress
- Not removing variables or DB items that are no longer in use
- Spending additional time and effort each time due to not automating repetitive tasks (deployment/build, etc.)
- Urgent specification changes

## Methods to minimize technical debt
### Setting conventions between developers
- When not developing alone, agreement is needed on languages, technology stacks, project directory structures, development styles, etc., for smooth collaboration
- Decisions must be made on what aspects of development to unify and what to leave to individual autonomy
- It is necessary to confirm each other's development styles and share opinions through code reviews

### Writing clean code & refactoring
- If existing code is messy and hinders development, technical debt can be cleared through refactoring, which cleanly changes the code structure
- Naturally, the messier the existing code (spaghetti code), the higher the difficulty of refactoring
- Efforts should be made to write readable and easily maintainable code from the beginning as much as possible