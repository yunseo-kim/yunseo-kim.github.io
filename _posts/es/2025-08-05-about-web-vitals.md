---
title: Métricas de rendimiento web (Web Vitals)
description: "Resumen de las Web Vitals y de los criterios de medición y evaluación de Lighthouse, con explicación de qué significa cada métrica y cómo optimizarlas para mejorar el rendimiento y el SEO."
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Factores que determinan el rendimiento web
Al optimizar el rendimiento web, los factores que lo determinan pueden agruparse en dos grandes categorías: rendimiento de carga y rendimiento de renderizado.

### Rendimiento de carga de HTML
- Tiempo desde la primera solicitud de la página al servidor a través de la red hasta que el navegador comienza a renderizar el documento HTML
- Determina cuán rápido comienza a mostrarse la página
- Se optimiza minimizando redirecciones, cacheando la respuesta HTML, comprimiendo recursos y utilizando adecuadamente una CDN

### Rendimiento de renderizado
- Tiempo que tarda el navegador en dibujar lo que ve el usuario y hacerlo interactivo
- Determina cuán suave y rápido se dibuja la pantalla
- Se optimiza eliminando CSS y JS innecesarios, evitando la carga diferida de fuentes y miniaturas, separando operaciones pesadas en un Web Worker para minimizar la ocupación del hilo principal, y optimizando animaciones

## Métricas de rendimiento web (Web Vitals)
Se describe con base en [web.dev de Google](https://web.dev/performance?hl={{ site.active_lang }}) y la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Salvo que haya un motivo específico, es mejor apuntar a una mejora global que centrarse únicamente en una métrica, e identificar qué partes de la página actúan como cuellos de botella. Si se dispone de datos de usuarios reales, conviene fijarse en el cuartil inferior (Q1) más que en la media o el cuartil superior, y comprobar que incluso en esos casos se cumplen los objetivos y se realizan mejoras.

### Métricas esenciales de la web (Core Web Vitals)
Como veremos enseguida, existen varias Web Vitals. Entre ellas, Google considera especialmente importantes tres que se relacionan estrechamente con la experiencia de usuario y que se pueden medir en condiciones reales (no solo de laboratorio); a estas se las denomina [métricas esenciales de la web (Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Google también incorpora estas métricas en el orden de resultados de su buscador, por lo que, desde la perspectiva del SEO, los administradores de sitios deben prestarles especial atención.
- [Pintura con contenido más grande (LCP)](#lcp-pintura-con-contenido-más-grande): refleja el rendimiento de carga; debe ser ≤ 2,5 s
- [Interacción hasta la siguiente pintura (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): refleja la capacidad de respuesta; debe ser ≤ 200 ms
- [Cambio de diseño acumulado (CLS)](#cls-cambio-de-diseño-acumulado): refleja la estabilidad visual; debe mantenerse ≤ 0,1

Aunque las Core Web Vitals están pensadas para medirse en el entorno real, dos de ellas (excepto INP) pueden medirse también en entornos de laboratorio como DevTools de Chrome o Lighthouse. INP requiere una entrada real del usuario y no puede medirse en laboratorio; en ese caso, [TBT](#tbt-tiempo-total-de-bloqueo) es una métrica muy correlacionada y similar, y puede usarse como referencia; [normalmente, al mejorar TBT también mejora INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Ponderación de la puntuación de rendimiento en Lighthouse 10
[La puntuación de rendimiento de Lighthouse es un promedio ponderado de las métricas medidas, con los siguientes pesos](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Métrica | Peso |
| --- | --- |
| [Primera pintura con contenido](#fcp-primera-pintura-con-contenido) | 10% |
| [Índice de velocidad](#si-índice-de-velocidad) | 10% |
| [Pintura con contenido más grande](#lcp-pintura-con-contenido-más-grande) | 25% |
| [Tiempo total de bloqueo](#tbt-tiempo-total-de-bloqueo) | 30% |
| [Cambio de diseño acumulado](#cls-cambio-de-diseño-acumulado) | 25% |

### FCP (Primera pintura con contenido)
- Mide el tiempo que tarda en renderizarse el primer contenido del DOM tras solicitar la página
- Considera como contenido del DOM imágenes dentro de la página, elementos `<canvas>` no blancos, SVG, etc.; no considera el contenido dentro de `iframe`

> Uno de los factores que más influyen en FCP es el tiempo de carga de las fuentes; la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recomienda consultar esta [entrada relacionada](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) sobre su optimización.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), los criterios de Lighthouse son los siguientes.

| Categoría por color | FCP en móvil (s) | FCP en escritorio (s) |
| --- | --- | --- |
| Verde (rápido) | 0-1.8 | 0-0.9 |
| Naranja (medio) | 1.8-3 | 0.9-1.6 |
| Rojo (lento) | > 3 | > 1.6 |

### LCP (Pintura con contenido más grande)
- Mide el tiempo que tarda en renderizarse el elemento más grande (imagen, bloque de texto, video, etc.) dentro del área visible inicial (viewport) al abrir por primera vez la página
- Cuanto mayor es el área que ocupa en pantalla, mayor es la probabilidad de que el usuario lo perciba como contenido principal
- Si el LCP es una imagen, el tiempo puede dividirse en cuatro subintervalos; es importante identificar dónde se produce el cuello de botella:
  1. Time to first byte (TTFB): tiempo desde el inicio de la carga de la página hasta la recepción del primer byte de la respuesta del documento HTML
  2. Retraso de carga (Load delay): diferencia entre el momento en que el navegador comienza a cargar el recurso LCP y el TTFB
  3. Tiempo de carga (Load time): tiempo que tarda en cargarse el propio recurso LCP
  4. Retraso de renderizado (Render delay): tiempo desde que finaliza la carga del recurso LCP hasta que el elemento LCP termina de renderizarse por completo

#### Criterios de evaluación de Lighthouse
Según la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), los criterios de Lighthouse son los siguientes.

| Categoría por color | LCP en móvil (s) | LCP en escritorio (s) |
| --- | --- | --- |
| Verde (rápido) | 0-2.5 | 0-1.2 |
| Naranja (medio) | 2.5-4 | 1.2-2.4 |
| Rojo (lento) | > 4 | > 2.4 |

### TBT (Tiempo total de bloqueo)
- Mide el tiempo total durante el cual la página no puede responder a entradas del usuario como clics, toques o teclas
- Entre FCP y [TTI (Time to Interactive, inicio de la interactividad)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }}), las tareas que duran 50 ms o más se consideran [tareas largas](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}). De cada tarea larga se resta 50 ms; la parte excedente se denomina *parte de bloqueo (blocking portion)* y TBT se define como la suma de todas esas partes de bloqueo

> TTI, por sí misma, es demasiado sensible a valores atípicos de red y a tareas largas, lo que reduce su consistencia y aumenta su variabilidad; por ello, [desde Lighthouse 10 se ha excluido de las métricas de puntuación](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> La causa más común de tareas largas suele ser la carga, el parseo y la ejecución de JavaScript innecesario o ineficiente. La [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) y [web.dev de Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recomiendan aplicar [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) para reducir el payload de JavaScript de forma que cada parte se ejecute en ≤ 50 ms, y, si es necesario, separar trabajo fuera del hilo principal usando un Service Worker para ejecutarlo en multihilo.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), los criterios de Lighthouse son los siguientes.

| Categoría por color | TBT en móvil (ms) | TBT en escritorio (ms) |
| --- | --- | --- |
| Verde (rápido) | 0-200 | 0-150 |
| Naranja (medio) | 200-600 | 150-350 |
| Rojo (lento) | > 600 | > 350 |

### CLS (Cambio de diseño acumulado)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Ejemplo de cambio de diseño repentino" autoplay=true loop=true %}
> Fuente del video: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Se percibe una profunda ira en el movimiento del cursor~~

- Los cambios de diseño inesperados perjudican la experiencia del usuario de múltiples maneras: el texto puede moverse de repente y hacerte perder la línea de lectura, o puedes hacer clic por error en un enlace o botón
- El método exacto de cálculo del CLS está descrito en [web.dev de Google](https://web.dev/articles/cls)
- Como se ve en la imagen inferior, conviene apuntar a ≤ 0.1

![¿Cuál es una buena puntuación de CLS?](/assets/img/about-web-vitals/good-cls-values.svg)
> Fuente de la imagen: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Índice de velocidad)
- Mide cuán rápido se muestra visualmente el contenido durante la carga de la página
- Lighthouse graba en video el proceso de carga en el navegador, analiza el video para calcular el progreso entre frames y usa el [módulo Speedline de Node.js](https://github.com/paulirish/speedline) para calcular la puntuación de SI

> Además de lo mencionado en [FCP](#fcp-primera-pintura-con-contenido), [LCP](#lcp-pintura-con-contenido-más-grande) y [TBT](#tbt-tiempo-total-de-bloqueo), cualquier medida que mejore la velocidad de carga de la página también repercute positivamente en el SI. Más que representar una sola fase del proceso, esta métrica refleja el avance visual a lo largo de la carga completa.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), los criterios de Lighthouse son los siguientes.

| Categoría por color | SI en móvil (s) | SI en escritorio (s) |
| --- | --- | --- |
| Verde (rápido) | 0-3.4 | 0-1.3 |
| Naranja (medio) | 3.4-5.8 | 1.3-2.3 |
| Rojo (lento) | > 5.8 | > 2.3 |
