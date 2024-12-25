---
title: Construindo um ambiente de desenvolvimento de Deep Learning com NVIDIA Container
  Toolkit e Docker (1) - Instalação do NVIDIA Container Toolkit & Docker Engine
description: Esta série aborda como configurar um ambiente de desenvolvimento de Deep
  Learning baseado em NVIDIA Container Toolkit e Docker localmente, e como configurar
  SSH e Jupyter Lab para utilizá-lo como um servidor remoto. Este post é o primeiro
  da série e introduz o método de instalação do NVIDIA Container Toolkit.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Visão Geral
Esta série aborda o processo de instalação do NVIDIA Container Toolkit e Docker, e a criação de um ambiente de desenvolvimento de Deep Learning escrevendo um Dockerfile baseado nas imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub. Para aqueles que precisam, compartilhamos o [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) e a [imagem](https://hub.docker.com/r/yunseokim/dl-env/tags) resultantes deste processo através do GitHub e Docker Hub para uso livre, e adicionalmente fornecemos um guia de configuração de SSH e Jupyter Lab para utilização como servidor remoto.
A série consistirá de 3 posts, e este é o primeiro deles.
- Parte 1: Instalação do NVIDIA Container Toolkit & Docker Engine (este post)
- [Parte 2: Configuração do runtime de contêiner para utilização de GPU, escrita do Dockerfile e build da imagem Docker](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Parte 3 (a ser publicada)

Assumimos um sistema com uma placa gráfica NVIDIA compatível com CUDA em um ambiente Linux x86_64, e embora não tenhamos testado diretamente em distribuições além de Ubuntu ou Fedora, alguns detalhes específicos podem variar ligeiramente.

### Configuração do Ambiente de Desenvolvimento
- Sistema operacional e arquitetura do host: Ambiente Linux x86_64 (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Stack tecnológico a ser construído (linguagens e bibliotecas)
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE
  - CUDA 12.4
  - cuDNN
  - JupyterLab
  - NumPy & SciPy
  - CuPy (opcional, biblioteca de arrays compatível com NumPy/SciPy para computação acelerada por GPU com Python)
  - pandas
  - cuDF (opcional, para acelerar pandas com mudanças zero de código com o acelerador GPU)
  - Matplotlib & Seaborn
  - DALI (opcional, alternativa de alto desempenho aos data loaders e iteradores de dados integrados usando GPU)
  - scikit-learn
  - cuML (opcional, para executar algoritmos de machine learning em GPUs com uma API que segue de perto a API do scikit-learn)
  - PyTorch
  - OpenSSH
  - tqdm

  > Dependendo da situação e preferência pessoal, pode-se considerar usar a biblioteca DataFrame [Polars](https://pola.rs/) em vez do pandas. Escrita em Rust, [ela tem um desempenho notavelmente superior ao pacote pandas puro, embora fique atrás da combinação cuDF + pandas no processamento de grandes volumes de dados](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), e fornece uma sintaxe mais especializada para consultas. De acordo com o [blog oficial do Polars](https://pola.rs/posts/polars-on-gpu/), eles planejam suportar integração com cuDF em um futuro próximo, em colaboração com a equipe NVIDIA RAPIDS.
  {: .prompt-tip }

### Tabela comparativa com o guia anterior de configuração de ambiente de machine learning
Já existe [um guia de configuração de ambiente de machine learning anteriormente publicado neste blog](/posts/Setting-up-a-Machine-Learning-Development-Environment) que ainda é válido em sua maior parte, mas há algumas mudanças que levaram à criação deste novo post. As diferenças são resumidas na tabela abaixo.

| Diferença | Post Anterior (versão 2021) | Este Post (versão 2024) |
| --- | --- | --- |
| Distribuição Linux | Baseado em Ubuntu | Aplicável a Ubuntu, Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Método de construção do ambiente | Ambiente virtual Python usando venv | Ambiente baseado em contêiner Docker usando<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Instalação do driver gráfico NVIDIA | O | O |
| Instalação direta de CUDA e cuDNN<br> no sistema host | O (usando o gerenciador de pacotes Apt) | X (Usa imagens pré-instaladas fornecidas pela NVIDIA<br> no [Docker Hub](https://hub.docker.com/r/nvidia/cuda), então não é necessário trabalho direto) |
| Portabilidade | Precisa reconstruir o ambiente de desenvolvimento<br> cada vez que muda para um novo sistema | Baseado em Docker, então pode facilmente construir<br> novas imagens com o Dockerfile criado quando necessário<br> ou portar imagens existentes (excluindo configurações<br> adicionais de volume ou rede) |
| Utilização de bibliotecas de aceleração<br> GPU adicionais além de cuDNN | X | Introdução de [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interface Jupyter Notebook | Jupyter Notebook (clássico) | JupyterLab (Nova Geração) |
| Configuração do servidor SSH | Não abordado separadamente | Inclui configuração básica do servidor SSH na Parte 3 |

Se você preferir usar um ambiente virtual Python como venv em vez do Docker, o [post anterior](/posts/Setting-up-a-Machine-Learning-Development-Environment) ainda é válido e recomendo consultá-lo.

## 0. Pré-requisitos
- [O NVIDIA Container Toolkit está disponível em distribuições Linux que suportam os gerenciadores de pacotes Apt, Yum ou Dnf, Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Você pode verificar a lista de distribuições Linux suportadas na página linkada, e embora não esteja listado especificamente na tabela de suporte oficial, Fedora também pode ser usado sem problemas, pois é baseado no Red Hat Linux como RHEL. Se você não está familiarizado com o ambiente Linux e não tem certeza de qual distribuição usar, usar a versão LTS do Ubuntu é a opção mais segura. Drivers proprietários não open-source também são instalados automaticamente, tornando-o relativamente conveniente para iniciantes, e devido ao grande número de usuários, a maioria da documentação técnica é escrita com base no Ubuntu.
  - Você pode verificar a arquitetura do seu sistema e a versão da distribuição Linux executando o comando `uname -m && cat /etc/*release` no terminal.
- Primeiro, você deve verificar se o modelo da placa gráfica instalada no seu sistema suporta as versões de CUDA e cuDNN que você pretende usar.
  - Você pode verificar o nome do modelo da GPU instalada no seu computador atual executando o comando `lspci | grep -i nvidia` no terminal.
  - Na página <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>, verifique a **versão do driver gráfico NVIDIA suportada** por versão do cuDNN, a condição de **CUDA Compute Capability** requerida, e a lista de **hardware NVIDIA suportado**.
  - Encontre o nome do modelo correspondente na lista de GPUs em <https://developer.nvidia.com/cuda-gpus> e verifique o valor de **Compute Capability**. Este valor deve atender à condição de **CUDA Compute Capability** verificada anteriormente para usar CUDA e cuDNN sem problemas.

> Se você planeja comprar uma nova placa gráfica para trabalhos de deep learning, os critérios de seleção de GPU estão bem resumidos no seguinte artigo. É um artigo que o autor atualiza continuamente.
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
> [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) escrito pelo mesmo autor também é muito informativo.
{: .prompt-tip }

Se você atender a todos os requisitos mencionados acima, vamos começar a configurar o ambiente de trabalho.

## 1. Instalação do Driver Gráfico NVIDIA
Primeiro, você precisa instalar o driver gráfico NVIDIA no sistema host. Você pode baixar e usar o instalador .run da [página de download de drivers NVIDIA](https://www.nvidia.com/drivers/), mas é preferível usar o gerenciador de pacotes do seu sistema para instalação, pois é melhor em termos de gerenciamento de versão e manutenção. Consulte a documentação oficial <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> para instalar o driver gráfico apropriado para o seu ambiente de sistema.

### Módulo Proprietário vs Módulo Open-source
Os drivers NVIDIA para Linux consistem em vários módulos de kernel, e a partir do driver versão 515 e lançamentos posteriores, a NVIDIA fornece dois tipos de módulos de kernel de driver:

- Proprietário: O driver de software proprietário que a NVIDIA tem fornecido tradicionalmente.
- Open-source: Driver de código aberto fornecido sob licença dupla MIT/GPLv2. O código-fonte é disponibilizado através de <https://github.com/NVIDIA/open-gpu-kernel-modules>.

O driver proprietário é fornecido para GPUs baseadas em arquiteturas desde Maxwell até antes de Blackwell, e será descontinuado a partir da arquitetura Blackwell.
Por outro lado, o driver open-source é suportado para arquiteturas Turing e posteriores.

[A NVIDIA recomenda usar o módulo de kernel open-source quando possível.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)
Você pode verificar se sua GPU é compatível com o driver open-source [neste link](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

Neste artigo, assumiremos que estamos instalando o driver open-source.

### Debian & Ubuntu
Para Ubuntu ou Debian, instale executando os seguintes comandos no terminal:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Com base no Fedora 40, introduziremos o método de baixar e instalar pacotes pré-construídos fornecidos pelo [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuração do repositório RPM Fusion
Siga o [guia oficial do RPM Fusion](https://rpmfusion.org/Configuration).
Execute os seguintes comandos no terminal:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Instalação do pacote akmod-nvidia-open
Referindo-se ao [guia de instalação do driver NVIDIA fornecido pelo RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open),
ative o repositório rpmfusion-nonfree-tainted e então instale o pacote akmod-nvidia-open.
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Registro de chave para carregamento normal do driver durante o Secure Boot

> Com apenas alguns procedimentos adicionais explicados abaixo, você pode usar o driver gráfico NVIDIA normalmente enquanto utiliza a função de Secure Boot, e como desativar o Secure Boot torna o sistema significativamente vulnerável, recomenda-se não desativá-lo. Pelo menos desde o início da década de 2020, não há quase nenhuma razão para desativar o Secure Boot.
{: .prompt-danger }

Primeiro, instale as seguintes ferramentas:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Em seguida, execute o seguinte comando para gerar uma chave:
```bash
sudo kmodgenca -a
```
Agora, você precisa registrar a chave gerada no MOK do firmware UEFI.
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Quando você executar o comando acima, será solicitado que você insira uma senha para o registro da chave. Você reiniciará em breve para completar o procedimento de registro da chave, então insira algo que você possa lembrar facilmente, pois será uma senha de uso único.

Agora, execute o seguinte comando para reiniciar o sistema:
```bash
systemctl reboot
```
Quando o sistema iniciar, a janela de gerenciamento MOK aparecerá automaticamente. Selecione "Enroll MOK" e então selecione "Continue" e "Yes" em sequência, e uma janela solicitando a senha que você definiu anteriormente aparecerá. Depois de inserir a senha que você definiu anteriormente, o procedimento de registro da chave será concluído. Agora, digite reboot para reiniciar novamente e o driver NVIDIA será carregado normalmente.

### Verificação da instalação do driver NVIDIA
Você pode verificar o módulo de kernel NVIDIA atualmente carregado executando o seguinte comando no terminal:
```bash
cat /proc/driver/nvidia/version
```
Se uma mensagem semelhante à seguinte for exibida, a instalação foi bem-sucedida:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Instalação do NVIDIA Container Toolkit
Agora você precisa instalar o [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Siga a instalação referindo-se ao [guia oficial de instalação do NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), mas no caso do Fedora, há precauções durante o processo de instalação, então verifique o conteúdo desta seção até o final antes de prosseguir.

### Para usuários do Apt (Ubuntu, Debian, etc.)
#### 2-Apt-1. Configuração do repositório para download de pacotes
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Atualização da lista de pacotes
```bash
sudo apt update
```

#### 2-Apt-3. Instalação do pacote
```bash
sudo apt install nvidia-container-toolkit
```

### Para usuários do Yum ou Dnf (Fedora, RHEL, Centos, etc.)
> Ao testar no Fedora 40, diferentemente do Ubuntu, o comando `nvidia-smi` e o pacote `nvidia-persistenced` não estavam incluídos por padrão no driver gráfico NVIDIA, então foi necessário instalar adicionalmente o pacote `xorg-x11-drv-nvidia-cuda`. Não testei diretamente no RHEL e Centos, mas como a configuração do sistema é muito semelhante ao Fedora, se você encontrar problemas ao seguir o guia abaixo, tentar o mesmo método pode ser útil.
{: .prompt-warning }

> Após instalar `xorg-x11-drv-nvidia-cuda` conforme o método acima e executar uma carga de trabalho de amostra para teste no Fedora 40, funcionou normalmente no sistema do autor. Se você ainda encontrar problemas devido a SELinux ou outras razões, o [pacote nvidia-container-toolkit específico para Fedora e guia](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) fornecido pelo grupo AI-ML do Fedora pode ser útil.
{: .prompt-tip }

#### 2-Dnf-1. Configuração do repositório para download de pacotes
```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Instalação do pacote
```bash
sudo dnf install nvidia-container-toolkit
```
ou
```bash
sudo yum install nvidia-container-toolkit
```

### Para usuários do Zypper (openSUSE, SLES)
#### 2-Zypper-1. Configuração do repositório para download de pacotes
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalação do pacote
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalação do Docker Engine
Em seguida, instale o Docker Engine. Siga a instalação referindo-se à [documentação oficial do Docker](https://docs.docker.com/engine/install/).

### Para Ubuntu
#### 3-Ubuntu-1. Remoção de versões anteriores ou pacotes não oficiais para evitar conflitos de pacotes
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

#### 3-Ubuntu-2. Configuração do repositório
```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
```

#### 3-Ubuntu-3. Instalação do pacote
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 3-Ubuntu-4. Criação do grupo `Docker` e registro do usuário
Para permitir que usuários não-root gerenciem o Docker sem `sudo`, você pode criar um grupo `Docker` e registrar os usuários que desejam usar o Docker. Execute os seguintes comandos no terminal:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Depois de fazer logout e login novamente, as configurações alteradas serão aplicadas. No caso do Ubuntu ou Debian, o serviço Docker será executado automaticamente a cada inicialização do sistema sem nenhum trabalho adicional.

### Para Fedora
#### 3-Fedora-1. Remoção de versões anteriores ou pacotes não oficiais para evitar conflitos de pacotes
```bash
sudo dnf remove docker \
                docker-client \
                docker-client-latest \
                docker-common \
                docker-latest \
                docker-latest-logrotate \
                docker-logrotate \
                docker-selinux \
                docker-engine-selinux \
                docker-engine
```

#### 3-Fedora-2. Configuração do repositório
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

#### 3-Fedora-3. Instalação do pacote
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Durante o processo de instalação do pacote, você será solicitado a aprovar a chave GPG. Se a chave GPG corresponder a `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, digite y para aprovar.
> Se a chave GPG não corresponder, você pode estar baixando um pacote falsificado devido a um ataque à cadeia de suprimentos e deve interromper a instalação.
{: .prompt-danger }

#### 3-Fedora-4. Iniciar o daemon Docker
Agora o Docker está instalado, mas não está em execução, então você pode iniciar o Docker digitando o seguinte comando:
```bash
sudo systemctl start docker
```
Para que o serviço Docker seja executado automaticamente na inicialização do sistema, execute os seguintes comandos:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

#### 3-Fedora-5. Registrar usuários no grupo `Docker`
Para permitir que usuários não-root gerenciem o Docker, registre os usuários que desejam usar o Docker no grupo `Docker`. No caso do Fedora, o grupo `Docker` é criado automaticamente durante o processo de instalação do pacote anterior, então você só precisa registrar os usuários.
```bash
sudo usermod -aG docker $USER
```
Depois de fazer logout e login novamente, as configurações alteradas serão aplicadas.

### Verificar se está configurado corretamente
Execute o seguinte comando no terminal:
```bash
docker run hello-world
```
Se você ver uma mensagem como a seguinte, foi bem-sucedido:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Leitura Adicional
Continua na [Parte 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
