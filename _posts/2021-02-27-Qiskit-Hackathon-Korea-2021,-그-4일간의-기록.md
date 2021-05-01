---
title: "Qiskit Hackathon Korea 2021, 그 4일간의 기록"
categories:
  - Quantum Computing
tags:
  - Machine learning
  - Deep learning
  - Qiskit
use_math: true
toc: true
toc_sticky: true
---

# 이 글의 목적
최근 2월 16일부터 2월 19일까지 4일간 진행된 [**Qiskit Hackathon Korea 2021**](https://www.hackerearth.com/challenges/hackathon/qiskit-hackathon-korea/)에 "Qiskit과 PyTorch를 이용한 양자 하이브리드 신경망 구현"이라는 주제로 참여할 기회가 있었다. 시간이 오래 지나면 이번 해커톤에 대한 기억이 희미해질 것 같아, 좀 두서없는 글이라도 참가 동기부터 4일간의 활동, 그리고 해커톤이 끝난 후에 얻은 교훈과 느낀 점까지 가능한 많은 세부사항을 기록해 두기로 결심하였다. 이 글은 **Qiskit Hackathon Korea 2021**에서 4일간 경험한 것들에 대한 기록이다.

# 팀 & 프로젝트 소개
글을 시작하기에 앞서 프로젝트 소개를 하고자 한다.
- 팀명: **Quanputing**
- 프로젝트 주제: *Exploring Hybrid quantum-classical Neural Networks with PyTorch and Qiskit*
- 프로젝트 아이디어:
  > While examining Qiskit and Tensorflow Quantum tutorial documents about *hybrid ML*, we found something interesting. In **Qiskit** tutorial documents, classical convolution layers are combined with quantum fully-connected layers. In the **Tensorflow Quantum** tutorial, on the other hand, quantum convolution layers are combined with classical fully-connected layers. Then one question arises: where is it better to apply the quantum layer?
  > 
  > In this project, we will do the following:
  > 1. Build MNIST multi-label classifiers using classical convolution layers and quantum fully-connected layers.
  > 2. Build MNIST multi-label classifiers using quantum convolution layers and classical fully-connected layers.
  > 3. Compare the performance of these two models.
- 팀 리포지터리: <https://github.com/yh08037/quantum-neural-network>
- 팀 HackerEarth 페이지: <https://www.hackerearth.com/challenges/hackathon/qiskit-hackathon-korea/dashboard/648082e/>
- 해커톤 결과: **Community Choice Award** 수상

# pre. 해커톤 참가 동기
## pre-1. Quantum Computing KR 페이스북 그룹
작년 7월 말쯤에 [Quantum Computing KR](https://www.facebook.com/groups/QuantumComputingKR)이라는 페이스북 그룹에 가입하게 되었다. 나는 페이스북을 주로 그룹을 통한 정보 습득 목적으로 사용하는데, 그날도 양자컴퓨팅 관련 정보를 찾다가 이 그룹을 발견했다. 그리고 1월 말에 신소영 님께서 그룹에 Qiskit Hackathon Korea 소개글을 올려 주셔서 처음 이 대회를 알게 되었다.

## pre-2. 해커톤 등록, 기대 반 걱정 반
처음 해커톤 소개글을 봤을 때는 좀 많이 망설였다. 사실 나는 이번 해커톤을 통해 처음 양자컴퓨팅에 입문하였기 때문에, 그 전까지는 양자컴퓨팅 관련 코딩 경험이 전무한 상태였다(사실 Qiskit이라는 게 있는 줄도 이번에 처음 알았다...). 하지만 신소영 님께서 양자컴퓨터 초보자를 위한 교육 세션이 준비되어 있다고 하셨기 때문에, 일단 쉬운 프로젝트라도 무작정 덤벼들어 보자는 마음으로 참가를 결심하였다(결과적으로 탁월한 선택이었다!). 다행히 페이스북 그룹 내 반응을 살펴보니 양자컴퓨팅 입문자가 나만은 아닌 것 같아 위안이 많이 되었다.

## pre-3. 입문자용 강의 & 사전 행사
Quantum Computing KR 그룹 내에 계신 경북대학교 배준현 교수님께서 정말 감사하게도 입문자용 강의 영상들을 유튜브에 올려주셨다. 해커톤 사전행사에서 제공해주신 강연 역시 유튜브 라이브 방송으로 업로드되어 있다.  
[주니온TV 아무거나연구소 - 어서와! 양자컴퓨팅은 처음이지?](https://youtube.com/playlist?list=PLHqxB9kMLLaMS6F5RSA973qptBlFsk5RE)

## pre-4. IBM Quantum Experience
[IBM Quantum Experience](https://quantum-computing.ibm.com/)는 IBM Quantum에서 제공하는 클라우드 양자컴퓨팅 플랫폼이다.
![IBM Quantum Experience](/assets/img/Qiskit-Hackathon-Korea-2021,-그-4일간의-기록/IBM_Quantum_Experience.png)
현재 총 20개의 양자컴퓨터 시스템(12개는 IBM Q Network 회원 전용 프리미엄 서비스, 8개는 무료 이용 가능)과 5개의 시뮬레이터를 제공한다.
![IBM Quantum services](/assets/img/Qiskit-Hackathon-Korea-2021,-그-4일간의-기록/IBM_Quantum_services.png)
IBM Quantum Composer을 이용하여 GUI 환경에서 양자 회로를 구성하거나, IBM Quantum Lab을 이용하여 웹 상에서 주피터 노트북으로 작업할 수 있다.
![IBM Quantum Composer](/assets/img/Qiskit-Hackathon-Korea-2021,-그-4일간의-기록/IBM_Quantum_Composer.png)
![IBM Quantum Lab](/assets/img/Qiskit-Hackathon-Korea-2021,-그-4일간의-기록/IBM_Quantum_Lab.png)

# 1. 1~2일차 오리엔테이션 & 특별 강연
첫날과 둘째 날에는 오리엔테이션과 특별 강연들이 준비되어 있었다.

## 1-1. Qiskit 설치
신소영 님께서 Zoom으로 Qiskit 설치 가이드를 제공해 주셨다. Qiskit이 워낙 활발하게 개발 중인 프레임워크이다 보니 버전업 속도도 굉장히 빠른 편이어서, 패키지 버전에 따른 의존성 문제가 많이 발생하는 편이라고 한다. 때문에 Qiskit에서는 데이터 사이언스를 위한 대부분의 파이썬 패키지들이 미리 갖춰져 있는 [Anaconda](https://www.anaconda.com/)를 이용하는 것을 권장하고 있다. 나는 원래는 아나콘다보다 파이썬 내에서 venv를 사용해서 가상환경을 직접 구축하는 쪽을 더 선호하는 편이지만, 공식적으로 아나콘다를 강하게 권장하는 데는 다 이유가 있을 테니 이번에는 아나콘다를 사용하여 진행하였다. 

리눅스 기준으로, [Anaconda 리눅스 설치 가이드](https://docs.anaconda.com/anaconda/install/linux/)대로 따라하면서 아나콘다를 설치하되 도중에 ```Do you wish the installer to initialize Anaconda3 by running conda init?```라고 묻는 단계에서 ```yes```를 입력하기만 하면 보통은 별다른 문제 없이 잘 동작한다. 아나콘다 설치 완료 후에는 터미널 창을 닫고 새로 열거나, ```source ~/.bashrc``` 명령을 실행해 준다. 

다음으로 Qiskit을 사용할 가상환경을 하나 생성해줘야 한다. 다음 명령으로 콘다 가상환경 생성 후 활성화해준다.
```
$ conda create --name (환경 이름)
$ conda activate (환경 이름)
```
여기까지 끝났다면 마지막으로 Qiskit을 설치해주면 되는데, 왜인지 잘은 모르지만 신소영 님께서 그냥 터미널에서 pip를 사용해서 설치할 경우 종종 문제가 발생하곤 한다며 주피터 노트북 실행 후 노트북 셀에서 ```!pip install qiskit[visualization]``` 를 실행해 달라고 상당히 강조하셨다. 이것도 다 이유가 있을 테니 말씀하신 대로 주피터 노트북 내에서 설치하였다. 초보자도 따라할 수 있게끔 각 단계별로 친절하게 설명해 주셔서 다행히 별다른 어려움 없이 잘 설치할 수 있었다.

## 1-2. 양자 게이트 & 알고리즘 강의
IBM의 강화정 박사님께서 양자 게이트와 양자컴퓨팅 알고리즘에 관한 양질의 강의를 제공해 주셨다. 오전에는 큐비트를 어떤 형태로 표현하는지와 양자 게이트에 대한 영상을 볼 수 있었다. 오후에는 양자 알고리즘에 관한 강의가 있었으나, 나는 그때 다른 일정이 있어서 아쉽게도 듣지 못했다. 강의자료를 제공해 주셔서 나중에 혼자서라도 공부해 볼 수 있는 점이 그나마 다행이다.

### 1-2-1. 큐비트
영상 내용에 따르면 큐비트의 상태는 **2차원 복소벡터공간상의 단위 벡터**로 표현하며, 이 큐비트 상태는 **unitary operations**, 즉 **양자 게이트(quantum gates)**를 통해 변화한다고 한다. 수식으로 나타내면 다음과 같다.

$$
\displaylines{
|0\rangle := \begin{bmatrix}
1 \\ 0
\end{bmatrix} \neq 0, \quad
|1\rangle := \begin{bmatrix}
0 \\ 1
\end{bmatrix} \neq 1 \\
|\psi〉= \alpha|0〉+ \beta|1〉
= \begin{bmatrix}
\alpha \\ \beta
\end{bmatrix} \\
(\alpha, \beta \in \mathbb{c}, \; |\alpha|^{2} + |\beta|^{2} = 1)
}
$$

### 1-2-2. 유니터리 연산(Unitary Operation)
**유니터리 연산(Unitary Operaion)**이란 2차원 복소벡터공간 안에서의 실수 회전(real rotations)의 일반적인 표현(generalization)이다. 아래와 같은 특성들을 지닌다.
- $U^{†}=U^{-1}, \; UU^{†}=U^{†}U=I$
- 선형적(Linear)
- 역연산 가능(Reversible)
- 상태들 간의 논리적 관계를 보존함

따라서 다음이 성립한다.

$$
\displaylines{
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad
|\phi\rangle = \gamma|0\rangle + \delta|1\rangle \\
\langle\phi|\psi\rangle 
= \begin{bmatrix} 
\gamma^{*} & \delta^{*} 
\end{bmatrix}\begin{bmatrix} 
\alpha \\ \beta 
\end{bmatrix} \\
\langle\phi|U^{†}U|\psi\rangle = \langle\phi|\psi\rangle
}
$$

### 1-2-3. 양자 게이트
양자 게이트의 경우 단일 큐비트 게이트로는 **Pauli-X 게이트**, **Hadamard(H) 게이트**, **Pauli-Z gate** 등이 있고, 2큐비트 게이트로는 **CNOT 게이트**가 대표적이다(물론 이거 말고도 많다). 강의 내용과 [영문 위키피디아](https://en.wikipedia.org/wiki/Quantum_logic_gate)를 참고하여 간략하게 정리해 보았다.

#### Pauli-X 게이트
X 게이트는 고전적인 컴퓨터에서의 NOT 게이트에 해당하는 녀석이다. 기본 상태 \|0〉을 \|1〉로, \|1〉을 \|0〉으로 바꾼다. 다음과 같은 Pauli X 행렬로 표현할 수 있다.

$$
X =
\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix}
$$

#### Hadamard(H) 게이트
Hadamard(H) 게이트는 기본 상태 \|0〉은 $\frac{\|0\rangle + \|1\rangle}{\sqrt{2}}$로, 기본 상태 \|1〉은 $\frac{\|0\rangle- \|1\rangle}{\sqrt{2}}$로 변환하여 \|0〉과 \|1〉이 측정될 확률이 각각 $\frac{1}{2}$로 같은 **중첩(superposition)** 상태를 만들어 주는 역할을 한다. 다음과 같은 Hadamard 행렬로 표현할 수 있다.

$$
H = 
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1\\ 
1 & -1
\end{bmatrix}
$$


#### Pauli-Z 게이트
Z 게이트는 단일 큐비트의 위상을 바꾸는 역할을 한다고 하는데 큐비트의 위상에 관한 부분은 제대로 이해하지 못해서 아무래도 공부가 더 필요할 듯하다. 기본 상태 \|0〉은 그대로 놔두고, 기본 상태 \|1〉은 -\|1〉로 바꾼다고 한다. 역시 다음과 같은 Pauli Z 행렬로 표현할 수 있다.

$$
Z = 
\begin{bmatrix}
1 & 0\\
0 & -1
\end{bmatrix}
$$

#### CNOT 게이트
CNOT 게이트는 2개의 큐비트상에서 동작하며, 큐비트의 입력 값이 \|0〉 또는 \|1〉로 한정될 경우 고전적인 컴퓨터에서의 XOR 게이트와 같은 역할을 한다. 기본 상태 \|00〉, \|01〉, \|10〉, \|11〉에 대하여 다음과 같은 행렬로 표현할 수 있다.

$$
CNOT = CX = 
\begin{bmatrix}
1 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0\\ 
0 & 0 & 0 & 1\\ 
0 & 0 & 1 & 0
\end{bmatrix}
$$

### 1-2-4. 측정
큐비트의 상태를 직접적으로 확인하는 것은 불가능하여 **측정(measurement)**을 통해 큐비트로 부호화된 정보를 읽어와야 하며, 이때 큐비트는 양자역학에 따라 확률적으로 행동하기 때문에 측정을 여러 번 실행하여 0과 1 각각의 값을 측정할 통계적 확률을 구한다고 한다. Qiskit에서는 이 측정 실행 횟수를 ```shots```라는 변수로 지정해 줄 수 있고, 기본값은 1024이다.

### 1-2-5. 위상
**위상(Phase)**의 경우, $\|\psi〉= \alpha\|0〉+\beta\|1〉=\begin{bmatrix} \alpha\\ \beta \end{bmatrix} = \|\alpha\|e^{i\theta_{0}}\|0〉+ \|\beta\|e^{i\theta_{1}}\|1〉$를 $\|\psi〉= e^{i\theta_{0}}(\|\alpha\|\|0〉+ \|\beta\|e^{i\phi}), \phi = \theta_{1}-\theta_{0}$ 꼴로 정리했을 때 $e^{i\theta_{0}}$이 **Global Phase**,  $e^{i\phi}$이 **Relative Phase**에 해당하는 부분이라고 한다. Global Phase는 측정을 통해 감지할 수 없지만 Relative Phase는 감지해낼 수 있다. 아까 Z 게이트도 그렇고 위상에 관한 부분은 내가 제대로 이해를 못 해서 앞으로 더 공부가 필요한 부분이다.

## 1-3. Qiskit 프레임워크의 구성요소별 기능
Qiskit 프레임워크는 크게 4개의 구성요소로 이루어져 있다. 각각 4원소설의 흙, 물, 공기, 불에서 이름을 따 왔다. ~~이름이 제법 멋있다.~~
![Qiskit's elements](/assets/img/Qiskit-Hackathon-Korea-2021,-그-4일간의-기록/Qiskit's_elements.jpeg)
> *이미지 출처: [Qiskit Medium 블로그](https://medium.com/qiskit/qiskit-and-its-fundamental-elements-bcd7ead80492)

### 1-3-1. Qiskit Terra
Qiskit Terra는 양자 회로를 기계어 혹은 그에 가까운 저수준의 코드로 생성할 수 있게 지원한다. 양자 프로세스를 게이트 단위로 설계하고 원격으로 양자컴퓨터에서 시뮬레이션하도록 지원한다. Qiskit Terra를 이용한 모의실험들이 연구논문으로도 많이 발표된다고 한다.

### 1-3-2. Qiskit Aqua
Qiskit Aqua는 사용자들이 직접 양자 프로그래밍을 하지 않고도 이용할 수 있는 도구들을 제공한다. 화학, 인공지능, 최적화 문제, 그리고 금융과 같은 특정 분야에 적용 가능한 응용 프로그램을 제작할 수 있다. 고전적인 코드를 그에 상응하는 양자 알고리즘으로 변환하여 실행해 주는 것으로 보인다.

### 1-3-3. Qiskit Aer
단기적으로는 양자 소프트웨어의 개발은 소형 양자컴퓨터의 에뮬레이션에 상당 부분 의존할 것이다(아직 양자컴퓨터가 널리 보급된 단계는 아니기 때문에 실제 양자컴퓨터를 이용한 실험은 제한적이다). Qiskit Aer는 고전적인 컴퓨터를 이용한 양자컴퓨터 에뮬레이션 및 시뮬레이션을 지원한다. 현재 Qiskit Aer의 Qasm 시뮬레이터는 로컬 머신에서는 최대 30큐비트, IBM Quantum 서버에서는 최대 32큐비트까지 시뮬레이션을 실행할 수 있다. 이번 해커톤에서 우리 팀이 가장 많이 사용한 구성요소이기도 하다.

### 1-3-4. Qiskit Ignis
큐비트는 고전적 비트보다 노이즈에 민감하다는 문제가 있다. 현 시점에서 양자컴퓨터의 오류율은 기존의 고전적 컴퓨터에 비해 매우 높으며, 양자컴퓨터에서 연산 도중 발생하는 양자 오류를 완벽히 억제하는 것은 적어도 가까운 미래에는 불가능할 것으로 보인다. 그렇기 때문에 발생한 양자 오류를 검출하고 보정하는 것은 양자컴퓨터 상용화를 위해 매우 중요한 과제이다. Qiskit Ignis는 근미래의 양자 시스템에서의 양자 오류 연구 및 개선을 위해 설계되었으며, 양자 오류를 검출하고, 회로를 개선하고, 노이즈가 존재하는 환경에서도 연산을 수행할 수 있도록 지원한다.

## 1-4. "Quantum Machine Learning" 강연
둘째 날 오전에는 IBM의 Paul Nation 님의 "Introduction to Quantum Computing", KAIST 이준구 교수님의 "Quantum Machine Learning", IBM의 백한희 님의 "Introduction to Superconducting Qubits", 그리고 IBM Zlatko Minev 님과 Thomas McConkey 님의 "Qiskit Metal Intro & Demonstration" 강연이 있었다.

"Introduction to Superconducting Qubits"와 "Qiskit Metal Intro & Demonstration" 강연은 실제 초전도 큐비트를 물리적으로 구현하는 방법에 관한 강연 같았는데, 상당히 전문적이고 깊이 있는 내용이라 현재 내 수준으로는 이해하기가 어려웠다. 다행히 이준구 교수님이 진행하신 "Quantum Machine Learning" 강연은 나 역시도 내용을 이해할 수 있었기에 간략하게 정리해 보고자 한다(물론 내용 일부는 내가 잘못 이해했을 수도 있다).

### 1-4-1. QML(Quantum Machine Learning, 양자 머신러닝)의 유형
양자컴퓨팅이 적용된 범위에 따라 다음의 3가지로 분류할 수 있다.
- Classical machine learning: 고전적인 머신러닝
- Hybrid quantum machine learning: 고전적인 레이어 + 양자 레이어 혼합 모델
- Fully quantum machine learning: 완전 양자 머신러닝

### 1-4-2. 앞으로 나아가야 할 방향
