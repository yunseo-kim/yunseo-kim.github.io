---
title: Cómo traducir automáticamente posts con la API de Claude 3.5 Sonnet (2) - Escribir y aplicar un script de automatización
description: Este post cubre el proceso de diseñar un prompt para la traducción multilingüe de archivos de texto markdown, y automatizar la tarea con Python utilizando una clave API obtenida de Anthropic y el prompt creado. Es el segundo artículo de la serie, que introduce cómo obtener y conectar la API, y cómo escribir el script de Python.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Introducción
Recientemente implementé la API de Claude 3.5 Sonnet de Anthropic para la traducción multilingüe de las entradas de mi blog. En esta serie, explicaré por qué elegí la API de Claude 3.5 Sonnet, cómo diseñar el prompt, y cómo implementar la automatización mediante la conexión de la API y un script de Python.  
La serie consta de dos artículos, y este es el segundo:
- Parte 1: [Introducción al modelo Claude 3.5 Sonnet, razones para seleccionarlo y prompt engineering](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Parte 2: Escribir y aplicar un script de automatización en Python utilizando la API (este artículo)

## Antes de empezar
Este artículo es una continuación de la [Parte 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1), así que si aún no la has leído, te recomiendo que empieces por ahí.

## Conexión con la API de Claude
### Obtener una clave API de Claude

> Esta sección explica cómo obtener una nueva clave API de Claude. Si ya tienes una clave API para usar, puedes omitir este paso.
{: .prompt-tip }

Accede a <https://console.anthropic.com> e inicia sesión. Si aún no tienes una cuenta, primero deberás registrarte. Una vez que hayas iniciado sesión, verás una pantalla de panel de control como la siguiente:
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Al hacer clic en el botón 'Get API keys' en esa pantalla, verás una pantalla como esta:
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Como yo ya tengo una clave creada, se muestra una clave llamada `yunseo-secret-key`, pero si acabas de crear tu cuenta y aún no has obtenido una clave API, probablemente no tengas ninguna clave. Puedes obtener una nueva clave haciendo clic en el botón 'Create Key' en la parte superior derecha.

> Cuando hayas completado la obtención de la clave, tu clave API se mostrará en la pantalla. Como no podrás volver a ver esta clave más adelante, asegúrate de guardarla en un lugar seguro.
{: .prompt-warning }

### (Recomendado) Registrar la clave API de Claude en una variable de entorno
Para utilizar la API de Claude en scripts de Python o Shell, necesitas cargar la clave API. Aunque podrías registrar la clave API directamente en el script, esto no es posible si necesitas subir el script a GitHub o compartirlo con otros de alguna otra manera. Además, incluso si no planeas compartir el archivo del script, existe el riesgo de que la clave API se filtre junto con el archivo del script en caso de una fuga accidental no intencionada. Por lo tanto, se recomienda registrar la clave API en una variable de entorno del sistema que solo tú uses, y luego cargar esa variable de entorno en el script. A continuación, se explica cómo registrar la clave API en una variable de entorno del sistema, basado en sistemas UNIX. Para Windows, consulta otros recursos en la web.

1. En la terminal, ejecuta `nano ~/.bashrc` o `nano ~/.zshrc` según el tipo de shell que uses para abrir el editor.
2. Añade `export ANTHROPIC_API_KEY='your-api-key-here'` al contenido del archivo. Reemplaza 'your-api-key-here' con tu propia clave API, y asegúrate de envolverla con comillas simples.
3. Guarda los cambios y sal del editor.
4. Ejecuta `source ~/.bashrc` o `source ~/.zshrc` en la terminal para aplicar los cambios.

### Instalar los paquetes de Python necesarios
Si el paquete anthropic no está instalado en tu entorno Python, instálalo con el siguiente comando:
```bash
pip3 install anthropic
```
Además, los siguientes paquetes son necesarios para usar el script de traducción de posts que se introducirá más adelante, así que instálalos o actualízalos con el siguiente comando:
```bash
pip3 install -U argparse tqdm
```

### Escribir el script de Python
El script de traducción de posts que se introducirá en este artículo consta de tres archivos de script Python y un archivo CSV:

- `compare_hash.py`: Calcula los valores hash SHA256 de los posts originales en coreano en el directorio `_posts/ko`{: .filepath}, los compara con los valores hash existentes registrados en el archivo `hash.csv`, y devuelve una lista de nombres de archivos que han sido modificados o añadidos recientemente.
- `hash.csv`: Un archivo CSV que registra los valores hash SHA256 de los archivos de posts existentes.
- `prompt.py`: Recibe los valores filepath, source_lang, target_lang, carga el valor de la clave API de Claude desde la variable de entorno del sistema, luego llama a la API y envía el prompt que escribimos anteriormente como prompt del sistema, y el contenido del post a traducir en 'filepath' como prompt del usuario. Luego recibe la respuesta (resultado de la traducción) del modelo Claude 3.5 Sonnet y la guarda como un archivo de texto en la ruta `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}.
- `translate_changes.py`: Contiene una variable de cadena source_lang y una lista 'target_langs', llama a la función `changed_files()` en `compare_hash.py` para obtener la lista de variables changed_files. Si hay archivos modificados, ejecuta un bucle doble para todos los archivos en la lista changed_files y todos los elementos en la lista target_langs, y dentro de ese bucle, llama a la función `translate(filepath, source_lang, target_lang)` en `prompt.py` para realizar la tarea de traducción.

El contenido de los archivos de script completados también se puede ver en el repositorio de GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
    # Ordena los hashes de archivos por nombre de archivo (las claves del diccionario)
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
            if not file.endswith('.md'):  # Procesa solo archivos .md
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
        print("Archivos modificados:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("No se han modificado archivos.")

    os.chdir(initial_wd)
```

#### prompt.py
Debido a que incluye el contenido del prompt que escribimos anteriormente y el contenido del archivo es bastante largo, lo reemplazo con un enlace al archivo fuente en el repositorio de GitHub.
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> En el archivo `prompt.py` del enlace anterior, `max_tokens` es una variable que especifica la longitud máxima de salida, independientemente del tamaño de la ventana de contexto. Aunque el tamaño de la ventana de contexto que se puede ingresar de una vez al usar la API de Claude es de 200k tokens (aproximadamente 680,000 caracteres), independientemente de eso, cada modelo tiene un número máximo de tokens de salida soportado, por lo que se recomienda verificarlo de antemano en la [documentación oficial de Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) antes de usar la API. Los modelos anteriores de la serie Claude 3 podían generar hasta un máximo de 4096 tokens, y aunque esto no fue un problema para la mayoría de los posts en este blog según mis experimentos, en algunos posts más largos de alrededor de 8000 caracteres en coreano, surgió el problema de que la parte final de la traducción se cortaba en algunos idiomas de salida al exceder los 4096 tokens. En el caso de Claude 3.5 Sonnet, el número máximo de tokens de salida se duplicó a 8192, por lo que rara vez hubo problemas que excedieran este límite máximo de tokens de salida, y en el archivo `prompt.py` del repositorio de GitHub mencionado arriba, también se ha especificado `max_tokens=8192`.
{: .prompt-tip }

#### translate_changes.py

```python
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

def is_valid_file(filename):
    # Patrones de archivos a excluir
    excluded_patterns = [
        '.DS_Store',  # Archivo de sistema macOS
        '~',          # Archivo temporal
        '.tmp',       # Archivo temporal
        '.temp',      # Archivo temporal
        '.bak',       # Archivo de respaldo
        '.swp',       # Archivo temporal de vim
        '.swo'        # Archivo temporal de vim
    ]
    
    # Devuelve False si el nombre del archivo incluye alguno de los patrones de exclusión
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin","Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    # Filtrar archivos temporales
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No se han modificado archivos.")
    print("Archivos modificados:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** ¡Comienza la traducción! ***")
    # Bucle externo: progreso de los archivos modificados
    for changed_file in tqdm(changed_files, desc="Archivos", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # Bucle interno: progreso de la traducción por idioma para cada archivo
        for target_lang in tqdm(target_langs, desc="Idiomas", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\n¡Traducción completada!")
    os.chdir(initial_wd)
```

### Cómo usar el script de Python
Basándose en un blog Jekyll, dentro del directorio `/_posts`{: .filepath} donde se encuentran los posts, crea subdirectorios para cada código de idioma [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) como `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Luego, coloca los scripts de Python y el archivo CSV mencionados anteriormente en el directorio `/tools`{: .filepath}, abre una terminal en esa ubicación y ejecuta el siguiente comando:

```bash
python3 translate_changes.py
```

Entonces, el script se ejecutará y verás una pantalla como esta:
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Experiencia de uso real
Como se mencionó anteriormente, he estado usando la traducción automática de posts utilizando la API de Claude 3.5 en este blog durante aproximadamente 2 meses. En la mayoría de los casos, se pueden obtener traducciones de excelente calidad sin necesidad de intervención humana adicional, y después de publicar los posts traducidos en varios idiomas, he confirmado que realmente se genera tráfico de búsqueda orgánica desde regiones fuera de Corea, como Brasil, Canadá, Estados Unidos y Francia. Además de aumentar el tráfico del blog, también hubo ventajas adicionales en términos de aprendizaje para el autor del post. Como Claude produce textos muy fluidos en inglés, durante el proceso de revisión antes de hacer push de los posts al repositorio de GitHub Pages, tengo la oportunidad de verificar cómo se expresan naturalmente en inglés ciertos términos o expresiones específicas de mi texto original en coreano. Aunque esto por sí solo no es suficiente para un aprendizaje completo del inglés, para un estudiante universitario de ingeniería en un país no angloparlante como Corea, parece ser bastante ventajoso poder acceder con frecuencia a expresiones naturales en inglés, no solo cotidianas sino también académicas y terminológicas, utilizando como ejemplo mi propio texto, que es el más familiar para mí, sin ningún esfuerzo adicional.
