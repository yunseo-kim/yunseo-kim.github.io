---
title: Cómo traducir automáticamente publicaciones con la API de Claude 3.5 Sonnet
description: >-
  Se presenta brevemente el modelo Claude 3.5 Sonnet recientemente lanzado, y se comparte el proceso de diseño del prompt y el resultado final para aplicarlo a la traducción multilingüe de las publicaciones de este blog.
  Además, se introduce cómo escribir y utilizar un script de automatización de traducción en Python utilizando la clave API obtenida de Anthropic y el prompt previamente escrito.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introducción
Recientemente, introduje la API de Claude 3.5 Sonnet de Anthropic para la traducción multilingüe de las publicaciones del blog. En este artículo, abordaré las razones para elegir la API de Claude 3.5 Sonnet, el método de diseño del prompt y cómo implementar la automatización mediante la integración de la API con un script de Python.

## Acerca de Claude 3.5 Sonnet
Los modelos de la serie Claude 3 se ofrecen en versiones Haiku, Sonnet y Opus según el tamaño del modelo.  
![Diferenciación de niveles de modelos Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Fuente de la imagen: [Página web oficial de la API de Anthropic Claude](https://www.anthropic.com/api)

Y el 21 de junio de 2024, hora de Corea, Anthropic lanzó su último modelo de lenguaje, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Según el anuncio de Anthropic, muestra un rendimiento de inferencia que supera a Claude 3 Opus con el mismo costo y velocidad que el Claude 3 Sonnet existente, y generalmente se considera que tiene ventajas sobre su modelo competidor GPT-4 en áreas como redacción, razonamiento lingüístico, comprensión multilingüe y traducción.  
![Imagen de introducción de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Resultados del benchmark de rendimiento de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Fuente de las imágenes: [Página web de Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

## Razones para introducir Claude 3.5 para la traducción de publicaciones
Incluso sin modelos de lenguaje como Claude 3.5 o GPT-4, existen APIs de traducción comerciales existentes como Google Translate o DeepL. Sin embargo, la razón por la que decidí usar un LLM para fines de traducción es que, a diferencia de otros servicios de traducción comerciales, el usuario puede proporcionar información contextual adicional o requisitos, como el propósito de escritura o los temas principales del texto, a través del diseño del prompt, y el modelo puede proporcionar una traducción que tenga en cuenta el contexto de acuerdo con esto. Aunque DeepL y Google Translate generalmente muestran una excelente calidad de traducción, debido a la limitación de no comprender bien el tema o el contexto general del texto, cuando se les pide que traduzcan textos largos sobre temas especializados en lugar de conversaciones cotidianas, los resultados de la traducción tienden a ser relativamente poco naturales. En particular, como se mencionó anteriormente, Claude se considera generalmente superior a su modelo competidor GPT-4 en áreas como redacción, razonamiento lingüístico, comprensión multilingüe y traducción, por lo que se consideró adecuado para la tarea de traducir los textos de ingeniería publicados en este blog a varios idiomas.

## Diseño del prompt
### Principios básicos del diseño del prompt
Para obtener resultados satisfactorios que cumplan con el propósito del modelo de lenguaje, es necesario proporcionar un prompt apropiado. Aunque el diseño del prompt puede parecer abrumador, en realidad no es muy difícil si se aborda desde la perspectiva de que "cómo solicitar algo bien" no es muy diferente ya sea que el destinatario sea un modelo de lenguaje o una persona. Es bueno explicar claramente la situación actual y los requisitos de acuerdo con los principios de las 5W1H, y si es necesario, agregar algunos ejemplos específicos. Existen numerosos consejos y técnicas para el diseño de prompts, pero la mayoría se derivan de los principios básicos mencionados anteriormente.

### Asignación de roles y explicación de la situación (quién, por qué)
Primero, asigné a Claude 3.5 el papel de *"traductor técnico profesional"* y proporcioné información contextual sobre el usuario como *"un bloguero de ingeniería que principalmente escribe sobre matemáticas, física y ciencia de datos"*.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Transmisión de requisitos generales (qué)
A continuación, solicité traducir el texto en formato markdown proporcionado por el usuario de {source_lang} a {target_lang} manteniendo el formato.
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Al llamar a la API de Claude, las posiciones {source_lang} y {target_lang} en el prompt se llenan respectivamente con las variables de idioma de origen y destino a través de la función f-string del script de Python.
{: .prompt-info }

### Especificación de requisitos y ejemplos (cómo)
Para tareas simples, los pasos anteriores pueden ser suficientes para obtener los resultados deseados, pero para tareas más complejas, puede ser necesaria una explicación adicional. En este caso, se agregaron las siguientes condiciones.

#### Manejo del YAML front matter
El YAML front matter ubicado al principio de las publicaciones escritas en markdown para cargar en el blog Jekyll registra información de 'title', 'description', 'categories' y 'tags'. Por ejemplo, el YAML front matter de este artículo es el siguiente:

```YAML
---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법
description: >-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
  그리고 Anthropic으로부터 발급받은 API 키와 앞서 작성한 프롬프트를 적용하여 Python으로 번역 자동화 스크립트를 작성하고 활용하는 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

Sin embargo, al traducir la publicación, las etiquetas de título (title) y descripción (description) deben traducirse a varios idiomas, pero para mantener la consistencia de la URL de la publicación, es más fácil de mantener si los nombres de categorías (categories) y etiquetas (tags) se dejan en inglés sin traducir. Por lo tanto, se dio la siguiente instrucción para no traducir las etiquetas excepto 'title' y 'description'. Como Claude probablemente ya ha aprendido información sobre el YAML front matter, esta explicación debería ser suficiente en la mayoría de los casos.
> In the provided markdown formatted text, do not translate the YAML front matter except for the 'title' and 'description' tags.

#### Manejo de casos en los que el texto original contiene idiomas distintos al idioma de origen
Al escribir el texto original en coreano, a menudo se incluye la expresión en inglés entre paréntesis cuando se introduce la definición de un concepto o se utilizan algunos términos técnicos, como '*중성자 감쇠 (Neutron Attenuation)*'. Al traducir tales expresiones, a veces se mantenían los paréntesis y otras veces se omitía el inglés entre paréntesis, lo que resultaba en un método de traducción inconsistente. Para abordar este problema, se agregó la siguiente oración al prompt:
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Manejo de enlaces a otras publicaciones
Algunas publicaciones incluyen enlaces a otras publicaciones, y a menudo surgía el problema de que los enlaces internos se rompían porque la parte de la ruta de la URL se interpretaba como algo que debía traducirse. Este problema se resolvió agregando esta oración al prompt:
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Solicitar que la respuesta solo contenga el resultado de la traducción
Finalmente, se presenta la siguiente oración para que solo se produzca el resultado de la traducción como respuesta, sin agregar ningún comentario adicional:
> The output should only contain the translated text.

### Prompt completado
El resultado del diseño del prompt a través de los pasos anteriores es el siguiente:
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.

## Integración de la API de Claude
### Obtención de la clave API de Claude

> Aquí se explica cómo obtener una nueva clave API de Claude. Si ya tienes una clave API para usar, puedes omitir este paso.
{: .prompt-tip }

Accede a <https://console.anthropic.com> e inicia sesión. Si aún no tienes una cuenta, primero debes registrarte. Después de iniciar sesión, verás una pantalla de panel de control como la siguiente.  
![Panel de control de Anthropic Console](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Al hacer clic en el botón 'Get API keys' en esa pantalla, verás una pantalla como la siguiente.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Como ya tengo una clave creada, se muestra una clave llamada `yunseo-secret-key`, pero si acabas de crear una cuenta y aún no has obtenido una clave API, probablemente no tengas ninguna clave. Puedes obtener una nueva clave haciendo clic en el botón 'Create Key' en la parte superior derecha.

> Cuando completes la obtención de la clave, se mostrará tu clave API en la pantalla, pero esta clave no se podrá ver nuevamente más adelante, así que asegúrate de guardarla en un lugar seguro.
{: .prompt-warning }

### (Recomendado) Registro de la clave API de Claude en variables de entorno
Para utilizar la API de Claude en scripts de Python o Shell, es necesario cargar la clave API. Aunque existe la opción de registrar la clave API en el propio script, esto no es posible si necesitas compartir el script con otros a través de GitHub u otros medios. Además, incluso si no tenías intención de compartir el archivo del script, existe el riesgo de que la clave API se filtre junto con el archivo del script en caso de una filtración accidental no intencionada. Por lo tanto, se recomienda registrar la clave API en las variables de entorno del sistema que solo tú utilizas y cargar esa variable de entorno en el script. A continuación, se introduce cómo registrar la clave API en las variables de entorno del sistema basado en UNIX. Para Windows, consulta otros artículos en la web.

1. En la terminal, ejecuta `nano ~/.bashrc` o `nano ~/.zshrc` según el tipo de shell que uses para abrir el editor.
2. Agrega `export ANTHROPIC_API_KEY='your-api-key-here'` al contenido del archivo. Reemplaza 'your-api-key-here' con tu propia clave API, y asegúrate de envolverla con comillas simples.
3. Guarda los cambios y sal del editor.
4. Ejecuta `source ~/.bashrc` o `source ~/.zshrc` en la terminal para aplicar los cambios.

### Instalación de los paquetes de Python necesarios
Si el paquete anthropic no está instalado en tu entorno de Python, instálalo con el siguiente comando:
```bash
pip3 install anthropic
```
Además, los siguientes paquetes también son necesarios para usar el script de traducción de publicaciones que se introducirá más adelante, así que instálalos o actualízalos con el siguiente comando:
```bash
pip3 install -U argparse tqdm
```

### Escritura del script de Python
El script de traducción de publicaciones que se introducirá en este artículo consta de 3 archivos de script de Python y 1 archivo CSV:

- `compare_hash.py`: Calcula los valores hash SHA256 de las publicaciones originales en coreano en el directorio `_posts/ko`{: .filepath}, los compara con los valores hash existentes registrados en el archivo `hash.csv`, y devuelve una lista de nombres de archivos modificados o recién agregados
- `hash.csv`: Archivo CSV que registra los valores hash SHA256 de los archivos de publicaciones existentes
- `prompt.py`: Recibe los valores de filepath, source_lang, target_lang, carga el valor de la clave API de Claude desde las variables de entorno del sistema, luego llama a la API y envía el prompt que escribimos anteriormente como prompt del sistema y el contenido de la publicación a traducir en 'filepath' como prompt del usuario. Luego recibe la respuesta (resultado de la traducción) del modelo Claude 3.5 Sonnet y la guarda como un archivo de texto en la ruta `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`: Contiene la variable de cadena source_lang y la lista 'target_langs', llama a la función `changed_files()` en `compare_hash.py` para devolver la lista de variables changed_files. Si hay archivos modificados, ejecuta un bucle doble para todos los archivos en la lista changed_files y todos los elementos en la lista target_langs, y dentro de ese bucle, llama a la función `translate(filepath, source_lang, target_lang)` en `prompt.py` para realizar la tarea de traducción.

El contenido de los archivos de script completados también se puede ver en el repositorio de GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

#### compare_hash.py

```python
import os
import hashlib
import csv

def compute_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load_existing_hashes(csv_path):
    existing_hashes = {}
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 2:
                    existing_hashes[row[0]] = row[1]
    return existing_hashes

def update_hash_csv(csv_path, file_hashes):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, hash_value in file_hashes.items():
            writer.writerow([file_path, hash_value])

def changed_files():
    posts_dir = '../_posts/ko/'
    hash_csv_path = './hash.csv'
    
    existing_hashes = load_existing_hashes(hash_csv_path)
    current_hashes = {}
    changed_files = []

    for root, _, files in os.walk(posts_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=posts_dir)
            
            current_hash = compute_file_hash(file_path)
            current_hashes[relative_path] = current_hash
            
            if relative_path in existing_hashes:
                if current_hash != existing_hashes[relative_path]:
                    changed_files.append(relative_path)
            else:
                changed_files.append(relative_path)

    update_hash_csv(hash_csv_path, current_hashes)

    if __name__ == "__main__":
        if changed_files:
            print("Changed files:")
            for file in changed_files:
                print(f"- {file}")
        else:
            print("No files have changed.")

    return changed_files
```

#### prompt.py
Debido a que incluye el contenido del prompt que escribimos anteriormente y el contenido del archivo es bastante largo, lo reemplazamos con el enlace al archivo fuente en el repositorio de GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> En el archivo `prompt.py` del enlace anterior, `max_tokens` es una variable que especifica la longitud máxima de salida independientemente del tamaño de la ventana de contexto. Al usar la API de Claude, el tamaño de la ventana de contexto que se puede ingresar de una vez es de 200k tokens (aproximadamente 680,000 caracteres), pero independientemente de eso, cada modelo tiene un número máximo de tokens de salida soportados, por lo que se recomienda verificar previamente en la [documentación oficial de Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) antes de utilizar la API. Los modelos de la serie Claude 3 existentes podían producir hasta un máximo de 4096 tokens, y aunque no hubo problemas con la mayoría de las publicaciones de este blog en los experimentos, en el caso de algunas publicaciones con un volumen bastante largo de más de 8000 caracteres en coreano, surgió el problema de que la parte posterior de la traducción se cortaba al exceder los 4096 tokens en algunos idiomas de salida. En el caso de Claude 3.5 Sonnet, el número máximo de tokens de salida se duplicó a 8192, por lo que generalmente no hubo problemas que excedieran este número máximo de tokens de salida, y en el `prompt.py` del repositorio de GitHub mencionado anteriormente, también se especificó `max_tokens=8192`.
{: .prompt-tip }

#### translate_changes.py

```python
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

posts_dir = '../_posts/ko/'
source_lang = "Korean"
target_langs = ["English", "Spanish", "Brazilian Portuguese", "Japanese", "French", "German"]

if __name__ == "__main__":
    changed_files = compare_hash.changed_files()
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")

    for file in changed_files:
        print(f"- {file}")
    print("")
    print("*** Translation start! ***")

    for changed_file in changed_files:
        print(f"- Translating {changed_file}")
        filepath = os.path.join(posts_dir, changed_file)
        for target_lang in tqdm(target_langs):
            prompt.translate(filepath, source_lang, target_lang)
```

### Cómo usar el script de Python
Basado en el blog Jekyll, dentro del directorio `/_posts`{: .filepath} donde se encuentran las publicaciones, se crean subdirectorios por código de idioma [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) como `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Luego, coloca los scripts de Python y el archivo CSV introducidos anteriormente en el directorio `/tools`{: .filepath}, abre una terminal en esa ubicación y ejecuta el siguiente comando:

```bash
python3 translate_changes.py
```

Entonces, el script se ejecutará y se mostrará una pantalla como la siguiente:  
![Captura de pantalla de la ejecución del script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Captura de pantalla de la ejecución del script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Experiencia de uso real
Como se mencionó anteriormente, he estado usando la traducción automática de publicaciones utilizando la API de Claude 3.5 en este blog durante aproximadamente 2 meses. En la mayoría de los casos, se pueden obtener traducciones de excelente calidad sin necesidad de intervención humana adicional, y después de publicar las publicaciones traducidas a varios idiomas, he confirmado que realmente se genera tráfico de búsqueda orgánica a través de búsquedas desde regiones fuera de Corea, como Brasil, Canadá, Estados Unidos y Francia. Además de aumentar el tráfico del blog, también hubo ventajas adicionales en términos de aprendizaje para el autor del texto, ya que Claude produce textos bastante fluidos en inglés, lo que me brinda la oportunidad de verificar cómo se expresan naturalmente en inglés ciertos términos o expresiones de mi texto original en coreano durante el proceso de revisión antes de hacer push de las publicaciones al repositorio de GitHub Pages. Aunque esto por sí solo no es suficiente para un aprendizaje completo del inglés, el hecho de poder encontrar frecuentemente expresiones naturales en inglés no solo para expresiones cotidianas sino también para expresiones académicas y términos, utilizando como ejemplo el texto que yo mismo escribí, que es más familiar que cualquier otro texto, sin ningún esfuerzo adicional, parece ser una ventaja considerable para un estudiante de pregrado de ingeniería en un país no angloparlante como Corea.
