---
title: Calculation of Radioactive Equilibrium
description: We explore the relationship between decay constants, half-lives, and
  mean lifetimes of radioactive nuclides, and calculate the radioactivity of radioactive
  nuclides at any given time t in a given decay chain.
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Radioactive Decay]
math: true
mermaid: true
image: /assets/img/atoms.png
---
## TL;DR
> **Radioactivity at any time t**
>
> $$\begin{align*}
> \alpha (t) &= \lambda n(t)
> \\ &= \alpha_0 e^{-\lambda t}
> \\ &= \alpha_0 e^{-0.693t/T_{1/2}}
> \end{align*}$$
{: .prompt-info }

> **Relationship between decay constant, half-life, and mean lifetime**
>
> $$ \begin{align*}
> T_{1/2}&=\frac {\ln 2}{\lambda} = \frac {0.693}{\lambda}
> \\
> \\ \overline{t}&=\frac {1}{\lambda}
> \\ &=\frac {T_{1/2}}{0.693}=1.44T_{1/2}
> \end{align*} $$
{: .prompt-info }

## Decay Constant
- The probability that a nucleus will decay per unit time
- A constant that is independent of time and determined only by the nuclide
- Denoted by the symbol $\lambda$

## Radioactivity
If the number of nuclei that have not yet decayed at time $t$ is n(t), then on average $\lambda n(t)$ nuclei decay during the interval $dt$ between times $t$ and $t+dt$. This decay rate is called the *radioactivity* of the sample and is denoted by the symbol $\alpha$. Therefore, the radioactivity at any time $t$ is:

$$ \alpha (t)=\lambda n(t) \tag{1}$$

## Units of Radioactivity
### Curie (Ci)
- Traditionally used unit before the becquerel
- Radioactivity of 1g of radium-226
- $3.7\times 10^{10}$ nuclear decays per second ($3.7\times 10^{10}\text{Bq}$)

### Becquerel (Bq)
- International Standard (SI) unit
- One nuclear decay per second
- $1 \text{Bq} = 2.703\times 10^{-11}\text{Ci} = 27\text{pCi}$

## Calculation of Radioactivity Change Over Time
Since $\lambda n(t)$ nuclei decay during time $dt$, the decrease in the number of nuclei remaining in the sample during $dt$ can be expressed as:

$$ -dn(t)=\lambda n(t)dt $$

Integrating this gives:

$$ n(t)=n_0e^{-\lambda t} \tag{2} $$

Multiplying both sides by $\lambda$, the radioactivity becomes:

$$ \alpha (t)=\alpha_0e^{-\lambda t} \tag{3} $$

Since radioactivity halves during the *half-life*:

$$ \alpha (T_{1/2})=\alpha_0/2 $$

Substituting this into equation (3):

$$ \alpha_0/2=\alpha_0e^{-\lambda T_{1/2}} $$

Taking the logarithm of both sides and solving for the half-life $T_{1/2}$:

$$ T_{1/2}=\frac {\ln 2}{\lambda}=\frac {0.693}{\lambda} \tag{4}$$

Solving this for $\lambda$ and substituting into equation (3):

$$ \alpha (t)=\alpha_0e^{-0.693t/T_{1/2}} \tag{5} $$

Equation (5) is often more convenient for radioactive decay calculations than equation (3), as half-life values are more commonly given than decay constants.

The *mean lifetime* $\overline{t}$ of a radioactive nucleus is the reciprocal of the decay constant:

$$ \overline{t}=1/\lambda $$

From equation (3), we can see that during one mean lifetime, the radioactivity falls to $1/e$ of its initial value. From equation (4), the following relationship holds between mean lifetime and half-life:

$$ \overline{t}=\frac {T_{1/2}}{0.693}=1.44T_{1/2} \tag{6} $$

### ※ Derivation of Mean Lifetime $\overline{t}$

$$ \begin{align*}
\overline{t}&=\frac {\int_0^\infty t\alpha(t)}{\int_0^\infty t} = \frac {\int_0^\infty t\alpha(t)}{n_0}
\\ &= \frac {\int_0^\infty n_0 \lambda te^{-\lambda t}}{n_0}
\\ &= \int_0^\infty \lambda te^{-\lambda t}
\\ &= \left[-te^{-\lambda t}\right]_0^\infty +\int_0^\infty e^{-\lambda t}
\\ &=\left[-\frac {1}{\lambda} e^{-\lambda t}\right]_0^\infty
\\ &=\frac {1}{\lambda}
\end{align*}$$

## Example: Radioactive Decay Chain 1
Assume that a radioactive nuclide is produced at a rate of $R$ atoms/s. These nuclei undergo radioactive decay as soon as they are formed. Calculate the radioactivity of this nuclide at any time t.
```mermaid
flowchart LR
	Start[?] -- R --> A[Mathematical Model]
	A -- α --> End[?]
```

### 1. Setting up the Model

$$ \text{Rate of change of nuclide} = \text{Production rate} - \text{Loss rate} $$

Expressed in mathematical notation:

$$ dn/dt = -\lambda n + R $$

### 2. General Solution
Move all terms related to $n$ to the left side and multiply both sides by $e^{\lambda t}$:

$$ \frac {dn}{dt} + \lambda n = R $$

$$ e^{\lambda t}\frac {dn}{dt} + \lambda e^{\lambda t}n = Re^{\lambda t} $$

Since $\lambda e^{\lambda t}=\frac {d}{dt} e^{\lambda t}$, we can rearrange as follows:

$$ e^{\lambda t}\frac {dn}{dt}+\left(\frac {d}{dt} e^{\lambda t}\right)n = Re^{\lambda t} $$

Integrating both sides gives the general solution:

$$ e^{\lambda t}n=\frac {R}{\lambda}e^{\lambda t}+c $$

$$ n=ce^{-\lambda t}+\frac {R}{\lambda} $$

### 3. Particular Solution
Let's say the number of this nuclide at $t=0$ is $n_0$ and find the value of the constant $c$:

$$ n(0)=c+\frac {R}{\lambda}=n_0 $$

$$ c=n_0-\frac {R}{\lambda} $$

Therefore, the particular solution for the given situation is:

$$ n = n_0e^{-\lambda t}+\frac {R}{\lambda}(1-e^{-\lambda t}) \tag{7} $$

We can find the radioactivity of this nuclide by multiplying both sides of the above equation by $\lambda$:

$$ \alpha = \alpha_0e^{-\lambda t}+R(1-e^{-\lambda t}) \tag{8} $$

That is, as $t\to\infty$, it converges to $\alpha_{\text{max}}=R$, $n_{\text{max}}=R/\lambda$.

## Example: Radioactive Decay Chain 2
Calculate the radioactivity of radioactive nuclide B in the following decay chain:
```mermaid
flowchart LR
	A --> B
	B --> C
```

### 1. Setting up the Model

$$ \text{Rate of change of B nuclei} = \text{Production rate from A decay} - \text{Decay rate of B to C} $$

$$ \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_A $$

Substituting equation (2) for $n_A$, we get the following differential equation for $n_B$:

$$  \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_{A0}e^{-\lambda_A t} \tag{9}$$ 

### 2. General Solution
To solve the differential equation, move all terms related to $n_B$ to the left side and multiply both sides by $e^{\lambda_B t}$:

$$ \frac {dn_B}{dt} + \lambda_B n_B = n_{A0}\lambda_A e^{-\lambda_A t} $$

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \lambda_B e^{\lambda_B t}n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

Since $\lambda_B e^{\lambda_B t}=\frac {d}{dt} e^{\lambda_b t}$, we can rearrange as follows:

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \left(\frac {d}{dt} e^{\lambda_B t}\right)n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

Integrating both sides:

$$ e^{\lambda_B t}n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{(\lambda_B-\lambda_A)t}+c $$

Dividing both sides by $e^{\lambda_B t}$ gives the general solution:

$$ n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{-\lambda_A t}+ce^{-\lambda_B t} $$

### 3. Particular Solution
Let's say the number of element B at $t=0$ is $n_{B0}$ and find the value of the constant $c$:

$$ n_B(0)=\frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}+c=n_{B0} $$

$$ c=n_{B0}-\frac{n_{A0}\lambda_A}{\lambda_B-\lambda_A} $$

Therefore, the particular solution for the given situation is:

$$ n_B = n_{B0}e^{-\lambda_B t} + \frac {n_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{10}$$

$$ \therefore \alpha_B = \alpha_{B0} e^{-\lambda_B t} + \frac {\alpha_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{11}$$
