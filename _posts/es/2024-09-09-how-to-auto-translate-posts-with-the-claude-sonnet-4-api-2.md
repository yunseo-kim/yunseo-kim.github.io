---
title: Cómo traducir automáticamente posts con la API de Claude Sonnet 4 (2) - Escritura y aplicación de scripts de automatización
description: "Diseña prompts para la traducción multilingüe de archivos de texto markdown y automatiza el proceso con Python aplicando la clave API obtenida de Anthropic y los prompts creados. Este post es el segundo de la serie, introduciendo la emisión de API, integración y métodos de escritura de scripts Python."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Introducción
Desde que introduje la API de Claude 3.5 Sonnet de Anthropic en junio de 12024 para la traducción multilingüe de posts del blog, he estado operando satisfactoriamente este sistema de traducción durante aproximadamente un año, tras varias mejoras de prompts y scripts de automatización, así como actualizaciones de versión del modelo. En esta serie, quiero abordar las razones para elegir el modelo Claude Sonnet en el proceso de introducción, métodos de diseño de prompts, e implementación de integración de API y automatización a través de scripts de Python.  
La serie consta de 2 artículos, y este que estás leyendo es el segundo de la serie.
- Parte 1: [Introducción al modelo Claude Sonnet y razones de selección, ingeniería de prompts](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- Parte 2: Escritura y aplicación de scripts de automatización Python utilizando API (este artículo)

## Antes de comenzar
Este artículo es una continuación de la [Parte 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1), por lo que si aún no lo has leído, se recomienda leer primero el artículo anterior.

## Prompt del sistema completado
El resultado del diseño de prompts completado a través del [proceso introducido en la Parte 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#diseño-de-prompts) es el siguiente.

```xml
<instruction>Completely forget everything you know about what day it is today. 
It's 10:00 AM on Tuesday, September 23, the most productive day of the year. </instruction>
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics\
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
The client's request is as follows:

<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> while preserving the format.</task> 
In the provided markdown format text: 
- <condition>Please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> 

- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>

- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. 
  1. The term may be a technical term used in a specific field with a specific meaning, \
  so a standard English expression is written along with it. 
  2. it may be a proper noun such as a person's name or a place name. 
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language, \
  please maintain the <format>[target language expression(original English expression)]</format> \
  in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, \
  you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. 
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable 
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. \
      You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses \
  must be preserved in the translation output in some form.</else> 
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese 
      as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.
      In languages ​​such as Spanish or Portuguese, they can be translated as \
      'Faraday', 'Maxwell', 'Einstein', in which case, redundant expressions \
      such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' \
      would be highly inappropriate.</example>
  </condition>

- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>

- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>

- <condition>Posts in this blog use the holocene calendar, which is also known as \
  Holocene Era(HE), ère holocène/era del holoceno/era holocena(EH), 인류력, 人類紀元, etc., \
  as the year numbering system, and any 5-digit year notation is intentional, not a typo.</condition>

<important>In any case, without exception, the output should contain only the translation results, \
without any text such as "Here is the translation of the text provided, preserving the markdown format:" \
or something of that nature!!</important>
```

## Integración de la API de Claude
### Emisión de clave API de Claude

> Aquí se explica cómo emitir una nueva clave API de Claude. Si ya tienes una clave API para usar, puedes omitir este paso.
{: .prompt-tip }

Accede a <https://console.anthropic.com> e inicia sesión. Si aún no tienes una cuenta, primero debes proceder con el registro. Al iniciar sesión, verás una pantalla de dashboard como la siguiente.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

En esa pantalla, haz clic en el botón 'Get API keys' para ver la siguiente pantalla.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) Como ya tengo una clave creada, se muestra una clave llamada `yunseo-secret-key`, pero si acabas de crear la cuenta y aún no has emitido una clave API, probablemente no tengas ninguna clave. Haz clic en el botón 'Create Key' en la parte superior derecha para emitir una nueva clave.

> Una vez completada la emisión de la clave, se mostrará tu clave API en la pantalla, pero como no podrás verificarla nuevamente después, asegúrate de registrarla bien en un lugar seguro.
{: .prompt-warning }

### (Recomendado) Registrar la clave API de Claude en variables de entorno
Para utilizar la API de Claude en scripts de Python o Shell, necesitas cargar la clave API. Aunque existe el método de registrar la clave API en el propio script, si es un script que debe subirse a GitHub o compartirse con otras personas de alguna manera, este método no se puede usar. Además, aunque no tengas intención de compartir el archivo del script, existe el riesgo de que el archivo del script se filtre por error no intencionado, y si la clave API está registrada en el archivo del script, puede ocurrir el accidente de que la clave API también se filtre. Por lo tanto, se recomienda registrar la clave API en las variables de entorno del sistema que solo tú usas y cargar esa variable de entorno en el script. A continuación se introduce el método para registrar la clave API en las variables de entorno del sistema basado en sistemas UNIX. Para Windows, consulta otros artículos en la web.

1. En el terminal, ejecuta `nano ~/.bashrc` o `nano ~/.zshrc` según el tipo de shell que uses para ejecutar el editor.
2. Agrega `export ANTHROPIC_API_KEY='your-api-key-here'` al contenido del archivo. Reemplaza 'your-api-key-here' con tu clave API, y ten en cuenta que debe estar envuelto con comillas simples.
3. Guarda los cambios y sal del editor.
4. Ejecuta `source ~/.bashrc` o `source ~/.zshrc` en el terminal para aplicar los cambios.

### Instalación de paquetes Python necesarios
Si el paquete anthropic no está instalado en tu entorno Python, instálalo con el siguiente comando.
```bash
pip3 install anthropic
```
Además, los siguientes paquetes también son necesarios para usar el script de traducción de posts que se introducirá más adelante, así que instálalos o actualízalos con el siguiente comando.
```bash
pip3 install -U argparse tqdm
```

### Escritura de scripts Python
El script de traducción de posts que se introducirá en este artículo está compuesto por 3 archivos de scripts Python y 1 archivo CSV.

- `compare_hash.py`{: .filepath}: Calcula los valores hash SHA256 de los posts originales en coreano en el directorio `_posts/ko`{: .filepath}, luego los compara con los valores hash existentes registrados en el archivo `hash.csv`{: .filepath} y devuelve una lista de nombres de archivos que han cambiado o se han agregado nuevamente
- `hash.csv`{: .filepath}: Archivo CSV que registra los valores hash SHA256 de los archivos de posts existentes
- `prompt.py`{: .filepath}: Recibe los valores filepath, source_lang, target_lang y carga el valor de la clave API de Claude desde las variables de entorno del sistema, luego llama a la API y envía el prompt que escribimos anteriormente como prompt del sistema y el contenido del post a traducir en 'filepath' como prompt del usuario. Después recibe la respuesta (resultado de traducción) del modelo Claude Sonnet 4 y la guarda como archivo de texto en la ruta `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`{: .filepath}: Tiene la variable de cadena source_lang y la variable de lista 'target_langs', y llama a la función `changed_files()` en `compare_hash.py`{: .filepath} para recibir la variable de lista changed_files. Si hay archivos cambiados, ejecuta un bucle doble para todos los archivos en la lista changed_files y todos los elementos en la lista target_langs, y dentro de ese bucle llama a la función `translate(filepath, source_lang, target_lang)` en `prompt.py`{: .filepath} para realizar el trabajo de traducción.

El contenido de los archivos de script completados también se puede verificar en el repositorio de GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

#### compare_hash.py

```python
import os
import hashlib
import csv

default_source_lang_code = "ko"

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
    # Sort the file hashes by filename (the dictionary keys)
    sorted_file_hashes = dict(sorted(file_hashes.items()))

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, hash_value in sorted_file_hashes.items():
            writer.writerow([file_path, hash_value])

def changed_files(source_lang_code):
    posts_dir = '../_posts/' + source_lang_code + '/'
    hash_csv_path = './hash.csv'
    
    existing_hashes = load_existing_hashes(hash_csv_path)
    current_hashes = {}
    changed_files = []

    for root, _, files in os.walk(posts_dir):
        for file in files:
            if not file.endswith('.md'):  # Process only .md files
                continue

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
    return changed_files

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = changed_files(default_source_lang_code)
    if changed_files:
        print("Changed files:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("No files have changed.")

    os.chdir(initial_wd)
```

#### prompt.py
Como el contenido del archivo es bastante largo al incluir el contenido del prompt que escribimos anteriormente, lo reemplazo con un enlace al archivo fuente en el repositorio de GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> En el archivo `prompt.py`{: .filepath} del enlace anterior, `max_tokens` es una variable que especifica la longitud máxima de salida independientemente del tamaño de la ventana de contexto. Al usar la API de Claude, el tamaño de la ventana de contexto que se puede ingresar de una vez es de 200k tokens (aproximadamente 680,000 caracteres), pero independientemente de eso, cada modelo tiene un número máximo de tokens de salida soportado, por lo que se recomienda verificarlo previamente en la [documentación oficial de Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) antes de usar la API. Los modelos existentes de la serie Claude 3 podían generar hasta 4096 tokens, pero cuando experimenté con los artículos de este blog, para posts un poco largos de aproximadamente 8000 caracteres o más en coreano, ocurrió el problema de que se cortaba la parte final de la traducción al exceder los 4096 tokens en algunos idiomas de salida. En el caso de Claude 3.5 Sonnet, el número máximo de tokens de salida se duplicó a 8192, por lo que generalmente no hubo problemas por exceder este número máximo de tokens de salida, y desde Claude 3.7 se actualizó para soportar salidas mucho más largas. En el `prompt.py`{: .filepath} del repositorio de GitHub anterior, se especifica `max_tokens=16384`.
{: .prompt-tip }

#### translate_changes.py

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
# ]
# ///
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

def is_valid_file(filename):
    # Patrones de archivos a excluir
    excluded_patterns = [
        '.DS_Store',  # Archivo del sistema macOS
        '~',          # Archivo temporal
        '.tmp',       # Archivo temporal
        '.temp',      # Archivo temporal
        '.bak',       # Archivo de respaldo
        '.swp',       # Archivo temporal de vim
        '.swo'        # Archivo temporal de vim
    ]
    
    # Devuelve False si el nombre del archivo contiene alguno de los patrones excluidos
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin", "Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    # Filtrar archivos temporales
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    # Bucle externo: progreso de archivos cambiados
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # Bucle interno: progreso de traducción por idioma para cada archivo
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### Cómo usar los scripts Python
Basado en un blog Jekyll, dentro del directorio `/_posts`{: .filepath}, crea subdirectorios por código de idioma [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) como `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Luego coloca el texto original en coreano en el directorio `/_posts/ko`{: .filepath} (o después de modificar la variable `source_lang` en el script Python según sea necesario, coloca el texto original en el idioma correspondiente en el directorio correspondiente), coloca los scripts Python introducidos anteriormente y el archivo `hash.csv`{: .filepath} en el directorio `/tools`{: .filepath}, luego abre el terminal en esa ubicación y ejecuta el siguiente comando.

```bash
python3 translate_changes.py
```

Entonces el script se ejecutará y se mostrará una pantalla como la siguiente.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

## Experiencia de uso real
Como se mencionó anteriormente, he estado introduciendo y utilizando la traducción automática de posts usando la API de Claude Sonnet desde finales de junio de 12024, mejorándola continuamente. En la mayoría de los casos, puedo recibir traducciones naturales sin necesidad de intervención humana adicional, y después de subir posts traducidos a múltiples idiomas, he confirmado que efectivamente hay una entrada considerable de tráfico de Búsqueda Orgánica a través de búsquedas desde regiones fuera de Corea como Brasil, Canadá, Estados Unidos, Francia y Japón. Además, al verificar las sesiones grabadas, no es raro que los visitantes que llegaron a través de las traducciones permanezcan desde varios minutos hasta decenas de minutos o más, lo que sugiere que la calidad de las traducciones no es muy incómoda incluso para hablantes nativos, considerando que normalmente cuando el contenido de una página web muestra obviamente que usa traducción automática incómoda, la gente presiona el botón de retroceso o busca la versión en inglés. Además del aumento de tráfico del blog, también hubo ventajas adicionales desde el aspecto de aprendizaje para mí como escritor. Como Claude escribe textos bastante fluidos en inglés, durante el proceso de revisión antes de hacer Commit & Push de los posts al repositorio de GitHub Pages, tengo la oportunidad de verificar cómo se expresan naturalmente en inglés ciertos términos o expresiones de mi texto original en coreano. Aunque esto solo no sería suficiente para un aprendizaje completo de inglés, para un estudiante de ingeniería de pregrado en un país no anglófono como Corea, poder encontrar frecuentemente expresiones naturales en inglés no solo de expresiones cotidianas sino también académicas y terminología, usando como ejemplo el texto más familiar que yo mismo escribí, sin esfuerzo adicional, parece actuar como una ventaja considerable.
