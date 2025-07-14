---
title: "Cómo traducir automáticamente posts con la API de Claude Sonnet 4 (2) - Escritura y aplicación de scripts de automatización"
description: "Diseña prompts para la traducción multilingüe de archivos de texto markdown y automatiza el proceso con Python aplicando claves API de Anthropic/Gemini y los prompts creados. Este post es el segundo de la serie, introduciendo la emisión e integración de API y métodos de escritura de scripts Python."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2/
---

## Introducción
Desde que introduje la API de Claude 3.5 Sonnet de Anthropic para la traducción multilingüe de posts del blog en junio de 12024, he estado operando satisfactoriamente este sistema de traducción durante aproximadamente un año, tras varias mejoras de prompts y scripts de automatización, así como actualizaciones de versión del modelo. En esta serie, quiero cubrir las razones para elegir el modelo Claude Sonnet y posteriormente añadir Gemini 2.5 Pro en el proceso de introducción, métodos de diseño de prompts, e implementación de integración API y automatización a través de scripts de Python.  
La serie consta de 2 artículos, y este que estás leyendo es el segundo artículo de la serie.
- Parte 1: [Introducción a los modelos Claude Sonnet/Gemini 2.5 y razones de selección, ingeniería de prompts](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- Parte 2: Escritura y aplicación de scripts de automatización Python utilizando API (texto principal)

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
or "```markdown" or something of that nature!!</important>
```

> Para la [función de traducción incremental añadida recientemente](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#120250704), se utiliza un prompt del sistema ligeramente diferente. Como hay muchas partes que se superponen, no las incluiré aquí, así que si es necesario, consulta directamente el contenido de [`prompt.py`{: .filepath }](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py) en el repositorio de GitHub.
{: .prompt-tip }

## Integración API
### Emisión de claves API

> Aquí se explica cómo emitir nuevas claves API de Anthropic o Gemini. Si ya tienes claves API para usar, puedes omitir este paso.
{: .prompt-tip }

#### Anthropic Claude
Accede a <https://console.anthropic.com> e inicia sesión con tu cuenta de Anthropic Console. Si aún no tienes una cuenta de Anthropic Console, primero debes registrarte. Una vez que inicies sesión, verás una pantalla de panel como la siguiente.  
![Panel de Anthropic Console](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

En esa pantalla, haz clic en el botón 'Get API keys' para ver la siguiente pantalla.  
![Claves API](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) Como ya tengo una clave creada, se muestra una clave llamada `yunseo-secret-key`, pero si acabas de crear la cuenta y aún no has emitido una clave API, probablemente no tengas ninguna clave. Haz clic en el botón 'Create Key' en la parte superior derecha para emitir una nueva clave.

> Una vez completada la emisión de la clave, se mostrará tu clave API en la pantalla, pero como no podrás verificar esa clave nuevamente después, asegúrate de anotarla bien en un lugar seguro.
{: .prompt-warning }

#### Google Gemini
La API de Gemini se puede gestionar en Google AI Studio. Accede a <https://aistudio.google.com/apikey> e inicia sesión con tu cuenta de Google para ver la siguiente pantalla de panel.  
![Panel de Google AI Studio](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/get-api-key-google-ai-studio.png)

En esa pantalla, haz clic en el botón 'Crear clave API' y sigue las instrucciones. Necesitarás crear y conectar un proyecto de Google Cloud y una cuenta de facturación para usarlo, lo que completará la preparación para usar la clave API. Aunque el procedimiento es un poco más complejo que la API de Anthropic, no debería haber grandes dificultades.

> A diferencia de Anthropic Console, puedes verificar tus claves API propias en el panel en cualquier momento. ~~Después de todo, si tu cuenta de Anthropic Console es comprometida, puedes limitar el daño protegiendo solo la clave API, pero si tu cuenta de Google es comprometida, probablemente tengas problemas más urgentes que la clave API de Gemini~~  
> Por lo tanto, no necesitas anotar la clave API por separado, pero asegúrate de mantener bien la seguridad de tu cuenta de Google.
{: .prompt-tip }

### (Recomendado) Registrar claves API en variables de entorno
Para utilizar la API de Claude en scripts de Python o Shell, necesitas cargar la clave API. Aunque existe el método de codificar directamente la clave API en el script, este método no se puede usar si el script debe subirse a GitHub o compartirse con otras personas de otras maneras. Además, incluso si no tenías intención de compartir el archivo del script, existe el riesgo de que el archivo del script pueda filtrarse por error accidental, y si la clave API está registrada en el archivo del script, existe el riesgo de que la clave API también se filtre. Por lo tanto, se recomienda registrar la clave API en las variables de entorno del sistema que solo tú usas y cargar esa variable de entorno en el script. A continuación se introduce cómo registrar la clave API en las variables de entorno del sistema basado en sistemas UNIX. Para Windows, consulta otros artículos en la web.

1. En el terminal, ejecuta `nano ~/.bashrc` o `nano ~/.zshrc` según el tipo de shell que uses para ejecutar el editor.
2. Si usas la API de Anthropic, añade `export ANTHROPIC_API_KEY=your-api-key-here` al contenido del archivo. Reemplaza la parte 'your-api-key-here' con tu clave API. Si usas la API de Gemini, añade `export GEMINI_API_KEY=your-api-key-here` de la misma manera.
3. Guarda los cambios y sal del editor.
4. Ejecuta `source ~/.bashrc` o `source ~/.zshrc` en el terminal para aplicar los cambios.

### Instalación de paquetes Python necesarios
Si las librerías API no están instaladas en tu entorno Python, instálalas con los siguientes comandos.

#### Anthropic Claude
```bash
pip3 install anthropic
```

#### Google Gemini
```bash
pip3 install google-genai
```

#### Común
Además, los siguientes paquetes también son necesarios para usar el script de traducción de posts que se introducirá más adelante, así que instálalos o actualízalos con el siguiente comando.
```bash
pip3 install -U argparse tqdm
```

### Escritura de scripts Python
El script de traducción de posts que se introducirá en este artículo consta de 3 archivos de script Python y 1 archivo CSV.

- `compare_hash.py`{: .filepath}: Calcula los valores hash SHA256 de los posts originales en coreano en el directorio `_posts/ko`{: .filepath}, los compara con los valores hash existentes registrados en el archivo `hash.csv`{: .filepath} y devuelve una lista de nombres de archivos que han cambiado o se han añadido nuevamente
- `hash.csv`{: .filepath}: Archivo CSV que registra los valores hash SHA256 de los archivos de posts existentes
- `prompt.py`{: .filepath}: Recibe valores de filepath, source_lang, target_lang, carga el valor de la clave API de Claude desde las variables de entorno del sistema, llama a la API y envía el prompt que escribimos anteriormente como prompt del sistema y el contenido del post a traducir en 'filepath' como prompt del usuario. Luego recibe la respuesta (resultado de traducción) del modelo Claude Sonnet 4 y la guarda como archivo de texto en la ruta `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`{: .filepath}: Tiene la variable de cadena source_lang y la variable de lista 'target_langs', llama a la función `changed_files()` en `compare_hash.py`{: .filepath} para recibir la variable de lista changed_files. Si hay archivos cambiados, ejecuta un bucle doble para todos los archivos en la lista changed_files y todos los elementos en la lista target_langs, y dentro de ese bucle llama a la función `translate(filepath, source_lang, target_lang)` en `prompt.py`{: .filepath} para realizar el trabajo de traducción.

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

> En el archivo `prompt.py`{: .filepath} del enlace anterior, `max_tokens` es una variable que especifica la longitud máxima de salida independientemente del tamaño de la ventana de contexto. Al usar la API de Claude, el tamaño de la ventana de contexto que se puede ingresar de una vez es de 200k tokens (aproximadamente 680,000 caracteres), pero independientemente de eso, cada modelo tiene un número máximo de tokens de salida soportado, por lo que se recomienda verificarlo con anticipación en la [documentación oficial de Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) antes de usar la API. Los modelos existentes de la serie Claude 3 podían generar hasta 4096 tokens, pero cuando experimenté con los artículos de este blog, para posts un poco largos de aproximadamente 8000 caracteres o más en coreano, algunos idiomas de salida excedían los 4096 tokens, causando que se cortara la parte final de la traducción. En el caso de Claude 3.5 Sonnet, el número máximo de tokens de salida se duplicó a 8192, por lo que rara vez había problemas por exceder este número máximo de tokens de salida, y desde Claude 3.7 se ha actualizado para soportar salidas mucho más largas. En el `prompt.py`{: .filepath} del repositorio de GitHub anterior, se ha establecido `max_tokens=16384`.
{: .prompt-tip }

> En el caso de Gemini, el número máximo de tokens de salida ha sido bastante generoso desde antes, y basado en Gemini 2.5 Pro, es posible generar hasta 65536 tokens, por lo que rara vez se excederá este número máximo de tokens de salida. Según la [documentación oficial de la API de Gemini](https://ai.google.dev/gemini-api/docs/models#token-size), en los modelos Gemini, 1 token equivale a 4 caracteres en inglés, y 100 tokens equivalen aproximadamente a 60-80 palabras en inglés.
{: .prompt-tip }

#### translate_changes.py

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
#     "argparse",
# ]
# ///
import sys
import os
import subprocess
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
    
    # Devuelve False si el nombre del archivo contiene alguno de los patrones de exclusión
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin", "Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

def get_git_diff(filepath):
    """Obtiene el diff del archivo usando git"""
    try:
        # Obtiene el diff del archivo
        result = subprocess.run(
            ['git', 'diff', '--unified=0', '--no-color', '--', filepath],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting git diff: {e}")
        return None

def translate_incremental(filepath, source_lang, target_lang, model):
    """Traduce solo las partes cambiadas de un archivo usando git diff"""
    # Obtiene el git diff
    diff_output = get_git_diff(filepath)
    # print(f"Diff output: {diff_output}")
    if not diff_output:
        print(f"No changes detected or error getting diff for {filepath}")
        return
    
    # Llama a la función de traducción con el diff
    prompt.translate_with_diff(filepath, source_lang, target_lang, diff_output, model)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Translate markdown files with optional incremental updates')
    parser.add_argument('--incremental', action='store_true', 
                       help='Only translate changed parts of files using git diff')
    args, _ = parser.parse_known_args()
    
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
    
    # Bucle externo: Progreso a través de archivos cambiados
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        
        # Bucle interno: Progreso a través de idiomas objetivo
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            model = "gemini-2.5-pro" if target_lang in ["English", "Taiwanese Mandarin", "German"] else "claude-sonnet-4-20250514"
            if args.incremental:
                translate_incremental(filepath, source_lang, target_lang, model)
            else:
                prompt.translate(filepath, source_lang, target_lang, model)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### Cómo usar los scripts Python
Basado en un blog Jekyll, dentro del directorio `/_posts`{: .filepath}, crea subdirectorios por código de idioma [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) como `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Luego coloca el texto original en coreano en el directorio `/_posts/ko`{: .filepath} (o después de modificar la variable `source_lang` en el script Python según sea necesario, coloca el texto original en el idioma correspondiente en el directorio correspondiente), coloca los scripts Python introducidos anteriormente y el archivo `hash.csv`{: .filepath} en el directorio `/tools`{: .filepath}, abre el terminal en esa ubicación y ejecuta el siguiente comando.

```bash
python3 translate_changes.py
```

Entonces el script se ejecutará y se mostrará una pantalla como la siguiente.  
![Captura de pantalla del script en ejecución 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Captura de pantalla del script en ejecución 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

Si no se especifica ninguna opción por separado, funciona en modo de traducción completa por defecto, y si se especifica la opción `--incremental`, se puede usar la función de traducción incremental.

```bash
python3 translate_changes.py --incremental
```

## Experiencia de uso real
Como se mencionó anteriormente, he estado utilizando la traducción automática de posts usando la API de Claude Sonnet desde finales de junio de 12024, mejorándola continuamente. En la mayoría de los casos, puedo recibir traducciones naturales sin necesidad de intervención humana adicional, y después de subir posts traducidos a múltiples idiomas, he confirmado que efectivamente hay una entrada considerable de tráfico de Búsqueda Orgánica a través de búsquedas desde regiones fuera de Corea como Brasil, Canadá, Estados Unidos, Francia y Japón. Además, al verificar las sesiones grabadas, no son pocos los visitantes que llegaron a través de traducciones y permanecen desde varios minutos hasta decenas de minutos o más, lo que sugiere que la calidad de las traducciones no es muy incómoda incluso para hablantes nativos, considerando que normalmente cuando el contenido de una página web muestra signos obvios de traducción automática incómoda, la gente presiona el botón de retroceso para salir o busca la versión en inglés en su lugar. Además, no solo hubo ventajas en términos de entrada de tráfico al blog, sino también beneficios adicionales en términos de aprendizaje para mí como escritor de los artículos. Como LLMs como Claude o Gemini escriben textos bastante fluidos basados en inglés, en el proceso de revisión antes de hacer Commit & Push de los posts al repositorio de GitHub Pages, tuve la oportunidad de verificar cómo expresar naturalmente en inglés ciertos términos o expresiones de mi texto original en coreano. Aunque esto por sí solo no sería suficiente para un aprendizaje completo de inglés, el poder encontrarse frecuentemente con expresiones naturales en inglés no solo de expresiones cotidianas sino también de expresiones y términos académicos, usando como ejemplo el texto más familiar para mí que escribí directamente, sin esfuerzo adicional, también parece actuar como una ventaja considerable para estudiantes universitarios de ingeniería en países de regiones no anglófonas como Corea.
