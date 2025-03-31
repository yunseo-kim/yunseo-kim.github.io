---
title: Cómo traducir automáticamente publicaciones con la API de Claude 3.5 Sonnet (1) - Diseño de prompts
description: Diseñamos prompts para la traducción multilingüe de archivos de texto en markdown y cubrimos el proceso de automatización del trabajo en Python aplicando la clave API obtenida de Anthropic y el prompt creado. Esta publicación es la primera de la serie e introduce los métodos y procesos de diseño de prompts.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Introducción
Recientemente, implementé la API de Claude 3.5 Sonnet de Anthropic para la traducción multilingüe de las publicaciones del blog. En esta serie, abordaré las razones para elegir la API de Claude 3.5 Sonnet, los métodos de diseño de prompts y cómo implementar la automatización mediante la integración de API y scripts de Python.  
La serie consta de dos publicaciones, y esta es la primera de ellas.
- Parte 1: Introducción al modelo Claude 3.5 Sonnet, razones para su selección y ingeniería de prompts (este artículo)
- Parte 2: [Escritura y aplicación de scripts de automatización en Python utilizando la API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## Acerca de Claude 3.5 Sonnet
Los modelos de la serie Claude 3 se ofrecen en versiones Haiku, Sonnet y Opus según el tamaño del modelo.  
![Diferenciación de niveles de modelos Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Fuente de la imagen: [Página web oficial de la API de Claude de Anthropic](https://www.anthropic.com/api)

Y el 21 de junio del 12024 (según el [calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar)), hora de Corea, Anthropic lanzó su último modelo de lenguaje, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Según el anuncio de Anthropic, supera el rendimiento de inferencia de Claude 3 Opus con el mismo costo y velocidad que el Claude 3 Sonnet original, y generalmente se considera que tiene ventajas sobre su modelo competidor, GPT-4, en áreas como redacción, razonamiento lingüístico, comprensión multilingüe y traducción.  
![Imagen de introducción de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Resultados de evaluación comparativa de rendimiento de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Fuente de las imágenes: [Página web de Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

(Actualización del 12024.10.31.) El 22 de octubre del 12024, Anthropic anunció una versión actualizada de la API de Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") y Claude 3.5 Haiku. Sin embargo, debido al [problema que se mencionará más adelante](#prevención-de-la-pereza-parche-de-halloween-del-20241031), este blog aún está utilizando la API "claude-3-5-sonnet-20240620" existente.

## Razones para implementar Claude 3.5 para la traducción de publicaciones
Incluso sin necesidad de modelos de lenguaje como Claude 3.5 o GPT-4, existen APIs de traducción comerciales existentes como Google Translate o DeepL. Sin embargo, la razón por la que decidí usar un LLM para fines de traducción es que, a diferencia de otros servicios de traducción comerciales, el usuario puede proporcionar información contextual adicional o requisitos a través del diseño de prompts, como el propósito de escritura o los temas principales del texto, además del contenido principal, y el modelo puede proporcionar una traducción que tenga en cuenta este contexto. Aunque DeepL y Google Translate generalmente muestran una excelente calidad de traducción, debido a la limitación de no comprender bien el tema o el contexto general del texto, cuando se les pide que traduzcan textos largos sobre temas especializados en lugar de conversaciones cotidianas, los resultados de la traducción tienden a ser relativamente poco naturales. En particular, como se mencionó anteriormente, Claude se considera generalmente superior a su modelo competidor GPT-4 en áreas como redacción, razonamiento lingüístico, comprensión multilingüe y traducción, y cuando lo probé brevemente, mostró una calidad de traducción más fluida que GPT-4o, por lo que consideré que era adecuado para la tarea de traducir los artículos de ingeniería publicados en este blog a varios idiomas.

## Diseño de prompts
### Principios básicos al hacer una solicitud
Para obtener resultados satisfactorios que cumplan con el propósito de un modelo de lenguaje, es necesario proporcionar un prompt adecuado. Aunque el diseño de prompts puede parecer abrumador, en realidad, "cómo hacer una buena solicitud" no es muy diferente ya sea que el destinatario sea un modelo de lenguaje o una persona, por lo que abordar desde esta perspectiva no es tan difícil. Es bueno explicar claramente la situación actual y los requisitos de acuerdo con las cinco W y una H, y si es necesario, agregar algunos ejemplos específicos. Aunque existen numerosos consejos y técnicas para el diseño de prompts, la mayoría se derivan de los principios básicos que se describirán a continuación.

#### Tono general
Se ha informado ampliamente que cuando se escriben y se ingresan prompts con un tono de solicitud cortés en lugar de un tono de comando autoritario, el modelo de lenguaje produce respuestas de mayor calidad. Normalmente, cuando se le pide algo a alguien en la sociedad, la probabilidad de que la otra persona realice la tarea solicitada con más sinceridad es mayor cuando se utiliza el primero tipo de tono en lugar del segundo, y parece que los modelos de lenguaje aprenden y emulan este patrón de respuesta humana.

#### Asignación de roles y explicación de la situación (quién, por qué)
Primero, asigné a Claude 3.5 el papel de *"traductor profesional técnico (professional technical translator)"* y proporcioné información contextual sobre el usuario como *"un bloguero de ingeniería que principalmente contribuye con artículos sobre matemáticas, física y ciencia de datos"*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Comunicación de la solicitud general (qué)
A continuación, solicité traducir el texto en formato markdown proporcionado por el usuario de {source_lang} a {target_lang} mientras se mantiene el formato.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Al llamar a la API de Claude, las posiciones de {source_lang} y {target_lang} en el prompt se llenan respectivamente con las variables de idioma de origen y destino de la traducción a través de la función f-string del script de Python.
{: .prompt-info }

#### Especificación de requisitos y ejemplos (cómo)
Para tareas simples, los pasos anteriores pueden ser suficientes para obtener los resultados deseados, pero para tareas que requieren explicaciones adicionales, puede ser necesario proporcionar más detalles.

Cuando los requisitos son complejos y múltiples, es más fácil de entender desde la perspectiva del lector (ya sea humano o modelo de lenguaje) si se presentan en forma de lista concisa en lugar de describirlos detalladamente. Además, proporcionar ejemplos si es necesario puede ser útil.
En este caso, se agregaron las siguientes condiciones:

##### Manejo del YAML front matter
El YAML front matter ubicado al principio de las publicaciones escritas en markdown para cargar en el blog Jekyll registra información de 'title', 'description', 'categories' y 'tags'. Por ejemplo, el YAML front matter de este artículo es el siguiente:

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

Sin embargo, al traducir la publicación, las etiquetas de título (title) y descripción (description) deben traducirse a varios idiomas, pero para mantener la coherencia de la URL de la publicación, es más fácil de mantener si los nombres de categorías (categories) y etiquetas (tags) se dejan en inglés sin traducir. Por lo tanto, se agregó la siguiente instrucción para evitar la traducción de etiquetas que no sean 'title' y 'description'. Como Claude probablemente ya ha aprendido información sobre el YAML front matter, esta explicación debería ser suficiente en la mayoría de los casos.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> Se enfatizó que no se deben modificar otras etiquetas del YAML front matter **sin excepciones** agregando la frase "under any circumstances, regardless of the language you are translating to".
{: .prompt-tip }

##### Manejo de casos en los que el texto original incluye idiomas distintos al idioma de origen
Al escribir el texto original en coreano, a menudo se incluye la expresión en inglés entre paréntesis cuando se introduce la definición de un concepto o se utilizan algunos términos técnicos, como en '*중성자 감쇠 (Neutron Attenuation)*'. Al traducir estas expresiones, a veces se mantienen los paréntesis y otras veces se omite el inglés entre paréntesis, lo que resulta en un problema de inconsistencia en el método de traducción. Para abordar esto, se establecieron las siguientes pautas detalladas:
- Para términos técnicos:
  - Al traducir a idiomas no basados en el alfabeto romano, como el japonés, mantener el formato 'expresión traducida(expresión en inglés)'.
  - Al traducir a idiomas basados en el alfabeto romano, como español, portugués o francés, se permite tanto la notación única 'expresión traducida' como la notación combinada 'expresión traducida(expresión en inglés)', y se permite que Claude elija autónomamente la que considere más apropiada.
- Para nombres propios, la ortografía original debe preservarse de alguna forma en el resultado de la traducción.

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
Algunas publicaciones incluyen enlaces a otras publicaciones, y durante la fase de prueba, cuando no se proporcionaron instrucciones específicas sobre esto, a menudo surgía el problema de que los enlaces internos se rompían porque se interpretaba que incluso la parte de la ruta de la URL debía ser traducida. Este problema se resolvió agregando la siguiente frase al prompt:

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
Finalmente, se presenta la siguiente frase para que solo se produzca el resultado de la traducción sin agregar ningún otro comentario en la respuesta:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Técnicas adicionales de diseño de prompts
Sin embargo, a diferencia de cuando se solicita una tarea a un humano, existen técnicas adicionales que se aplican específicamente en el caso de los modelos de lenguaje.
Aunque hay muchos recursos útiles sobre esto en la web, aquí se resumen algunos consejos representativos que se pueden utilizar de manera general:  
Se ha consultado principalmente la [guía de ingeniería de prompts en la documentación oficial de Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Estructuración utilizando etiquetas XML
De hecho, esto ya se ha estado utilizando hasta ahora. Para prompts complejos que incluyen varios contextos, instrucciones, formatos y ejemplos, el uso apropiado de etiquetas XML como `<instructions>`, `<example>`, `<format>`, etc., puede ser de gran ayuda para que el modelo de lenguaje interprete con precisión el prompt y produzca una salida de alta calidad que se ajuste a la intención. El repositorio de GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) tiene una buena recopilación de etiquetas XML útiles para escribir prompts, por lo que se recomienda consultarlo.

#### Técnica de razonamiento paso a paso (CoT, chain of thinking)
Para tareas que requieren un nivel considerable de razonamiento, como la resolución de problemas matemáticos o la redacción de documentos complejos, guiar al modelo de lenguaje para que piense en el problema paso a paso puede mejorar significativamente el rendimiento. Sin embargo, en este caso, el tiempo de respuesta puede aumentar, y esta técnica no siempre es útil para todas las tareas, así que hay que tener cuidado.

#### Técnica de encadenamiento de prompts (prompt chaining)
Cuando se necesita realizar una tarea compleja, puede haber limitaciones al abordarla con un solo prompt. En este caso, se puede considerar dividir todo el flujo de trabajo en varias etapas desde el principio, presentar prompts especializados para cada etapa y pasar la respuesta obtenida en la etapa anterior como entrada para la siguiente etapa. Esta técnica se conoce como encadenamiento de prompts (prompt chaining).

#### Prellenado de la primera parte de la respuesta
Al ingresar el prompt, se puede forzar a omitir saludos innecesarios u otros preámbulos, o forzar a responder en un formato específico como XML o JSON, presentando previamente la primera parte del contenido de la respuesta y solicitando que se continúe la respuesta a partir de ahí. [En el caso de la API de Claude, esta técnica se puede utilizar enviando un mensaje de `Assistant` junto con el mensaje de `User` al hacer la llamada.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevención de la pereza (Parche de Halloween del 12024.10.31.)
Aunque hubo una o dos mejoras menores en el prompt y una mayor especificación de las instrucciones después de escribir este artículo por primera vez, no hubo grandes problemas durante los 4 meses de aplicación de este sistema de automatización.

Sin embargo, a partir de las 6 PM del 12024.10.31. hora de Corea, cuando se asignaba la tarea de traducir una nueva publicación, persistía una anomalía en la que solo se traducía la primera parte 'TL;DR' de la publicación y luego se interrumpía arbitrariamente la traducción.

La causa probable de este problema y el método de solución se tratan en [una publicación separada](/posts/does-ai-hate-to-work-on-halloween), así que por favor consulta ese artículo.

### Prompt completado
El resultado del diseño del prompt siguiendo los pasos anteriores es el siguiente:

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

## Lectura adicional
Continúa en la [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
