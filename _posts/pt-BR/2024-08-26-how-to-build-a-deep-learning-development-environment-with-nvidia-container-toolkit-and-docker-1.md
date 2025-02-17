---
title: Construindo um ambiente de desenvolvimento de Deep Learning com NVIDIA Container Toolkit e Docker/Podman (1) - Instalação do NVIDIA Container Toolkit e do mecanismo de contêiner
description: Esta série aborda como configurar um ambiente de desenvolvimento de Deep Learning baseado em contêineres usando o NVIDIA Container Toolkit localmente, e como configurar SSH e Jupyter Lab para utilizá-lo como um servidor remoto. Este post é o primeiro da série e introduz os métodos de instalação do NVIDIA Container Toolkit e do mecanismo de contêiner.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Visão Geral
Esta série aborda o processo de instalação do NVIDIA Container Toolkit e Docker ou Podman, e a construção de um ambiente de desenvolvimento de Deep Learning usando um Dockerfile baseado em imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda no Docker Hub](https://hub.docker.com/r/nvidia/cuda). O [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) e a [imagem](https://hub.docker.com/r/yunseokim/dl-env/tags) resultantes deste processo são compartilhados via GitHub e Docker Hub para que aqueles que precisam possam usá-los livremente, e adicionalmente, um guia de configuração de SSH e Jupyter Lab é fornecido para uso como servidor remoto.  
A série consistirá em 3 posts, e este que você está lendo é o primeiro da série.
- Parte 1: Instalação do NVIDIA Container Toolkit e do mecanismo de contêiner (este post)
- [Parte 2: Configuração do runtime de contêiner para utilização de GPU, escrita do Dockerfile e construção da imagem do contêiner](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Parte 3 (a ser publicada)

Assumimos um sistema com uma placa gráfica NVIDIA compatível com CUDA em um ambiente Linux x86_64, e embora não tenha sido testado diretamente em distribuições além do Ubuntu ou Fedora, pode haver pequenas diferenças em alguns detalhes específicos.  
(Conteúdo atualizado em 18.02.2025)

### Configuração do Ambiente de Desenvolvimento
- Sistema operacional e arquitetura do host: Ambiente Linux x86_64 (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Pilha tecnológica a ser construída (linguagens e bibliotecas)
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
  - cuDF (opcional, para acelerar pandas com mudanças zero de código com o acelerador GPU)
  - Matplotlib & Seaborn
  - DALI (opcional, alternativa de alto desempenho aos carregadores de dados e iteradores de dados integrados usando GPU)
  - scikit-learn
  - cuML (opcional, para executar algoritmos de aprendizado de máquina em GPUs com uma API que segue de perto a API do scikit-learn)
  - PyTorch
  - tqdm

  > Dependendo da situação e da preferência pessoal, pode-se considerar usar a biblioteca DataFrame [Polars](https://pola.rs/) em vez do pandas. Escrita em Rust, ela [mostra um desempenho notavelmente superior ao pacote pandas puro ao processar grandes volumes de dados, embora fique atrás da combinação cuDF + pandas](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), e fornece uma sintaxe mais especializada para consultas. De acordo com o [blog oficial do Polars](https://pola.rs/posts/polars-on-gpu/), eles planejam suportar a integração com cuDF em um futuro próximo, em colaboração com a equipe NVIDIA RAPIDS.
  {: .prompt-tip }

  > Se você está em dúvida entre usar Docker CE ou Podman, a [tabela comparativa mencionada posteriormente](#3-instalação-do-mecanismo-de-contêiner) pode ser útil.
  {: .prompt-tip }

### Tabela comparativa com o guia anterior de configuração de ambiente de desenvolvimento de aprendizado de máquina
Já existe um [guia de configuração de ambiente de desenvolvimento de aprendizado de máquina previamente carregado neste blog](/posts/Setting-up-a-Machine-Learning-Development-Environment) que ainda é válido em sua maioria, mas há algumas mudanças que levaram à criação deste novo post. As diferenças são resumidas na tabela abaixo.

| Diferença | Post Anterior (versão 2021) | Este Post (versão 2024) |
| --- | --- | --- |
| Distribuição Linux | Baseado no Ubuntu | Aplicável a outras distribuições além do Ubuntu,<br> como Fedora/RHEL/Centos, Debian, openSUSE/SLES |
| Método de construção do<br> ambiente de desenvolvimento | Ambiente virtual Python usando venv | Ambiente baseado em contêiner Docker usando<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Instalação do driver gráfico NVIDIA | O | O |
| Instalação direta de CUDA e cuDNN<br> no sistema host | O (usando o gerenciador de pacotes Apt) | X (Usa imagens pré-instaladas fornecidas pela NVIDIA<br> no [Docker Hub](https://hub.docker.com/r/nvidia/cuda), então não é necessário trabalho direto) |
| Portabilidade | Precisa reconstruir o ambiente de<br> desenvolvimento cada vez que muda<br> para um novo sistema | Baseado em Docker, então é fácil construir uma nova<br> imagem com o Dockerfile criado quando necessário<br> ou portar uma imagem existente (excluindo configurações<br> adicionais de volume ou rede) |
| Utilização de bibliotecas de<br> aceleração GPU adicionais além do cuDNN | X | Introdução de [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interface Jupyter Notebook | Jupyter Notebook (clássico) | JupyterLab (Próxima Geração) |
| Configuração do servidor SSH | Não abordado separadamente | Inclui configuração básica do servidor SSH na Parte 3 |

Se você deseja usar um ambiente virtual Python como venv em vez do Docker, o [post anterior](/posts/Setting-up-a-Machine-Learning-Development-Environment) ainda é válido, então recomendo consultá-lo.

## 0. Pré-requisitos
- [O NVIDIA Container Toolkit pode ser usado em distribuições Linux que suportam os gerenciadores de pacotes Apt, Yum ou Dnf, Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Você pode verificar a lista de distribuições Linux suportadas na página linkada, e embora não esteja listado separadamente na tabela de suporte oficial, o Fedora também pode ser usado sem problemas, pois é baseado no Red Hat Linux como o RHEL. Se você não está familiarizado com o ambiente Linux e não tem certeza de qual distribuição usar, usar a versão LTS do Ubuntu é a opção mais segura. Ela é relativamente conveniente para iniciantes, pois drivers proprietários também são instalados automaticamente, e como tem muitos usuários, a maioria da documentação técnica é escrita com base no Ubuntu.
  - Você pode verificar a arquitetura do sistema e a versão da distribuição Linux que está usando com o comando `uname -m && cat /etc/*release` no terminal.
- Primeiro, você deve verificar se a placa gráfica instalada no seu sistema suporta as versões de CUDA e cuDNN que você pretende usar.
  - Você pode verificar o nome do modelo da GPU instalada no seu computador atual com o comando `lspci | grep -i nvidia` no terminal.
  - Na página <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>, verifique a **versão do driver gráfico NVIDIA suportada** por versão do cuDNN, a condição de **CUDA Compute Capability** requerida e a lista de **hardware NVIDIA suportado**.
  - Encontre o nome do modelo correspondente na lista de GPUs em <https://developer.nvidia.com/cuda-gpus> e verifique o valor de **Compute Capability**. Este valor deve atender à condição de **CUDA Compute Capability** verificada anteriormente para usar CUDA e cuDNN sem problemas.

> Se você planeja comprar uma nova placa gráfica para trabalhos de Deep Learning, os critérios de seleção de GPU estão bem resumidos no seguinte artigo. É um artigo que o autor atualiza continuamente.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> O artigo [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) escrito pela mesma pessoa também é muito útil.
{: .prompt-tip }

Se todos os requisitos mencionados acima forem atendidos, vamos começar a configurar o ambiente de trabalho.

## 1. Instalação do Driver Gráfico NVIDIA
Primeiro, você precisa instalar o driver gráfico NVIDIA no sistema host. Você pode baixar e usar o instalador .run da [página de download de drivers NVIDIA](https://www.nvidia.com/drivers/), mas é melhor usar o gerenciador de pacotes do seu sistema para instalação, se possível, para facilitar o gerenciamento de versões e manutenção. Consulte a documentação oficial <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> e instale o driver gráfico apropriado para o seu ambiente de sistema.

### Módulo proprietário vs Módulo de código aberto
O driver Linux NVIDIA consiste em vários módulos de kernel, e a partir do driver versão 515 e lançamentos posteriores, a NVIDIA fornece dois tipos de módulos de kernel de driver:

- Proprietário: O driver de software proprietário que a NVIDIA tem fornecido tradicionalmente.
- Código aberto: Driver de código aberto fornecido sob licença dupla MIT/GPLv2. O código-fonte é disponibilizado através de <https://github.com/NVIDIA/open-gpu-kernel-modules>.

O driver proprietário é fornecido para GPUs baseadas em arquiteturas desde Maxwell até antes de Blackwell, e será descontinuado a partir da arquitetura Blackwell.
Por outro lado, o driver de código aberto é suportado para arquiteturas Turing e posteriores.

[A NVIDIA recomenda usar o módulo de kernel de código aberto quando possível.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
Você pode verificar se sua GPU é compatível com o driver de código aberto [neste link](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

Este artigo assume a instalação do driver de código aberto.

### Debian & Ubuntu
Para Ubuntu ou Debian, digite o seguinte comando no terminal para instalar:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Com base no Fedora 40, introduzimos um método para baixar e instalar pacotes pré-construídos fornecidos pelo [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuração do repositório RPM Fusion  
Siga o [guia oficial do RPM Fusion](https://rpmfusion.org/Configuration).  
Execute o seguinte comando no terminal:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Instalação do pacote akmod-nvidia-open  
Consulte o [guia de instalação do driver NVIDIA fornecido pelo RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), 
ative o repositório rpmfusion-nonfree-tainted e então instale o pacote akmod-nvidia-open.
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Registro de chave para carregamento normal do driver durante o boot seguro (Secure Boot)  

> Com apenas alguns procedimentos adicionais explicados abaixo, você pode usar normalmente o driver gráfico NVIDIA enquanto utiliza a função de boot seguro, e como a segurança do sistema fica consideravelmente vulnerável quando o boot seguro é desativado, recomenda-se não desativá-lo. Pelo menos desde o início da década de 2020, não há quase nenhuma razão para desativar o boot seguro.
{: .prompt-danger }

Primeiro, instale as seguintes ferramentas:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Em seguida, execute o comando abaixo para gerar uma chave:
```bash
sudo kmodgenca -a
```
Agora, você precisa registrar a chave gerada no MOK do firmware UEFI.
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Quando você executar o comando acima, será solicitado que você insira uma senha para o registro da chave. Esta é uma senha de uso único que você usará para concluir o procedimento de registro da chave quando reiniciar em breve, então insira algo que possa lembrar facilmente.

Agora, execute o seguinte comando para reiniciar o sistema:
```bash
systemctl reboot
```
Enquanto o sistema estiver inicializando, a janela de gerenciamento MOK aparecerá automaticamente. Selecione "Enroll MOK" e então selecione "Continue" e "Yes" em sequência, e uma janela solicitando a senha que você definiu anteriormente aparecerá. Depois de inserir a senha que você definiu anteriormente, o procedimento de registro da chave será concluído. Agora, digite reboot para reiniciar novamente e o driver NVIDIA será carregado normalmente.

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
Agora você precisa instalar o [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Siga a instalação consultando o [guia oficial de instalação do NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), mas no caso do Fedora, há pontos a serem observados durante o processo de instalação, então verifique o conteúdo desta seção até o final antes de prosseguir.

### Para quem usa Apt (Ubuntu, Debian, etc.)
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

### Para quem usa Yum ou Dnf (Fedora, RHEL, Centos, etc.)
> Ao testar no Fedora 40, diferentemente do Ubuntu, o comando `nvidia-smi` e o pacote `nvidia-persistenced` não estavam incluídos por padrão no driver gráfico NVIDIA, então foi necessário instalar adicionalmente o pacote `xorg-x11-drv-nvidia-cuda`. Não testei diretamente no RHEL e Centos, mas como a configuração do sistema é muito semelhante ao Fedora, se você encontrar problemas ao seguir o guia abaixo, tentar o mesmo método pode ser útil.
{: .prompt-warning }

> No Fedora 40, após instalar `xorg-x11-drv-nvidia-cuda` conforme o método acima e executar uma carga de trabalho de amostra para teste, funcionou normalmente no sistema do autor. Se você ainda encontrar problemas devido a SELinux ou outras razões, o [pacote nvidia-container-toolkit específico para Fedora e guia](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) fornecido pelo grupo AI-ML do Fedora pode ser útil.
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

### Para quem usa Zypper (openSUSE, SLES)
#### 2-Zypper-1. Configuração do repositório para download de pacotes
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalação do pacote
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalação do Mecanismo de Contêiner
Em seguida, instale o Docker CE ou Podman como mecanismo de contêiner. Você pode escolher um dos dois para instalar de acordo com seu ambiente de uso e preferência, consultando a [documentação oficial do Docker](https://docs.docker.com/engine/install/) e a [documentação oficial do Podman](https://podman.io/docs/installation).

A tabela a seguir resume as principais diferenças e vantagens/desvantagens entre Docker e Podman.

| Item de Comparação | Docker | Podman |
| --- | --- | --- |
| Arquitetura | Modelo cliente-servidor, baseado em daemon | Estrutura sem daemon (daemonless) |
| Segurança | Potencial risco de segurança devido à dependência<br> de um daemon executado com privilégios root por padrão<br>(Suporta modo rootless desde a versão 20.10<br> lançada em 2020, mas requer configuração adicional) | Não depende de daemon, opera em rootless por <br>padrão a menos que especificado de outra forma, e é<br> protegido pelo SELinux |
| Uso de recursos | Geralmente usa mais recursos devido à natureza<br> da estrutura baseada em daemon, com processos<br> em segundo plano sempre em execução | Geralmente menor overhead de recursos |
| Tempo de inicialização<br> do contêiner | Relativamente mais lento | Executa até 50% mais rápido devido à<br> arquitetura simplificada |
| Ecossistema e<br> documentação | Amplo ecossistema e suporte da comunidade,<br> documentação abundante | Ecossistema e documentação relacionada<br> relativamente menores |
| Rede | Usa Docker Bridge Network | Usa plugins CNI (Container Network Interface) |
| Suporte nativo a<br> Kubernetes YAML | X (requer conversão) | O |

Referências:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

A maior vantagem do Docker é que, como tem uma história mais longa e tem desfrutado de um status de padrão de facto na indústria, existe um ecossistema amplo e documentação abundante relacionada.  
O Podman foi desenvolvido relativamente recentemente pela Red Hat e, como é uma estrutura avançada que visa nativamente ser sem daemon (daemonless) e sem root (rootless), tem vantagens em vários aspectos, como segurança, uso de recursos do sistema e tempo de inicialização do contêiner. Outra vantagem do Podman é que, diferentemente do Docker, onde todos os contêineres caem juntos se houver um problema com o daemon e ele cair, cada contêiner é completamente independente, então a queda de um contêiner específico não afeta outros contêineres.

O mais importante é escolher a ferramenta que se adapta às suas condições dadas, e para um usuário individual que está começando, começar com o Podman pode ser uma boa escolha. Embora o tamanho do ecossistema seja relativamente menor em comparação com o Docker, está crescendo rapidamente e reduzindo a lacuna devido às várias vantagens mencionadas acima, e como é compatível com a sintaxe do Dockerfile, imagens Docker, CLI (interface de linha de comando) e muitos outros aspectos do Docker existente, não deve ser um problema para indivíduos ou pequenos grupos.

### Podman
Pode ser instalado facilmente, pois é suportado nos repositórios padrão do sistema da maioria das principais distribuições Linux.

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
##### 3-Ubuntu-1. Remoção de versões anteriores ou pacotes não oficiais para evitar conflitos de pacotes
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configuração do repositório
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

##### 3-Ubuntu-3. Instalação do pacote
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Criação do grupo `Docker` e registro do usuário
Para permitir que usuários não-root gerenciem o Docker sem `sudo`, você pode criar um grupo `Docker` e registrar o usuário que deseja usar o Docker. Execute os seguintes comandos no terminal:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Depois disso, faça logout e login novamente para aplicar as configurações alteradas. No caso do Ubuntu ou Debian, o serviço Docker será executado automaticamente a cada inicialização do sistema sem nenhum trabalho adicional.

#### Para Fedora
##### 3-Fedora-1. Remoção de versões anteriores ou pacotes não oficiais para evitar conflitos de pacotes
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

##### 3-Fedora-2. Configuração do repositório
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Instalação do pacote
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Durante o processo de instalação do pacote, você será notificado para aprovar a chave GPG. Se a chave GPG corresponder a `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, digite y para aprovar.  
> Se a chave GPG não corresponder, você deve interromper a instalação, pois pode ter baixado um pacote falsificado devido a um ataque à cadeia de suprimentos.
{: .prompt-danger }

##### 3-Fedora-4. Iniciar o daemon Docker
Agora o Docker está instalado, mas não está em execução, então você pode iniciar o Docker digitando o seguinte comando:
```bash
sudo systemctl start docker
```
Para fazer com que o serviço Docker seja executado automaticamente na inicialização do sistema, execute o seguinte comando:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Registrar o usuário no grupo `Docker`
Para permitir que usuários não-root gerenciem o Docker, registre o usuário que deseja usar o Docker no grupo `Docker`. No caso do Fedora, o grupo `Docker` é criado automaticamente durante o processo de instalação do pacote anterior, então você só precisa registrar o usuário.
```bash
sudo usermod -aG docker $USER
```
Depois disso, faça logout e login novamente para aplicar as configurações alteradas.

#### Verificar se foi configurado corretamente
Execute o seguinte comando no terminal:
```bash
docker run hello-world
```
Se a seguinte mensagem for exibida, foi bem-sucedido:

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
