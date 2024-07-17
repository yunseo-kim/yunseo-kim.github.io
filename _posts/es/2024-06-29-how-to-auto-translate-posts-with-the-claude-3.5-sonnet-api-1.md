---
title: Cómo traducir automáticamente publicaciones con la API de Claude 3.5 Sonnet (1)
description: >-
  Se presenta brevemente el modelo Claude 3.5 Sonnet recientemente lanzado, y se comparte el proceso de diseño del prompt y el resultado final del prompt para aplicarlo a la traducción multilingüe de las publicaciones de este blog.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introducción
Recientemente, he introducido la API de Claude 3.5 Sonnet de Anthropic para la traducción multilingüe de las publicaciones del blog. En este contexto, quiero abordar las razones por las que elegí la API de Claude 3.5 Sonnet, el método de diseño del prompt, y cómo implementar la integración y automatización de la API a través de un script de Python. Dado que el contenido que quiero cubrir es bastante extenso, esto no será una sola publicación sino una serie, y esta es la primera publicación de la serie.

## Acerca de Claude 3.5 Sonnet
Los modelos de la serie Claude 3 se ofrecen en versiones Haiku, Sonnet y Opus según el tamaño del modelo.  
![Distinción de niveles de modelos Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Fuente de la imagen: [Página web oficial de la API de Anthropic Claude](https://www.anthropic.com/api)

Y el 21 de junio de 2024, hora de Corea, Anthropic lanzó su último modelo de lenguaje, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Según el anuncio de Anthropic, muestra un rendimiento de inferencia que supera a Claude 3 Opus con el mismo costo y velocidad que el Claude 3 Sonnet existente, y generalmente se considera que tiene ventajas sobre su modelo competidor GPT-4 en las áreas de redacción, razonamiento lingüístico, comprensión multilingüe y traducción.  
![Imagen de introducción de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Resultados del benchmark de rendimiento de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Fuente de las imágenes: [Página web de Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

## Razones para introducir Claude 3.5 para la traducción de publicaciones
Incluso sin modelos de lenguaje como Claude 3.5 o GPT-4, existen APIs de traducción comerciales existentes como Google Translate o DeepL. Sin embargo, la razón por la que decidí usar un LLM para fines de traducción es que, a diferencia de otros servicios de traducción comerciales, el usuario puede proporcionar información contextual adicional o requisitos además del texto principal, como el propósito de escritura o los temas principales del artículo, a través del diseño del prompt, y el modelo puede proporcionar una traducción que tenga en cuenta el contexto en consecuencia. Aunque DeepL y Google Translate generalmente muestran una excelente calidad de traducción, debido a la limitación de no comprender bien el tema o el contexto general del texto, a veces los resultados de traducción son relativamente poco naturales cuando se les pide que traduzcan textos largos sobre temas especializados en lugar de conversaciones cotidianas. En particular, como se mencionó anteriormente, Claude se considera superior a su modelo competidor GPT-4 en las áreas de redacción, razonamiento lingüístico, comprensión multilingüe y traducción, por lo que se consideró adecuado para la tarea de traducir los artículos de ingeniería publicados en este blog a varios idiomas.

## Diseño del prompt
### Principios básicos del diseño del prompt
Para obtener resultados satisfactorios que cumplan con el propósito de un modelo de lenguaje, es necesario proporcionar un prompt apropiado. Aunque el diseño del prompt puede parecer abrumador, en realidad no es muy difícil si se aborda desde la perspectiva de que "cómo solicitar algo bien" no es muy diferente ya sea que el destinatario sea un modelo de lenguaje o una persona. Es bueno explicar claramente la situación actual y los requisitos de acuerdo con los principios de las 5W1H, y si es necesario, agregar algunos ejemplos específicos. Aunque existen numerosos consejos y técnicas para el diseño de prompts, la mayoría se derivan de los principios básicos mencionados anteriormente.

### Asignación de roles y explicación de la situación (quién, por qué)
Primero, asigné a Claude 3.5 el papel de *"traductor técnico profesional"* y proporcioné información contextual sobre el usuario como *"un bloguero de ingeniería que escribe principalmente sobre matemáticas, física y ciencia de datos"*.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Transmisión de requisitos generales (qué)
A continuación, solicité traducir el texto en formato markdown proporcionado por el usuario de {source_lang} a {target_lang} mientras se mantiene el formato.
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Al llamar a la API de Claude, las posiciones {source_lang} y {target_lang} en el prompt se llenan respectivamente con las variables de idioma de origen y destino a través de la función f-string del script de Python.
{: .prompt-info }

### Especificación de requisitos y ejemplos (cómo)
Aunque hasta este punto puede ser suficiente para obtener los resultados deseados en algunos casos, para tareas más complejas puede ser necesaria una explicación adicional. En este caso, se agregaron las siguientes condiciones.

#### Manejo de casos donde el texto original incluye idiomas distintos al idioma de origen
Al escribir el texto original en coreano, a veces cuando se introduce la definición de un concepto por primera vez o se usan algunos términos técnicos, se incluye la expresión en inglés entre paréntesis, como en '*중성자 감쇠 (Neutron Attenuation)*'. Al traducir tales expresiones, a veces se mantenían los paréntesis y otras veces se omitía el inglés dentro de los paréntesis, lo que resultaba en un método de traducción inconsistente. Para abordar este problema, se agregó la siguiente oración al prompt:
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Manejo de enlaces a otras publicaciones
Algunas publicaciones incluyen enlaces a otras publicaciones, y a menudo surgía el problema de que los enlaces internos se rompían porque la parte de la ruta de la URL se interpretaba como algo que debía traducirse. Este problema se resolvió agregando esta oración al prompt:
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Solicitud de producir solo el resultado de la traducción como respuesta
Finalmente, se presenta la siguiente oración para que solo se produzca el resultado de la traducción como salida, sin agregar ningún comentario adicional:
> The output should only contain the translated text.

### Prompt completado
El resultado del diseño del prompt a través de los pasos anteriores es el siguiente:
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.