---
title: Principle of Relativity and Lorentz Transformation
description: Learn about the concept of reference frames and the Galilean transformation
  widely used in classical mechanics. Also, briefly examine Maxwell's equations and
  the Michelson-Morley experiment, which formed the background for the emergence of
  the Lorentz transformation, and derive the transformation matrix of the Lorentz
  transformation.
categories: [Engineering Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Principle of Relativity**: The principle that all physical laws should be the same in all inertial reference frames moving at constant velocity relative to each other
{: .prompt-info }

> **Lorentz factor $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **Lorentz transformation**
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

> **Inverse Lorentz transformation**
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

## Reference Frames and Principle of Relativity
### Frame of Reference
- **Frame of reference**: Since all motion is relative, to describe any motion, a reference frame must be established as its basis. The movement of an object means that its position changes relative to other objects.
- **Inertial frames of reference**: A frame in which Newton's first law of motion ("The motion state of an object remains unchanged as long as the net force acting on the object is 0") holds. Any reference frame moving at a constant velocity relative to one inertial frame is an inertial frame.

### Principle of Relativity
One of the main concepts and basic premises in physics, stating that all physical laws should be the same in all inertial frames moving at constant velocities relative to each other. If observers moving relative to each other had different physical laws, this difference could be used to set up an absolute reference frame and determine who is stationary and who is moving. However, according to the principle of relativity, there is no such distinction, so there is no absolute reference frame or absolute motion for the entire universe, and all inertial frames are equivalent.

## Limitations of Galilean Transformation
### Galilean Transformation
Let there be two inertial frames $S$ and $S^{\prime}$, where $S^{\prime}$ is moving at a constant velocity $\vec{v}$ in the $+x$ direction relative to $S$, and the same event is observed to occur at coordinates $(x, y, z)$ at time $t$ in $S$, and at coordinates $(x^{\prime}, y^{\prime}, z^{\prime})$ at time $t^{\prime}$ in $S^{\prime}$.

In this case, the $x$ direction value of the motion measured in $S^{\prime}$ will be greater than the value measured in $S$ by $\vec{v}t$, which is the distance $S^{\prime}$ has moved relative to $S$ in the $x$ direction, so

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

and since there is no relative motion in the $y$ and $z$ directions,

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

and intuitively,

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

can be assumed. The coordinate transformation between different inertial frames classically used in physics, as shown in equations ($\ref{eqn:galilean_transform_x}$) to ($\ref{eqn:galilean_transform_t}$), is called the **Galilean transformation**, which is simple and intuitive as it fits most everyday situations. However, as will be discussed later, this contradicts Maxwell's equations.

### Maxwell's Equations
In the late 19th century, Maxwell expanded on the ideas and previous research results proposed by other scientists such as Faraday and Ampere, revealing that electricity and magnetism are actually one force, and derived the following four equations describing the electromagnetic field.

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: The electric flux through any closed surface is equal to the net charge inside (Gauss's law).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: Magnetic monopoles do not exist.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: Changes in magnetic field create an electric field (Faraday's law).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: Changes in electric field and current create a magnetic field (Ampère-Maxwell law).}
\end{gather*}$$

Maxwell's equations successfully explained all known electrical and magnetic phenomena, predicted the existence of electromagnetic waves, and derived that the speed of electromagnetic waves in vacuum, $c$, is an invariant constant, establishing themselves as the core formulas of electromagnetism.

### Contradiction Between Galilean Transformation and Maxwell's Equations
Newtonian mechanics using the Galilean transformation has been the foundation of physics for over 200 years, and Maxwell's equations are, as mentioned above, the core equations describing electrical and magnetic phenomena. However, there is a contradiction between the two:

- According to the principle of relativity, Maxwell's equations are expected to have the same form in all inertial frames, but when applying the Galilean transformation to convert values measured in one inertial frame to values measured in another inertial frame, Maxwell's equations take on a very different form.
- The magnitude of the speed of light $c$ can be calculated from Maxwell's equations and is an invariant constant, but according to Newtonian mechanics and the Galilean transformation, the speed of light $c$ is measured differently depending on the inertial frame.

Therefore, Maxwell's equations and the Galilean transformation do not match, and at least one of them had to be modified. This became the background for the emergence of the **Lorentz transformation**, which will be discussed later.

## Aether Theory and Michelson-Morley Experiment
Meanwhile, in 19th-century physics, it was believed that light, like other waves such as surface waves and sound waves, was transmitted by a hypothetical medium called *aether*, and efforts were made to discover the existence of this aether.

According to aether theory, even if outer space is a vacuum, it is filled with aether, so it was thought that an aether wind would be formed across the Earth due to the Earth's orbital motion, which moves at a speed of about 30km/s relative to the Sun.  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Image source*
> - Author: Wikimedia user [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

To verify this hypothesis, in 1887, Michelson collaborated with Morley to perform the *Michelson-Morley Experiment* using the interferometer shown below.  
![Michelson-Morley Interferometer](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Image source*
> - Author: Albert Abraham Michelson with Edward Morley
> - License: public domain

In this experiment, the light beam is split into two by passing through a half-mirror, then each travels back and forth along the two perpendicular arms of the interferometer for a total of about 11m, meeting at the midpoint. At this point, constructive or destructive interference patterns appear depending on the phase difference between the two light beams. According to aether theory, the speed of light would differ depending on the relative velocity to the aether, so it was expected that this phase difference would change, resulting in observable changes in the interference pattern. However, in reality, no change in the interference pattern could be observed. There were several attempts to explain this experimental result, among which FitzGerald and Lorentz proposed the *Lorentz–FitzGerald contraction* or *length contraction*, which states that an object contracts in length when it <u>moves relative to the aether</u>. This leads to the Lorentz transformation.

> At this time, Lorentz believed that aether existed and thought that length contraction occurred due to relative motion to the aether. Later, Einstein interpreted the true physical meaning of the Lorentz transformation with his *Theory of Special Relativity*, explaining length contraction in terms of spacetime rather than aether, and it was also later revealed that aether does not exist.
{: .prompt-info }

## Lorentz Transformation
### Derivation of the Lorentz Transformation
In the same situation as in the Galilean transformation (equations [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]) discussed earlier, let's assume that the correct transformation relationship between $x$ and $x^{\prime}$ that does not contradict Maxwell's equations is as follows:

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Here, $\gamma$ is independent of $x$ and $t$, but can be a function of $\vec{v}$. The reasons for this assumption are as follows:

- For events occurring in $S$ and $S^{\prime}$ to have a one-to-one correspondence, $x$ and $x^{\prime}$ must have a linear relationship.
- Since it is known that the Galilean transformation is correct in mechanics for everyday situations, it should be able to approximate equation ($\ref{eqn:galilean_transform_x}$).
- It should be in the simplest form possible.

Since physical formulas should have the same form in reference frames $S$ and $S^{\prime}$, to express $x$ in terms of $x^{\prime}$ and $t$, we only need to change the sign of $\vec{v}$ (the direction of relative motion), and since there should be no difference between the two reference frames except for the sign of $\vec{v}$, $\gamma$ should be the same.

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

As in the Galilean transformation, there is no reason for the components perpendicular to the direction of $\vec{v}$, $y$ and $y^{\prime}$, and $z$ and $z^{\prime}$, to be different, so we set

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Now, substituting equation ($\ref{eqn:lorentz_transform_x}$) into ($\ref{eqn:lorentz_transform_x_inverse}$),

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

Solving for $t^{\prime}$,

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

holds.

Also, to avoid contradiction with Maxwell's equations, the speed of light should be $c$ in both reference frames, which can be used to find $\gamma$. If the origins of the two reference frames were at the same place when $t=0$, then by this initial condition, $t^\prime = 0$. Now, let's consider a situation where there was a flash at the common origin of $S$ and $S^\prime$ when $t=t^\prime=0$, and observers in each reference frame measure the speed of this light. In this case, in reference frame $S$,

$$ x = ct \label{eqn:ct_S}\tag{9}$$

and in reference frame $S^\prime$,

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Using equations ($\ref{eqn:lorentz_transform_x}$) and ($\ref{eqn:lorentz_transform_t}$) to substitute $x$ and $t$ in the above equation,

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Solving this equation for $x$,

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

However, from equation ($\ref{eqn:ct_S}$) earlier, $x=ct$, so

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

Therefore,

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Substituting this equation for $\gamma$ as a function of $\vec{v}$ into equations ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$), ($\ref{eqn:lorentz_transform_t}$), we finally obtain the transformation equations from reference frame $S$ to $S^\prime$.

### Transformation Matrix of the Lorentz Transformation

The final transformation equations obtained above are as follows:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

These equations are the **Lorentz transformation**. If we let $\vec{\beta}=\vec{v}/c$, it can be expressed in matrix form as follows:

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

Lorentz showed that when using these transformation equations, the basic formulas of electromagnetism hold in the same form in all inertial reference frames. Also, we can confirm that when the velocity $v$ is very small compared to the speed of light $c$, $\gamma \to 1$, so it can be approximated by the Galilean transformation.

### Inverse Lorentz Transformation
Sometimes it is more convenient to transform measurements from the moving frame $S^\prime$ to measurements in the stationary frame $S$, rather than transforming measurements from the stationary frame $S$ to the moving frame $S^\prime$.
In such cases, the **inverse Lorentz transformation** can be used.  
By finding the inverse matrix of ($\ref{lorentz_transform_matrix}$), we obtain the following inverse Lorentz transformation matrix:

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

This is equivalent to swapping the primed and unprimed physical quantities in equations ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$) and replacing $v$ with $-v$ (i.e., $\beta$ with $-\beta$).

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
