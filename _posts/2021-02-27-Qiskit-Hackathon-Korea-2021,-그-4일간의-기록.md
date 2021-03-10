---
title: "Qiskit Hackathon Korea 2021, 그 4일간의 기록"
categories:
  - Quantum Computing
tags:
  - Machine learning
  - Deep learning
  - Qiskit
use_math: true
---

## 이 글의 목적
최근 2월 16일부터 2월 19일까지 4일간 진행된 [**Qiskit Hackathon Korea 2021**](https://www.hackerearth.com/challenges/hackathon/qiskit-hackathon-korea/)에 "Qiskit과 PyTorch를 이용한 양자 하이브리드 신경망 구현"이라는 주제로 참여할 기회가 있었다. 시간이 오래 지나면 이번 해커톤에 대한 기억이 희미해질 것 같아, 좀 두서없는 글이라도 참가 동기부터 4일간의 활동, 그리고 해커톤이 끝난 후에 얻은 교훈과 소감까지 가능한 많은 세부사항을 기록해 두기로 결심하였다. 이 글은 **Qiskit Hackathon Korea 2021**에서 4일간 경험한 것들에 대한 기록이다.

## 팀 & 프로젝트 소개
글을 시작하기에 앞서 팀 소개를 먼저 해야 할 듯하다.
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

## pre. 해커톤 참가 동기
### pre-1. Quantum Computing KR 페이스북 그룹
작년 7월 말쯤에 [Quantum Computing KR](https://www.facebook.com/groups/QuantumComputingKR)이라는 페이스북 그룹에 가입하게 되었다. 나는 페이스북을 주로 그룹을 통한 정보 습득 목적으로 사용하는데, 그날도 ~~고3인데 하라는 수능공부는 안 하고~~ 양자컴퓨팅 관련 정보를 찾다가 이 그룹을 발견했다. 그리고 1월 말에 신소영 님께서 그룹에 Qiskit Hackathon Korea 소개글을 올려 주셔서 처음 이 대회를 알게 되었다.

### pre-2. 해커톤 등록, 기대 반 걱정 반
처음 해커톤 소개글을 봤을 때는 좀 많이 망설였다. 사실 나는 이번 해커톤을 통해 처음 양자컴퓨팅에 입문하였기 때문에, 그 전까지는 양자컴퓨팅 관련 코딩 경험이 전무한 상태였다(사실 Qiskit이라는 게 있는 줄도 이번에 처음 알았다...). 하지만 신소영 님께서 양자컴퓨터 초보자를 위한 교육 세션이 준비되어 있다고 하셨기 때문에, 일단 쉬운 프로젝트라도 무작정 덤벼들어 보자는 마음으로 참가를 결심하였다(결과적으로 탁월한 선택이었다!). 다행히 페이스북 그룹 내 반응을 살펴보니 양자컴퓨팅 입문자가 나만은 아닌 것 같아 위안이 많이 되었고, 기대도 되기 시작했다.

### pre-3. 입문자용 강의 & 사전 행사
Quantum Computing KR 그룹 내에 계신 경북대학교 배준현 교수님께서 정말 감사하게도 입문자용 강의 영상들을 유튜브에 올려주셨다. 해커톤 사전행사에서 제공해주신 강연 역시 유튜브 라이브 방송으로 업로드되어 있다.  
[주니온TV 아무거나연구소 - 어서와! 양자컴퓨팅은 처음이지?](https://youtube.com/playlist?list=PLHqxB9kMLLaMS6F5RSA973qptBlFsk5RE)

## 1. 1~2일차 오리엔테이션 & 특별 강연
첫날과 둘째 날에는 오리엔테이션과 특별 강연들이 준비되어 있었다.

### 1-1. Qiskit 설치
신소영 님께서 zoom으로 맥과 리눅스 환경에서의 Qiskit 설치 방법을 설명해 주셨다. Qiskit이 워낙 활발하게 개발 중인 프레임워크이다 보니 버전업 속도도 굉장히 빠른 편이어서, 패키지 버전에 따른 의존성 문제가 많이 발생하는 편이라고 한다. 때문에 Qiskit에서는 데이터 사이언스를 위한 대부분의 파이썬 패키지들이 미리 갖춰져 있는 [Anaconda](https://www.anaconda.com/)를 이용하는 것을 권장하고 있다. 나는 원래는 아나콘다보다 파이썬 내에서 venv를 사용해서 가상환경을 직접 구축하는 쪽을 더 선호하는 편이지만, 공식적으로 아나콘다를 강하게 권장하는 데는 다 이유가 있을 테니 이번에는 아나콘다를 사용하여 진행하였다. 

리눅스 기준으로, [Anaconda 리눅스 설치 가이드](https://docs.anaconda.com/anaconda/install/linux/)대로 따라하면서 아나콘다를 설치하되 도중에 “**Do you wish the installer to initialize Anaconda3 by running conda init?**”라고 묻는 단계에서 "**yes**"를 입력하기만 하면 보통은 별다른 문제 없이 잘 동작한다. 아나콘다 설치 완료 후에는 터미널 창을 닫고 새로 열거나, **source ~/.bashrc** 명령을 실행해 준다. 

다음으로 Qiskit을 사용할 가상환경을 하나 생성해줘야 한다. 다음 명령으로 콘다 가상환경 생성 후 활성화해준다.
```
$ conda create --name (환경 이름)
$ conda activate (환경 이름)
```
여기까지 끝났다면 마지막으로 Qiskit을 설치해주면 되는데, 왜인지 잘은 모르지만 신소영 님께서 그냥 터미널에서 pip를 사용해서 설치할 경우 종종 에러가 발생하곤 한다며 주피터 노트북 실행 후 노트북 셀에서 **!pip install qiskit[visualization]** 를 실행해 달라고 상당히 강조하셨다. 마찬가지로 다 이유가 있을 테니 말씀하신 대로 주피터 노트북 내에서 설치하였다. 초보자도 따라할 수 있게끔 각 단계별로 친절하게 설명해 주셔서 다행히 별다른 어려움 없이 잘 설치할 수 있었다.

### 1-2. 양자 게이트 & 알고리즘 강의
IBM의 강화정 박사님께서 양자 게이트와 양자컴퓨팅 알고리즘에 관한 귀중한 강의를 제공해 주셨다. 오전에는 큐비트를 어떤 형태로 표현하는지와 양자 게이트에 대한 영상을 볼 수 있었다.

영상 내용에 따르면 큐비트의 상태는 **2차원 벡터공간상의 단위 벡터**로 표현하며, 이 큐비트 상태는 **unitary operations**, 즉 **양자 게이트(quantum gates)**를 통해 변화한다고 한다(이 **unitary operation**은 대략 복소수 행렬에서의 연산인 것 같기는 한데, 정확히 어떤 의미인지는 아직 이해가 가질 않는다. [위키피디아](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%88%ED%84%B0%EB%A6%AC_%EC%9E%91%EC%9A%A9%EC%86%8C)에 검색해봐도 분명히 한국어이긴 한데 뭔 소리인지 모르겠고... 아마도 선형대수학 개념인 것 같다. 아무튼 갈 길이 멀다.).

양자 게이트의 경우 단일 큐비트 게이트로는 **Pauli-X 게이트**, **Hadamard(H) 게이트**, **Pauli-Z gate**를 소개해 주셨고, 2큐비트 게이트로는 **CNOT 게이트**가 대표적이라고 한다. X 게이트는 고전적인 컴퓨터에서의 NOT 게이트에 해당하는 녀석이고, Hadamard(H) 게이트는 기본 상태 \|0〉은 $\frac{\|0〉+ \|1〉}{\sqrt{2}}$로, 기본 상태 \|1〉은 $\frac{\|0〉- \|1〉}{\sqrt{2}}$로 변환하여 \|0〉과 \|1〉이 측정될 확률이 각각 $\frac{1}{2}$로 같은 **중첩(superposition)** 상태를 만들어 주는 역할을 한다고 한다. Z 게이트는 단일 큐비트의 위상을 바꾸는 역할을 한다고 하는데 이 부분은 제대로 이해하지 못해서 아무래도 공부가 더 필요할 듯하다. CNOT 게이트는 2개의 큐비트상에서 동작하며, 큐비트의 입력 값이 \|0〉 또는 \|1〉로 한정될 경우 고전적인 컴퓨터에서의 XOR 게이트와 같은 역할을 한다.

그리고 큐비트의 상태를 직접적으로 관측하는 것은 불가능하여 **측정(measurement)**을 통해 큐비트로 부호화된 정보를 읽어와야 하며, 이때 큐비트는 양자역학에 따라 확률적으로 행동하기 때문에 측정을 여러 번 실행하여 0과 1 각각의 값을 측정할 통계적 확률을 구한다고 한다. Qiskit에서는 이 측정 실행 횟수를 ```shots```라는 변수로 지정해 줄 수 있고, 기본값은 1024이다.

**위상(Phase)**의 경우, $\|\psi〉= \alpha\|0〉+\beta\|1〉=\begin{bmatrix} \alpha\\ \beta \end{bmatrix} = \|\alpha\|e^{i\theta_{0}}|0〉+ \|\beta\|e^{i\theta_{1}}\|1〉$를 $\psi = e^{i\theta_{0}}(\|\alpha\|\|0〉+ \|\beta\|e^{i\phi}), \phi = \theta_{1}-\theta_{0}$ 꼴로 정리했을 때 $e^{i\theta_{0}}$이 **Global Phase**,  $e^{i\phi}$이 **Relative Phase**에 해당하는 부분이라고 한다. 강의 영상에서 Global Phase는 감지할 수 없지만 Relative Phase는 감지할 수 있다는 말씀을 하셨는데, 아까 Z 게이트도 그렇고 위상에 관한 부분은 내가 제대로 이해를 못 해서 앞으로 더 공부가 필요한 부분이다.