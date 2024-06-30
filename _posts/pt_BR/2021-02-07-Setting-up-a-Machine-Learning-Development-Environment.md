---
title: "Configurando um ambiente de desenvolvimento para Machine Learning"
description: >-
  Este artigo aborda como configurar um ambiente de desenvolvimento para estudar machine learning em uma máquina local. Todo o conteúdo foi escrito com base no Ubuntu 20.04 LTS usando uma placa gráfica NVIDIA GeForce RTX 3070.
categories:
  - Data Science  
tags:
  - Machine Learning
  - Deep Learning
toc: true
toc_sticky: true
---

## Visão geral
Este artigo aborda como configurar um ambiente de desenvolvimento para estudar machine learning em uma máquina local. Todo o conteúdo foi escrito com base no Ubuntu 20.04 LTS usando uma placa gráfica NVIDIA GeForce RTX 3070.

- Pilha tecnológica a ser configurada
  - Ubuntu 20.04 LTS
  - Python 3.8
  - pip 21.0.1
  - jupyter
  - matplotlib
  - numpy
  - pandas
  - scipy
  - scikit-learn
  - CUDA 11.0.3
  - cuDNN 8.0.5
  - Frameworks de deep learning (recomenda-se instalar apenas um por ambiente)
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

## 0. Pré-requisitos
- Para estudar machine learning, recomenda-se usar Linux. Embora seja possível no Windows, pode haver muito desperdício de tempo em vários pequenos detalhes. Usar a versão LTS mais recente do Ubuntu é a opção mais segura. Drivers proprietários não open source também são instalados automaticamente para conveniência, e como tem muitos usuários, a maioria da documentação técnica é escrita com base no Ubuntu.
- Geralmente, o Python já vem pré-instalado na maioria das distribuições Linux, incluindo o Ubuntu. No entanto, se o Python não estiver instalado, você deve instalá-lo antes de seguir este guia.
  - Você pode verificar a versão atual do Python instalada com o seguinte comando:
  ```
  $ python3 --version
  ```
  - Se você planeja usar TensorFlow 2 ou PyTorch, deve verificar as versões compatíveis do Python. No momento da escrita deste artigo, [a versão mais recente do PyTorch suporta Python 3.6-3.8](https://pytorch.org/get-started/locally/#linux-python), e [a versão mais recente do TensorFlow 2 suporta Python 3.5-3.8](https://www.tensorflow.org/install).  
  Neste artigo, usaremos Python 3.8.
- Se você planeja estudar machine learning em uma máquina local, é recomendável ter pelo menos uma GPU. Embora o pré-processamento de dados possa ser feito na CPU, a diferença de velocidade de treinamento entre CPU e GPU se torna esmagadora à medida que o modelo cresce (especialmente no caso de deep learning).
  - Para machine learning, há essencialmente apenas uma opção de fabricante de GPU. Você deve usar produtos NVIDIA. A NVIDIA é uma empresa que investiu muito no campo de machine learning, e quase todos os frameworks de machine learning usam a biblioteca CUDA da NVIDIA.
  - Se você planeja usar uma GPU para machine learning, primeiro deve verificar se o modelo da placa gráfica que pretende usar é compatível com CUDA. Você pode verificar o nome do modelo da GPU instalada atualmente no seu computador usando o comando ```nvidia-smi``` no terminal. Encontre o nome do modelo correspondente na lista de GPUs no [link](https://developer.nvidia.com/cuda-gpus) e verifique o valor de **Compute Capability**. Este valor deve ser pelo menos 3.5 para que o CUDA possa ser usado.
  - Os critérios para seleção de GPU estão bem resumidos no seguinte artigo. O autor continua atualizando o artigo.  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) escrito pelo mesmo autor também é muito útil. Para referência, a conclusão do artigo acima é a seguinte:
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

Se você atender a todos os requisitos mencionados acima, vamos começar a configurar o ambiente de trabalho.

## 1. Criando o diretório de trabalho
Abra o terminal e modifique o arquivo .bashrc para registrar a variável de ambiente (o comando vem após o prompt $).  
Primeiro, use o seguinte comando para abrir o editor nano (você pode usar vim ou qualquer outro editor, se preferir):
```
$ nano ~/.bashrc
```
Adicione o seguinte conteúdo na última linha. Você pode alterar o caminho entre aspas duplas para outro local, se desejar.  
```export ML_PATH="$HOME/ml"```

Pressione Ctrl+O para salvar e Ctrl+X para sair.

Agora execute o seguinte comando para aplicar a variável de ambiente:
```
$ source ~/.bashrc
```
Crie o diretório:
```
$ mkdir -p $ML_PATH
```

## 2. Instalando o gerenciador de pacotes pip
Existem várias maneiras de instalar os pacotes Python necessários para machine learning. Você pode usar uma distribuição científica Python como Anaconda (método recomendado para o sistema operacional Windows), ou usar o pip, a ferramenta de empacotamento nativa do Python. Aqui, usaremos o comando pip no shell bash do Linux ou macOS.

Verifique se o pip está instalado no seu sistema com o seguinte comando:
```
$ pip3 --version

Comando 'pip3' não encontrado, mas pode ser instalado com:

sudo apt install python3-pip

```
Se aparecer algo assim, significa que o pip não está instalado no seu sistema. Use o gerenciador de pacotes do sistema (apt neste caso) para instalá-lo (se o número da versão aparecer, significa que já está instalado, então pule este comando):
```
$ sudo apt install python3-pip
```
Agora o pip está instalado no seu sistema.

## 3. Criando um ambiente virtual independente (recomendado)
Para criar um ambiente virtual (para evitar conflitos de versões de bibliotecas com outros projetos), instale o venv:
```
$ sudo apt install python3-venv
```
Em seguida, crie um ambiente Python independente da seguinte forma. Isso é feito para evitar conflitos entre versões de bibliotecas necessárias para diferentes projetos, então você deve criar um novo ambiente virtual sempre que iniciar um novo projeto para manter ambientes independentes.
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(nome do ambiente)
```
Para ativar este ambiente virtual, abra um terminal e digite o seguinte comando:
```
$ cd $ML_PATH
$ source ./(nome do ambiente)/bin/activate
```
Após ativar o ambiente virtual, atualize o pip dentro do ambiente virtual:
```
(env) $ pip install -U pip
```
Para desativar o ambiente virtual posteriormente, use o comando ```deactivate```. Quando o ambiente está ativado, qualquer pacote instalado usando o comando pip será instalado neste ambiente independente e o Python usará esses pacotes.

## 3′. (Se não criar um ambiente virtual) Atualizando a versão do pip
Ao instalar o pip no sistema, você baixa e instala um arquivo binário do servidor espelho da distribuição (Ubuntu neste caso), mas esse arquivo binário geralmente não é atualizado e frequentemente não é a versão mais recente (no meu caso, a versão 20.3.4 foi instalada). Para usar a versão mais recente do pip, execute o seguinte comando para instalar (ou atualizar, se já estiver instalado) o pip no *diretório home do usuário*:  
```
$ python3 -m pip install -U pip

Collecting pip
(omitido)
Successfully installed pip-21.0.1
```
Você pode ver que o pip foi instalado na versão 21.0.1, que é a mais recente no momento da escrita deste artigo. Neste ponto, o pip instalado no diretório home do usuário não é reconhecido automaticamente pelo sistema, então você precisa registrá-lo como uma variável de ambiente PATH para que o sistema possa reconhecê-lo e usá-lo.

Abra novamente o arquivo .bashrc com um editor:
```
$ nano ~/.bashrc
```
Desta vez, procure a linha que começa com ```export PATH=```. Se não houver nenhum caminho escrito depois disso, basta adicionar o conteúdo como fizemos na [etapa 1](#1-criando-o-diretório-de-trabalho). Se já houver outros caminhos registrados, adicione o conteúdo após eles usando dois pontos:  
```export PATH="$HOME/.local/bin"```  
```export PATH="(caminho existente):$HOME/.local/bin"```

[Atualizar o pip do sistema de outra forma que não seja o gerenciador de pacotes do sistema pode causar problemas devido a conflitos de versão](https://github.com/pypa/pip/issues/5599). É por isso que instalamos o pip no diretório home do usuário sem usar ```sudo```. Pela mesma razão, é melhor usar o comando ```python3 -m pip``` em vez de ```pip``` para usar o pip quando não estiver em um ambiente virtual.

## 4. Instalando pacotes para machine learning (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)
Instale todos os pacotes necessários e suas dependências com o seguinte comando pip.  
Se você não estiver usando venv, precisará de privilégios de administrador.  
Além disso, como estou usando venv, usei apenas o comando ```pip```, mas se você não estiver usando venv, recomendo usar o comando ```python3 -m pip``` em vez disso, como mencionado anteriormente.
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(omitido)
```
Se você usou venv, registre um kernel no Jupyter e dê um nome:
```
(env) $ python3 -m ipykernel install --user --name=(nome do kernel)
```
Agora você pode executar o Jupyter com o seguinte comando:
```
(env) $ jupyter notebook
```

## 5. Instalando CUDA & cuDNN
### 5-1. Verificando as versões necessárias de CUDA & cuDNN
Verifique as versões de CUDA suportadas na [documentação oficial do PyTorch](https://pytorch.org/get-started/locally/).  
![Verificando versões de CUDA compatíveis com PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
Com base na versão 1.7.1 do PyTorch, as versões de CUDA suportadas são 9.2, 10.1, 10.2, 11.0. Para GPUs NVIDIA da série 30, é necessário CUDA 11, então sabemos que precisamos da versão 11.0.

Verifique também as versões necessárias de CUDA na [documentação oficial do TensorFlow 2](https://www.tensorflow.org/install/gpu).  
![Verificando versões de CUDA compatíveis com TensorFlow 2](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
Com base na versão 2.4.0 do TensorFlow, confirmamos que precisamos da versão 11.0 do CUDA e da versão 8.0 do cuDNN.

Eu verifiquei as versões de CUDA compatíveis com ambos os pacotes porque às vezes uso PyTorch e às vezes uso TensorFlow 2. Você deve verificar os requisitos do pacote que precisa e ajustar de acordo.

### 5-2. Instalando CUDA
Acesse o [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) e selecione a versão que verificamos anteriormente. Neste artigo, selecionamos [CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive).  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
Agora selecione a plataforma e o tipo de instalador correspondentes e siga as instruções na tela. Neste ponto, [é recomendável usar o gerenciador de pacotes do sistema para o instalador, se possível](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method). Meu método preferido é deb (network).  
![Selecionando plataforma CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-2.png)  
![Instalando CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-3.png)  

Execute os seguintes comandos para instalar o CUDA:
```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
$ sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
$ sudo apt update
$ sudo apt install cuda-toolkit-11-0 cuda-drivers
```
Se você for observador, notará que a última linha é ligeiramente diferente das instruções na imagem. Na instalação via rede, se você digitar apenas cuda como mostrado na imagem, a versão mais recente 11.2 será instalada, o que não é o que queremos. Você pode ver várias opções de meta-pacotes no [guia de instalação do CUDA 11.0 para Linux](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas). Aqui, modificamos a última linha para instalar especificamente o pacote CUDA Toolkit versão