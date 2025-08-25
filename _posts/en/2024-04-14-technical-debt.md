---
title: Technical Debt
description: "Learn what technical debt is, why it arises in software projects, and how to minimize it with conventions, clean code, automation, and refactoring."
categories: [Dev, Programming]
tags: [Coding]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Technical-debt/
---

## Technical Debt
> **Technical debt**  
> The future cost incurred by taking shortcuts to finish the current project faster in order to meet immediate requirements
{: .prompt-info }

Just as taking on financial debt lets you invest quickly where needed but brings financial pressure and requires repaying principal with interest, rushing development to meet urgent needs—even if the code gets a bit messy—tends to increase complexity and duplication, making it harder to implement new features or scale later.

Like how companies leverage debt to invest at the right time to develop new products and grow market share, or how individuals take loans to buy a home, taking on technical debt to ship features quickly isn’t inherently bad. The key is to reduce its accumulation and manage it at a level you can handle.

## Why Technical Debt Occurs
Even highly capable developers inevitably create technical debt during development; preventing it entirely is impossible.
As a service evolves and the original design hits its limits, you may need to revise designs—even for code that was once readable and worked well.
As technology advances and once-dominant libraries/frameworks fall out of favor, you may decide to switch stacks; in such cases, the existing code also becomes a form of technical debt.

Other common causes include:
- Failing to document designs as the project progresses, making it hard for others—or for your future self—to understand the code later
- Not removing unused variables or database fields
- Not automating repetitive tasks (deploy/build, etc.), incurring extra time and effort each time
- Urgent specification changes

## How to Minimize Technical Debt
### Setting Conventions Among Developers
- When not working solo, agree on language and tech stack, project directory structure, coding style, etc., to collaborate smoothly
- Decide what to standardize and where to leave room for individual autonomy
- Use code reviews to understand each other's styles and exchange feedback

### Writing Clean Code & Refactoring
- If messy existing code impedes development, refactoring to clarify structure can pay down technical debt
- The messier the spaghetti code, the harder refactoring becomes; in extreme cases you might abandon refactoring, discard the code, and rewrite from scratch
- Strive to write readable, maintainable code from the outset whenever possible
