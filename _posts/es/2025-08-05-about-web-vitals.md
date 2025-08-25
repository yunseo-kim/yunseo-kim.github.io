---
title: Métricas de rendimiento web (Web Vitals)
description: Resumen de las métricas de rendimiento web (Web Vitals) y los criterios de medición y evaluación de Lighthouse, explorando qué significa cada métrica de rendimiento.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Factores que determinan el rendimiento web
Los factores que determinan el rendimiento web que deben considerarse al optimizar el rendimiento web se pueden clasificar principalmente en dos categorías: rendimiento de carga y rendimiento de renderizado.

### Rendimiento de carga HTML
- Tiempo desde la primera solicitud de una página web al servidor a través de la red hasta que el navegador recibe el documento HTML y comienza el renderizado
- Determina qué tan rápido comienza a mostrarse la página
- Se optimiza mediante métodos como minimizar redirecciones, caché de respuestas HTML, compresión de recursos y uso adecuado de CDN

### Rendimiento de renderizado
- Tiempo que tarda el navegador en dibujar la pantalla que ve el usuario y hacerla interactiva
- Determina qué tan suave y rápido se dibuja la pantalla
- Se optimiza mediante métodos como eliminación de CSS y JS innecesarios, prevención de carga diferida de fuentes y miniaturas, separación de operaciones pesadas a Web Workers separados para minimizar la ocupación del hilo principal, y optimización de animaciones

## Métricas de rendimiento web (Web Vitals)
Se describe basándose en [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) de Google y la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). A menos que haya una razón especial, es mejor apuntar a una mejora general en lugar de centrarse en una sola métrica de rendimiento, y es importante identificar qué partes actúan como cuellos de botella en el rendimiento de la página web que se desea optimizar. Además, cuando hay estadísticas de datos de usuarios reales, es recomendable prestar atención a los valores del cuartil inferior (Q1) en lugar de los valores promedio o del cuartil superior, y verificar y mejorar si se alcanzan los criterios objetivo incluso en esos casos.

### Métricas principales de rendimiento web (Core Web Vitals)
Como se tratará en breve, existen varias métricas de rendimiento web (Web Vitals). Sin embargo, entre ellas, Google considera especialmente importantes las siguientes 3 métricas que están estrechamente relacionadas con la experiencia del usuario y pueden medirse en entornos reales en lugar de simulados, y las denomina [Métricas principales de rendimiento web (Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Dado que Google también refleja las métricas principales de rendimiento web del sitio objetivo en el orden de los resultados de búsqueda de su motor de búsqueda, desde la perspectiva de los operadores de sitios, estas métricas también deben examinarse cuidadosamente desde el aspecto de la optimización para motores de búsqueda (SEO).
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint): Refleja el *rendimiento de carga*, debe ser inferior a 2.5 segundos
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): Refleja la *capacidad de respuesta*, debe ser inferior a 200ms
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): Refleja la *estabilidad visual*, debe mantenerse por debajo de 0.1

Las métricas principales de rendimiento web están básicamente destinadas a medirse en entornos reales, pero las dos restantes excepto INP también pueden medirse en entornos simulados como las herramientas para desarrolladores de Chrome o Lighthouse. En el caso de INP, no puede medirse en entornos simulados ya que requiere entrada real del usuario, pero en tales casos se puede consultar [TBT](#tbt-total-blocking-time) como referencia, ya que tiene una correlación muy alta con INP y es una métrica de rendimiento similar, y [generalmente mejorar TBT también mejora INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Ponderaciones de puntuación de rendimiento de Lighthouse 10
[La puntuación de rendimiento de Lighthouse se calcula como un promedio ponderado de las puntuaciones de cada elemento de medición, siguiendo las ponderaciones de la siguiente tabla](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Elemento de medición | Ponderación |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Mide el tiempo necesario para renderizar el primer contenido DOM después de solicitar la página
- Considera como contenido DOM imágenes, elementos `<canvas>` que no sean blancos, SVG, etc., dentro de la página, sin considerar el contenido dentro de `iframe`

> Uno de los factores que afecta especialmente a FCP es el tiempo de carga de fuentes, y la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recomienda consultar [publicaciones relacionadas](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) para optimización relacionada con esto.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), los criterios de evaluación de Lighthouse son los siguientes:

| Grado de color | FCP móvil (segundos) | FCP escritorio (segundos) |
| --- | --- | --- |
| Verde (rápido) | 0-1.8 | 0-0.9 |
| Naranja (medio) | 1.8-3 | 0.9-1.6 |
| Rojo (lento) | Más de 3 | Más de 1.6 |

### LCP (Largest Contentful Paint)
- Mide el tiempo necesario para renderizar el elemento más grande (imágenes, bloques de texto, videos, etc.) dentro del área de visualización (viewport) que se muestra primero en la pantalla cuando se abre una página web por primera vez
- Cuanto mayor sea el área que ocupa en la pantalla, mayor será la probabilidad de que el usuario lo perciba como contenido principal
- Cuando LCP es una imagen, el tiempo necesario puede dividirse en 4 subintervalos, y es importante identificar dónde ocurre el cuello de botella entre estos
  1. Time to first byte (TTFB): Tiempo desde el inicio de la carga de la página hasta recibir el primer byte de la respuesta del documento HTML
  2. Retraso de carga (Load delay): Diferencia entre el momento en que el navegador comenzó a cargar el recurso LCP y TTFB
  3. Tiempo de carga (Load time): Tiempo necesario para cargar el recurso LCP en sí
  4. Retraso de renderizado (Render delay): Tiempo desde completar la carga del recurso LCP hasta completar completamente el renderizado del elemento LCP

#### Criterios de evaluación de Lighthouse
Según la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), los criterios de evaluación de Lighthouse son los siguientes:

| Grado de color | FCP móvil (segundos) | FCP escritorio (segundos) |
| --- | --- | --- |
| Verde (rápido) | 0-2.5 | 0-1.2 |
| Naranja (medio) | 2.5-4 | 1.2-2.4 |
| Rojo (lento) | Más de 4 | Más de 2.4 |

### TBT (Total Blocking Time)
- Mide el tiempo total en que una página web no puede responder a entradas del usuario como clics del ratón, toques en pantalla o entradas del teclado
- Entre las tareas entre FCP y [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*, considera como [tareas largas](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) aquellas que se ejecutaron durante 50ms o más, y define como *porción de bloqueo (blocking portion)* el exceso obtenido al restar 50ms del tiempo necesario para cada una de estas tareas largas, y TBT como la suma de todas las porciones de bloqueo

> \* TTI en sí es demasiado sensible a valores atípicos de respuesta de red y tareas largas, lo que resulta en baja consistencia y alta variabilidad, por lo que [se excluyó de los elementos de evaluación de rendimiento desde Lighthouse 10](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> En general, la causa más común de tareas largas es la carga, análisis y ejecución innecesaria o ineficiente de JavaScript, y la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) y [web.dev de Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recomiendan reducir el tamaño de la carga útil de JavaScript a través de [división de código](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) para que cada uno pueda ejecutarse dentro de 50ms, y si es necesario, considerar separarlo a un service worker separado en lugar del hilo principal para ejecución multihilo.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), los criterios de evaluación de Lighthouse son los siguientes:

| Grado de color | FCP móvil (milisegundos) | FCP escritorio (milisegundos) |
| --- | --- | --- |
| Verde (rápido) | 0-200 | 0-150 |
| Naranja (medio) | 200-600 | 150-350 |
| Rojo (lento) | Más de 600 | Más de 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Ejemplo de cambio repentino de diseño" autoplay=true loop=true %}
> Fuente del video: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Se siente una profunda ira en el movimiento del cursor~~

- Los cambios inesperados de diseño perjudican la experiencia del usuario de varias maneras, como hacer que el texto se mueva repentinamente y perder la posición de lectura, o hacer clic incorrectamente en enlaces o botones
- El método específico para calcular la puntuación CLS está descrito en [web.dev de Google](https://web.dev/articles/cls)
- Como se puede confirmar en la imagen a continuación, se debe apuntar a 0.1 o menos

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> Fuente de la imagen: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Mide qué tan rápido se muestra visualmente el contenido durante la carga de la página
- Lighthouse graba en video el proceso de carga de la página en el navegador, analiza el video para calcular el progreso entre fotogramas, y luego usa el [módulo Speedline Node.js](https://github.com/paulirish/speedline) para calcular la puntuación SI

> Cualquier medida que mejore la velocidad de carga de la página, incluyendo las mencionadas anteriormente al resumir [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint) y [TBT](#tbt-total-blocking-time), también afectará positivamente la puntuación SI. Se puede ver como una métrica de rendimiento que refleja todo el proceso de carga en cierto nivel en lugar de representar solo un proceso de carga de página.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), los criterios de evaluación de Lighthouse son los siguientes:

| Grado de color | SI móvil (segundos) | SI escritorio (segundos) |
| --- | --- | --- |
| Verde (rápido) | 0-3.4 | 0-1.3 |
| Naranja (medio) | 3.4-5.8 | 1.3-2.3 |
| Rojo (lento) | Más de 5.8 | Más de 2.3 |
