---
title: "Neutroneninteraktionen und Wirkungsquerschnitte"
description: >-
  Neutronen sind elektrisch neutral und können daher ohne elektrische Beeinflussung durch die Elektronenwolke des Atoms direkt mit dem Atomkern reagieren. Wir betrachten die Arten der Neutroneninteraktionen und das Konzept des Wirkungsquerschnitts von Atomkernen.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
mermaid: true
---

## Neutroneninteraktionen
Neutronen sind elektrisch neutral und werden daher nicht von den Elektronen oder der positiven Ladung des Atomkerns beeinflusst. Folglich können Neutronen durch die Elektronenwolke des Atoms hindurch direkt mit dem Atomkern reagieren.

### Elastische Streuung (elastic scattering)
- Neutronen prallen nach der Kollision mit dem Atomkern ab
- Der Atomkern bleibt ohne Energieänderung im Grundzustand
- Wird als (n, n) dargestellt

### Inelastische Streuung (inelastic scattering)
- Neutronen prallen nach der Kollision mit dem Atomkern ab
- Im Gegensatz zur elastischen Streuung absorbiert der Atomkern einen Teil der Neutronenenergie und geht in einen angeregten Zustand über (endotherme Reaktion)
- Wird als (n, n′) dargestellt
- Der angeregte Atomkern kehrt unter Emission von Gammastrahlung in den Grundzustand zurück, wobei die entstehende Gammastrahlung als *inelastische Gammastrahlung (inelastic γ-ray)* bezeichnet wird

### Strahlungseinfang (radiative capture)
- Der Atomkern fängt ein Neutron ein und emittiert ein oder mehrere Gammastrahlen (exotherme Reaktion)
- Wird als (n, γ) dargestellt
- Die dabei entstehende Gammastrahlung wird als *Einfanggammastrahlung (capture γ-ray)* bezeichnet

### Geladene Teilchen Reaktionen
- Der Atomkern fängt ein Neutron ein und emittiert geladene Teilchen wie Alphateilchen (α) oder Protonen (p)
- Wird als (n, α), (n, p) usw. dargestellt
- Kann je nach Fall eine exotherme oder endotherme Reaktion sein

### Neutronenproduzierende Reaktionen
- Hochenergetische Neutronen kollidieren mit Atomkernen und erzeugen zwei oder mehr neue Neutronen (endotherme Reaktion)
- Wird als (n, 2n), (n, 3n) usw. dargestellt
- Die (n, 2n) Reaktion ist besonders wichtig in Reaktoren, die schweres Wasser oder Beryllium enthalten, da die Neutronen in ²H und ⁹Be schwach gebunden sind und leicht durch Kollisionen mit niederenergetischen Neutronen freigesetzt werden können

### Kernspaltung (fission)
- Ein Neutron kollidiert mit einem Atomkern und spaltet diesen in zwei oder mehr Tochterkerne

## Wirkungsquerschnitt (cross-section) oder mikroskopischer Wirkungsquerschnitt (microscopic cross-section)
Angenommen, ein monoenergetischer Neutronenstrahl trifft auf ein (sehr dünnes) Target mit der Dicke τ und der Fläche A, wobei I Neutronen/cm²·s die Anzahl der Neutronen ist, die pro Sekunde und Einheitsfläche auf das Target treffen. Da das Volumen, das der Atomkern im Atom einnimmt, sehr klein ist und wir ein sehr dünnes Target angenommen haben, passieren die meisten Neutronen das Target ohne mit den Atomkernen zu reagieren. Die Anzahl der Neutronen, die pro Sekunde und Einheitsfläche mit den Atomkernen kollidieren, ist dann proportional zur Intensität des Neutronenstrahls I, der Dicke des Targets τ und der atomaren Dichte des Targets N.

$$ \Delta I \propto I\tau N $$

Mit der Einführung der Proportionalitätskonstante σ können wir dies wie folgt ausdrücken:

$$ \Delta I = \sigma I\tau N\ \text{[Neutronen/cm}^2\cdot\text{s]} \tag{1} $$

Der Anteil der einfallenden Neutronen, die mit den Atomkernen kollidieren, ergibt sich wie folgt:

$$ p = \frac {\Delta I}{I} = \sigma\tau N = \frac {\sigma}{A} A\tau N = \frac {\sigma}{A} N_t \tag{2} $$

(N_t: Gesamtzahl der Atome im Target)

Aus dieser Gleichung können wir erkennen, dass σ die Einheit einer Fläche hat. Diese Proportionalitätskonstante σ wird als *Wirkungsquerschnitt (cross-section)* oder *mikroskopischer Wirkungsquerschnitt (microscopic cross-section)* bezeichnet. Physikalisch repräsentiert der Wirkungsquerschnitt die effektive Fläche, mit der ein Atomkern mit Neutronen reagieren kann.

## Einheit des mikroskopischen Wirkungsquerschnitts
Da cm² eine zu große Einheit ist, um den mikroskopischen Wirkungsquerschnitt auszudrücken, wird üblicherweise die Einheit *barn* (b) verwendet.

$$ 1\ \text{b} = 10^{-24}\ \text{cm}^2 $$

## Arten des mikroskopischen Wirkungsquerschnitts
- Totaler Wirkungsquerschnitt (total): σ_t
  - Streuquerschnitt (scattering): σ_s
    - Elastischer Streuquerschnitt (elastic scattering): σ_e
    - Inelastischer Streuquerschnitt (inelastic scattering): σ_i
  - Absorptionsquerschnitt (absorption): σ_a
    - Strahlungseinfangquerschnitt (radiative capture): σ_γ
    - Spaltungsquerschnitt (fission): σ_f
    - Geladene Teilchen Reaktionsquerschnitt: σ_p, σ_α, ...
    - Neutronenproduzierende Reaktionsquerschnitt: σ_2n, σ_3n, ...

```mermaid
flowchart LR
	total["Totaler Wirkungsquerschnitt t"] --- s["Streuquerschnitt s"]
	total --- a["Absorptionsquerschnitt a"]

	s --- e["Elastischer Streuquerschnitt e"]
	s --- i["Inelastischer Streuquerschnitt i"]

	a --- gamma["Strahlungseinfangquerschnitt γ"]
	a --- f["Spaltungsquerschnitt f"]
	a --- p["Geladene Teilchen Reaktionsquerschnitt p, α, ..."]
	a --- n["Neutronenproduzierende Reaktionsquerschnitt 2n, 3n, ..."]
```

## Makroskopischer Wirkungsquerschnitt (macroscopic cross-section)
Aus Gleichung (2) erhalten wir die Kollisionsrate pro Einheitslänge des Neutronenstrahls wie folgt:

$$ \frac {p}{\tau} = \frac {1}{\tau} \frac {\Delta I}{I} = \sigma N \equiv \Sigma\ \text{[cm}^{-1}\text{]} \tag{3}$$

Der *makroskopische Wirkungsquerschnitt (macroscopic cross-section)* wird wie oben als Produkt der atomaren Dichte N und des Wirkungsquerschnitts definiert. Physikalisch repräsentiert der makroskopische Wirkungsquerschnitt die Kollisionsrate pro Einheitslänge der Neutronenbewegung in einem Target. Ähnlich wie beim mikroskopischen Wirkungsquerschnitt kann er wie folgt unterteilt werden:

- Makroskopischer totaler Wirkungsquerschnitt Σ_t = Nσ_t
  - Makroskopischer Streuquerschnitt Σ_s = Nσ_s
  - Makroskopischer Absorptionsquerschnitt Σ_a = Nσ_a

Im Allgemeinen gilt für den makroskopischen Wirkungsquerschnitt einer bestimmten Reaktion: Σ_reaction = Nσ_reaction.

## Kollisionsdichte (collision density), d.h. Reaktionsrate (reaction rate)
Die *Kollisionsdichte (collision density)* oder *Reaktionsrate (reaction rate)* bezeichnet die Anzahl der Kollisionen pro Zeiteinheit und Volumeneinheit im Target. Aus den Gleichungen (1) und (3) können wir sie wie folgt definieren:

$$ F = \frac {\Delta I}{\tau} = I\sigma N = I\Sigma \tag{4} $$