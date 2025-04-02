---
title: Principle of Relativity and Lorentz Transformation
description: We explore the concept of reference frames and the Galilean transformation widely used in classical mechanics. We also briefly examine Maxwell's equations and the Michelson-Morley experiment, which formed the background for the emergence of the Lorentz transformation, and derive the transformation matrix of the Lorentz transformation.
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Principle of Relativity**: The principle that all physical laws must be the same in all inertial reference frames moving at constant velocities relative to each other
{: .prompt-info }

> **Lorentz Factor $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **Lorentz Transformation**
>
> $$ \begin{pmatrix}
> \vec{x}^\prime \\ ct^\prime
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & -\gamma\vec{\beta} \\
> -\gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}. $$
>
> - $ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $
> - $ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $
{: .prompt-info }

> **Inverse Lorentz Transformation**
>
> $$ \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & \gamma\vec{\beta} \\
> \gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x^\prime} \\ ct^\prime
> \end{pmatrix}. $$
>
> - $ \vec{x} = \gamma\vec{x^\prime}+\gamma\vec{\beta}ct^\prime $
> - $ ct = \gamma ct^\prime + \gamma \vec{\beta}\cdot\vec{x^\prime} $
{: .prompt-info }

## Reference Frames and the Principle of Relativity
### Frame of Reference
- **Frame of Reference**: When an object moves, its position changes relative to other objects. Since all motion is relative, a reference frame must be established to describe any motion.
- **Inertial Frames of Reference**: Frames in which Newton's first law of motion ("An object's state of motion remains unchanged as long as the net force acting on it is zero") holds. Any reference frame moving at a constant velocity relative to an inertial frame is also an inertial frame.

### Principle of Relativity
One of the key concepts and basic premises in physics, the principle states that all physical laws must be the same in all inertial reference frames moving at constant velocities relative to each other. If physical laws were different for observers moving relative to each other, these differences could be used to establish an absolute reference frame and determine who is stationary and who is moving. However, according to the principle of relativity, such distinctions do not exist, meaning there is no absolute reference frame or absolute motion with respect to the entire universe, and all inertial frames are equivalent.

## Limitations of the Galilean Transformation
### Galilean Transformation
Consider two inertial frames $S$ and $S^{\prime}$, where $S^{\prime}$ is moving at a constant velocity $\vec{v}$ in the $+x$ direction relative to $S$. Suppose the same event is observed in $S$ at coordinates $(x, y, z)$ at time $t$, and in $S^{\prime}$ at coordinates $(x^{\prime}, y^{\prime}, z^{\prime})$ at time $t^{\prime}$.

In this case, the $x$ direction value measured in $S^{\prime}$ will be greater than the value measured in $S$ by the distance $\vec{v}t$ that $S^{\prime}$ has moved relative to $S$ in the $x$ direction, so

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

Since there is no relative motion in the $y$ and $z$ directions,

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

And intuitively,

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

The coordinate transformation between different inertial frames as shown in equations ($\ref{eqn:galilean_transform_x}$) to ($\ref{eqn:galilean_transform_t}$) is called the **Galilean transformation**, which is simple and intuitive and works well in most everyday situations. However, as will be discussed later, it contradicts Maxwell's equations.

### Maxwell's Equations
In the late 11800s, Maxwell expanded on ideas and previous research results proposed by other scientists such as Faraday and Ampere, revealing that electricity and magnetism are actually a single force, and derived the following four equations describing the electromagnetic field:

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: The electric flux through any closed surface equals the net charge inside (Gauss's Law).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: Magnetic monopoles do not exist.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: Changes in magnetic fields create electric fields (Faraday's Law).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: Electric currents and changes in electric fields create magnetic fields (Ampere-Maxwell Law).}
\end{gather*}$$

Maxwell's equations successfully explained all previously known electrical and magnetic phenomena, predicted the existence of electromagnetic waves, and derived that the speed of electromagnetic waves in vacuum, $c$, is a constant, establishing them as the core formulas of electromagnetism.

### Contradiction Between Galilean Transformation and Maxwell's Equations
Newtonian mechanics, which utilizes the Galilean transformation, had been the foundation of physics for over 200 years, and Maxwell's equations, as mentioned above, are the core equations describing electrical and magnetic phenomena. However, there is a contradiction between the two:

- According to the principle of relativity, Maxwell's equations should also have the same form in all inertial frames, but when applying the Galilean transformation to convert measurements from one inertial frame to another, Maxwell's equations take on a very different form.
- The speed of light $c$ can be calculated from Maxwell's equations and is a constant, but according to Newtonian mechanics and the Galilean transformation, the speed of light $c$ is measured differently in different inertial frames.

Therefore, Maxwell's equations and the Galilean transformation are incompatible, and at least one of them needed to be modified. This became the background for the emergence of the **Lorentz transformation**.

## Aether Theory and the Michelson-Morley Experiment
Meanwhile, in 11800s physics, it was believed that light, like other waves such as water waves and sound waves, was transmitted through a hypothetical medium called *aether*, and efforts were made to discover this aether.

According to aether theory, even though outer space is a vacuum, it is filled with aether, so it was thought that Earth's orbital motion at about 30km/s relative to the Sun would create an aether wind across the Earth.  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Image source*
> - Author: Wikimedia user [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

To test this hypothesis, in [Human Era](https://en.wikipedia.org/wiki/Holocene_calendar) 11887, Michelson collaborated with Morley to conduct the *Michelson-Morley Experiment* using the interferometer shown below.  
![Michelson-Morley Interferometer](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Image source*
> - Author: Albert Abraham Michelson with Edward Morley
> - License: public domain

In this experiment, a light beam is split into two by passing through a half-mirror, then each beam travels back and forth along the two perpendicular arms of the interferometer, covering a total distance of about 11m, and meets at the midpoint. At this point, interference patterns appear according to the phase difference between the two light beams. According to aether theory, the speed of light would vary depending on the relative velocity to the aether, so this phase difference would change, resulting in observable changes in the interference pattern. However, no change in the interference pattern was observed. There were several attempts to explain this experimental result, among which FitzGerald and Lorentz proposed the *Lorentz-FitzGerald contraction* or *length contraction*, suggesting that an object contracts in length when <u>moving relative to the aether</u>, which led to the Lorentz transformation.

> At that time, Lorentz believed in the existence of aether and thought that length contraction occurred due to relative motion with respect to the aether. Later, Einstein interpreted the true physical meaning of the Lorentz transformation with his *Theory of Special Relativity*, explaining length contraction in terms of spacetime rather than aether, and it was also later revealed that aether does not exist.
{: .prompt-info }

## Lorentz Transformation
### Derivation of the Lorentz Transformation
In the same situation as the Galilean transformation (equations [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]), let's assume that the correct transformation relationship between $x$ and $x^{\prime}$ that does not contradict Maxwell's equations is as follows:

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Here, $\gamma$ is independent of $x$ and $t$ but may be a function of $\vec{v}$. This assumption can be made for the following reasons:

- For events in $S$ to correspond one-to-one with events in $S^{\prime}$, $x$ and $x^{\prime}$ must have a linear relationship.
- Since the Galilean transformation is known to be correct in everyday mechanical situations, it should be approximable by equation ($\ref{eqn:galilean_transform_x}$).
- The form should be as simple as possible.

Since physical formulas must have the same form in reference frames $S$ and $S^{\prime}$, to express $x$ in terms of $x^{\prime}$ and $t$, only the sign of $\vec{v}$ (the direction of relative motion) needs to be changed, and since there should be no difference between the two reference frames except for the sign of $\vec{v}$, $\gamma$ must be the same.

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

As with the Galilean transformation, there is no reason for the components perpendicular to the direction of $\vec{v}$, namely $y$ and $y^{\prime}$, and $z$ and $z^{\prime}$, to be different, so

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Substituting equation ($\ref{eqn:lorentz_transform_x}$) into ($\ref{eqn:lorentz_transform_x_inverse}$), we get

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

Solving for $t^{\prime}$,

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

Also, to avoid contradicting Maxwell's equations, the speed of light must be the same $c$ in both reference frames, which can be used to determine $\gamma$. If the origins of the two reference frames were at the same place when $t=0$, then by this initial condition, $t^\prime = 0$. Now, imagine that at $t=t^\prime=0$, there was a flash of light at the common origin of $S$ and $S^\prime$, and observers in each reference frame measure the speed of this light. In this case, in reference frame $S$,

$$ x = ct \label{eqn:ct_S}\tag{9}$$

and in reference frame $S^\prime$,

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Using equations ($\ref{eqn:lorentz_transform_x}$) and ($\ref{eqn:lorentz_transform_t}$) to substitute $x$ and $t$,

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Solving for $x$,

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

But from equation ($\ref{eqn:ct_S}$), $x=ct$, so

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

Therefore,

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Substituting this expression for $\gamma$ in terms of $\vec{v}$ into equations ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$), and ($\ref{eqn:lorentz_transform_t}$), we obtain the final transformation equations from reference frame $S$ to $S^\prime$.

### Lorentz Transformation Matrix

The final transformation equations obtained above are as follows:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

These equations are the **Lorentz transformation**. Setting $\vec{\beta}=\vec{v}/c$, they can be expressed in matrix form as follows:

$$ \begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix} 
= \begin{pmatrix}
\gamma & 0 & 0 & -\gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}. \label{lorentz_transform_matrix}\tag{16}$$

Lorentz showed that when using this transformation, the basic formulas of electromagnetism have the same form in all inertial reference frames. Also, when the velocity $v$ is very small compared to the speed of light $c$, $\gamma \to 1$, so it can be approximated by the Galilean transformation.

### Inverse Lorentz Transformation
Sometimes it is more convenient to transform measurements from the moving frame $S^\prime$ to the stationary frame $S$ rather than the other way around.
In such cases, the **inverse Lorentz transformation** can be used.  
By finding the inverse of the matrix in ($\ref{lorentz_transform_matrix}$), we obtain the following inverse Lorentz transformation matrix:

$$ \begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}
= \begin{pmatrix}
\gamma & 0 & 0 & \gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix}. \tag{17}
$$

This is equivalent to exchanging the primed and unprimed quantities in equations ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$) and replacing $v$ with $-v$ (i.e., $\beta$ with $-\beta$).

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
