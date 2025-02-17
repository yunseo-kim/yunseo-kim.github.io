---
title: Construindo um ambiente de desenvolvimento de Deep Learning com NVIDIA Container Toolkit e Docker/Podman (2) - Configuração do runtime de contêiner para utilização de GPU, escrita de Dockerfile e construção de imagem de contêiner
description: Esta série aborda como configurar um ambiente de desenvolvimento de Deep Learning baseado em contêiner usando o NVIDIA Container Toolkit localmente, e como configurar SSH e Jupyter Lab para utilizá-lo como um servidor remoto. Este post é o segundo da série e cobre o processo de escrever um Dockerfile e construir uma imagem de contêiner.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Visão Geral
Nesta série, abordaremos o processo de instalação do NVIDIA Container Toolkit e Docker ou Podman, e a construção de um ambiente de desenvolvimento de Deep Learning escrevendo um Dockerfile baseado nas imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub. Para aqueles que precisam, compartilhamos o [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) e a [imagem](https://hub.docker.com/r/yunseokim/dl-env/tags) concluídos através deste processo no GitHub e Docker Hub para uso livre, e fornecemos adicionalmente um guia de configuração de SSH e Jupyter Lab para uso como servidor remoto.  
A série consistirá em 3 posts, e este que você está lendo é o segundo post da série.
- [Parte 1: Instalação do NVIDIA Container Toolkit & Engine de Contêiner](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Parte 2: Configuração do Runtime de Contêiner para Utilização de GPU, Escrita de Dockerfile e Construção de Imagem de Contêiner (Este post)
- Parte 3 (A ser publicada)

Assumimos um ambiente Linux x86_64 com uma placa gráfica NVIDIA que suporta CUDA, e embora não tenhamos testado diretamente em distribuições além do Ubuntu ou Fedora, alguns detalhes específicos podem variar ligeiramente.  
(Atualizado em 18.02.2025)

> **Aviso de Correção de Erro**  
> Na versão inicial deste post, publicada em agosto de 2024, havia alguns erros na seção de [Escrita do Dockerfile](#5-escrita-do-dockerfile) e na imagem construída a partir desse Dockerfile. Os problemas eram os seguintes:
> - A parte de criação da conta remota onde a senha era definida estava incorreta, e não era possível fazer login com a senha "000000" como deveria ser originalmente
> - O daemon SSH não era iniciado automaticamente ao iniciar o contêiner
>
> Recentemente percebi esses problemas e, por volta das 2h da manhã (UTC+9) de 16 de fevereiro de 2025, substituí o Dockerfile e as imagens Docker problemáticas por arquivos corrigidos no [repositório GitHub](https://github.com/yunseo-kim/dl-env-docker) e no [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags).  
> Se você fez o Pull do Dockerfile ou da imagem Docker antes dessa data e hora, por favor, substitua pela versão corrigida.  
> Peço desculpas a quem possa ter enfrentado confusão devido ao conteúdo incorreto entre aqueles que consultaram este post anteriormente.
{: .prompt-info }

## Antes de Começar
Este post é uma continuação da [Parte 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), então se você ainda não leu, recomendo que leia o post anterior primeiro.

## 4. Configuração do Runtime de Contêiner
### Se estiver usando Podman
[Configure usando CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

Execute o seguinte comando para gerar o arquivo de especificação CDI no diretório `/etc/cdi`{: .filepath}:
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> Se você trocar o dispositivo gráfico ou alterar a configuração do driver CUDA (incluindo atualização de versão), você precisará gerar novamente o arquivo de especificação CDI.
{: .prompt-warning }

> Usar o NVIDIA Container Runtime hook junto com CDI pode causar conflitos, então se `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} existir, exclua esse arquivo ou tenha cuidado para não executar contêineres com a variável de ambiente `NVIDIA_VISIBLE_DEVICES` definida.
{: .prompt-warning }

### Se estiver usando Docker
Explicaremos com base no [modo rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configure o runtime de contêiner usando o comando `nvidia-ctk`
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
Este comando modifica o arquivo `/etc/docker/daemon.json`{: .filepath} para permitir que o Docker use o NVIDIA Container Runtime.

#### 4-Docker-2. Reinicie o daemon do Docker
Reinicie o daemon do Docker para aplicar as configurações alteradas.
```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configure o arquivo de configuração `/etc/nvidia-container-runtime/config.toml`{: .filepath} usando o comando `sudo nvidia-ctk`
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Verifique se foi configurado corretamente
Execute um contêiner CUDA de exemplo.

Se estiver usando Podman, execute o seguinte comando:
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Se estiver usando Docker, execute o seguinte comando:
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Se uma tela semelhante à seguinte for exibida, foi bem-sucedido.

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
Escreveremos um Dockerfile para usar como ambiente de desenvolvimento baseado nas imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub.

- Você deve decidir qual imagem usar considerando as versões necessárias de CUDA e cuDNN, o tipo e versão da distribuição Linux, etc. 
- ![Versão CUDA suportada pelo PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)No momento da escrita deste post, no final de agosto de 2024, a versão mais recente do PyTorch, 2.4.0, suporta CUDA 12.4. Portanto, usaremos aqui a imagem [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Você pode verificar a versão mais recente do PyTorch e a versão CUDA suportada na [página inicial do PyTorch](https://pytorch.org/get-started/locally/).

O código-fonte do Dockerfile completo está disponível publicamente no repositório GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Abaixo, explicamos o processo de escrita deste Dockerfile passo a passo.

### 5-1. Especificação da imagem base
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Instalação de utilitários básicos e pré-requisitos do Python
```Dockerfile
# Install basic utilities and Python-related packages, gosu, and SSH server
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    apt-utils \
    curl \
    gosu \
    openssh-server \
    python3 \
    python-is-python3 \
    python3-pip \
    ssh \
    tmux \
    && rm -rf /var/lib/apt/lists/* \
# verify that the binary works
    && gosu nobody true
```

### 5-3. Configuração do fuso horário do sistema (neste post, prosseguiremos com 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. Configuração do servidor SSH para acesso remoto  
Configure para que o login da conta root não seja possível ao acessar remotamente via SSH por motivos de segurança.
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Crie um usuário non-root chamado 'remote' para usar ao acessar via SSH.
```Dockerfile
# Create remote user (password can be passed to --build-arg at build time)
#
# This default password is very weak. Make sure to change it to your own unique
# password string!
#
# This Dockerfile assumes that the built image will only be used by yourself or
# a small group of trusted insiders, and if you need to distribute the image
# without exposing sensitive information, using --build-arg is dangerous.
# See the official Docker documentation.
ARG USER_NAME="remote"
ARG USER_PASSWORD="000000"
ARG HOME_DIR="/home/$USER_NAME"
RUN useradd --create-home --home-dir $HOME_DIR --shell /bin/bash $USER_NAME \
    && echo "$USER_NAME:$USER_PASSWORD" | chpasswd
```

> Ao construir uma imagem Docker usando este Dockerfile, se nenhuma opção for especificada separadamente, o valor inicial da senha da conta do usuário 'remote' é 000000. Isso é muito vulnerável em termos de segurança, então ao construir a imagem Docker, use a opção `--build-arg` para especificar uma senha de login de conta separadamente, ou altere a configuração imediatamente após executar o contêiner pela primeira vez. Para segurança, é desejável desativar o login por senha ao acessar via SSH e configurar posteriormente para que o login seja possível apenas através de um arquivo de chave separado, e seria ideal usar uma chave de hardware como Yubikey.
> A configuração do servidor SSH será abordada até certo ponto na próxima parte desta série, e se você quiser saber mais detalhes, pode consultar os documentos na seguinte lista:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> Além disso, este Dockerfile assume que a imagem construída será usada apenas por você ou um pequeno grupo de pessoas confiáveis, e se você precisar distribuir a imagem construída externamente, a configuração de senha através de `--build-arg` é perigosa e você deve usar outro método. Consulte [este documento](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/).
{: .prompt-danger }

### 5-5. Instalação do setuptools, pip e registro da variável de ambiente PATH
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. Instalação de pacotes de machine learning e deep learning para usar no ambiente de desenvolvimento
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
Se você quiser usar Cupy, cuDF, cuML e DALI, adicione o seguinte conteúdo ao Dockerfile:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Criação de diretório para usar como espaço de trabalho
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. Abertura de portas e configuração do `ENTRYPOINT` para executar ao iniciar o contêiner
Abra as portas 22 e 8888 para acesso SSH e Jupyter Lab.  
Além disso, para executar automaticamente o daemon SSH ao iniciar o contêiner, são necessários privilégios de root, então usaremos o seguinte método:
1. Estado de login como conta root ao iniciar o contêiner
2. Execução do script `/entrypoint.sh`{: .filepath} imediatamente após o início do contêiner
3. Iniciar o serviço SSH no script e então mudar para a conta remote usando [`gosu`](https://github.com/tianon/gosu)
4. Se nenhum comando for especificado separadamente ao executar o contêiner, execute o Jupyter Lab como conta remote (privilégios non-root) por padrão

> Geralmente, o uso de `sudo` ou `su` dentro de contêineres Docker ou Podman não é recomendado, e se privilégios de root forem necessários, é melhor iniciar o contêiner como conta root, realizar as tarefas que requerem privilégios de root e então mudar para um usuário non-root usando [`gosu`](https://github.com/tianon/gosu) como explicado aqui. As razões para fazer isso estão explicadas em detalhes nos materiais abaixo, que podem ser úteis para referência se necessário:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Primeiro, insira o seguinte conteúdo na última parte do Dockerfile:
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Em seguida, crie um arquivo de script chamado `entrypoint.sh`{: .filepath} no mesmo caminho que o Dockerfile escrito e escreva o conteúdo da seguinte forma:
```sh
#!/bin/bash
set -e

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

## 6. Construção da Imagem Docker e Execução do Contêiner
### 6-1. Construção da imagem
Abra um terminal no diretório onde o Dockerfile está localizado e execute o seguinte comando:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> No lugar de \<password\>, insira a senha de login que você usará ao acessar via SSH.
{: .prompt-info }

### 6-2. Execução de carga de trabalho de exemplo
Após concluir a construção, execute um contêiner descartável para verificar se está funcionando corretamente.

Para Podman, execute o seguinte comando:
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Para Docker, execute o seguinte comando:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Quando você inserir o comando acima no terminal, ele executará um contêiner chamado `test-container` a partir da imagem `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` construída anteriormente e conectará a porta 22 do sistema host à porta 22 do contêiner, e a porta 88 do sistema host à porta 8888 do contêiner. Se a imagem Docker foi construída corretamente na etapa anterior e o contêiner foi iniciado sem problemas, o JupyterLab deve estar em execução dentro do contêiner `test-container` no endereço padrão `http:127.0.0.1:8888`. Portanto, ao abrir um navegador no sistema host onde o Docker Engine está em execução e acessar <http://127.0.0.1:88>, ele deve se conectar ao endereço `http://127.0.0.1:8888` dentro do contêiner e exibir uma tela semelhante à seguinte:

![Captura de tela da interface do JupyterLab](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Abra um terminal no sistema host e execute o comando `ssh remote@127.0.0.1` para fazer login remoto na conta remote do sistema Ubuntu em execução dentro do contêiner.  
Ao fazer login pela primeira vez, você receberá um aviso de que não há informações sobre a chave de criptografia do destino de conexão e que a autenticação não é possível, e perguntará se deseja continuar a conexão. Digite "yes" para continuar.  
Em seguida, insira a senha para fazer login (se você não a alterou durante a construção da imagem, será o valor padrão "000000").
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {fingerprint (cada chave tem um valor único diferente)}.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '127.0.0.1' (ED25519) to the list of known hosts.
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
Se a saída for aproximadamente semelhante à acima, você fez login remoto com sucesso via SSH. Para encerrar a conexão, basta digitar o comando `exit`.

### 6-3. (opcional) Push para o Docker Hub
Para poder utilizar a imagem do ambiente de desenvolvimento que criamos através do processo anterior sempre que necessário, é bom fazer o Push da imagem construída para o Docker Hub.  

> Para fazer o Push de sua própria imagem para o Docker Hub, você precisa de sua própria conta Docker, então se ainda não tiver uma, primeiro complete o registro em <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Login no Docker Hub
##### Para Podman
```bash
podman login docker.io
```

##### Para Docker
```bash
docker login
```

#### 6-3-2. Especificação da tag da imagem
Você pode preencher as partes `<dockerhub_username>`, `<repository_name>`, (opcional)`:TAG` com o conteúdo que se aplica a você.  
ex. "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### Para Podman
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Para Docker
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Push da imagem
Por fim, execute o comando abaixo para fazer o Push da imagem para o Docker Hub.

##### Para Podman
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Para Docker
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Você pode confirmar que o Push foi bem-sucedido em <https://hub.docker.com/> como mostrado abaixo.  
![Captura de tela do Docker Hub](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

A imagem concluída através do processo anterior foi disponibilizada publicamente no repositório público [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) no Docker Hub, e qualquer pessoa pode usá-la livremente.

Para fazer o Pull da imagem, basta executar o mesmo comando usado para o Push, substituindo apenas a parte `push` por `pull`.
