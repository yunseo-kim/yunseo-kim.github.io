---
title: Newton's Laws of Motion
description: Explore Newton's laws of motion, their meanings, the definitions of inertial and gravitational mass, and the principle of equivalence, which is significant not only in classical mechanics but also in the later theory of general relativity.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Newton's laws of motion**
> 1. An object remains at rest or in uniform motion in a straight line unless acted upon by an external force.
> 2. The rate of change of momentum of a body is equal to the force applied to it.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. When two bodies exert forces on each other, these forces are equal in magnitude and opposite in direction.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Principle of equivalence**
> - Inertial mass: The mass that determines an object's acceleration when a given force is applied
> - Gravitational mass: The mass that determines the gravitational force between an object and other objects
> - Currently, inertial mass and gravitational mass are known to be clearly identical within an error range of about $10^{-12}$
> - The assertion that inertial mass and gravitational mass are exactly the same is called the **principle of equivalence**
{: .prompt-info }

## Newton's Laws of Motion
Newton's laws of motion are three laws published by Isaac Newton in 1687 through his work Philosophiæ Naturalis Principia Mathematica (Mathematical Principles of Natural Philosophy, abbreviated as 'Principia'), forming the foundation of Newtonian mechanics.

1. An object remains at rest or in uniform motion in a straight line unless acted upon by an external force.
2. The rate of change of momentum of a body is equal to the force applied to it.
3. When two bodies exert forces on each other, these forces are equal in magnitude and opposite in direction.

### Newton's First Law
> I. An object remains at rest or in uniform motion in a straight line unless acted upon by an external force.

An object in this state, without any external force acting on it, is called a **free body** or a **free particle**.
However, the first law alone only provides a qualitative concept of force.

### Newton's Second Law
> II. The rate of change of momentum of a body is equal to the force applied to it.

Newton defined **momentum** as the product of mass and velocity:

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

From this, Newton's Second Law can be expressed as:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Newton's First and Second Laws, despite their names, are actually closer to 'definitions' of force rather than 'laws'. It's also evident that the definition of force depends on the definition of 'mass'.

### Newton's Third Law
> III. When two bodies exert forces on each other, these forces are equal in magnitude and opposite in direction.

This physical law is also known as the 'law of action and reaction', and applies when the force exerted by one object on another is directed along the line connecting the two points of action. Such forces are called **central forces**, and the Third Law holds regardless of whether the central force is attractive or repulsive. Gravity or electrostatic force between stationary objects, and elastic force are examples of such central forces. On the other hand, forces that depend on the velocities of the interacting objects, such as the force between moving charges or gravity between moving objects, are non-central forces, and in these cases, the Third Law cannot be applied.

Reflecting the definition of mass we examined earlier, the Third Law can be rephrased as follows:

> III$^\prime$. If two objects form an ideal isolated system, the accelerations of these two objects are in opposite directions, and the ratio of their magnitudes is equal to the inverse ratio of the masses of the two objects.

According to Newton's Third Law:

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

Applying the Second Law ($\ref{eqn:2nd_law}$) we examined earlier to this:

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

From this, we can see that momentum is conserved in the isolated interaction of two particles.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Also, in equation ($\ref{eqn:3rd-1_law}$), since $\vec{p}=m\vec{v}$ and mass $m$ is constant:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

From this, we obtain:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

However, while Newton's Third Law describes the case where two objects form an isolated system, it is actually impossible to realize such ideal conditions in reality. In this sense, Newton's assertion in the Third Law could be seen as quite bold. Despite being a conclusion drawn from limited observations, thanks to Newton's deep physical insight, Newtonian mechanics held a firm position for nearly 300 years without errors being found in various experimental verifications. It was not until the 20th century that measurements precise enough to show differences between Newton's theoretical predictions and reality became possible, leading to the birth of the theory of relativity and quantum mechanics.

## Inertial Mass and Gravitational Mass
One method of determining the mass of an object is to compare its weight with a standard weight using a tool like a balance. This method utilizes the fact that the weight of an object in a gravitational field is equal to the magnitude of the gravitational force acting on that object. In this case, the Second Law $\vec{F}=m\vec{a}$ takes the form $\vec{W}=m\vec{g}$. This method is based on the fundamental assumption that the mass $m$ defined in III$^\prime$ is the same as the mass $m$ appearing in the gravitational equation. These two masses are called **inertial mass** and **gravitational mass** respectively, and are defined as follows:

- Inertial mass: The mass that determines an object's acceleration when a given force is applied
- Gravitational mass: The mass that determines the gravitational force between an object and other objects

Although it's a story made up in later generations unrelated to Galileo Galilei, the Leaning Tower of Pisa experiment is a thought experiment that first showed that inertial mass and gravitational mass would be the same. Newton also attempted to show that there was no difference between the two masses by measuring the periods of pendulums of the same length but with different bob masses, but his experimental method and accuracy were crude, so he failed to provide accurate proof.

Later, at the end of the 19th century, Hungarian physicist Loránd Eötvös conducted the Eötvös experiment to accurately measure the difference between inertial mass and gravitational mass, proving their identity with considerable accuracy (within an error of 1 in 20 million).

More recent experiments conducted by Robert Henry Dicke and others have further increased accuracy, and currently, inertial mass and gravitational mass are known to be clearly identical within an error range of about $10^{-12}$. This result has extremely important implications in the general theory of relativity, and the assertion that inertial mass and gravitational mass are exactly the same is called the **principle of equivalence**.
