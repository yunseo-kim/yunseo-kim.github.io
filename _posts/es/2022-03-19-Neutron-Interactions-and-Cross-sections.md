---
title: "Interacciones de neutrones y secciones eficaces"
description: >-
  Los neutrones son eléctricamente neutros, por lo que pueden atravesar la nube de electrones del átomo sin ser afectados por fuerzas eléctricas y reaccionar directamente con el núcleo atómico. Exploramos los tipos de interacciones de neutrones y el concepto de sección eficaz nuclear.
categories: [Física de Ingeniería, Ingeniería Nuclear]
tags: [Física Nuclear, Interacción de la Radiación con la Materia]
math: true
mermaid: true
---

## Interacciones de neutrones
Los neutrones son eléctricamente neutros, por lo que no se ven afectados por las fuerzas eléctricas de los electrones o la carga positiva del núcleo atómico. Por lo tanto, los neutrones pueden atravesar la nube de electrones del átomo y reaccionar directamente con el núcleo.

### Dispersión elástica (elastic scattering)
- El neutrón colisiona con el núcleo atómico y rebota
- El núcleo atómico mantiene su estado fundamental sin cambios de energía
- Se representa como (n, n)

### Dispersión inelástica (inelastic scattering)
- El neutrón colisiona con el núcleo atómico y rebota
- A diferencia de la dispersión elástica, el núcleo absorbe parte de la energía del neutrón y pasa a un estado excitado (reacción endotérmica)
- Se representa como (n, n′)
- El núcleo excitado vuelve a su estado fundamental emitiendo rayos gamma, que se denominan *rayos gamma inelásticos (inelastic $\gamma$-ray)*

### Captura radiativa (radiative capture)
- El núcleo captura el neutrón y emite uno o más rayos gamma (reacción exotérmica)
- Se representa como (n, $\gamma$)
- Los rayos gamma emitidos se denominan *rayos gamma de captura (capture $\gamma$-ray)*

### Reacciones de partículas cargadas
- El núcleo captura el neutrón y emite partículas cargadas como partículas alfa ($\alpha$) o protones (p)
- Se representa como (n, $\alpha$), (n, p), etc.
- Puede ser una reacción exotérmica o endotérmica dependiendo del caso

### Reacciones de producción de neutrones
- Un neutrón de alta energía colisiona con un núcleo, produciendo dos o más neutrones nuevos (reacción endotérmica)
- Se representa como (n, 2n), (n, 3n), etc.
- La reacción (n, 2n) es particularmente importante en reactores que contienen agua pesada o berilio, ya que los neutrones en $^2\text{H}$ y $^9\text{Be}$ tienen baja energía de enlace y pueden ser fácilmente expulsados incluso por neutrones de baja energía

### Fisión (fission)
- Un neutrón colisiona con ciertos núcleos, dividiéndolos en dos o más núcleos hijos

## Sección eficaz (cross-section) o sección eficaz microscópica (microscopic cross-section)
Consideremos un haz de neutrones monoenergético que incide sobre un blanco (muy delgado) de espesor $\tau$ y área $A$, donde el número de neutrones que inciden por unidad de área y por segundo es $I\ \text{neutrones/cm}^2\cdot \text{s}$. Dado que el volumen ocupado por el núcleo en un átomo es muy pequeño y hemos asumido que el blanco es muy delgado, la mayoría de los neutrones atravesarán el blanco sin interactuar con los núcleos. Entonces, el número de neutrones que colisionan con los núcleos por unidad de área y por segundo es proporcional a la intensidad del haz de neutrones $I$, el espesor del blanco $\tau$, y la densidad atómica del blanco $N$.

$$ \Delta I \propto I\tau N $$

Introduciendo una constante de proporcionalidad $\sigma$, podemos expresarlo como:

$$ \Delta I = \sigma I\tau N\ \text{[neutrones/cm}^2\cdot\text{s]} \tag{1} $$

La fracción de neutrones incidentes que colisionan con los núcleos se puede calcular como:

$$ p = \frac {\Delta I}{I} = \sigma\tau N = \frac {\sigma}{A} A\tau N = \frac {\sigma}{A} N_t \tag{2} $$

($N_t$: número total de átomos en el blanco)

De esta ecuación, podemos ver que $\sigma$ tiene unidades de área. Esta constante de proporcionalidad $\sigma$ se denomina *sección eficaz (cross-section)* o *sección eficaz microscópica (microscopic cross-section)*. Físicamente, la sección eficaz representa el área efectiva que un núcleo presenta para interactuar con un neutrón.

## Unidades de la sección eficaz microscópica
Como cm$^2$ es una unidad demasiado grande para expresar la sección eficaz microscópica, generalmente se utiliza una unidad llamada *barn* (b).

$$ 1\ \text{b} = 10^{-24}\ \text{cm}^2 $$

## Tipos de secciones eficaces microscópicas
- Sección eficaz total: $\sigma_t$
  - Sección eficaz de dispersión: $\sigma_s$
    - Sección eficaz de dispersión elástica: $\sigma_e$
    - Sección eficaz de dispersión inelástica: $\sigma_i$
  - Sección eficaz de absorción: $\sigma_a$
    - Sección eficaz de captura radiativa: $\sigma_\gamma$
    - Sección eficaz de fisión: $\sigma_f$
    - Sección eficaz de reacciones de partículas cargadas: $\sigma_p, \sigma_\alpha, \cdots$
    - Sección eficaz de reacciones de producción de neutrones: $\sigma_{2n}, \sigma_{3n}, \cdots$

```mermaid
flowchart LR
	total["Sección eficaz total t"] --- s["Sección eficaz de dispersión s"]
	total --- a["Sección eficaz de absorción a"]

	s --- e["Sección eficaz de dispersión elástica e"]
	s --- i["Sección eficaz de dispersión inelástica i"]

	a --- gamma["Sección eficaz de captura radiativa γ"]
	a --- f["Sección eficaz de fisión f"]
	a --- p["Sección eficaz de reacciones de partículas cargadas p, α, ..."]
	a --- n["Sección eficaz de reacciones de producción de neutrones 2n, 3n, ..."]
```

## Sección eficaz macroscópica (macroscopic cross-section)
De la ecuación (2), podemos obtener la tasa de colisión por unidad de distancia del haz de neutrones:

$$ \frac {p}{\tau} = \frac {1}{\tau} \frac {\Delta I}{I} = \sigma N \equiv \Sigma\ \text{[cm}^{-1}\text{]} \tag{3}$$

La *sección eficaz macroscópica (macroscopic cross-section)* se define como el producto de la densidad atómica $N$ y la sección eficaz, como se muestra arriba. Físicamente, la sección eficaz macroscópica representa la tasa de colisión por unidad de distancia recorrida por un neutrón en un material dado. Al igual que con la sección eficaz microscópica, se puede subdividir de la siguiente manera:

- Sección eficaz macroscópica total $\Sigma_t=N\sigma_t$
  - Sección eficaz macroscópica de dispersión $\Sigma_s=N\sigma_s$
  - Sección eficaz macroscópica de absorción $\Sigma_a=N\sigma_a$

En general, para cualquier reacción, la sección eficaz macroscópica es $\Sigma_{reacción}=N\sigma_{reacción}$.

## Densidad de colisión (collision density), es decir, tasa de reacción (reaction rate)
La *densidad de colisión (collision density)* o *tasa de reacción (reaction rate)* representa el número de colisiones por unidad de tiempo y volumen en el blanco. Se puede definir a partir de las ecuaciones (1) y (3) como:

$$ F = \frac {\Delta I}{\tau} = I\sigma N = I\Sigma \tag{4} $$