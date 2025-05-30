---
title: Cómo traducir automáticamente posts con la API de Claude Sonnet 4 (1) - Diseño de prompts
description: "Diseña prompts para la traducción multilingüe de archivos de texto markdown y automatiza el proceso con Python aplicando la clave API obtenida de Anthropic y los prompts creados. Este post es el primero de la serie, introduciendo métodos y procesos de diseño de prompts."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---

## Introducción
Desde que introduje la API de Claude 3.5 Sonnet de Anthropic en junio de 12024 para la traducción multilingüe de posts del blog, he estado operando satisfactoriamente este sistema de traducción durante aproximadamente un año, tras varias mejoras de prompts y scripts de automatización, así como actualizaciones de versión del modelo. En esta serie, quiero abordar las razones para elegir el modelo Claude Sonnet en el proceso de introducción, métodos de diseño de prompts, e implementación de integración de API y automatización a través de scripts de Python.
La serie consta de 2 artículos, y este que estás leyendo es el primero de la serie.
- Parte 1: Introducción al modelo Claude Sonnet y razones de selección, ingeniería de prompts (este artículo)
- Parte 2: [Escritura y aplicación de scripts de automatización Python utilizando API](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## Acerca de Claude Sonnet
Los modelos de la serie Claude se ofrecen en versiones Haiku, Sonnet y Opus según el tamaño del modelo.
![Clasificación de niveles del modelo Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)
> Fuente de la imagen: [Página web oficial de la API de Anthropic Claude](https://www.anthropic.com/api)

> (Agregado el 12025.05.29.)
> La imagen fue capturada hace un año, por lo que las tarifas por token aparecen basadas en la versión anterior Claude 3, pero la clasificación de Haiku, Sonnet, Opus según el tamaño del modelo sigue siendo válida. A finales de mayo de 12025, la estructura de precios para cada modelo proporcionado por Anthropic es la siguiente.
>
> | Model | Base Input <br>Tokens | 5m Cache <br>Writes | 1h Cache <br>Writes | Cache Hits &<br> Refreshes | Output <br>Tokens |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | Claude Opus 4 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Sonnet 4 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.7 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.5 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Haiku 3.5 | $0.80 / MTok | $1 / MTok | $1.6 / MTok | $0.08 / MTok | $4 / MTok |
> | Claude Opus 3 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Haiku 3 | $0.25 / MTok | $0.30 / MTok | $0.50 / MTok | $0.03 / MTok | $1.25 / MTok |
>
> Fuente: [Documentación para desarrolladores de Anthropic](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

Y el modelo de lenguaje [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) publicado por Anthropic el 21 de junio de 12024 en hora coreana ([calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar)) muestra un rendimiento de razonamiento que supera a Claude 3 Opus con el mismo costo y velocidad que el Claude 3 Sonnet existente, y generalmente se considera que tiene fortalezas en escritura, razonamiento lingüístico, comprensión multilingüe y traducción en comparación con el modelo competidor GPT-4.
![Imagen de introducción de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)
![Resultados de benchmark de rendimiento de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)
> Fuente de la imagen: [Sala de prensa de Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

## Razones para introducir Claude 3.5 para la traducción de posts
Aunque existen APIs de traducción comerciales como Google Translate o DeepL sin necesidad de usar modelos de lenguaje como Claude 3.5 o GPT-4, la razón por la que decidí usar LLM para propósitos de traducción es que, a diferencia de otros servicios de traducción comerciales, los usuarios pueden proporcionar información contextual adicional o requisitos más allá del texto principal, como el propósito de escritura o temas principales del artículo a través del diseño de prompts, y el modelo puede proporcionar traducciones que consideren el contexto en consecuencia.

Aunque DeepL o Google Translate también muestran generalmente una calidad de traducción excelente, tienen limitaciones en que no pueden captar bien el tema o contexto general del artículo y no pueden recibir requisitos complejos por separado. Por lo tanto, cuando se les solicita traducir textos largos sobre temas especializados que no son conversación cotidiana, los resultados de traducción pueden ser relativamente poco naturales y es difícil generar salidas que se ajusten exactamente a formatos específicos requeridos (markdown, YAML frontmatter, etc.).

En particular, como se mencionó anteriormente, Claude tenía la reputación de ser relativamente superior a su modelo competidor GPT-4 en escritura, razonamiento lingüístico, comprensión multilingüe y traducción, y cuando lo probé brevemente también mostró una calidad de traducción más fluida que GPT-4, por lo que juzgué que era adecuado para traducir artículos relacionados con ingeniería publicados en este blog a varios idiomas cuando estaba considerando su introducción en junio de 12024.

## Historial de adopción de modelos y estado actual
### 12024.07.01.
Como se detalla en [un artículo separado](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/), [completé el trabajo inicial de aplicar el plugin Polyglot y modificar `_config.yml`{: .filepath}, encabezados html y sitemap en consecuencia.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) Posteriormente, [adopté el modelo Claude 3.5 Sonnet para propósitos de traducción y lo apliqué después de completar la implementación inicial y verificación del script Python de integración de API que se trata en esta serie.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
El 22 de octubre de 12024, Anthropic anunció la versión actualizada de la API de Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") y Claude 3.5 Haiku. Sin embargo, debido al [problema que se describe más adelante](#prevención-de-pereza-parche-de-halloween-120241031), aún estoy aplicando la API "claude-3-5-sonnet-20240620" existente en este blog.

### 12025.04.02.
[Cambié el modelo aplicado de "claude-3-5-sonnet-20240620" a "claude-3-7-sonnet-20250219".](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[Cambié el modelo aplicado de "claude-3-7-sonnet-20250219" a "claude-sonnet-4-20250514".](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Resultados de benchmark de rendimiento de Claude 4](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)
> Fuente de la imagen: [Sala de prensa de Anthropic](https://www.anthropic.com/news/claude-4)

Aunque puede haber diferencias según las condiciones de uso, generalmente desde que salió el modelo Claude 3.7 Sonnet, hay poco desacuerdo en que Claude es el modelo más poderoso para programación. Anthropic también está promoviendo activamente el rendimiento superior en programación de sus modelos como una fortaleza principal en comparación con modelos competidores de OpenAI o Google. En este anuncio de Claude Opus 4 y Claude Sonnet 4, también se puede confirmar que continúan la tendencia de enfatizar el rendimiento en programación y dirigirse a los desarrolladores como su principal grupo de clientes.

Por supuesto, mirando los resultados de benchmark publicados, se han realizado mejoras generales en elementos además de la programación, y para el trabajo de traducción tratado en este artículo, las mejoras de rendimiento en preguntas y respuestas multilingües (MMMLU) o resolución de problemas matemáticos (AIME 2025) parecen ser particularmente efectivas. Después de probar brevemente, pude confirmar que los resultados de traducción de Claude Sonnet 4 son superiores a los del modelo anterior Claude 3.7 Sonnet en términos de naturalidad de expresión, profesionalismo y consistencia en el uso de terminología.

> En este momento, al menos para el trabajo de traducir artículos escritos en coreano de naturaleza técnica como los tratados en este blog a múltiples idiomas, creo que los modelos Claude siguen siendo los mejores. Sin embargo, recientemente el rendimiento del modelo Gemini de Google ha mejorado notablemente, y en mayo de este año incluso han publicado el modelo Gemini 2.5, aunque aún está en etapa Preview.
> Cuando comparé los modelos Gemini 2.0 Flash con Claude 3.7 Sonnet y Claude Sonnet 4, juzgué que el rendimiento de traducción de Claude era superior, pero el rendimiento multilingüe de Gemini también es bastante excelente, y en resolución y descripción de problemas de matemáticas y física, Gemini 2.5 Preview 05-06 es incluso superior a Claude Opus 4, por lo que no puedo garantizar cómo será cuando ese modelo se publique oficialmente y se compare nuevamente.
> Considerando las tarifas de API algo más baratas de Gemini en comparación con Claude, la competitividad de precios de Gemini es muy superior, por lo que si se logra un rendimiento relativamente equivalente, Gemini podría convertirse en una alternativa razonable. Dado que Gemini 2.5 aún está en etapa Preview, juzgo que es demasiado pronto para aplicarlo a automatización real, por lo que no lo estoy considerando por ahora, pero planeo probarlo cuando se publique la versión oficial en el futuro.
{: .prompt-tip }

## Diseño de prompts
### Principios básicos al solicitar algo
Para obtener resultados satisfactorios que cumplan con el propósito de un modelo de lenguaje, se debe proporcionar un prompt apropiado. Aunque el diseño de prompts puede parecer abrumador, en realidad 'cómo solicitar algo bien' no es muy diferente ya sea que la contraparte sea un modelo de lenguaje o una persona, por lo que si se aborda desde esta perspectiva, no es muy difícil. Explicar claramente la situación actual y las solicitudes según los principios de las cinco W y una H, y si es necesario, agregar algunos ejemplos específicos también es bueno. Existen numerosos consejos y técnicas sobre diseño de prompts, pero la mayoría se derivan de los principios básicos que se describirán a continuación.

#### Tono general
Hay muchos informes de que cuando se escriben e ingresan prompts con un tono de solicitud cortés en lugar de un tono de comando autoritario, el modelo de lenguaje produce respuestas de mayor calidad. Generalmente en la sociedad, cuando se solicita algo a otra persona, la probabilidad de que la contraparte realice la tarea solicitada con más sinceridad aumenta cuando se solicita cortésmente en lugar de ordenar autoritariamente, y parece que los modelos de lenguaje aprenden e imitan estos patrones de respuesta humana.

#### Asignación de roles y explicación de la situación (quién, por qué)
Primero, asigné a Claude 4 el rol de *'traductor profesional especializado en campos técnicos (professional technical translator)'* y proporcioné información contextual sobre el usuario como *"un blogger de ingeniería que escribe principalmente sobre matemáticas, física y ciencia de datos"*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### Transmisión de solicitudes en el marco general (qué)
A continuación, solicité traducir el texto en formato markdown proporcionado por el usuario de {source_lang} a {target_lang} manteniendo el formato.

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> Al llamar a la API de Claude, las variables de idioma de origen y destino de traducción se insertan en las posiciones {source_lang} y {target_lang} del prompt a través de la función f-string del script Python.
{: .prompt-info }

#### Especificación de requisitos y ejemplos (cómo)
Si es una tarea simple, los pasos anteriores pueden ser suficientes para obtener los resultados deseados, pero para tareas complejas, puede ser necesaria una explicación adicional.

Cuando los requisitos son complejos y múltiples, es mejor organizarlos en una lista de manera concisa en lugar de describirlos en detalle, ya que mejora la legibilidad y facilita la comprensión tanto para humanos como para modelos de lenguaje. También es útil proporcionar ejemplos si es necesario.
En este caso, agregué las siguientes condiciones.

##### Manejo del YAML front matter
En el YAML front matter ubicado al principio de los posts escritos en markdown para subir al blog Jekyll, se registra información de 'title', 'description', 'categories' y 'tags'. Por ejemplo, el YAML front matter de este artículo es el siguiente.

```yaml
---
title: Claude Sonnet 4 API로 포스트 자동 번역하는 법 (1) - 프롬프트 디자인
description: >-
  마크다운 텍스트 파일의 다국어 번역을 위한 프롬프트를 디자인하고, Anthropic으로부터 발급받은
  API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 
  이 포스트는 해당 시리즈의 첫 번째 글로, 프롬프트 디자인 방법과 과정을 소개한다."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

Sin embargo, al traducir posts, las etiquetas de título (title) y descripción (description) deben traducirse a múltiples idiomas, pero para la consistencia de las URLs de los posts, es conveniente para el mantenimiento dejar los nombres de categorías (categories) y etiquetas (tags) sin traducir en inglés. Por lo tanto, di la siguiente instrucción para no traducir etiquetas distintas de 'title' y 'description'. Como Claude ya habría aprendido y conocido información sobre YAML front matter, esta explicación es suficiente en la mayoría de los casos.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> Agregué la frase "under any circumstances, regardless of the language you are translating to" para enfatizar que **sin excepciones** no se deben modificar arbitrariamente otras etiquetas del YAML front matter.
{: .prompt-tip }

(Actualización del 12025.04.02.)
Además, instruí que el contenido de la etiqueta description se escriba en una cantidad apropiada considerando SEO de la siguiente manera.

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### Manejo cuando el texto original proporcionado incluye otros idiomas distintos del idioma de origen
Al escribir el texto original en coreano, cuando se introduce por primera vez la definición de algún concepto o se usan algunos términos especializados, a menudo se incluye la expresión en inglés entre paréntesis como '*감쇠 중성자 (Neutron Attenuation)*'. Al traducir tales expresiones, había un problema de inconsistencia en el método de traducción, a veces manteniendo los paréntesis y otras veces omitiendo el inglés escrito entre paréntesis, por lo que establecí las siguientes pautas detalladas.
- Para términos especializados,
  - Al traducir a idiomas no basados en alfabeto romano como el japonés, mantener el formato 'expresión traducida(expresión en inglés)'.
  - Al traducir a idiomas basados en alfabeto romano como español, portugués, francés, permitir tanto la notación independiente 'expresión traducida' como la notación combinada 'expresión traducida(expresión en inglés)', y dejar que Claude elija autónomamente la más apropiada de las dos.
- Para nombres propios, la ortografía original debe preservarse en el resultado de traducción de alguna forma.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases.
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it.
  2. it may be a proper noun such as a person's name or a place name.
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language,
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'.
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### Manejo de enlaces que conectan a otros posts
Algunos posts incluyen enlaces que conectan a otros posts, y durante la fase de prueba, cuando no se proporcionaron pautas separadas sobre esto, a menudo ocurrió el problema de que interpretaba incluso la parte de la ruta de la URL como algo que debía traducirse y la cambiaba, rompiendo los enlaces internos. Este problema se resolvió agregando esta cláusula al prompt.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

(Actualización del 12025.04.06.)
Aunque proporcionar las pautas anteriores hace que el modelo maneje correctamente la parte de la ruta de los enlaces durante la traducción, reduciendo considerablemente la frecuencia de enlaces rotos, para enlaces que incluyen identificadores de fragmento (Fragment identifier), todavía había la limitación de que el modelo de lenguaje tenía que llenar aproximadamente la parte del identificador de fragmento a menos que conociera el contenido del artículo objetivo del enlace, haciendo imposible una solución fundamental del problema. Por ello, mejoré el script Python y el prompt para proporcionar información contextual sobre otros posts enlazados dentro de la etiqueta XML `<reference_context>` del prompt del usuario y manejar la traducción de enlaces según ese contexto. Como resultado de aplicar esta actualización, pude prevenir en su mayoría el problema de enlaces rotos, y para artículos de series estrechamente conectados, también se puede esperar el efecto de proporcionar traducciones más consistentes a través de múltiples posts.

Se presenta la siguiente pauta en el prompt del sistema.
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

Y la parte `<reference_context>` del prompt del usuario se compone del siguiente formato y contenido, proporcionándose adicionalmente después del contenido del texto principal que se desea traducir.
```xml
<reference_context>
The following are contents of posts linked with hash fragments in the original post. 
Use these for context when translating links and references:

<referenced_post path="{post_1_path}" hash="{hash_fragment_1}">
{post_content}
</referenced_post>

<referenced_post path="{post__2_path}" hash="{hash_fragment_2}">
{post_content}
</referenced_post>

...

</reference_context>
```

> Para ver cómo se implementó esto específicamente, consulta la [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2) de esta serie y el contenido del [script Python](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py) en el repositorio de GitHub.
{: .prompt-tip }

##### Generar solo los resultados de traducción como respuesta
Finalmente, presento la siguiente oración para que solo genere los resultados de traducción sin agregar otras palabras en la respuesta.

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Técnicas adicionales de diseño de prompts
Sin embargo, a diferencia de solicitar trabajo a humanos, también existen técnicas adicionales que se aplican específicamente a los modelos de lenguaje.
Aunque hay muchos materiales útiles sobre esto en la web, resumiendo algunos consejos representativos que se pueden usar de manera universal:
Principalmente me referí a la [guía de ingeniería de prompts de la documentación oficial de Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Estructuración usando etiquetas XML
De hecho, esto ya se ha estado usando anteriormente. Para prompts complejos que incluyen múltiples contextos, instrucciones, formatos y ejemplos, usar apropiadamente etiquetas XML como `<instructions>`, `<example>`, `<format>` ayuda al modelo de lenguaje a interpretar el prompt con precisión y producir salidas de alta calidad que cumplan con la intención. Recomiendo consultar el repositorio de GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) donde están bien organizadas las etiquetas XML útiles para escribir prompts.

#### Técnica de razonamiento paso a paso (CoT, chain of thinking)
Para tareas que requieren un nivel considerable de razonamiento como resolver problemas matemáticos o escribir documentos complejos, inducir al modelo de lenguaje a pensar en el problema paso a paso puede mejorar significativamente el rendimiento. Sin embargo, en este caso, el tiempo de respuesta puede alargarse, y esta técnica no siempre es útil para todas las tareas, por lo que hay que tener cuidado.

#### Técnica de encadenamiento de prompts (prompt chaining)
Para realizar tareas complejas, puede haber limitaciones para responder con un solo prompt. En este caso, también se puede considerar dividir todo el flujo de trabajo en varias etapas desde el principio, presentar prompts especializados para cada etapa paso a paso, y usar el método de pasar la respuesta obtenida en la etapa anterior como entrada para la siguiente etapa. Esta técnica se llama encadenamiento de prompts (prompt chaining).

#### Prellenar la primera parte de la respuesta
Al ingresar un prompt, se puede presentar previamente la primera parte del contenido a responder y hacer que escriba la respuesta que seguirá, permitiendo así omitir saludos innecesarios u otros preámbulos, o forzar respuestas en formatos específicos como XML o JSON. [En el caso de la API de Claude, se puede usar esta técnica enviando no solo el mensaje `User` sino también el mensaje `Assistant` al hacer la llamada.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevención de pereza (Parche de Halloween 12024.10.31.)
Aunque después de escribir este artículo por primera vez pasé por una o dos mejoras adicionales de prompts y especificación de instrucciones, de todos modos no hubo problemas importantes durante los 4 meses de aplicación de este sistema de automatización.

Sin embargo, desde aproximadamente las 6 PM del 12024.10.31. en hora coreana, cuando asigné el trabajo de traducción de un post recién escrito, continuó ocurriendo el fenómeno anormal de traducir solo la primera parte 'TL;DR' del post y luego interrumpir arbitrariamente la traducción.

Las posibles causas de este problema y métodos de solución se trataron en [un post separado](/posts/does-ai-hate-to-work-on-halloween), así que consulta ese artículo.

### Prompt del sistema completado
El resultado del diseño de prompts después de pasar por los pasos anteriores se puede verificar en la [siguiente parte](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2).

## Lectura adicional
Continúa en la [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
