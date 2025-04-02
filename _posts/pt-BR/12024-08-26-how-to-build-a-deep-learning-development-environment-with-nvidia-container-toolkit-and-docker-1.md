---
title: NVIDIA Container Toolkit e Docker/Podman para Construir um Ambiente de Desenvolvimento de Deep Learning (1) - Instalação do NVIDIA Container Toolkit & Motor de Contêiner
description: Esta série aborda como configurar um ambiente de desenvolvimento de deep learning baseado em contêineres usando o NVIDIA Container Toolkit localmente, e como configurar SSH e Jupyter Lab para utilizá-lo como servidor remoto. Este post é o primeiro da série e introduz os métodos de instalação do NVIDIA Container Toolkit e do motor de contêiner.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Visão Geral
Esta série aborda o processo de instalação do NVIDIA Container Toolkit e Docker ou Podman, e a criação de um ambiente de desenvolvimento de deep learning usando um Dockerfile baseado nas imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub. Para aqueles que precisam, compartilho o [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) e a [imagem](https://hub.docker.com/r/yunseokim/dl-env/tags) resultantes deste processo no GitHub e Docker Hub para uso livre, além de fornecer um guia de configuração de SSH e Jupyter Lab para uso como servidor remoto.  
A série consistirá em 3 posts, e este é o primeiro deles.
- Parte 1: Instalação do NVIDIA Container Toolkit e Engine de Contêiner (este post)
- [Parte 2: Configuração do Runtime de Contêiner para Uso de GPU, Escrita de Dockerfile e Construção de Imagem de Contêiner](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Parte 3 (em breve)

Assumimos um sistema Linux x86_64 com uma placa gráfica NVIDIA compatível com CUDA. Embora os detalhes possam variar ligeiramente em distribuições além do Ubuntu ou Fedora, pois não foram testadas diretamente.  
(Atualizado em 18.02.12025)

### Configuração do Ambiente de Desenvolvimento
- Sistema operacional e arquitetura do host: x86_64, ambiente Linux (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Stack tecnológico a ser construído (linguagens e bibliotecas)
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE / Podman
  - CUDA 12.4
  - cuDNN
  - OpenSSH
  - tmux
  - JupyterLab
  - NumPy & SciPy
  - CuPy (opcional, biblioteca de arrays compatível com NumPy/SciPy para computação acelerada por GPU com Python)
  - pandas
  - cuDF (opcional, para acelerar pandas com zero mudanças de código usando acelerador GPU)
  - Matplotlib & Seaborn
  - DALI (opcional, alternativa de alto desempenho aos data loaders e iteradores nativos usando GPU)
  - scikit-learn
  - cuML (opcional, para executar algoritmos de machine learning em GPUs com uma API que segue de perto a API do scikit-learn)
  - PyTorch
  - tqdm

  > Dependendo da situação e preferência pessoal, você pode considerar usar a biblioteca DataFrame [Polars](https://pola.rs/) em vez do pandas. Escrita em Rust, ela [tem desempenho inferior à combinação cuDF + pandas para processamento de grandes volumes de dados, mas supera significativamente o pacote pandas puro](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/) e oferece uma sintaxe mais especializada para consultas. De acordo com o [blog oficial do Polars](https://pola.rs/posts/polars-on-gpu/), eles estão trabalhando com a equipe NVIDIA RAPIDS para suportar integração com cuDF em um futuro próximo.
  {: .prompt-tip }

  > Se você está em dúvida entre Docker CE e Podman, a [tabela comparativa abaixo](#3-instalação-do-motor-de-contêiner) pode ajudar.
  {: .prompt-tip }

### Tabela Comparativa com o Guia Anterior de Configuração de Ambiente de Machine Learning
Já existe [um guia anterior de configuração de ambiente de machine learning neste blog](/posts/Setting-up-a-Machine-Learning-Development-Environment) que ainda é válido em grande parte, mas há algumas mudanças que motivaram este novo post. As diferenças são resumidas na tabela abaixo:

| Diferença | Post Anterior (versão 12021) | Este Post (versão 12024) |
| --- | --- | --- |
| Distribuição Linux | Baseado no Ubuntu | Aplicável ao Ubuntu e também Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Método de configuração<br> do ambiente | Ambiente virtual Python usando venv | Ambiente baseado em contêiner usando<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Instalação do driver<br> gráfico NVIDIA | Sim | Sim |
| Instalação direta de CUDA<br> e cuDNN no sistema host | Sim (usando o gerenciador de pacotes Apt) | Não (usando [imagens pré-instaladas fornecidas<br> pela NVIDIA no Docker Hub](https://hub.docker.com/r/nvidia/cuda),<br> eliminando a necessidade de instalação direta) |
| Portabilidade | Necessidade de reconstruir o ambiente<br> ao migrar para outro sistema | Baseado em Docker, permitindo fácil portabilidade<br> usando o Dockerfile criado para construir novas<br> imagens ou transferir imagens existentes<br> (excluindo configurações adicionais de volume<br> ou rede) |
| Uso de bibliotecas adicionais<br> de aceleração GPU além<br> do cuDNN | Não | Introdução de [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/),<br> [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interface Jupyter Notebook | Jupyter Notebook (clássico) | JupyterLab (Nova Geração) |
| Configuração do servidor SSH | Não abordado | Inclui configuração básica de servidor SSH na parte 3 |

Se você preferir usar ambientes virtuais Python como venv em vez do Docker, o [post anterior](/posts/Setting-up-a-Machine-Learning-Development-Environment) ainda é válido e recomendado.

## 0. Verificações Preliminares
- [O NVIDIA Container Toolkit está disponível para distribuições Linux que suportam os gerenciadores de pacotes Apt, Yum ou Dnf, e Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Você pode verificar a lista de distribuições Linux suportadas no link fornecido. Embora não esteja listado explicitamente na tabela de suporte oficial, o Fedora também é compatível por ser baseado no Red Hat Linux. Se você não está familiarizado com o Linux e não sabe qual distribuição escolher, o Ubuntu LTS é a opção mais segura. Ele inclui drivers proprietários que facilitam o uso para iniciantes, e por ter muitos usuários, a maioria da documentação técnica é escrita com base no Ubuntu.
  - Você pode verificar a arquitetura do seu sistema e a versão da distribuição Linux executando `uname -m && cat /etc/*release` no terminal.
- Primeiro, verifique se a placa gráfica instalada no seu sistema suporta a versão CUDA e cuDNN que você pretende usar.
  - Você pode verificar o modelo da GPU instalada executando `lspci | grep -i nvidia` no terminal.
  - Na página <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>, verifique a **versão do driver NVIDIA** suportada por cada versão do cuDNN, os requisitos de **CUDA Compute Capability**, e a lista de **hardware NVIDIA suportado**.
  - Em <https://developer.nvidia.com/cuda-gpus>, encontre seu modelo de GPU e verifique seu valor de **Compute Capability**. Este valor deve atender aos requisitos de **CUDA Compute Capability** verificados anteriormente para usar CUDA e cuDNN sem problemas.

> Se você planeja comprar uma nova placa gráfica para deep learning, os critérios de seleção de GPU estão bem resumidos no seguinte artigo, que o autor atualiza continuamente:  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> Outro artigo muito útil do mesmo autor é [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/).
{: .prompt-tip }

Se você atender a todos os requisitos mencionados acima, vamos começar a configurar o ambiente de trabalho.

## 1. Instalação do Driver Gráfico NVIDIA
Primeiro, você precisa instalar o driver gráfico NVIDIA no sistema host. Você pode baixar o instalador .run da [página de download de drivers NVIDIA](https://www.nvidia.com/drivers/), mas é preferível usar o gerenciador de pacotes do seu sistema para facilitar o gerenciamento de versões e manutenção. Consulte a documentação oficial <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> e instale o driver gráfico adequado para seu ambiente.

### Módulo Proprietário vs Módulo Open-source
Os drivers Linux da NVIDIA consistem em vários módulos de kernel, e a partir do driver versão 515 e posteriores, a NVIDIA oferece dois tipos de módulos de kernel:

- Proprietário: O driver de software proprietário que a NVIDIA fornecia tradicionalmente.
- Open-source: Driver de código aberto fornecido sob licença dupla MIT/GPLv2. O código-fonte está disponível em <https://github.com/NVIDIA/open-gpu-kernel-modules>.

Os drivers proprietários são fornecidos para GPUs baseadas em arquiteturas desde Maxwell até antes de Blackwell, e serão descontinuados a partir da arquitetura Blackwell.
Por outro lado, os drivers open-source são suportados para arquiteturas Turing e posteriores.

[A NVIDIA recomenda usar o módulo de kernel open-source quando possível.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)
Você pode verificar se sua GPU é compatível com o driver open-source [neste link](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

Este guia assume a instalação do driver open-source.

### Debian & Ubuntu
Para Ubuntu ou Debian, execute os seguintes comandos no terminal:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Para Fedora 40, apresentamos o método de instalação usando pacotes pré-compilados fornecidos pelo [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuração do Repositório RPM Fusion  
Seguindo o [guia oficial do RPM Fusion](https://rpmfusion.org/Configuration), execute o seguinte comando no terminal:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Instalação do Pacote akmod-nvidia-open  
Seguindo o [guia de instalação de drivers NVIDIA do RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), ative o repositório rpmfusion-nonfree-tainted e instale o pacote akmod-nvidia-open:
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Registro de Chave para Carregamento Correto do Driver com Secure Boot  

> Com apenas alguns procedimentos adicionais explicados abaixo, você pode usar normalmente o driver gráfico NVIDIA com o Secure Boot ativado. Desativar o Secure Boot torna o sistema significativamente vulnerável, então é recomendado não desativá-lo. Pelo menos desde o início da década de 12020, raramente há motivo para desativar o Secure Boot.
{: .prompt-danger }

Primeiro, instale as seguintes ferramentas:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Em seguida, execute o comando abaixo para gerar uma chave:
```bash
sudo kmodgenca -a
```
Agora, você precisa registrar a chave gerada no MOK do firmware UEFI:
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Ao executar este comando, será solicitada uma senha para o registro da chave. Esta é uma senha de uso único que você usará após reiniciar, então escolha algo que possa lembrar facilmente.

Agora reinicie o sistema com o seguinte comando:
```bash
systemctl reboot
```
Durante a inicialização, a tela de gerenciamento MOK aparecerá automaticamente. Selecione "Enroll MOK", depois "Continue" e "Yes" em sequência, e então será solicitada a senha que você definiu anteriormente. Após inserir a senha, o processo de registro da chave será concluído. Digite reboot para reiniciar novamente, e o driver NVIDIA será carregado normalmente.

### Verificação da Instalação do Driver NVIDIA
Execute o seguinte comando no terminal para verificar o módulo de kernel NVIDIA atualmente carregado:
```bash
cat /proc/driver/nvidia/version
```
Se você ver uma mensagem semelhante à seguinte, a instalação foi bem-sucedida:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Instalação do NVIDIA Container Toolkit
Agora você precisa instalar o [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Siga o [guia oficial de instalação do NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), mas observe que há considerações especiais para o Fedora, então leia esta seção até o final antes de prosseguir.

### Para usuários de Apt (Ubuntu, Debian, etc.)
#### 2-Apt-1. Configuração do Repositório para Download de Pacotes
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Atualização da Lista de Pacotes
```bash
sudo apt update
```

#### 2-Apt-3. Instalação do Pacote
```bash
sudo apt install nvidia-container-toolkit
```

### Para usuários de Yum ou Dnf (Fedora, RHEL, Centos, etc.)
> Ao testar no Fedora 40, diferentemente do Ubuntu, o comando `nvidia-smi` e o pacote `nvidia-persistenced` não estavam incluídos por padrão no driver gráfico NVIDIA, sendo necessário instalar o pacote `xorg-x11-drv-nvidia-cuda` adicionalmente. Não testei diretamente no RHEL e Centos, mas como a configuração do sistema é muito semelhante ao Fedora, se você encontrar problemas seguindo este guia, tentar o mesmo método pode ser útil.
{: .prompt-warning }

> No Fedora 40, após instalar o `xorg-x11-drv-nvidia-cuda` conforme descrito acima e testar com uma carga de trabalho de exemplo, funcionou normalmente no meu sistema. Se você ainda encontrar problemas, possivelmente devido ao SELinux, o [pacote nvidia-container-toolkit específico para Fedora e guia fornecido pelo grupo AI-ML do Fedora](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) pode ser útil.
{: .prompt-tip }

#### 2-Dnf-1. Configuração do Repositório para Download de Pacotes
```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Instalação do Pacote
```bash
sudo dnf install nvidia-container-toolkit
```
ou
```bash
sudo yum install nvidia-container-toolkit
```

### Para usuários de Zypper (openSUSE, SLES)
#### 2-Zypper-1. Configuração do Repositório para Download de Pacotes
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalação do Pacote
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalação do Motor de Contêiner
Em seguida, instale Docker CE ou Podman como motor de contêiner. Escolha um deles de acordo com seu ambiente e preferência, consultando a [documentação oficial do Docker](https://docs.docker.com/engine/install/) ou a [documentação oficial do Podman](https://podman.io/docs/installation).

A tabela a seguir resume as principais diferenças e vantagens/desvantagens entre Docker e Podman.

| Item de Comparação | Docker | Podman |
| --- | --- | --- |
| Arquitetura | Modelo cliente-servidor, baseado em daemon | Estrutura sem daemon (daemonless) |
| Segurança | Potenciais riscos de segurança por depender de<br> um daemon executado com privilégios root<br> (suporta modo rootless desde a versão 20.10<br> lançada em 12020, mas requer configuração adicional) | Não depende de daemon, opera por padrão<br> em modo rootless e é protegido pelo SELinux |
| Uso de Recursos | Maior consumo de recursos devido ao processo<br> de daemon em segundo plano | Geralmente menor overhead de recursos |
| Tempo de Inicialização<br> do Contêiner | Relativamente mais lento | Até 50% mais rápido devido à<br> arquitetura simplificada |
| Ecossistema e<br> Documentação | Amplo ecossistema e suporte comunitário,<br> documentação abundante | Ecossistema e documentação<br> relativamente menores |
| Redes | Usa Docker Bridge Network | Usa plugins CNI<br> (Container Network Interface) |
| Suporte Nativo a<br> YAML do Kubernetes | Não (requer conversão) | Sim |

Referências:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker tem uma história mais longa e desfrutou do status de padrão de facto na indústria, resultando em um ecossistema mais amplo e documentação abundante, o que é sua maior vantagem.  
Podman foi desenvolvido mais recentemente pela Red Hat e, por design, visa ser daemonless e rootless, oferecendo vantagens em segurança, uso de recursos do sistema e tempo de inicialização de contêineres. Outra vantagem do Podman é que, diferentemente do Docker, onde todos os contêineres caem juntos se o daemon tiver problemas, cada contêiner é completamente independente, então a queda de um contêiner específico não afeta os outros.

É importante escolher a ferramenta que melhor se adapta às suas circunstâncias, e para usuários individuais iniciantes, começar com Podman pode ser uma boa escolha. Embora seu ecossistema seja relativamente menor comparado ao Docker, está crescendo rapidamente devido às vantagens mencionadas, e como é compatível com a sintaxe Dockerfile, imagens Docker e CLI (interface de linha de comando), isso não deve ser um problema para indivíduos ou pequenos grupos.

### Podman
Disponível nos repositórios padrão da maioria das principais distribuições Linux, pode ser instalado facilmente.

#### Para Ubuntu
```bash
sudo apt install podman
```

#### Para Fedora
```bash
sudo dnf install podman
```

#### Para openSUSE
```bash
sudo zypper install podman
```

### Docker CE
#### Para Ubuntu
##### 3-Ubuntu-1. Remoção de Versões Anteriores ou Pacotes Não Oficiais para Evitar Conflitos
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configuração do Repositório
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

##### 3-Ubuntu-3. Instalação dos Pacotes
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Criação do Grupo `Docker` e Registro de Usuário
Para permitir que usuários não-root gerenciem o Docker sem `sudo`, crie um grupo `Docker` e adicione os usuários que desejam usar o Docker. Execute os seguintes comandos no terminal:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Depois, faça logout e login novamente para aplicar as configurações alteradas. No Ubuntu ou Debian, o serviço Docker é iniciado automaticamente a cada inicialização do sistema sem necessidade de configuração adicional.

#### Para Fedora
##### 3-Fedora-1. Remoção de Versões Anteriores ou Pacotes Não Oficiais para Evitar Conflitos
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

##### 3-Fedora-2. Configuração do Repositório
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Instalação dos Pacotes
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Durante a instalação, você será solicitado a aprovar uma chave GPG. Se a chave GPG corresponder a `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, digite y para aprovar.  
> Se a chave GPG não corresponder, você pode estar baixando um pacote falsificado por um ataque à cadeia de suprimentos e deve interromper a instalação.
{: .prompt-danger }

##### 3-Fedora-4. Inicialização do Daemon Docker
Agora o Docker está instalado, mas não iniciado. Execute o seguinte comando para iniciar o Docker:
```bash
sudo systemctl start docker
```
Para que o serviço Docker seja iniciado automaticamente na inicialização do sistema, execute:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Registro de Usuário no Grupo `Docker`
Para permitir que usuários não-root gerenciem o Docker, adicione-os ao grupo `Docker`. No Fedora, o grupo `Docker` é criado automaticamente durante a instalação do pacote, então você só precisa registrar os usuários:
```bash
sudo usermod -aG docker $USER
```
Depois, faça logout e login novamente para aplicar as configurações alteradas.

#### Verificação da Configuração
Execute o seguinte comando no terminal:
```bash
docker run hello-world
```
Se você ver uma mensagem como esta, a configuração foi bem-sucedida:

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
