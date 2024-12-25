---
title: Construindo um ambiente de desenvolvimento de Deep Learning com NVIDIA Container
  Toolkit e Docker (2) - Configuração do runtime do contêiner para utilização da GPU,
  escrita do Dockerfile e construção da imagem Docker
description: Esta série aborda como configurar um ambiente de desenvolvimento de Deep
  Learning baseado em NVIDIA Container Toolkit e Docker localmente, e como configurar
  SSH e Jupyter Lab para utilizá-lo como um servidor remoto. Este post é o segundo
  da série e apresenta como configurar o runtime do contêiner para utilização da GPU,
  escrever o Dockerfile e construir a imagem Docker.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Visão geral
Nesta série, abordamos o processo de instalação do NVIDIA Container Toolkit e Docker, e a construção de um ambiente de desenvolvimento de Deep Learning escrevendo um Dockerfile baseado nas imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub. Para aqueles que precisam, compartilhamos o [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) e a [imagem](https://hub.docker.com/r/yunseokim/dl-env/tags) concluídos através deste processo no GitHub e Docker Hub para uso livre, e fornecemos adicionalmente um guia de configuração de SSH e Jupyter Lab para utilização como servidor remoto.  
A série consistirá em 3 posts, e este é o segundo post da série.
- [Parte 1: Instalação do NVIDIA Container Toolkit & Docker Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Parte 2: Configuração do runtime do contêiner para utilização da GPU, escrita do Dockerfile e construção da imagem Docker (este post)
- Parte 3 (a ser publicada)

Prosseguiremos assumindo um sistema Linux x86_64 com uma placa gráfica NVIDIA que suporta CUDA, e embora não tenhamos testado diretamente em distribuições além do Ubuntu ou Fedora, pode haver algumas pequenas diferenças em alguns detalhes específicos.

## Antes de começar
Este post é uma continuação da [Parte 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), então se você ainda não leu, recomendo que leia o post anterior primeiro.

## 4. Configuração do runtime do contêiner
### 4-1. Executar o comando `nvidia-ctk`
```bash
sudo nvidia-ctk runtime configure --runtime=docker
```
Este comando modifica o arquivo `/etc/docker/daemon.json`{: .filepath} para permitir que o Docker utilize o NVIDIA Container Runtime.

### 4-2. Reiniciar o daemon do Docker
Reinicie o daemon do Docker para aplicar as configurações alteradas.
```bash
sudo systemctl restart docker
```

### 4-3. Verificar se foi configurado corretamente
Execute um contêiner CUDA de exemplo.
```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
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
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)No momento da escrita deste post, no final de agosto de 2024, a versão mais recente do PyTorch, 2.4.0, suporta CUDA 12.4. Portanto, usaremos a imagem [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) aqui. Você pode verificar a versão mais recente do PyTorch e as versões CUDA suportadas na [página inicial do PyTorch](https://pytorch.org/get-started/locally/).

O código-fonte do Dockerfile concluído está disponível publicamente no repositório GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Abaixo, explicamos o processo de escrita deste Dockerfile passo a passo.

### 5-1. Especificar a imagem base
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Instalar utilitários básicos e pré-requisitos do Python
```Dockerfile
RUN apt-get update -y && apt-get install -y --no-install-recommends\
    apt-utils \
    ssh \
    curl \
    openssh-server \
    python3 \
    python-is-python3 \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*
```

### 5-3. Configurar o fuso horário do sistema (neste post, usaremos 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

### 5-4. Configurar o servidor SSH para acesso remoto  
Configure para que o login na conta root não seja possível com senha durante o acesso SSH remoto por motivos de segurança.
```Dockerfile
# Disable root access via password
RUN echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config
```
Configure para que o serviço SSH inicie automaticamente quando o contêiner for iniciado.
```Dockerfile
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
```
Crie um usuário não-root chamado 'remote' para usar ao acessar via SSH.
```Dockerfile
# Create a non-root user and switch to it
ARG USER_NAME="remote"
ARG USER_PASSWORD="000000"
RUN useradd --create-home --password $USER_PASSWORD $USER_NAME
ENV HOME=/home/$USER_NAME
USER $USER_NAME
WORKDIR $HOME
# Re-run ssh when the container restarts.
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
# Create a workspace directory to locate jupyter notebooks and .py files
RUN mkdir -p $HOME/workspace
```

> Se você não especificar opções separadas ao construir a imagem Docker usando este Dockerfile, o valor inicial da senha da conta do usuário 'remote' será 000000. Isso é extremamente vulnerável em termos de segurança, então use a opção `--build-arg` ao construir a imagem Docker para especificar uma senha de login de conta separadamente, ou altere as configurações imediatamente após executar o contêiner pela primeira vez. Para segurança, é desejável desativar o login por senha ao acessar via SSH e configurar posteriormente para permitir o login apenas através de um arquivo de chave separado, e seria ideal usar uma chave de hardware como o Yubikey.
> A configuração do servidor SSH será abordada até certo ponto na próxima parte desta série, e se você quiser saber mais detalhes, pode consultar os documentos na seguinte lista:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Instalar setuptools, pip e registrar a variável de ambiente PATH
```Dockerfile
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME/.local/bin:$PATH"
```

### 5-6. Instalar pacotes de machine learning e deep learning para usar no ambiente de desenvolvimento
```Dockerfile
RUN python3 -m pip install -U jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm
RUN python3 -m pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
Se você quiser usar Cupy, cuDF, cuML e DALI, adicione o seguinte conteúdo ao Dockerfile:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x
RUN python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Configurar para executar o JupyterLab ao iniciar o contêiner
```Dockerfile
CMD cd $HOME/workspace && \
    jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="$HOME/workspace"
```

## 6. Construir a imagem Docker e executar o contêiner
### 6-1. Construir a imagem
Abra um terminal no diretório onde o Dockerfile está localizado e execute o seguinte comando:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> No lugar de \<password\>, insira a senha de login que você usará ao acessar via SSH.
{: .prompt-info }

### 6-2. Executar uma carga de trabalho de exemplo
Após concluir a construção, execute o seguinte comando para iniciar um contêiner descartável e verificar se está funcionando corretamente:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```
Quando você inserir o comando acima no terminal, ele executará um contêiner chamado `test-container` a partir da imagem `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` que acabamos de construir e conectará a porta 88 do sistema host à porta 8888 desse contêiner. Se a imagem Docker foi construída corretamente na etapa anterior e o contêiner foi iniciado sem problemas, o JupyterLab deve estar em execução no endereço padrão `http:127.0.0.1:8888` dentro do contêiner `test-container`. Portanto, ao abrir um navegador no sistema host onde o Docker Engine está em execução e acessar <http://127.0.0.1:88>, você deve ser conectado ao endereço `http://127.0.0.1:8888` dentro do contêiner e ver uma tela como a seguinte:

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

### 6-3. (opcional) Fazer Push para o Docker Hub
Para poder utilizar a imagem do ambiente de desenvolvimento que criamos através do processo anterior sempre que necessário, é bom fazer o Push da imagem construída para o Docker Hub.  

> Para fazer o Push de sua própria imagem para o Docker Hub, você precisa de uma conta Docker, então se ainda não tiver uma, primeiro complete o registro em <https://app.docker.com/signup>.
{: .prompt-tip }

Primeiro, faça login no Docker Hub com o seguinte comando:
```bash
docker login
```
Agora, execute um comando no seguinte formato para criar uma tag de imagem:
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```
Por fim, execute o seguinte comando para fazer o Push da imagem para o Docker Hub:
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Você pode confirmar que o Push foi bem-sucedido em <https://hub.docker.com/> como mostrado abaixo:  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

A imagem concluída através do processo anterior está disponível publicamente no repositório público [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) no Docker Hub e pode ser usada livremente por qualquer pessoa.
