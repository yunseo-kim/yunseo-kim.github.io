---
title: Cómo traducir automáticamente posts con la API de Claude 3.5 Sonnet (1) - Diseño de prompts
description: Este post cubre el proceso de diseñar un prompt para la traducción multilingüe de archivos de texto markdown, y automatizar la tarea con Python utilizando una clave API obtenida de Anthropic y el prompt creado. Esta publicación es la primera de la serie e introduce los métodos y procesos de diseño de prompts.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Introducción
Recientemente implementé la API de Claude 3.5 Sonnet de Anthropic para la traducción multilingüe de las entradas de mi blog. En esta serie, explicaré por qué elegí la API de Claude 3.5 Sonnet, cómo diseñar el prompt, y cómo implementar la automatización mediante la conexión de la API y un script de Python.  
La serie consta de 2 artículos, y este que estás leyendo es el primero de ellos.
- Parte 1: Introducción al modelo Claude 3.5 Sonnet, razones para seleccionarlo y prompt engineering (este artículo)
- Parte 2: [Escribir y aplicar un script de automatización en Python utilizando la API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## Acerca de Claude 3.5 Sonnet
Los modelos de la serie Claude 3 se ofrecen en versiones Haiku, Sonnet y Opus según el tamaño del modelo.  
![Diferenciación de niveles de modelos Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Fuente de la imagen: [Página web oficial de Anthropic Claude API](https://www.anthropic.com/api)

El 21 de junio de 12024 (según el [calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar)), hora de Corea, Anthropic lanzó su modelo de lenguaje más reciente, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Según el anuncio de Anthropic, ofrece un rendimiento de razonamiento que supera a Claude 3 Opus con el mismo costo y velocidad que Claude 3 Sonnet, y generalmente se considera que tiene ventajas sobre su competidor GPT-4 en áreas como redacción, razonamiento lingüístico, comprensión multilingüe y traducción.  
![Imagen de introducción de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Resultados de benchmark de rendimiento de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Fuente de las imágenes: [Sitio web de Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

(Actualización 12024.10.31.) El 22 de octubre de 12024, Anthropic anunció una versión actualizada de la API de Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") y Claude 3.5 Haiku. Sin embargo, debido al [problema que se mencionará más adelante](#prevención-de-pereza-parche-de-halloween-120241031), este blog sigue utilizando la API "claude-3-5-sonnet-20240620" original.

## Razones para implementar Claude 3.5 para la traducción de publicaciones
Existen APIs de traducción comerciales como Google Translate o DeepL, sin necesidad de usar modelos de lenguaje como Claude 3.5 o GPT-4. Sin embargo, decidí usar un LLM para traducción porque, a diferencia de otros servicios comerciales, permite proporcionar información contextual adicional o requisitos a través del diseño de prompts, como el propósito de escritura o los temas principales, y el modelo puede ofrecer traducciones que tienen en cuenta este contexto. Aunque DeepL y Google Translate generalmente ofrecen excelente calidad de traducción, tienen limitaciones para captar el tema o el contexto general, lo que puede resultar en traducciones menos naturales para textos largos sobre temas especializados. Como se mencionó anteriormente, Claude tiene una reputación de ser relativamente superior a GPT-4 en redacción, razonamiento lingüístico, comprensión multilingüe y traducción, y mis propias pruebas mostraron que ofrecía traducciones más fluidas que GPT-4o, por lo que lo consideré adecuado para traducir los artículos de ingeniería de este blog a varios idiomas.

## Diseño de prompts
### Principios básicos para hacer solicitudes
Para obtener resultados satisfactorios que cumplan con nuestro propósito de un modelo de lenguaje, debemos proporcionar prompts apropiados. Aunque el diseño de prompts puede parecer abrumador, en realidad "cómo solicitar algo correctamente" no es muy diferente ya sea que estemos hablando con un modelo de lenguaje o con una persona, por lo que abordar desde esta perspectiva lo hace bastante sencillo. Es útil explicar claramente la situación actual y los requisitos siguiendo los principios de las 5W1H, y añadir algunos ejemplos específicos si es necesario. Existen numerosos consejos y técnicas para el diseño de prompts, pero la mayoría derivan de los principios básicos que se describen a continuación.

#### Tono general
Hay muchos informes que indican que los modelos de lenguaje producen respuestas de mayor calidad cuando los prompts se escriben en un tono educado de solicitud en lugar de órdenes autoritarias. Normalmente, en la sociedad, cuando pedimos algo a alguien, es más probable que realicen la tarea con diligencia si lo pedimos cortésmente en lugar de ordenarlo autoritariamente. Los modelos de lenguaje parecen imitar estos patrones de respuesta humana que han aprendido.

#### Asignación de roles y explicación de la situación (quién, por qué)
Primero, asigné a Claude 3.5 el rol de *'traductor técnico profesional'* y proporcioné información contextual sobre el usuario como *"un blogger de ingeniería que escribe principalmente sobre matemáticas, física y ciencia de datos"*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Comunicación de la solicitud general (qué)
A continuación, solicité que tradujera el texto en formato markdown proporcionado del {source_lang} al {target_lang} manteniendo el formato.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Al llamar a la API de Claude, las variables de idioma de origen y destino se insertan en los marcadores {source_lang} y {target_lang} del prompt mediante la función f-string de Python.
{: .prompt-info }

#### Especificación de requisitos y ejemplos (cómo)
Para tareas simples, los pasos anteriores podrían ser suficientes para obtener los resultados deseados, pero para tareas más complejas, pueden ser necesarias explicaciones adicionales.

Cuando los requisitos son complejos y múltiples, es mejor presentarlos como una lista concisa en lugar de explicaciones largas, lo que mejora la legibilidad y facilita la comprensión tanto para humanos como para modelos de lenguaje. También es útil proporcionar ejemplos cuando sea necesario.
En este caso, añadí las siguientes condiciones:

##### Manejo del YAML front matter
El YAML front matter al principio de las publicaciones de blog escritas en markdown para Jekyll contiene información sobre 'title', 'description', 'categories' y 'tags'. Por ejemplo, el YAML front matter de este artículo es:

```yaml
---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법
description: \>-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
  그리고 Anthropic으로부터 발급받은 API 키와 앞서 작성한 프롬프트를 적용하여 Python으로 번역 자동화 스크립트를 작성하고 활용하는 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

Al traducir publicaciones, los tags 'title' y 'description' deben traducirse a varios idiomas, pero para mantener la consistencia de las URLs, es mejor dejar los nombres de 'categories' y 'tags' en inglés. Por lo tanto, añadí la siguiente instrucción para evitar que se traduzcan tags que no sean 'title' y 'description':

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> Añadí la frase "under any circumstances, regardless of the language you are translating to" para enfatizar que **sin excepciones** no se deben modificar otros tags del YAML front matter.
{: .prompt-tip }

##### Manejo de texto que contiene idiomas distintos al idioma de origen
Al escribir en coreano, a veces incluyo expresiones en inglés entre paréntesis cuando introduzco definiciones de conceptos o uso términos técnicos, como '*중성자 감쇠 (Neutron Attenuation)*'. Al traducir estas expresiones, a veces se mantienen los paréntesis y otras veces se omite el inglés entre paréntesis, lo que resulta en inconsistencias. Para abordar esto, establecí las siguientes directrices:
- Para términos técnicos:
  - Al traducir a idiomas no basados en el alfabeto romano como el japonés, mantener el formato 'expresión traducida(expresión en inglés)'.
  - Al traducir a idiomas basados en el alfabeto romano como español, portugués o francés, permitir tanto la notación única 'expresión traducida' como la notación combinada 'expresión traducida(expresión en inglés)', dejando que Claude elija la más apropiada.
- Para nombres propios, la ortografía original debe preservarse de alguna forma en la traducción.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
  2. it may be a proper noun such as a person's name or a place name. \n\
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
  <if>it is the first case, and the target language is not a Roman alphabet-based language, \
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
      You can choose whichever you think is more appropriate.</example>\n\
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### Manejo de enlaces a otras publicaciones
Algunas publicaciones incluyen enlaces a otras publicaciones, y durante la fase de prueba, sin directrices específicas, el modelo a veces traducía incluso la parte de la ruta de la URL, rompiendo los enlaces internos. Resolví este problema añadiendo esta instrucción:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Producir solo el resultado de la traducción como respuesta
Finalmente, para asegurar que la respuesta contenga solo el resultado de la traducción sin texto adicional, incluí esta instrucción:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Técnicas adicionales de diseño de prompts
A diferencia de hacer solicitudes a humanos, existen técnicas adicionales que se aplican específicamente a los modelos de lenguaje.
Hay muchos recursos útiles en línea sobre este tema, pero aquí hay algunos consejos representativos que pueden ser útiles de manera general:  
Me basé principalmente en la [guía oficial de ingeniería de prompts de Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Estructuración mediante etiquetas XML
De hecho, ya he estado utilizando esto a lo largo del artículo. Para prompts complejos que incluyen varios contextos, instrucciones, formatos y ejemplos, el uso adecuado de etiquetas XML como `<instructions>`, `<example>`, `<format>` puede ayudar significativamente al modelo a interpretar correctamente el prompt y producir resultados de alta calidad que se ajusten a la intención. El repositorio GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) tiene una buena compilación de etiquetas XML útiles para la redacción de prompts.

#### Técnica de razonamiento paso a paso (CoT, chain of thinking)
Para tareas que requieren un nivel significativo de razonamiento, como resolver problemas matemáticos o crear documentos complejos, guiar al modelo para que piense en pasos puede mejorar considerablemente su rendimiento. Sin embargo, esto puede aumentar el tiempo de respuesta y no es útil para todas las tareas.

#### Técnica de encadenamiento de prompts (prompt chaining)
Para tareas complejas, un solo prompt puede tener limitaciones. En estos casos, se puede considerar dividir todo el flujo de trabajo en varios pasos desde el principio, presentando prompts especializados para cada paso y pasando la respuesta de un paso como entrada para el siguiente. Esta técnica se conoce como encadenamiento de prompts.

#### Prellenado de la primera parte de la respuesta
Al introducir un prompt, se puede presentar la primera parte de la respuesta esperada y hacer que el modelo continúe, lo que permite omitir saludos innecesarios o forzar respuestas en formatos específicos como XML o JSON. [En el caso de la API de Claude, esta técnica se puede utilizar enviando tanto un mensaje de `User` como un mensaje de `Assistant` al hacer la llamada.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevención de pereza (Parche de Halloween 12024.10.31.)
Aunque hice algunas mejoras menores en el prompt y aclaré algunas instrucciones después de escribir este artículo por primera vez, el sistema de automatización funcionó sin problemas importantes durante 4 meses.

Sin embargo, alrededor de las 6 PM KST del 12024.10.31., comenzó a ocurrir un fenómeno extraño: al asignar la traducción de nuevas publicaciones, el modelo solo traducía la sección inicial 'TL;DR' y luego interrumpía arbitrariamente la traducción.

He abordado las causas probables de este problema y las soluciones en [una publicación separada](/posts/does-ai-hate-to-work-on-halloween), a la que puedes referirte para más detalles.

### Prompt finalizado
El resultado del diseño de prompt siguiendo los pasos anteriores es el siguiente:

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role> The customer's request is as follows:\n\n \
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task> \
In the provided markdown format text, \n\
  - <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
  - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
    1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
    2. it may be a proper noun such as a person's name or a place name. \n\
    After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
    <if>it is the first case, and the target language is not a Roman alphabet-based language, \
    please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
      - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
      - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
    <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
      - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
        You can choose whichever you think is more appropriate.</example>\n\
      - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
        French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
    <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
      - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
        In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
        redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
    </condition>\n\n\
  - <condition><if>the provided text contains links in markdown format, \
    please translate the link text and the fragment part of the URL into {target_lang}, \
    but keep the path part of the URL intact.</if> \n\
    - <example> the German translation of '[중성자 상호작용과 반응단면적]\
      (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
      would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
      #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

## Lecturas adicionales
Continúa en la [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
