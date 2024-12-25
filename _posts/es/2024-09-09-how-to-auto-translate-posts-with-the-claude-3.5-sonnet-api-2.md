---
title: Cómo traducir automáticamente publicaciones con la API de Claude 3.5 Sonnet
  (2) - Escribir y aplicar un script de automatización
description: Diseñamos un prompt para la traducción multilingüe de archivos de texto
  en markdown, y cubrimos el proceso de automatización del trabajo en Python aplicando
  la clave API obtenida de Anthropic y el prompt escrito. Este post es el segundo
  de la serie y presenta cómo obtener y conectar la API, así como cómo escribir el
  script de Python.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Introducción
Recientemente implementé la API de Claude 3.5 Sonnet de Anthropic para la traducción multilingüe de posts del blog. En esta serie, cubriremos las razones para elegir la API de Claude 3.5 Sonnet, cómo diseñar prompts, y cómo implementar la automatización mediante la conexión API y scripts Python.  
La serie consta de 2 posts, y este que estás leyendo es el segundo de la serie.
- Parte 1: [Introducción al modelo Claude 3.5 Sonnet, razones de selección y prompt engineering](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Parte 2: Escribiendo y aplicando scripts de automatización Python usando la API (este post)

## Antes de empezar
Este post es una continuación de la [Parte 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1), así que se recomienda leer el post anterior primero si aún no lo has hecho.

## Conectando con la API de Claude
### Obteniendo una clave API de Claude

> Esta sección explica cómo obtener una nueva clave API de Claude. Si ya tienes una clave API para usar, puedes saltarte este paso.
{: .prompt-tip }

Accede a <https://console.anthropic.com> e inicia sesión. Si aún no tienes una cuenta, primero deberás registrarte. Después de iniciar sesión, verás una pantalla de dashboard como la siguiente.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Al hacer clic en el botón 'Get API keys' en esta pantalla, verás una pantalla como la siguiente.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Como ya tengo una clave creada, se muestra una clave llamada `yunseo-secret-key`, pero si acabas de crear una cuenta y aún no has obtenido una clave API, probablemente no tengas ninguna clave. Puedes obtener una nueva clave haciendo clic en el botón 'Create Key' en la parte superior derecha.

> Cuando completes la generación de la clave, tu clave API se mostrará en la pantalla, pero no podrás volver a verla después, así que asegúrate de guardarla en un lugar seguro.
{: .prompt-warning }

### (Recomendado) Registrar la clave API de Claude en variables de entorno
Para utilizar la API de Claude en scripts Python o Shell, necesitas cargar la clave API. Aunque podrías registrar la clave API en el script mismo, esto no es posible si necesitas compartir el script con otros a través de GitHub u otros medios. Además, incluso si no planeas compartir el archivo del script, existe el riesgo de que la clave API se filtre junto con el archivo del script si este se filtra por error no intencionado. Por lo tanto, se recomienda registrar la clave API en las variables de entorno del sistema que solo tú uses y cargar esa variable de entorno en el script. A continuación, se introduce cómo registrar la clave API en las variables de entorno del sistema basado en UNIX. Para Windows, consulta otros recursos en la web.

1. En la terminal, ejecuta `nano ~/.bashrc` o `nano ~/.zshrc` según el shell que uses para iniciar el editor.
2. Agrega `export ANTHROPIC_API_KEY='your-api-key-here'` al contenido del archivo. Reemplaza 'your-api-key-here' con tu clave API, y ten en cuenta que debe estar envuelta en comillas simples.
3. Guarda los cambios y sal del editor.
4. Ejecuta `source ~/.bashrc` o `source ~/.zshrc` en la terminal para aplicar los cambios.

### Instalando los paquetes Python necesarios
Si el paquete anthropic no está instalado en tu entorno Python, instálalo con el siguiente comando:
```bash
pip3 install anthropic
```
Además, los siguientes paquetes son necesarios para usar el script de traducción de posts que se introducirá más adelante, así que instálalos o actualízalos con el siguiente comando:
```bash
pip3 install -U argparse tqdm
```

### Escribiendo scripts Python
El script de traducción de posts que se introducirá en este post consiste en 3 archivos Python y 1 archivo CSV:

- `compare_hash.py`: Calcula los valores hash SHA256 de los posts originales en coreano en el directorio `_posts/ko`{: .filepath} y los compara con los valores hash existentes registrados en el archivo `hash.csv` para devolver una lista de nombres de archivos modificados o nuevos
- `hash.csv`: Archivo CSV que registra los valores hash SHA256 de los archivos de posts existentes
- `prompt.py`: Recibe los valores filepath, source_lang, target_lang y carga el valor de la clave API de Claude desde las variables de entorno del sistema, luego llama a la API y envía el prompt escrito anteriormente como prompt del sistema y el contenido del post a traducir en 'filepath' como prompt del usuario. Luego recibe la respuesta (resultado de la traducción) del modelo Claude 3.5 Sonnet y la guarda como archivo de texto en la ruta `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`: Tiene una variable string source_lang y una lista 'target_langs', llama a la función `changed_files()` en `compare_hash.py` para recibir la lista changed_files. Si hay archivos modificados, ejecuta un bucle doble para todos los archivos en la lista changed_files y todos los elementos en la lista target_langs, y dentro de ese bucle llama a la función `translate(filepath, source_lang, target_lang)` en `prompt.py` para realizar la traducción.

El contenido de los scripts completados también se puede encontrar en el repositorio de GitHub [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
    # Sort the file hashes by filename (the dictionary keys)
    sorted_file_hashes = dict(sorted(file_hashes.items()))

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, hash_value in sorted_file_hashes.items():
            writer.writerow([file_path, hash_value])

def changed_files():
    posts_dir = '../_posts/ko/'
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

    changed_files = changed_files()
    if changed_files:
        print("Changed files:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("No files have changed.")

    os.chdir(initial_wd)
```

#### prompt.py
Debido a que incluye el contenido del prompt escrito anteriormente y el archivo es bastante largo, se reemplaza con el enlace al archivo fuente en el repositorio de GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> En el archivo `prompt.py` del enlace anterior, `max_tokens` es una variable que especifica la longitud máxima de salida independientemente del tamaño de la ventana de contexto. Aunque el tamaño de la ventana de contexto que se puede ingresar de una vez al usar la API de Claude es de 200k tokens (aproximadamente 680,000 caracteres), cada modelo tiene un número máximo de tokens de salida soportado, así que se recomienda verificarlo en la [documentación oficial de Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) antes de usar la API. Los modelos anteriores de la serie Claude 3 podían generar hasta 4096 tokens, y aunque esto no fue un problema para la mayoría de los posts de este blog en las pruebas, algunos posts más largos de más de 8000 caracteres en coreano tuvieron problemas donde la parte final de la traducción se cortaba al exceder los 4096 tokens en algunos idiomas de salida. En el caso de Claude 3.5 Sonnet, el número máximo de tokens de salida se duplicó a 8192, por lo que rara vez hubo problemas por exceder este límite, y en el archivo `prompt.py` del repositorio de GitHub anterior también se estableció `max_tokens=8192`.
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
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

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
    
    os.chdir(initial_wd)
```

### Cómo usar los scripts Python
Para blogs Jekyll, dentro del directorio `/_posts`{: .filepath} donde se ubican los posts, crea subdirectorios por código de idioma [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) como `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Luego, coloca los scripts Python y el archivo CSV mencionados anteriormente en el directorio `/tools`{: .filepath}, abre una terminal en esa ubicación y ejecuta el siguiente comando:

```bash
python3 translate_changes.py
```

Entonces el script se ejecutará y verás una pantalla como la siguiente:  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Experiencia de uso real
Como se mencionó anteriormente, he estado usando la traducción automática de posts con la API de Claude 3.5 en este blog durante aproximadamente 2 meses. En la mayoría de los casos, se pueden obtener traducciones de excelente calidad sin necesidad de intervención humana adicional, y después de publicar los posts traducidos en varios idiomas, he confirmado que realmente hay tráfico orgánico de búsqueda proveniente de regiones fuera de Corea, como Brasil, Canadá, Estados Unidos y Francia. Además de aumentar el tráfico del blog, también hubo beneficios adicionales en términos de aprendizaje para el autor, ya que Claude produce textos muy fluidos en inglés, lo que me permite verificar cómo expresar naturalmente en inglés ciertos términos o expresiones de mi texto original en coreano durante el proceso de revisión antes de hacer Push al repositorio de GitHub Pages. Aunque esto solo no es suficiente para un aprendizaje completo del inglés, para un estudiante universitario de ingeniería en una región no angloparlante como Corea, parece ser bastante ventajoso poder encontrar frecuentemente expresiones naturales en inglés, tanto cotidianas como académicas, usando como ejemplo mi propio texto, que es más familiar que cualquier otro, sin necesidad de esfuerzo adicional.
