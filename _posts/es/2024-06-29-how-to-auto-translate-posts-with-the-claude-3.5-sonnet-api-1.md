---
title: Cómo traducir automáticamente publicaciones con la API de Claude 3.5 Sonnet (1) - Diseño del prompt
description: >-
  Cubrimos el proceso de diseñar prompts y automatizar el trabajo con Python utilizando una clave API de Anthropic y los prompts creados para traducir las publicaciones de este blog a varios idiomas. Este es el primer artículo de la serie que introduce el método y proceso de diseño de prompts.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introducción
Recientemente, implementé la API de Claude 3.5 Sonnet de Anthropic para traducir las publicaciones del blog a varios idiomas. En esta serie, cubriremos las razones para elegir la API de Claude 3.5 Sonnet, los métodos de diseño de prompts y cómo implementar la automatización mediante la integración de API con scripts de Python.  
La serie consta de dos artículos, y este que estás leyendo es el primero.
- Parte 1: Introducción al modelo Claude 3.5 Sonnet, razones para su selección y prompt engineering (este artículo)
- Parte 2: [Escritura e implementación de scripts de automatización en Python utilizando la API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## Sobre Claude 3.5 Sonnet
Los modelos de la serie Claude 3 vienen en versiones Haiku, Sonnet y Opus según el tamaño del modelo.  
![Diferenciación de niveles de modelos Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Fuente de la imagen: [Página web oficial de la API de Anthropic Claude](https://www.anthropic.com/api)

Y el 21 de junio de 2024 (hora de Corea), Anthropic lanzó su último modelo de lenguaje, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Según el anuncio de Anthropic, supera el rendimiento de inferencia de Claude 3 Opus con el mismo costo y velocidad que Claude 3 Sonnet, y generalmente se considera que tiene ventajas sobre su competidor GPT-4 en áreas como redacción, razonamiento lingüístico, comprensión multilingüe y traducción.  
![Imagen de introducción de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Resultados del benchmark de rendimiento de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Fuente de las imágenes: [Página web de Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

(Actualización 31.10.2024) El 22 de octubre de 2024, Anthropic anunció una versión actualizada de la API de Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") y Claude 3.5 Haiku. Sin embargo, debido al [problema que se mencionará más adelante](#prevención-de-pereza-parche-de-halloween-31102024), este blog aún utiliza la API "claude-3-5-sonnet-20240620" original.

## Razones para implementar Claude 3.5 para la traducción de publicaciones
Incluso sin modelos de lenguaje como Claude 3.5 o GPT-4, existen APIs de traducción comerciales establecidas como Google Translate o DeepL. La razón por la que decidí usar un LLM para propósitos de traducción es que, a diferencia de otros servicios de traducción comerciales, los usuarios pueden proporcionar información contextual adicional y requisitos a través del diseño de prompts, como el propósito de escritura y los temas principales del texto, y el modelo puede proporcionar traducciones que consideren este contexto. Aunque DeepL y Google Translate generalmente muestran una excelente calidad de traducción, pueden producir resultados relativamente poco naturales cuando se les pide que traduzcan textos largos sobre temas especializados, no conversaciones cotidianas, debido a sus limitaciones para comprender el tema y el contexto general. En particular, como se mencionó anteriormente, Claude es considerado relativamente superior a su competidor GPT-4 en áreas de redacción, razonamiento lingüístico, comprensión multilingüe y traducción, y cuando lo probé brevemente, mostró una calidad de traducción más fluida que GPT-4, por lo que determiné que era adecuado para traducir los artículos de ingeniería publicados en este blog a varios idiomas.

## Diseño del Prompt
### Principios básicos para hacer solicitudes
Para obtener resultados satisfactorios que cumplan con el propósito de un modelo de lenguaje, es necesario proporcionar prompts apropiados. Aunque el diseño de prompts puede parecer abrumador, en realidad "cómo hacer una buena solicitud" no es muy diferente ya sea que el destinatario sea un modelo de lenguaje o una persona, por lo que no es tan difícil si se aborda desde esta perspectiva. Es bueno explicar claramente la situación actual y los requisitos siguiendo los principios de las 5W1H, y si es necesario, agregar algunos ejemplos específicos. Aunque existen numerosos consejos y técnicas para el diseño de prompts, la mayoría se derivan de los principios básicos que se describirán a continuación.

#### Tono general
Hay muchos informes que indican que los modelos de lenguaje producen respuestas de mayor calidad cuando los prompts se escriben y se ingresan en un tono cortés de solicitud en lugar de un tono autoritario de comando. En la sociedad en general, cuando se le pide algo a alguien, es más probable que la persona realice la tarea solicitada con más sinceridad cuando se usa el último tono en lugar del primero, y parece que los modelos de lenguaje aprenden y emulan estos patrones de respuesta humana.

#### Asignación de roles y explicación de la situación (quién, por qué)
Primero, asigné a Claude 3.5 el rol de "traductor técnico profesional" y proporcioné información contextual sobre el usuario como "un blogger de ingeniería que principalmente contribuye con artículos sobre matemáticas, física y ciencia de datos".

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Comunicación de requisitos generales (qué)
Luego, solicité traducir el texto en formato markdown proporcionado del {source_lang} al {target_lang} mientras se mantiene el formato.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Al llamar a la API de Claude, las variables de idioma de origen y destino se insertan respectivamente en los lugares {source_lang} y {target_lang} a través de la función f-string del script Python.
{: .prompt-info }

#### Especificación de requisitos y ejemplos (cómo)
Para tareas simples, las etapas anteriores pueden ser suficientes para obtener los resultados deseados, pero para tareas que requieren instrucciones más complejas, puede ser necesaria una explicación adicional.

Cuando los requisitos son complejos y múltiples, es más fácil de entender (tanto para humanos como para modelos de lenguaje) si se presentan como una lista concisa en lugar de explicarlos de manera narrativa. Además, proporcionar ejemplos cuando sea necesario puede ser útil.
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

Sin embargo, al traducir las publicaciones, aunque el título (title) y la descripción (description) deben traducirse a varios idiomas, es más conveniente para el mantenimiento dejar los nombres de categorías (categories) y etiquetas (tags) en inglés para mantener la consistencia en las URLs de las publicaciones. Por lo tanto, se resolvió este problema agregando la siguiente instrucción para no traducir ninguna etiqueta excepto 'title' y 'description'.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> Se enfatizó que **sin excepción** no se deben modificar otras etiquetas del YAML front matter agregando la frase "under any circumstances, regardless of the language you are translating to".
{: .prompt-tip }

##### Manejo de texto que incluye idiomas distintos al idioma de origen
Al escribir el texto original en coreano, cuando se introduce la definición de un concepto o se utilizan ciertos términos técnicos, a menudo se incluye la expresión en inglés entre paréntesis, como en '*중성자 감쇠 (Neutron Attenuation)*'. Al traducir estas expresiones, a veces se mantienen los paréntesis y otras veces se omite la expresión en inglés entre paréntesis, lo que resulta en inconsistencias en el método de traducción. Para abordar esto, se establecieron las siguientes pautas detalladas:
- Para términos técnicos:
  - Al traducir a idiomas que no usan el alfabeto romano, como el japonés, mantener el formato 'expresión traducida(expresión en inglés)'.
  - Al traducir a idiomas basados en el alfabeto romano, como español, portugués o francés, se permite tanto la notación independiente 'expresión traducida' como la notación combinada 'expresión traducida(expresión en inglés)', dejando que Claude elija autónomamente la que considere más apropiada.
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
Algunas publicaciones incluyen enlaces a otras publicaciones, y durante la fase de prueba, cuando no se proporcionaron pautas específicas sobre esto, surgió frecuentemente el problema de que los enlaces internos se rompían porque se interpretaba que la parte de la ruta de la URL también debía traducirse. Este problema se resolvió agregando esta frase al prompt:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Producir solo el resultado de la traducción
Finalmente, se presenta la siguiente oración para asegurar que solo se produzca el resultado de la traducción sin agregar comentarios adicionales en la respuesta:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Técnicas adicionales de diseño de prompts
Sin embargo, existen técnicas adicionales que se aplican específicamente a los modelos de lenguaje, a diferencia de cuando se solicita trabajo a humanos.
Aunque hay muchos recursos útiles sobre esto en la web, aquí hay algunos consejos representativos que pueden ser útiles de manera general.  
Se consultó principalmente la [guía de prompt engineering en la documentación oficial de Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Estructuración utilizando etiquetas XML
De hecho, esto ya se ha estado utilizando hasta ahora. Para prompts complejos que incluyen varios contextos, instrucciones, formatos y ejemplos, el uso apropiado de etiquetas XML como `<instructions>`, `<example>`, `<format>` ayuda significativamente al modelo de lenguaje a interpretar el prompt con precisión y producir resultados de alta calidad que se ajusten a la intención. El repositorio GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) tiene una buena compilación de etiquetas XML útiles para escribir prompts.

#### Técnica de razonamiento paso a paso (CoT, chain of thinking)
Para tareas que requieren un nivel considerable de razonamiento, como resolver problemas matemáticos o crear documentos complejos, guiar al modelo de lenguaje para que piense en el problema paso a paso puede mejorar significativamente su rendimiento. Sin embargo, esto puede aumentar el tiempo de respuesta, y esta técnica no siempre es útil para todas las tareas, así que hay que tener cuidado.

#### Técnica de encadenamiento de prompts (prompt chaining)
Para tareas complejas, puede haber limitaciones al usar un solo prompt. En estos casos, se puede considerar dividir el flujo de trabajo completo en varios pasos desde el principio, presentar prompts especializados para cada paso y pasar la respuesta obtenida en un paso como entrada para el siguiente paso. Esta técnica se conoce como encadenamiento de prompts.

#### Prellenado del inicio de la respuesta
Al ingresar un prompt, se puede forzar al modelo a omitir saludos innecesarios y otros preámbulos, o a responder en un formato específico como XML o JSON, presentando previamente la primera parte del contenido de la respuesta y haciendo que continúe escribiendo la respuesta a partir de ahí. [En el caso de la API de Claude, esta técnica se puede usar enviando un mensaje `Assistant` junto con el mensaje `User` al hacer la llamada.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevención de pereza (Parche de Halloween 31.10.2024)
Aunque hubo un par de mejoras menores en el prompt y especificaciones más detalladas de las instrucciones después de escribir este artículo por primera vez, no hubo problemas importantes durante los 4 meses de aplicación de este sistema de automatización.

Sin embargo, alrededor de las 6 PM (hora de Corea) del 31.10.2024, comenzó a ocurrir continuamente un fenómeno anormal donde, al asignar la traducción de nuevas publicaciones, solo traducía la parte inicial 'TL;DR' del post y luego detenía arbitrariamente la traducción.

Las causas sospechadas de este problema y sus soluciones se tratan en [una publicación separada](/posts/does-ai-hate-to-work-on-halloween), así que por favor consulta ese artículo.

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

## Lecturas adicionales
Continúa en la [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
