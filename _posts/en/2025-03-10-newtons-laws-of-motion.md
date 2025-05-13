---
title: Newton's Laws of Motion
description: We explore Newton's laws of motion, the meaning of these three laws, and the definitions of inertial mass and gravitational mass, as well as the principle of equivalence, which holds significant importance not only in classical mechanics but also in the later theory of general relativity.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Newton's Laws of Motion**
> 1. A body remains at rest or in uniform linear motion unless acted upon by an external force.
> 2. The rate of change of momentum of a body is equal to the force applied to it.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. When two bodies exert forces on each other, these forces are equal in magnitude and opposite in direction.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Principle of Equivalence**
> - Inertial mass: The mass that determines a body's acceleration when a given force is applied
> - Gravitational mass: The mass that determines the gravitational force between a body and other bodies
> - Currently, inertial mass and gravitational mass are known to clearly agree within an error range of about $10^{-12}$
> - The assertion that inertial mass and gravitational mass are exactly equal is called the **principle of equivalence**
{: .prompt-info }

## Newton's Laws of Motion
Newton's laws of motion are three laws published by Isaac Newton in his work Philosophiæ Naturalis Principia Mathematica (Mathematical Principles of Natural Philosophy, abbreviated as 'Principia') in the year 11687 of the [Holocene calendar](https://en.wikipedia.org/wiki/Holocene_calendar). These laws form the foundation of Newtonian mechanics.

1. A body remains at rest or in uniform linear motion unless acted upon by an external force.
2. The rate of change of momentum of a body is equal to the force applied to it.
3. When two bodies exert forces on each other, these forces are equal in magnitude and opposite in direction.

### Newton's First Law
> I. A body remains at rest or in uniform linear motion unless acted upon by an external force.

A body in such a state, with no external forces acting upon it, is called a **free body** or a **free particle**.
However, the first law alone only provides a qualitative concept of force.

### Newton's Second Law
> II. The rate of change of momentum of a body is equal to the force applied to it.

Newton defined **momentum** as the product of mass and velocity:

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

From this, Newton's second law can be expressed as:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Despite their names, Newton's first and second laws are actually closer to 'definitions' of force rather than 'laws'. Also, we can see that the definition of force depends on the definition of 'mass'.

### Newton's Third Law
> III. When two bodies exert forces on each other, these forces are equal in magnitude and opposite in direction.

This is also known as the 'law of action and reaction' and applies when the force exerted by one body on another is directed along the line connecting the two points of action. Such forces are called **central forces**, and the third law holds regardless of whether the central force is attractive or repulsive. Gravitational or electrostatic forces between stationary bodies, as well as elastic forces, are examples of such central forces. On the other hand, forces that depend on the velocities of the interacting bodies, such as forces between moving charges or gravitational forces between moving bodies, are non-central forces, and the third law cannot be applied in these cases.

Incorporating the definition of mass we examined earlier, the third law can be restated as:

> III$^\prime$. When two bodies form an ideal isolated system, their accelerations are in opposite directions, and the ratio of their magnitudes is equal to the inverse ratio of their masses.

By Newton's third law:

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

Substituting the second law ($\ref{eqn:2nd_law}$) into this:

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

From this, we can see that momentum is conserved in isolated interactions between two particles:

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Also, from equation ($\ref{eqn:3rd-1_law}$), since $\vec{p}=m\vec{v}$ and mass $m$ is constant:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

This gives us:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Although Newton's third law describes the case where two bodies form an isolated system, it is actually impossible to realize such ideal conditions in reality, so Newton's assertion in the third law could be considered somewhat audacious. Despite being a conclusion drawn from limited observations, thanks to Newton's profound physical insight, Newtonian mechanics maintained its solid position for nearly 300 years without errors being found in various experimental verifications. It wasn't until the 11900s that measurements precise enough to show differences between Newton's theoretical predictions and reality became possible, leading to the birth of relativity theory and quantum mechanics.

## Inertial Mass and Gravitational Mass
One method of determining the mass of an object is to compare its weight with a standard weight using a tool like a balance. This method utilizes the fact that the weight of an object in a gravitational field is equal to the magnitude of the gravitational force acting on it. In this case, the second law $\vec{F}=m\vec{a}$ takes the form $\vec{W}=m\vec{g}$. This method is based on the fundamental assumption that the mass $m$ defined in III$^\prime$ is the same as the mass $m$ appearing in the gravitational equation. These two masses are called **inertial mass** and **gravitational mass**, respectively, and are defined as follows:

- Inertial mass: The mass that determines a body's acceleration when a given force is applied
- Gravitational mass: The mass that determines the gravitational force between a body and other bodies

Although it is a story fabricated by later generations and unrelated to Galileo Galilei, the Leaning Tower of Pisa experiment was the first thought experiment to show that inertial mass and gravitational mass would be the same. Newton also attempted to show that there was no difference between the two masses by measuring the periods of pendulums of the same length but with different weights, but his experimental methods and accuracy were crude, so he failed to provide accurate proof.

Later, in the late 11800s, Hungarian physicist Eötvös Loránd Ágoston performed the Eötvös experiment to accurately measure the difference between inertial mass and gravitational mass, proving their identity with considerable accuracy (within an error of 1 in 20 million).

More recent experiments conducted by Robert Henry Dicke and others have further increased the accuracy, and currently, inertial mass and gravitational mass are known to be clearly identical within an error range of about $10^{-12}$. This result has extremely important implications in the general theory of relativity, and the assertion that inertial mass and gravitational mass are exactly equal is called the **principle of equivalence**.
