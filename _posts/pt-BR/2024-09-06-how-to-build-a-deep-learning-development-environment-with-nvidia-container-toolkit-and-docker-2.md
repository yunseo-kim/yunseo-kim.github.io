---
title: Construindo um ambiente de desenvolvimento de Deep Learning com NVIDIA Container Toolkit e Docker/Podman (2) - Configuração do runtime de contêiner para uso de GPU, escrita de Dockerfile e construção de imagem de contêiner
description: Esta série aborda como configurar um ambiente de desenvolvimento de deep learning baseado em contêineres com NVIDIA Container Toolkit localmente e configurar SSH e Jupyter Lab para utilizá-lo como servidor remoto. Este post é o segundo da série e cobre o processo de escrita de Dockerfile e construção de imagem de contêiner.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Visão Geral
Esta série aborda a instalação do NVIDIA Container Toolkit e Docker ou Podman, e a construção de um ambiente de desenvolvimento de deep learning escrevendo um Dockerfile baseado nas imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub. Para aqueles que precisam, compartilho o [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) e a [imagem](https://hub.docker.com/r/yunseokim/dl-env/tags) completos através do GitHub e Docker Hub para uso livre, além de fornecer um guia de configuração de SSH e Jupyter Lab para uso como servidor remoto.  
A série consistirá em 3 posts, e este é o segundo post da série.
- [Parte 1: Instalação do NVIDIA Container Toolkit e Engine de Contêiner](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Parte 2: Configuração do Runtime de Contêiner para Uso de GPU, Escrita de Dockerfile e Construção de Imagem de Contêiner (este post)
- Parte 3 (a ser publicada)

Assumimos um sistema Linux x86_64 com uma placa gráfica NVIDIA que suporta CUDA, e embora tenhamos testado principalmente no Ubuntu e Fedora, alguns detalhes podem variar em outras distribuições.  
(Atualizado em 18.02.12025)

> **Aviso de correção de erro**  
> Na versão inicial deste post, publicada em agosto do ano 12024 da [Era Holocena](https://en.wikipedia.org/wiki/Holocene_calendar), havia alguns erros na seção [Escrita do Dockerfile](#5-escrita-do-dockerfile) e na imagem construída a partir dele. Os problemas eram:
> - A parte de criação da conta 'remote' tinha um erro na configuração da senha, que deveria permitir login com a senha "000000", mas não funcionava
> - O daemon SSH não iniciava automaticamente ao iniciar o contêiner
>
> Esses problemas foram identificados recentemente e, por volta das 2h da manhã (UTC+9) de 16 de fevereiro de 12025, o Dockerfile problemático e as imagens Docker foram substituídos por versões corrigidas no [repositório GitHub](https://github.com/yunseo-kim/dl-env-docker) e no [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags).  
> Se você baixou o Dockerfile ou a imagem Docker antes dessa data, por favor, substitua-os pelas versões atualizadas.  
> Peço desculpas a quem possa ter enfrentado confusão devido a essas informações incorretas.
{: .prompt-info }

## Antes de começar
Este post é uma continuação da [Parte 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), então recomendo ler o post anterior primeiro, caso ainda não o tenha feito.

## 4. Configuração do Runtime de Contêiner
### Para usuários do Podman
[Configure usando CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

Execute o seguinte comando para gerar o arquivo de especificação CDI no diretório `/etc/cdi`{: .filepath}:
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> Você precisa regenerar o arquivo de especificação CDI se trocar a placa gráfica ou alterar a configuração do driver CUDA (incluindo atualizações de versão).
{: .prompt-warning }

> O uso do NVIDIA Container Runtime hook junto com CDI pode causar conflitos. Se o arquivo `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} existir, remova-o ou evite executar contêineres com a variável de ambiente `NVIDIA_VISIBLE_DEVICES` definida.
{: .prompt-warning }

### Para usuários do Docker
Explicaremos com base no [modo rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configure o runtime do contêiner com o comando `nvidia-ctk`
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
Este comando modifica o arquivo `/etc/docker/daemon.json`{: .filepath} para permitir que o Docker utilize o NVIDIA Container Runtime.

#### 4-Docker-2. Reinicie o daemon do Docker
Reinicie o daemon do Docker para aplicar as configurações alteradas:
```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configure o arquivo `/etc/nvidia-container-runtime/config.toml`{: .filepath} com o comando `sudo nvidia-ctk`
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Verificando se a configuração está correta
Execute um contêiner CUDA de exemplo para testar.

Para usuários do Podman:
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Para usuários do Docker:
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Se você ver uma saída semelhante à seguinte, a configuração foi bem-sucedida:

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
Vamos escrever um Dockerfile para nosso ambiente de desenvolvimento baseado nas imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub.

- Você deve escolher uma imagem considerando as versões necessárias de CUDA e cuDNN, bem como o tipo e versão da distribuição Linux.
- ![Versão CUDA suportada pelo PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)No momento da escrita deste post, final de agosto de 12024, a versão mais recente do PyTorch, 2.4.0, suporta CUDA 12.4. Portanto, usaremos a imagem [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Você pode verificar a versão mais recente do PyTorch e as versões CUDA suportadas no [site do PyTorch](https://pytorch.org/get-started/locally/).

O Dockerfile completo está disponível no repositório GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Abaixo, explicarei o processo de criação deste Dockerfile passo a passo.

### 5-1. Especificando a imagem base
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Instalando utilitários básicos e pré-requisitos do Python
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

### 5-3. Configurando o fuso horário do sistema (neste exemplo, 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. Configurando o servidor SSH para acesso remoto  
Por segurança, configuramos o SSH para impedir login como root:
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Criamos um usuário não-root chamado 'remote' para acesso SSH:
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

> Ao construir uma imagem Docker usando este Dockerfile sem especificar opções adicionais, a senha inicial para o usuário 'remote' será 000000. Isso é extremamente vulnerável em termos de segurança, então você deve especificar uma senha diferente usando a opção `--build-arg` ao construir a imagem Docker, ou alterar a senha imediatamente após executar o contêiner pela primeira vez. Para maior segurança, é recomendável desativar o login por senha para conexões SSH e permitir login apenas através de arquivos de chave separados, e idealmente usar uma chave de hardware como Yubikey.
> A configuração do servidor SSH será abordada na próxima parte desta série, e para informações mais detalhadas, consulte os seguintes documentos:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> Além disso, este Dockerfile assume que a imagem construída será usada apenas por você ou um pequeno grupo de pessoas confiáveis. Se você precisar distribuir a imagem externamente, usar `--build-arg` para configurar senhas é perigoso e você deve usar outros métodos. Consulte [este documento](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/) para mais informações.
{: .prompt-danger }

### 5-5. Instalando setuptools, pip e registrando a variável de ambiente PATH
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. Instalando pacotes de machine learning e deep learning
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
Se você quiser usar Cupy, cuDF, cuML e DALI, adicione o seguinte ao Dockerfile:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Criando um diretório para o espaço de trabalho
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. Expondo portas e configurando o `ENTRYPOINT` para execução no início do contêiner
Expomos as portas 22 e 8888 para SSH e Jupyter Lab.  
Para executar automaticamente o daemon SSH quando o contêiner inicia, precisamos de privilégios root, então usaremos a seguinte abordagem:
1. O contêiner inicia com o usuário root
2. Logo após o início, o script `/entrypoint.sh`{: .filepath} é executado
3. O script inicia o serviço SSH e depois muda para o usuário 'remote' usando [`gosu`](https://github.com/tianon/gosu)
4. Se nenhum comando específico for fornecido ao executar o contêiner, o Jupyter Lab será iniciado como usuário 'remote' (privilégios não-root) por padrão

> Geralmente, o uso de `sudo` ou `su` dentro de contêineres Docker ou Podman não é recomendado. Se você precisar de privilégios root, é melhor iniciar o contêiner como root, realizar as tarefas que precisam de privilégios root e depois mudar para um usuário não-root usando [`gosu`](https://github.com/tianon/gosu), como explicado aqui. Para entender melhor por que isso é recomendado, consulte os seguintes recursos:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Primeiro, adicione o seguinte ao final do seu Dockerfile:
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Em seguida, crie um arquivo de script chamado `entrypoint.sh`{: .filepath} no mesmo diretório do seu Dockerfile com o seguinte conteúdo:
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

## 6. Construindo a imagem Docker e executando o contêiner
### 6-1. Construindo a imagem
Abra um terminal no diretório onde está o Dockerfile e execute o seguinte comando:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> Substitua \<password\> pela senha de login que você deseja usar para acesso SSH.
{: .prompt-info }

### 6-2. Executando uma carga de trabalho de exemplo
Após a construção, execute um contêiner descartável para verificar se tudo está funcionando corretamente.

Para Podman:
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Para Docker:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Este comando executa um contêiner chamado `test-container` a partir da imagem `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` que construímos, mapeando a porta 22 do host para a porta 22 do contêiner e a porta 88 do host para a porta 8888 do contêiner. Se a imagem Docker foi construída corretamente e o contêiner iniciou sem problemas, o JupyterLab deve estar rodando dentro do contêiner `test-container` no endereço padrão `http:127.0.0.1:8888`. Portanto, ao abrir um navegador no sistema host onde o Docker Engine está rodando e acessar <http://127.0.0.1:88>, você deve ser conectado ao endereço `http://127.0.0.1:8888` dentro do contêiner e ver uma tela como esta:

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Abra um terminal no sistema host e execute o comando `ssh remote@127.0.0.1` para fazer login remoto na conta 'remote' do sistema Ubuntu rodando dentro do contêiner.  
Na primeira vez que você fizer login, receberá um aviso de que não há informações sobre a chave de criptografia do destino e que a autenticação não é possível, perguntando se deseja continuar a conexão. Digite "yes" para continuar.  
Em seguida, digite a senha para login (se você não alterou durante a construção da imagem, o valor padrão é "000000").
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {impressão digital (cada chave tem um valor único)}.
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
Se você vir uma saída semelhante a esta, o login remoto via SSH foi bem-sucedido. Para encerrar a sessão, digite o comando `exit`.

### 6-3. (opcional) Enviando para o Docker Hub
Para poder utilizar a imagem do ambiente de desenvolvimento que criamos a qualquer momento, é bom enviá-la para o Docker Hub.

> Para enviar sua imagem para o Docker Hub, você precisa ter uma conta Docker. Se ainda não tiver uma, registre-se em <https://app.docker.com/signup>.
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

#### 6-3-2. Marcando a imagem
Substitua `<dockerhub_username>`, `<repository_name>` e (opcional) `:TAG` com suas informações específicas.  
Ex: "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### Para Podman
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Para Docker
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Enviando a imagem
Finalmente, execute o comando abaixo para enviar a imagem para o Docker Hub:

##### Para Podman
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Para Docker
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Você pode verificar se o envio foi bem-sucedido em <https://hub.docker.com/>, como mostrado abaixo:  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

A imagem completa que criamos está disponível publicamente no repositório [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) no Docker Hub, e qualquer pessoa pode usá-la livremente.

Para baixar a imagem, basta executar o mesmo comando usado para enviar, substituindo `push` por `pull`.
