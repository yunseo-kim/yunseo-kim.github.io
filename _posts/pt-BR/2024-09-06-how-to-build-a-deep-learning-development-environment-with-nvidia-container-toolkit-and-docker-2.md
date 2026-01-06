---
title: "Como configurar um ambiente de desenvolvimento de deep learning com NVIDIA Container Toolkit e Docker/Podman (2) - Configuração do runtime de contêiner para uso de GPU, escrita do Dockerfile e build da imagem"
description: "Esta série mostra como montar localmente um ambiente de deep learning baseado em contêiner usando o NVIDIA Container Toolkit e, para uso remoto, configurar SSH e JupyterLab. Este post (parte 2) cobre a escrita do Dockerfile e o processo de build da imagem."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Visão geral

Nesta série, abordo o processo de instalar o NVIDIA Container Toolkit e o Docker ou Podman, e de construir um ambiente de desenvolvimento de deep learning escrevendo um Dockerfile baseado nas imagens CUDA e cuDNN disponibilizadas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub. Para que quem precisar possa usar livremente, compartilho via GitHub e Docker Hub o [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) e a [imagem](https://hub.docker.com/r/yunseokim/dl-env/tags) finalizados após esse processo; além disso, forneço um guia adicional de configuração de SSH e JupyterLab para utilizá-lo como servidor remoto.  
A série terá 3 posts, e este que você está lendo é o segundo.
- [Parte 1: Instalação do NVIDIA Container Toolkit & do engine de contêiner](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Parte 2: Configuração do runtime de contêiner para uso de GPU, escrita do Dockerfile e build da imagem (este post)
- Parte 3 (a ser publicado)

O procedimento parte do pressuposto de um ambiente Linux x86_64 em um sistema equipado com uma placa NVIDIA que suporte CUDA; como não testei diretamente em distribuições além de Ubuntu ou Fedora, alguns detalhes podem variar.  
(Revisado em 12026.1.6.)

> **Aviso de correção de erros**
>
> No rascunho inicial deste post, publicado em agosto de 12024, havia alguns erros na descrição da seção [Escrita do Dockerfile](#5-escrita-do-dockerfile) e em parte das imagens buildadas a partir daquele Dockerfile. Os problemas eram:
> - Na criação da conta `remote`, a parte de definir a senha estava incorreta; eu afirmei que seria possível fazer login inserindo `"000000"` como senha inicial, mas na prática não era assim (Adicionado em 12025.12.19: agora a senha inicial não é `"000000"`, então confira obrigatoriamente o [conteúdo abaixo](#5-4-configuração-do-servidor-ssh-para-acesso-remoto))
> - Ao iniciar o contêiner, o daemon SSH não era iniciado automaticamente
>
> Eu percebi esses problemas em fevereiro de 12025 e, em 16 de fevereiro de 12025 por volta das 2h (horário da Coreia, UTC+9), substituí no [repositório do GitHub](https://github.com/yunseo-kim/dl-env-docker) e no [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) os Dockerfiles e imagens problemáticos por versões corrigidas.  
> Se você fez pull do Dockerfile ou da imagem antes desse momento, substitua pela versão corrigida.  
> Peço desculpas a quem tenha se confundido por conta das informações incorretas.
{: .prompt-info }

## Antes de começar

Como este post dá continuidade à [Parte 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), recomendo ler primeiro o post anterior, caso você ainda não o tenha lido.

## 4. Configuração do runtime de contêiner

### Caso você use Podman

[Configure usando CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> Em versões antigas, ao instalar o NVIDIA Container Toolkit pela primeira vez — e depois, sempre que a configuração do dispositivo GPU ou do driver fosse alterada (incluindo upgrade de versão) — era necessário recriar manualmente o arquivo de especificação CDI toda vez.
>
> Porém, a partir do NVIDIA Container Toolkit `v1.18.0`, via o serviço systemd `nvidia-cdi-refresh`, o arquivo de especificação CDI `/var/run/cdi/nvidia.yaml` é criado e atualizado automaticamente nos casos abaixo:
> - Ao instalar ou atualizar o NVIDIA Container Toolkit
> - Ao instalar ou atualizar o driver da GPU NVIDIA
> - Ao reiniciar o sistema
>
> Portanto, diferente do passado, agora não é necessário fazer nada separadamente. Atualizei o texto do post para refletir isso.
>
> Observação: em caso de remoção do driver da GPU ou reconfiguração de dispositivos MIG, o `nvidia-cdi-refresh` não consegue lidar sozinho; então, é preciso reiniciar manualmente o `nvidia-cdi-refresh.service` para induzir a regeneração da especificação CDI.
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> Se você usar o NVIDIA Container Runtime hook junto com CDI, pode haver conflito; portanto, se existir `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath}, apague esse arquivo ou tome cuidado para não executar contêineres com a variável de ambiente `NVIDIA_VISIBLE_DEVICES` definida.
{: .prompt-warning }

### Caso você use Docker

Explico com base no [modo rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configurar o runtime de contêiner com o comando `nvidia-ctk`

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

O comando acima modifica o arquivo `/etc/docker/daemon.json`{: .filepath} para que o Docker possa usar o NVIDIA Container Runtime.

#### 4-Docker-2. Reiniciar o daemon do Docker

Reinicie o daemon do Docker para aplicar as alterações.

```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configurar o arquivo `/etc/nvidia-container-runtime/config.toml`{: .filepath} com `sudo nvidia-ctk`

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Verificar se está configurado corretamente

Execute um contêiner CUDA de exemplo.

No caso de Podman, execute:

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

No caso de Docker, execute:

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

Se aparecer uma tela semelhante à abaixo, deu certo.

```bash
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 555.58.02              Driver Version: 555.58.02      CUDA Version: 12.5     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3090        Off |   00000000:01:00.0  On |                  N/A |
|  0%   46C    P8             29W /  350W |     460MiB /  24576MiB |      2%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

## 5. Escrita do Dockerfile

Escreva um Dockerfile para usar como ambiente de desenvolvimento, baseado nas imagens CUDA e cuDNN fornecidas no [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) do Docker Hub.

- É preciso decidir qual imagem usar considerando a versão necessária de CUDA e cuDNN, e o tipo/versão da distribuição Linux.
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  Considerando o final de agosto de 12024, quando este post foi escrito, a versão mais recente do PyTorch (2.4.0) oferece suporte a CUDA 12.4. Portanto, aqui utilizo a imagem [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Você pode verificar a versão mais recente do PyTorch e as versões de CUDA suportadas no [site do PyTorch](https://pytorch.org/get-started/locally/).

O código-fonte do Dockerfile final foi disponibilizado publicamente no repositório GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Abaixo descrevo passo a passo o processo de escrita desse Dockerfile.

> (+ Revisado em 12026.1.6.)  
> Adicionei ao mesmo repositório no GitHub e ao repositório público no Docker Hub [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) os Dockerfiles e imagens que suportam PyTorch 2.9.1 e CUDA 12.8 / 13.0. O conteúdo do post também foi atualizado de acordo com PyTorch 2.9.1 e CUDA 13.0.
>
> Além disso, incluí na imagem scikit-image e XGBoost, bem como as bibliotecas do ecossistema RAPIDS cuGraph, cuxfilter, cuCIM, RAFT e cuVS, e adicionei suporte a `arm64` além da arquitetura `amd64` existente.
{: .prompt-info }

### 5-1. Definir a imagem base

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. Configurar o fuso horário do sistema (neste post, usando 'Asia/Seoul')

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> Usei principalmente o conteúdo [deste post](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22) como referência.
{: .prompt-tip }

### 5-3. Instalar utilitários básicos do sistema

```Dockerfile
# Install basic utilities, gosu, and SSH server
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update -y && apt-get install -y --no-install-recommends \
        apt-utils \
        curl \
        gosu \
        openssh-server \
        ssh \
        tmux \
        tzdata \
# verify that the binary works
    && gosu nobody true
```

### 5-4. Configuração do servidor SSH para acesso remoto

Por segurança, configure o SSH para impedir login remoto via conta root.

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Crie um usuário não-root chamado `remote` para usar no acesso via SSH.

```Dockerfile
# Create remote user
#
# The password must be pre-specified at build time with the `DL_ENV_PASSWD`
# environment variable.
ARG USER_NAME="remote"
ARG USER_UID=1001
ARG USER_GID=$USER_UID
ARG HOME_DIR="/home/$USER_NAME"
RUN --mount=type=secret,id=USER_PASSWORD \
    groupadd --gid $USER_GID $USER_NAME && \
    useradd --uid $USER_UID --gid $USER_GID --create-home \
        --home-dir $HOME_DIR --shell /bin/bash $USER_NAME \
    && awk -v user="$USER_NAME" '{print user ":" $0}' /run/secrets/USER_PASSWORD | chpasswd
```

> Como o conteúdo de argumentos de build (`ARG`) e variáveis de ambiente (`ENV`) fica exposto na imagem resultante, ao definir informações sensíveis como senhas e chaves de API [é preciso usar outro método](https://docs.docker.com/build/building/secrets/). Aqui utilizei [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts).
{: .prompt-danger }

> Como será descrito [mais adiante](#6-1-build-da-imagem), ao buildar a imagem com este Dockerfile você deve definir, via variável de ambiente `DL_ENV_PASSWD`, a string que será usada como senha da conta. No caso da [imagem distribuída no Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags), o valor inicial da senha da conta é `satisfied-flip-remake`; se você usar essa senha padrão pública como está, ficará extremamente vulnerável — então, após executar o contêiner pela primeira vez, altere imediatamente a configuração. Além disso, por segurança, é recomendável desabilitar login por senha no SSH e configurar para que o login seja possível apenas via arquivo de chave; se você também usar uma chave de hardware como Yubikey, melhor ainda.
>
> Sobre a configuração do servidor SSH, pretendo cobrir parte disso no próximo post desta série; se quiser mais detalhes, consulte os documentos abaixo:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Instalar o uv e registrar variáveis de ambiente

> **Adoção do `uv` e adequação ao padrão Externally Managed Environments conforme [PEP 668](https://peps.python.org/pep-0668/) (Revisado em 12026.1.6.)**
>
> No passado, este post escrevia o Dockerfile de modo que a instalação de pacotes via `pip` fosse feita diretamente dentro da imagem do contêiner, sem criar um ambiente virtual (`venv`) separado. O motivo era que, em uma imagem de contêiner com propósito único, o risco de “quebrar” o software do sistema é menor e, mesmo que algo desse errado, bastaria criar um novo contêiner a partir da imagem; portanto, julguei que a necessidade de criar um ambiente virtual era baixa. Esse ponto é parcialmente reconhecido no próprio [PEP 668](https://peps.python.org/pep-0668/#use-cases) conforme abaixo.
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> Porém, mesmo em imagens de contêiner de propósito único, consolidou-se como padrão que instalações via gerenciadores de pacotes Python como `pip` devem ser feitas apenas dentro de um ambiente virtual, distinguindo estritamente os pacotes gerenciados externamente (externally managed) via gerenciadores do sistema operacional. Assim, revisei o conteúdo para criar um ambiente virtual e instalar os pacotes necessários dentro dele, cumprindo o [PEP 668](https://peps.python.org/pep-0668/) e a especificação de [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) e seguindo o padrão do ecossistema Python.
>
> A biblioteca padrão oficialmente suportada para criação e gestão de ambientes virtuais em Python é o `venv`, como apresentei brevemente em [outro post que escrevi no início de 12021](https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended). No entanto, após o lançamento em 12024 do gerenciador de pacotes e projetos Python de alto desempenho, [`uv`](https://docs.astral.sh/uv/), desenvolvido em Rust pela [Astral](https://astral.sh/), ele rapidamente se consolidou como um novo padrão de facto no ecossistema Python, graças a vantagens relevantes como:
> - [Resolução de dependências e velocidade de instalação esmagadoramente superiores ao `pip` (10–100x)](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)
> - Excelente usabilidade
> - [Ótima compatibilidade com `pip` e `venv` existentes](https://docs.astral.sh/uv/pip/)
>
> Em especial, pacotes de ML como PyTorch e RAPIDS, que abordamos aqui, têm muitas dependências e costumam ser grandes, então as vantagens do `uv` se destacam ainda mais. Além disso, como o [`uv` utiliza cache de forma ativa e eficiente](https://docs.astral.sh/uv/concepts/cache/), ao usar corretamente cache mounts durante o build da imagem — como neste caso — [é possível maximizar esses benefícios e reduzir bastante o tempo de build](https://docs.astral.sh/uv/guides/integration/docker/#caching). Por isso, também adotarei o `uv` para criação/gestão do ambiente virtual e instalação de pacotes. Trabalhei principalmente com base na documentação oficial ["Using uv in Docker"](https://docs.astral.sh/uv/guides/integration/docker/).
{: .prompt-info }

```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_UID:$USER_GID
WORKDIR $HOME_DIR

# Install uv by copying the binary from the official distroless image
COPY --from=ghcr.io/astral-sh/uv:0.9.21 /uv /uvx /bin/
ENV PATH="$HOME_DIR/.local/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ARG UV_CACHE_DIR="/tmp/uv-cache"
```

> **Por que definir `UV_CACHE_DIR` como `"/tmp/uv-cache"` em vez do padrão `"$HOME_DIR/.cache/uv"`**
>
> Normalmente, quando se adiciona um usuário com `useradd --create-home`, o usuário deve ter propriedade do próprio diretório home — e aqui é o caso.
> Porém, ao buildar imagens com Podman, descobri um bug em que, mesmo que a propriedade tenha sido corretamente transferida em camadas anteriores, ao montar caches etc. em camadas posteriores os metadados de propriedade do diretório pai são resetados para o valor padrão (propriedade do root). Ao pesquisar, encontrei [um issue reportado por outro usuário sobre o mesmo comportamento há cerca de 3 semanas](https://github.com/containers/podman/issues/27777), mas até o momento não houve resposta. Informações detalhadas do que eu vivenciei foram adicionadas [como comentário nesse issue](https://github.com/containers/podman/issues/27777#issuecomment-3712237296).
>
> Para evitar problemas mesmo que a propriedade seja resetada para root, durante o build defini `UV_CACHE_DIR` como `"/tmp/uv-cache"`, um caminho separado de `$HOME_DIR`. De qualquer forma, esse cache não é incluído na imagem final resultante do build, então alterar o caminho é ok.
{: .prompt-tip }

### 5-6. Instalar Python, criar ambiente virtual, instalar setuptools & pip

```Dockerfile
# Install the latest, managed Python executables
ARG UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv python install 3.13 --default

# Create a virtual environment
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv venv --python 3.13 --seed
# Use the virtual environment automatically
ENV VIRTUAL_ENV=$HOME_DIR/.venv
# Place entry points in the environment at the front of the path & .profile
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN echo "source $VIRTUAL_ENV/bin/activate" >> $HOME_DIR/.profile
# Allow pip to only run in a virtual environment; exit with an error otherwise
ENV PIP_REQUIRE_VENV=true

# Install setuptools
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install setuptools
```

### 5-7. Instalar pacotes de ML/DL para uso no ambiente de desenvolvimento

#### 5-7-1. Pacotes comuns

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch & bibliotecas de aceleração por GPU específicas de CUDA

##### Se você for instalar apenas PyTorch

Para instalar apenas PyTorch, adicione o seguinte ao Dockerfile.

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch & Cupy & RAPIDS & DALI

Se você quiser usar não apenas PyTorch, mas também Cupy e RAPIDS (cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS), além de DALI, adicione o seguinte ao Dockerfile.

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        --index-url https://download.pytorch.org/whl/cu130 \
        --extra-index-url=https://pypi.org/simple \
        --extra-index-url=https://pypi.nvidia.com \
        "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        cupy-cuda13x \
        "cudf-cu13==25.12.*" "dask-cudf-cu13==25.12.*" "cuml-cu13==25.12.*" \
        "cugraph-cu13==25.12.*" "nx-cugraph-cu13==25.12.*" "cuxfilter-cu13==25.12.*" \
        "cucim-cu13==25.12.*" "pylibraft-cu13==25.12.*" "raft-dask-cu13==25.12.*" \
        "cuvs-cu13==25.12.*" nvidia-dali-cuda130
```

> Nesse caso, os pacotes do PyTorch e do RAPIDS compartilham algumas bibliotecas de dependência (cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE). Se forem instalados separadamente, as versões exigidas por cada um podem divergir; assim, a versão instalada primeiro pode ser sobrescrita depois, aumentando bastante o risco de conflito de dependências. Portanto, ao instalar esses pacotes, integre tudo em um único comando `uv pip install` para que o resolvedor considere todas as restrições ao mesmo tempo e priorize a versão exigida pelo PyTorch.
{: .prompt-tip }

### 5-8. Criar um diretório para usar como workspace

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. Abrir portas e configurar o `ENTRYPOINT` a ser executado ao iniciar o contêiner

Para acesso via SSH e Jupyter Lab, abra as portas 22 e 8888.  
Além disso, para iniciar automaticamente o daemon SSH ao iniciar o contêiner é necessário privilégio de root, então usaremos o seguinte método:
1. Ao iniciar o contêiner, estar logado como root
2. Logo após iniciar, executar o script `/entrypoint.sh`{: .filepath}
3. No script, iniciar o serviço SSH e então trocar para a conta `remote` usando [`gosu`](https://github.com/tianon/gosu)
4. Se nenhum comando extra for especificado ao executar o contêiner, como padrão executar Jupyter Lab na conta `remote` (permissões non-root)

> Em geral, não é recomendado usar `sudo` ou `su` dentro de contêineres Docker/Podman; se for necessário privilégio de root, como descrito aqui, é melhor iniciar o contêiner como root, realizar as tarefas que exigem root e então trocar para um usuário non-root usando [`gosu`](https://github.com/tianon/gosu). As razões estão explicadas em detalhes nos materiais abaixo (consulte se necessário):
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Primeiro, na parte final do Dockerfile, adicione o seguinte.

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Depois, no mesmo caminho do Dockerfile que você escreveu, crie um arquivo de script chamado `entrypoint.sh`{: .filepath} com o conteúdo abaixo.

```sh
#!/bin/bash
set -e

# Dump environment variables
printenv | grep _ >> /etc/environment

# Run SSH daemon in the background
service ssh start

# Move to the workspace directory and run Jupyter Lab
cd "$WORK_DIR"
if [ $# -gt 0 ];then
    #su ${USER_NAME} -c "exec $@"
    exec gosu ${USER_NAME} $@
else
    #su ${USER_NAME} -c "exec jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="${WORK_DIR}""
    exec gosu ${USER_NAME} jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="${WORK_DIR}"
fi
```

> Em geral, processos executados via `docker exec` ou `CMD` herdam normalmente o `ENV` do Docker; porém, sessões conectadas via SSH muitas vezes não herdam automaticamente as variáveis de ambiente do Docker. Isso acontece porque o SSH cria uma nova sessão de shell no login.
>
> Para resolver isso e permitir que, mesmo ao conectar via SSH, você consiga acessar variáveis já definidas como `$WORK_DIR`, é necessário “despejar” as variáveis previamente em `/etc/environment`{: .filepath } antes de iniciar o serviço ssh, por exemplo com algo como `printenv | grep _ >> /etc/environment`.
>
> Os links abaixo podem ajudar:
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. Build da imagem OCI e execução do contêiner

### 6-1. Build da imagem

Abra um terminal no diretório onde o Dockerfile está localizado e defina a variável de ambiente `DL_ENV_PASSWD`.

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> Em \<your_own_password\>, basta inserir a senha de login que será usada ao se conectar via SSH.
{: .prompt-info }

Agora, **não feche esta janela do terminal** e, nela mesma, execute o comando abaixo para fazer o build.

#### No caso de Podman

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> Em Podman, se você quiser buildar a imagem não apenas para a plataforma (sistema operacional/arquitetura) do seu dispositivo, mas para todas as plataformas suportadas pela imagem base, pensando em distribuição, use a opção [`--all-platforms`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms) e, em vez de `--tag` ou `-t`, use a opção [`--manifest`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant).
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> Para Docker, não organizei isso separadamente aqui; se precisar, consulte a [documentação oficial do Docker](https://docs.docker.com/build/building/multi-platform/).
{: .prompt-tip }

#### No caso de Docker

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. Executar uma workload de exemplo

Ao concluir o build, execute um contêiner descartável para verificar se tudo funciona.

No caso de Podman:

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

No caso de Docker:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Ao digitar o comando acima no terminal, você executa um contêiner chamado `test-container` a partir da imagem `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04` que você buildou e conecta a porta 2222 do host à porta 22 do contêiner, e a porta 8888 do host à porta 8888 do contêiner. Se a imagem tiver sido buildada corretamente e o contêiner tiver iniciado sem problemas, dentro do contêiner o JupyterLab estará rodando no endereço padrão `http:127.0.0.1:8888`. Portanto, ao abrir um navegador no host onde o Podman/Docker está rodando e acessar <http://127.0.0.1:8888>, você deve ser conectado ao `http://127.0.0.1:8888` dentro do contêiner e ver uma tela como a seguinte.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

No host, abra um terminal e execute `ssh remote@127.0.0.1 -p 2222` para tentar fazer login remoto como o usuário `remote` do sistema Ubuntu rodando dentro do contêiner.  
No primeiro login, como não há informação sobre a chave do host de destino, será exibido um aviso dizendo que não é possível autenticar, e perguntará se você quer continuar; basta digitar `"yes"` para prosseguir.  
Depois, para fazer login, insira a senha que você definiu no build (ou, se você tiver feito pull da [imagem distribuída no Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) e estiver logando pela primeira vez, a senha inicial `satisfied-flip-remake`).

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {fingerprint (cada chave tem seu próprio valor único)}.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[127.0.0.1]:2222' (ED25519) to the list of known hosts.
remote@127.0.0.1's password: 
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 6.12.11-200.fc41.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

```

Se a saída for aproximadamente como acima, o login remoto via SSH foi bem-sucedido. Para encerrar a sessão, basta executar `exit`.

### 6-3. (opcional) Fazer push no Docker Hub

Para poder dar pull e reutilizar a imagem do ambiente de desenvolvimento sempre que precisar, é uma boa ideia fazer push da imagem que você buildou no Docker Hub.  

> Para fazer push de uma imagem no Docker Hub, você precisa de uma conta Docker; se ainda não tiver, cadastre-se primeiro em <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Login no Docker Hub

##### No caso de Podman

```bash
podman login docker.io
```

##### No caso de Docker

```bash
docker login
```

#### 6-3-2. Definir a tag da imagem

Em `<dockerhub_username>`, `<repository_name>` e (opcional) `:TAG`, preencha com o que for correspondente a você.  
Ex.: `"yunseokim"`, `"dl-env"`, `"rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04"`

> Se você tiver buildado a imagem não apenas para a plataforma (sistema operacional/arquitetura) do seu dispositivo, mas para todas as plataformas suportadas pela imagem base, e quiser fazer push em massa da lista de manifest (ou índice de imagem), então pule esta etapa e vá direto para [Push da imagem](#6-3-3-push-da-imagem), seguindo o método descrito lá.
{: .prompt-tip }

##### No caso de Podman

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### No caso de Docker

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Push da imagem

Por fim, execute o comando abaixo para fazer push da imagem no Docker Hub.

##### No caso de Podman

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> No Podman, para fazer push de uma vez de várias imagens correspondentes a múltiplas plataformas, agrupadas como uma lista de manifest ou índice de imagem, use o comando [`podman manifest push`](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls) como abaixo.
>
> ```bash
> podman manifest push --all REPOSITORY:MANIFEST_TAG \
> docker.io/<dockerhub_username>/<repository_name>[:TAG]
> ```
>
> Ex.:
>
> ```bash
> podman manifest push --all dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> docker.io/yunseokim/dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04
> ```
>
{: .prompt-tip }

##### No caso de Docker

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

Em <https://hub.docker.com/> você poderá verificar que foi feito push corretamente, como abaixo.

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

A imagem final criada seguindo o processo acima foi publicada no repositório público do Docker Hub [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags), e qualquer pessoa pode usá-la livremente.

Para dar pull da imagem, basta executar o mesmo comando usado no push trocando apenas `push` por `pull`.
