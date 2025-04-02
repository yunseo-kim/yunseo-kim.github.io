---
title: Separation of Variables
description: Explore the method of separation of variables and introduce related examples.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## Separation of Variables
**Separable equation**: An equation that can be expressed in the form $g(y)y'=f(x)$ through algebraic manipulation.

Integrating both sides of a separable equation $g(y)y'=f(x)$ with respect to $x$ yields:

$$ \int g(y)y'dx = \int f(x)dx + c $$

Since $y'dx=dy$, we get:

$$ \int g(y)dy = \int f(x)dx + c $$

This allows us to separate the expressions involving variable $x$ and $y$ on the right and left sides, respectively. If $f$ and $g$ are continuous functions, we can calculate these integrals to obtain the general solution of the given differential equation. This solving method is called **separation of variables**.

## Modeling Example: Radiocarbon Dating
Oetzi is a Neolithic mummy discovered in the Oetztal Alps in 11991 HE (Holocene Era). If the ratio of carbon-14 to carbon-12 in this mummy is 52.5% of that in living organisms, approximately when did Oetzi live and die?
> The ratio of radioactive carbon-14 to carbon-12 is constant in the atmosphere and living organisms. When an organism dies, carbon-14 absorption through respiration and eating stops, but carbon-14 decay continues, causing the ratio of radioactive carbon to decrease. Thus, by comparing the radioactive carbon ratio in fossils to that in the atmosphere, we can estimate the age of fossils. The half-life of carbon-14 is 5715 years.
{: .prompt-info }

### Solution
Separating variables in the ordinary differential equation $y'=ky$ and integrating gives:

$$\frac {dy}{y}=k dt$$

$$ \log |y|=kt+c $$

$$ y=y_{0}e^{kt}\ (y_0=e^c) $$

To determine the constant $k$, we use the half-life $H=5715$:

$$ y_{0}e^{kH}=0.5y_0 $$

$$e^{kH}=0.5$$

$$ k=\frac {\log 0.5}{H}=-\frac {0.693}{5715}=-0.0001213. $$

Finally, to find the time $t$ when Oetzi died, we substitute the ratio 52.5%:

$$ e^{kt}=e^{-.0.0001213t}=0.525$$

$$ t=\frac {\log 0.525}{-0.0001213}=5312.$$

$$ \therefore \text{Estimated death about 5310 years ago, around 6680 HE}. $$

## Modeling Example: Mixing Problem
Initially, a tank contains 1000L of water with 10kg of dissolved salt. Salt water flows in at a rate of 10L per minute, containing 0.2kg of dissolved salt per liter. The solution in the tank is well-stirred and maintained uniformly, and this salt water flows out at a rate of 10L per minute. Find the amount of salt $y(t)$ in the tank at time $t$.

### 1. Model Setup

$$ y'=\text{rate in} - \text{rate out}. $$

The salt inflow rate is 2kg per minute. The salt water outflow per minute is 0.01 of the total salt water volume, so the salt outflow per minute is $0.01 y(t)$. Therefore, the model is the ordinary differential equation:

$$y'=2-0.01y=-0.01(y-200) $$

### 2. Model Solution
The differential equation we just set up is separable. Let's separate variables, integrate, and then take the exponential of both sides:

$$ \frac {dy}{y-200}=-0.01 dt $$

$$ \log |y-200| = -0.01t+c^* $$

$$ y-200=ce^{-0.01t}. $$

Initially, the amount of salt in the tank is 10kg, so the initial condition is $y(0)=10$. Substituting $y=10,\ t=0$ into the above equation gives $10-200=ce^0=c$, thus $c=-190$.

$$ \therefore y(t)=200-190e^{-0.01t} $$

In other words, we can see that the amount of salt in the tank exponentially approaches and converges to 200kg in the given situation.

## Modeling Example: Newton's Law of Cooling
In winter, the daytime temperature of an office building is maintained at 20°C. The heating is turned off at 10 PM and turned back on at 6 AM. At 2 AM one day, the internal temperature of the building was 17.4°C. The external temperature was 10°C at 10 PM and dropped to 4°C at 6 AM. What was the internal temperature of the building when the heating was turned on at 6 AM?
> **Newton's Law of Cooling**  
> The rate of change of the temperature T of an object over time is proportional to the difference between the temperature of the object and its surroundings
{: .prompt-info }

### 1. Model Setup
Let $T(t)$ be the internal temperature of the building and $T_A$ be the external temperature. Then, according to Newton's Law of Cooling:

$$ \frac {dT}{dt}=k(T-T_A) $$

### 2. General Solution
We only know that $T_A$ changes between 10°C and 4°C, but we don't know its exact value, so we can't solve the equation we just set up. In such cases, *it can be helpful to attempt a solution by simplifying the situation to an easier problem*. The average of the two known values is 7°C, so let's assume the unknown function $T_A$ is a constant function $T_A=7$. Even if not exact, we can expect to obtain an approximate value of the internal building temperature $T$ at 6 AM that we're trying to find.

For the constant $T_A=7$, the differential equation we set up earlier is separable. By separating variables, integrating, and taking the exponential, we can obtain the general solution:

$$ \frac {dT}{T-7}=k dt $$

$$ \log |T-7|=kt+c^* $$

$$ T(t)=7+ce^{kt} \quad(c=e^{c^*}).$$

### 3. Particular Solution
Let's choose 10 PM as $t=0$, then the given initial condition is $T(0)=20$. Let's call the particular solution we obtain at this time $T_p$. Substituting:

$$ T(0)=7+ce^0=20 $$

$$ c=20-7=13 $$

$$ T_p(t)=7+13e^{kt}. $$

### 4. Determining $k$
Since the internal building temperature was 17.4°C at 2 AM, $T(4)=17.4$. If we algebraically find the value of $k$ and insert $k$ into $T_p(t)$:

$$ T_p(4)=7+13e^{4k}=17.4 $$

$$ e^{4k}=0.8 $$

$$ k=\frac {1}{4} \log 0.8=-0.056 $$

$$ T_p(t)=7+13e^{-0.056t}. $$

### 5. Answer and Interpretation
6 AM is $t=8$, so:

$$ T_p(8)=7+13e^{-0.056\cdot8}=15.3\text{[°C]}. $$

## Modeling Example: Torricelli's Theorem
A tank has a diameter of 2m and a hole with a diameter of 1cm. When the hole is opened, the initial water height is 2.25m. Find the water height in the tank at any time and the time it takes for the tank to empty.
> **Torricelli's Theorem**  
> The velocity of water flowing out under the influence of gravity is:
>
> $$ v(t)=0.600\sqrt{2gh(t)}. $$
>
> $h(t)$: Water height above the hole at time $t$
> $g=980\text{cm/s²}$: Gravitational acceleration at the Earth's surface
{: .prompt-info }

### 1. Model Setup
The outflow volume $\Delta V$ during a short time $\Delta t$ is:

$$ \Delta V = Av\Delta t \qquad (A: \text{Area of the hole})$$

$\Delta V$ must be equal to the change in volume $\Delta V^*$ of water in the tank. Also,

$$ \Delta V^* = -B\Delta h \qquad (B: \text{Cross-sectional area of the tank}) $$

where $\Delta h(>0)$ is the decrease in water height $h(t)$. Setting $\Delta V$ and $\Delta V^*$ equal:

$$ -B\Delta h = Av\Delta t $$

Now, expressing $v$ according to Torricelli's theorem and letting $\Delta t$ approach infinitely close to 0, we obtain the following model expressed as a first-order ordinary differential equation:

$$ \frac {\Delta h}{\Delta t} = -\frac {A}{B}v = -\frac{A}{B}0.600\sqrt{2gh(t)} $$

$$ \frac {dh}{dt} = \lim_{t\to0}\frac {\Delta h}{\Delta t} = -26.56\frac {A}{B}\sqrt{h}. $$

### 2. General Solution
This differential equation is separable. Separating variables and integrating:

$$ \frac {dh}{\sqrt{h}} = -26.56\frac{A}{B}dt $$

$$ 2\sqrt{h} = c^* - 26.56\frac{A}{B}t $$

Dividing both sides by 2 and squaring gives $h=(c-13.28At/B)^2$. Substituting $13.28A/B=13.28 \cdot 0.5^2 \pi /100^2 \pi = 0.000332$, we get the general solution:

$$ h(t)=(c-0.000332t)^2 $$

### 3. Particular Solution
The initial condition is $h(0)=225\text{cm}$. Substituting $t=0$ and $h=225$ into the general solution gives $c^2=225, c=15.00$, thus we obtain the particular solution:

$$ h_p(t)=(15.00-0.000332t)^2 $$

### 4. Time for the Tank to Empty

$$ t = 15.00/0.000332 = 45181 \text{[s]} = 12.6 \text{[h]}. $$

## Transformation to Separable Form
In some cases, differential equations that are not separable can be made separable by introducing a new unknown function of $y$.

$$ y'=f\left(\frac {y}{x}\right). $$

When solving such a differential equation, if we let $y/x=u$, then:

$$ y=ux,\quad y'=u'x+u $$

Substituting this into $y'=f(y/x)$ gives $u'x=f(u)-u$. If $f(u)-u\neq0$, then:

$$ \frac {du}{f(u)-u}=\frac {dx}{x} $$

becomes separated.
