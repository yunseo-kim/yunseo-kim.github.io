---
title: "Construindo um ambiente de desenvolvimento de Deep Learning com NVIDIA Container Toolkit e Docker/Podman (1) - Instalação do NVIDIA Container Toolkit e do engine de contêiner"
description: "Esta série mostra como montar localmente um ambiente de desenvolvimento de deep learning baseado em contêineres com o NVIDIA Container Toolkit e como configurá-lo para uso remoto via SSH e JupyterLab. Neste primeiro post, apresento a instalação do NVIDIA Container Toolkit e do engine de contêiner (Docker/Podman)."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Visão geral

Nesta série, instalamos o NVIDIA Container Toolkit e Docker ou Podman e, com base nas imagens CUDA e cuDNN fornecidas pelo [repositório nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) no Docker Hub, escrevemos um Dockerfile para construir um ambiente de desenvolvimento de deep learning. Para quem precisar, compartilho via GitHub e Docker Hub o [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) e a [imagem](https://hub.docker.com/r/yunseokim/dl-env/tags) final produzidos por esse processo, além de fornecer um guia adicional de configuração de SSH e JupyterLab para uso como servidor remoto.  
A série será composta por 3 posts, e este post que você está lendo é o primeiro da série.
- Parte 1: Instalação do NVIDIA Container Toolkit e do engine de contêiner (este post)
- [Parte 2: Configuração do runtime de contêiner para uso de GPU, escrita do Dockerfile e build da imagem de contêiner](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Parte 3 (a ser publicada)

Partimos do pressuposto de um sistema Linux x86_64 com uma GPU NVIDIA que suporte CUDA. Não testei diretamente em distribuições além de Ubuntu ou Fedora, então alguns detalhes podem variar ligeiramente.  
(Revisado em 12026.1.6.)

### Composição do ambiente

- Sistema operacional e arquitetura do host: x86_64, ambiente Linux (Ubuntu 22.04/24.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x etc.)
- Stack a ser montada (linguagens e bibliotecas)
  - [Python 3](https://www.python.org/)
  - [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
  - [Docker Engine](https://docs.docker.com/engine/) / [Podman](https://podman.io/)
  - CUDA 12.4 / 12.8 / 13.0
  - cuDNN 9
  - [OpenSSH](https://www.openssh.com/)
  - [tmux](https://github.com/tmux/tmux/wiki)
  - [JupyterLab](https://jupyter.org/)
  - [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
  - [CuPy](https://cupy.dev/) (opcional, biblioteca de arrays compatível com NumPy/SciPy para computação acelerada por GPU com Python)
  - [pandas](https://pandas.pydata.org/)
  - [cuDF](https://docs.rapids.ai/api/cudf/stable/) (opcional, para acelerar pandas com zero alteração de código usando o acelerador de GPU)
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
  - [cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/) (opcional, para visualizar e filtrar rapidamente grandes datasets com poucas linhas de código, usando bibliotecas de gráficos de alto nível)
  - [DALI](https://developer.nvidia.com/DALI) (opcional, alternativa de alto desempenho aos data loaders e iteradores embutidos usando GPU)
  - [scikit-image](https://scikit-image.org/)
  - [cuCIM](https://docs.rapids.ai/api/cucim/stable/) (opcional, alternativa acelerada para processamento e I/O de imagens n-dimensionais ao scikit-image)
  - [scikit-learn](https://scikit-learn.org/)
  - [XGBoost](https://xgboost.ai/)
  - [cuML](https://docs.rapids.ai/api/cuml/stable/) (opcional, para executar algoritmos de machine learning em GPUs com uma API que segue de perto a API do scikit-learn)
  - [cuVS](https://docs.rapids.ai/api/cuvs/stable/) (opcional, algoritmos otimizados para vizinhos aproximados e clustering, além de outras ferramentas essenciais para busca vetorial acelerada)
  - [RAFT](https://docs.rapids.ai/api/raft/stable/) (opcional, primitivas aceleradas por CUDA usadas por outras bibliotecas RAPIDS)
  - [PyTorch](https://pytorch.org/)
  - [cuGraph](https://docs.rapids.ai/api/cugraph/stable/) (opcional, biblioteca de analytics de grafos acelerada por GPU que inclui um acelerador “zero-code-change” para NetworkX)
  - [tqdm](https://tqdm.github.io/)

  > Dependendo da situação e da sua preferência, você também pode considerar usar a biblioteca de DataFrame [Polars](https://pola.rs/) no lugar de pandas. Ela é escrita em Rust e, [embora perca para a combinação cuDF + pandas no processamento de dados em grande escala, apresenta desempenho excelente quando comparada ao pacote pandas “puro”](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/). Além disso, oferece uma sintaxe mais especializada para queries. De acordo com o [blog oficial do Polars](https://pola.rs/posts/polars-on-gpu/) e a [documentação do cuDF](https://docs.rapids.ai/api/cudf/stable/cudf_polars/), o Polars e a equipe do NVIDIA RAPIDS estão colaborando para oferecer, em open beta, um engine de aceleração por GPU baseado em cuDF, e o desenvolvimento está avançando rapidamente.
  {: .prompt-tip }

  > Se você estiver em dúvida sobre qual usar entre Docker CE e Podman, a [tabela comparativa apresentada mais adiante](#3-instalacao-do-engine-de-conteiner) pode ajudar.
  {: .prompt-tip }

### Tabela comparativa com o guia de ambiente de ML que escrevi anteriormente

Já existe um [guia de configuração de ambiente de desenvolvimento de machine learning publicado anteriormente neste blog](/posts/Setting-up-a-Machine-Learning-Development-Environment), mas escrevi este post novamente porque houve várias mudanças. As diferenças estão resumidas na tabela abaixo.

| Diferença | Post antigo (versão 12021) | Este post (escrito em 12024, revisado em 12026) |
| --- | --- | --- |
| Distribuição Linux | Baseado em Ubuntu | Além de Ubuntu, aplicável também em Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES etc. |
| Método de montagem do ambiente | Instalação direta no host<br>Ambiente virtual Python com venv | Ambiente baseado em contêiner Docker<br> com [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)<br>Ambiente virtual Python e gestão de pacotes com uv |
| Instalação do driver gráfico NVIDIA | O | O |
| Instalação direta de <br>CUDA e cuDNN no host | O (usando o gerenciador Apt) | X ([usa imagens pré-instaladas fornecidas pela NVIDIA<br> no Docker Hub](https://hub.docker.com/r/nvidia/cuda), então não é necessário fazer manualmente) |
| Portabilidade | Ao migrar para outro sistema, era necessário<br> reconstruir o ambiente do zero | Por ser baseado em Docker, é possível<br> construir novas imagens quando necessário a partir do Dockerfile<br> ou migrar facilmente a imagem usada anteriormente<br> (exceto configurações adicionais de volume ou rede) |
| Uso de bibliotecas adicionais <br>de aceleração por GPU além de cuDNN | X | Introdução de [CuPy](https://cupy.dev/), [RAPIDS](https://rapids.ai/), [DALI](https://developer.nvidia.com/DALI) |
| Interface do Jupyter Notebook | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| Configuração de servidor SSH | Não abordado separadamente | Inclui uma configuração básica de servidor SSH |

## 0. Verificações prévias

- [O NVIDIA Container Toolkit pode ser usado em distribuições Linux que suportem os gerenciadores de pacotes Apt, Yum ou Dnf, e Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Na página linkada, você pode conferir a lista de distribuições suportadas. Embora não esteja explicitamente listado na tabela oficial de suporte, o Fedora também é baseado em Red Hat Linux (como o RHEL), então pode ser usado sem problemas. Se você não tem familiaridade com Linux e não sabe qual distribuição usar, a opção mais segura é usar o Ubuntu LTS. Drivers proprietários (não open source) também costumam ser instalados automaticamente, o que é relativamente conveniente para iniciantes, e como há muitos usuários, a maioria da documentação técnica é escrita com base em Ubuntu.
  - Você pode verificar a arquitetura do sistema e a versão da distribuição Linux em uso executando `uname -m && cat /etc/*release` no terminal.
- Primeiro, é necessário verificar se a GPU instalada no sistema suporta as versões de CUDA e cuDNN que você pretende usar.
  - Você pode verificar o modelo da GPU instalada executando `lspci | grep -i nvidia` no terminal.
  - Na página <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>, confira por versão do cuDNN: a **versão do driver gráfico NVIDIA suportada**, os requisitos de **CUDA Compute Capability** e a lista de **hardware NVIDIA suportado**.
  - Na lista de GPUs em <https://developer.nvidia.com/cuda-gpus>, encontre o modelo correspondente e verifique o valor de **Compute Capability**. Esse valor deve satisfazer o requisito de **CUDA Compute Capability** verificado acima para que CUDA e cuDNN funcionem sem problemas.

> Se você pretende comprar uma nova GPU para deep learning, os critérios de seleção estão bem organizados no post abaixo (o autor atualiza de tempos em tempos):  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> Além da GPU, se você precisar de um guia de configuração de hardware de forma mais ampla, o post [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) do mesmo autor também é muito útil.
{: .prompt-tip }

Se você atende a todos os requisitos citados acima, vamos começar a montar o ambiente.

## 1. Instalação do driver gráfico NVIDIA

Primeiro, é preciso instalar o driver gráfico NVIDIA no host. Você pode baixar e usar o instalador `.run` na [página de download de drivers da NVIDIA](https://www.nvidia.com/drivers/), mas, sempre que possível, é melhor instalar via o gerenciador de pacotes do seu sistema, do ponto de vista de versionamento e manutenção. Consulte a documentação oficial em <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> e instale o driver adequado ao seu ambiente.

### Módulo proprietário vs módulo open source

O driver NVIDIA para Linux é composto por vários módulos de kernel e, a partir do driver versão 515 e releases posteriores, a NVIDIA passou a oferecer dois tipos de módulos de kernel do driver.

- Proprietary: driver proprietário que a NVIDIA vinha fornecendo tradicionalmente.
- Open-source: driver open source sob licença dupla MIT/GPLv2. O código-fonte é publicado em <https://github.com/NVIDIA/open-gpu-kernel-modules>.

O driver Proprietary é fornecido para GPUs projetadas com base em arquiteturas desde Maxwell até antes de Blackwell, e deverá ser descontinuado a partir da arquitetura Blackwell.  
Já o driver Open-source é suportado para Turing e arquiteturas posteriores.

[A NVIDIA recomenda usar os módulos de kernel open source sempre que possível.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
Você pode verificar se a sua GPU é compatível com o driver open source [neste link](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

Neste post, vou assumir a instalação do driver open source.

### Debian & Ubuntu

No Ubuntu ou Debian, execute os comandos abaixo no terminal:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Com base no Fedora 40, apresento o método de baixar e instalar os pacotes pré-compilados fornecidos pelo [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuração do repositório RPM Fusion

Siga o [guia oficial do RPM Fusion](https://rpmfusion.org/Configuration).  
Execute os comandos abaixo no terminal.

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> Em versões antigas do DNF (Fedora 40 e anteriores), a linha de comando para habilitar o repositório da biblioteca openh264 na segunda linha era a seguinte:
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> Porém, a partir do DNF 5 (Fedora 41+), em vez disso é necessário usar:
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> Atualizei o conteúdo do post para refletir isso.
{: .prompt-info }

#### 1-Fedora-2. Instalação do pacote akmod-nvidia

Com base no [guia de instalação do driver NVIDIA fornecido pelo RPM Fusion](https://rpmfusion.org/Howto/NVIDIA), instale o pacote akmod-nvidia.

```bash
sudo dnf update  # se houver atualização de kernel nesta etapa, reinicie no kernel mais recente e continue
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> Da mesma forma, em versões antigas do DNF (Fedora 40 e anteriores), a linha de comando da terceira linha para evitar que o driver NVIDIA fosse removido por autoremove era:
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> Porém, a partir do DNF 5 (Fedora 41+), em vez disso é necessário usar:
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> Atualizei o conteúdo do post para refletir isso.
{: .prompt-info }

> Por outro lado, no passado o RPM Fusion mostrava uma posição negativa em relação aos [módulos de kernel open source da NVIDIA](#modulo-proprietario-vs-modulo-open-source) e, a menos que você especificasse algo, fornecia por padrão o driver Proprietary. No entanto, de acordo com a [diretriz recente do RPM Fusion (alterada em dezembro de 12025)](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), para hardwares com suporte duplicado (arquiteturas de Turing até antes de Blackwell), ele agora selecionará automaticamente a melhor opção entre as duas e, portanto, não seria necessário escolher manualmente. Para arquiteturas antigas anteriores a Turing, e para arquiteturas mais recentes como Blackwell e posteriores, já existia apenas uma opção desde antes, então não há mudanças.
> Com isso, confirmei que foi removido o conteúdo sobre especificar a opção de uso do módulo open source via `/etc/rpm/macros.nvidia-kmod`.
>
> Além disso, no caso do pacote `akmod-nvidia-open`, é recomendado não usá-lo, a menos que você precise aplicar diretamente alterações downstream no driver em kernel space.
>
> Também incorporei esses pontos ao post.
{: .prompt-info }

#### 1-Fedora-3. Registro de chave para carregar corretamente o driver com Secure Boot habilitado

> Com apenas alguns passos adicionais como descrito abaixo, é possível usar normalmente o driver gráfico NVIDIA mantendo o Secure Boot ativado. Como desativar o Secure Boot torna o sistema significativamente mais vulnerável, recomendo não desativá-lo. Pelo menos desde que entramos nos anos 12020, dificilmente há motivo para desativar o Secure Boot.
{: .prompt-danger }

Primeiro, instale as ferramentas abaixo.

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Em seguida, gere a chave executando:

```bash
sudo kmodgenca -a
```

Agora é necessário registrar a chave gerada no MOK do firmware UEFI.

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

Ao executar esse comando, será solicitado que você digite uma senha para registro da chave. Em breve você reiniciará o sistema para concluir o processo; essa senha será usada apenas uma vez nesse momento, então digite algo que consiga lembrar.

Agora reinicie o sistema:

```bash
systemctl reboot
```

Durante a inicialização, a tela de gerenciamento do MOK aparecerá automaticamente. Selecione “Enroll MOK” e então escolha “Continue” e “Yes” em seguida; aparecerá uma tela solicitando a senha que você definiu há pouco. Após inserir a senha, o registro da chave será concluído. Agora, ao digitar reboot para inicializar novamente, o driver NVIDIA deverá ser carregado corretamente.

### Verificando a instalação do driver NVIDIA

No terminal, você pode verificar os módulos de kernel NVIDIA atualmente carregados com:

```bash
cat /proc/driver/nvidia/version
```

Se uma mensagem semelhante à seguinte aparecer, a instalação foi bem-sucedida.

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

Além disso, o driver gráfico open source **nouveau** (módulo de kernel), que em muitos casos é adotado por padrão no Linux, deve ficar desativado após instalar o driver NVIDIA; caso contrário, pode causar problemas. Após instalar o driver NVIDIA e reiniciar, ao executar o comando abaixo não deve haver saída alguma.

```bash
lsmod |grep nouveau
```

## 2. Instalação do NVIDIA Container Toolkit

Agora é necessário instalar o [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Siga o [guia oficial de instalação do NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), mas, no caso do Fedora, há pontos de atenção durante a instalação; portanto, leia esta seção até o fim antes de prosseguir.

### Caso use Apt (Ubuntu, Debian etc.)

#### 2-Apt-1. Configurar o repositório para download dos pacotes

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Atualizar a lista de pacotes

```bash
sudo apt update
```

#### 2-Apt-3. Instalar os pacotes

```bash
sudo apt install nvidia-container-toolkit
```

### Caso use Yum ou Dnf (Fedora, RHEL, Centos etc.)

> Ao testar no Fedora 40, diferentemente do Ubuntu, o comando `nvidia-smi` e o pacote `nvidia-persistenced` não vinham incluídos por padrão no driver gráfico NVIDIA, então foi necessário instalar adicionalmente o pacote `xorg-x11-drv-nvidia-cuda`. Não testei diretamente em RHEL e Centos, mas como a composição do sistema é bastante semelhante à do Fedora, se ocorrer algum problema ao seguir o guia abaixo, pode ser útil tentar o mesmo método.
{: .prompt-warning }

> Ao instalar `xorg-x11-drv-nvidia-cuda` pelo método acima no Fedora 40 e executar um workload de exemplo para testar, no meu sistema funcionou corretamente. Se ainda houver problemas por motivos como SELinux etc., o [pacote e guia específicos para Fedora do nvidia-container-toolkit](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) fornecidos pelo grupo AI-ML do Fedora também podem ajudar.
{: .prompt-tip }

#### 2-Dnf-1. Configurar o repositório para download dos pacotes

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Instalar os pacotes

```bash
sudo dnf install nvidia-container-toolkit
```

Ou

```bash
sudo yum install nvidia-container-toolkit
```

### Caso use Zypper (openSUSE, SLES)

#### 2-Zypper-1. Configurar o repositório para download dos pacotes

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalar os pacotes

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalação do engine de contêiner

Em seguida, instale Docker CE ou Podman como engine de contêiner. Você pode escolher um dos dois conforme seu ambiente e preferência; consulte a [documentação oficial do Docker](https://docs.docker.com/engine/install/) e a [documentação oficial do Podman](https://podman.io/docs/installation).

A tabela abaixo resume as principais diferenças e prós/contras do Docker e do Podman.

| Item de comparação | Docker | Podman |
| --- | --- | --- |
| Arquitetura | Modelo cliente-servidor, baseado em daemon | Estrutura daemonless |
| Segurança | Depende de um daemon que roda com privilégios root <br>por padrão, então há risco potencial de segurança<br>(a partir da versão 20.10 lançada em 12020, suporta<br> modo rootless, mas requer configuração adicional) | Não depende de daemon e, a menos que você especifique<br> o contrário, funciona em modo rootless por padrão,<br> protegido por SELinux |
| Uso de recursos | Por ser baseado em daemon, há um processo em<br> segundo plano rodando continuamente; em geral,<br> consome mais recursos | Em geral, menor overhead |
| Tempo de inicialização do contêiner | Relativamente mais lento | Arquitetura simplificada: até ~50%<br> mais rápido |
| Ecossistema e documentação | Ecossistema amplo e suporte de comunidade,<br> muita documentação | Ecossistema menor e menos documentação |
| Networking | Usa Docker Bridge Network | Usa plugins CNI (Container Network Interface) |
| Suporte nativo a<br> Kubernetes YAML | X (precisa converter) | O |

Referências:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

O Docker tem uma história mais longa e foi, na prática, o padrão de fato da indústria, então seu maior ponto forte é a existência de um ecossistema amplo e muita documentação relacionada.  
O Podman foi desenvolvido mais recentemente pela Red Hat e, por ter uma estrutura mais moderna que prioriza daemonless e rootless desde a origem, tem vantagens em vários aspectos, como segurança, uso de recursos do sistema e tempo de inicialização do contêiner. Outra vantagem do Podman é que, ao contrário do Docker (onde se o daemon cai todos os contêineres caem junto), cada contêiner é totalmente independente, então a queda de um contêiner específico não afeta os demais.

O mais importante é escolher a ferramenta adequada às suas condições e necessidades; no entanto, para quem está começando, parece uma boa escolha iniciar com Podman. Embora o ecossistema seja menor do que o do Docker, graças às vantagens mencionadas ele cresce rapidamente e vem reduzindo a diferença; além disso, é compatível com muitos aspectos do Docker, como a sintaxe de Dockerfile, imagens Docker e a CLI (interface de linha de comando). A menos que você já tenha um sistema de grande escala baseado em Docker e a adoção do Podman implique um alto custo de migração, é mais racional adotar Podman desde o início.

### Podman

Como a maioria das principais distribuições Linux oferece suporte via repositórios padrão do sistema, a instalação é simples.

#### No Ubuntu

```bash
sudo apt install podman
```

#### No Fedora

```bash
sudo dnf install podman
```

#### No openSUSE

```bash
sudo zypper install podman
```

#### Verificando se está configurado corretamente

Execute o comando abaixo no terminal:

```bash
podman run --rm hello-world
```

Se aparecer uma mensagem como a seguir, deu certo.

```bash
!... Hello Podman World ...!

         .--"--.           
       / -     - \         
      / (O)   (O) \        
   ~~~| -=(,Y,)=- |         
    .---. /`  \   |~~      
 ~/  o  o \~~~~.----. ~~   
  | =(X)= |~  / (O (O) \   
   ~~~~~~~  ~| =(Y_)=-  |   
  ~~~~    ~~~|   U      |~~ 

Project:   https://github.com/containers/podman
Website:   https://podman.io
Desktop:   https://podman-desktop.io
Documents: https://docs.podman.io
YouTube:   https://youtube.com/@Podman
X/Twitter: @Podman_io
Mastodon:  @Podman_io@fosstodon.org
```

> Ao testar em 12025-12-18T00:43:00+09:00 com podman versão 5.7.1, [passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64`, em ambiente Fedora 43, ao executar o hello-world acima e também ao rodar contêineres ou fazer build de imagens, ocorreu o seguinte erro:
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> Apesar de eu não usar IPv6 e estar em uma rede IPv4, o problema parece ocorrer porque, na etapa de configuração de rede do contêiner, o pasta (incluído na biblioteca passt) tenta configurar roteamento IPv6. Confirmei que, ao especificar explicitamente `--net=pasta:-4` para forçar IPv4, como abaixo, o problema não ocorre durante a execução do contêiner ou na [etapa de build da imagem descrita mais adiante](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-construindo-a-imagem-docker-e-executando-o-conteiner).
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> Pesquisando, encontrei [um issue registrado anteriormente com o mesmo sintoma](https://github.com/containers/podman/issues/22824). O issue teria sido corrigido em [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/), mas como o sintoma observado é idêntico e vários detalhes (como o fato de ter ocorrido usando Proton VPN) são muito parecidos, suspeito que um problema semelhante tenha reaparecido.
{: .prompt-warning }

### Docker CE

#### No Ubuntu

##### 3-Ubuntu-1. Remover versões antigas ou pacotes não oficiais para evitar conflitos

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configurar o repositório

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

##### 3-Ubuntu-3. Instalar os pacotes

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Criar o grupo `Docker` e registrar o usuário

Para permitir que usuários non-root gerenciem Docker sem `sudo`, crie o grupo `Docker` e adicione o usuário que vai usar Docker. Execute:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Depois disso, faça logout e login novamente para aplicar a configuração. No Ubuntu ou Debian, sem ações adicionais, o serviço do Docker inicia automaticamente a cada boot do sistema.

#### No Fedora

##### 3-Fedora-1. Remover versões antigas ou pacotes não oficiais para evitar conflitos

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

##### 3-Fedora-2. Configurar o repositório

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Instalar os pacotes

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Durante a instalação, aparecerá um prompt perguntando se você deseja aprovar a chave GPG. Se a chave GPG corresponder a `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, digite `y` para aprovar.  
> Se a chave GPG não corresponder, pode ser que você tenha baixado um pacote falsificado por um ataque à cadeia de suprimentos; nesse caso, você deve interromper a instalação.
{: .prompt-danger }

##### 3-Fedora-4. Iniciar o daemon do Docker

Agora o Docker está instalado, mas ainda não está em execução. Para iniciá-lo:

```bash
sudo systemctl start docker
```

Para iniciar automaticamente o serviço do Docker no boot do sistema:

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Registrar o usuário no grupo `Docker`

Para permitir que usuários non-root gerenciem Docker, registre o usuário que vai usar Docker no grupo `Docker`. No Fedora, o grupo `Docker` é criado automaticamente durante a instalação; portanto, basta registrar o usuário.

```bash
sudo usermod -aG docker $USER
```

Depois disso, faça logout e login novamente para aplicar a configuração.

#### Verificando se está configurado corretamente

Execute o comando abaixo no terminal:

```bash
docker run hello-world
```

Se a saída for semelhante à abaixo, deu certo.

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

## Leitura adicional
Continua na [Parte 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
