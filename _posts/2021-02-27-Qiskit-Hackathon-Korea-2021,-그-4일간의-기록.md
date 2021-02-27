---
title: "Qiskit Hackathon Korea 2021, 그 4일간의 기록"
categories:
  - Quantum Computing
tags:
  - Machine learning
  - Deep learning
  - Qiskit
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
시간을 거슬러 2020년 7월 말(내가 고3이던 시절), [Quantum Computing KR](https://www.facebook.com/groups/QuantumComputingKR)이라는 페이스북 그룹에 가입하게 되었다. 나는 페이스북을 주로 그룹을 통한 정보 습득 목적으로 사용하는데, 그날도 ~~하라는 수능공부는 안 하고~~ 양자컴퓨팅 관련 정보를 찾다가 이 그룹을 발견한 것으로 기억한다. 그리고 시간이 흘러 대입이 끝나고 내가 세상 잉여롭게 지내던 1월 말에, 마침 Qiskit Advocate인 신소영 님께서 올리신 Qiskit Hackathon Korea 소개글을 보게 되었다.

### pre-2. 해커톤 등록, 기대와 걱정
처음 해커톤 소개글을 봤을 때는 좀 많이 망설였다. 사실 나는 이번 해커톤을 통해 처음 양자컴퓨팅에 입문하였기 때문에, 그 전까지는 양자컴퓨팅 관련 코딩 경험이 전무한 상태였다(사실 Qiskit이라는 게 있는 줄도 이번에 처음 알았다...). 하지만 신소영 님께서 양자컴퓨터 초보자를 위한 교육 세션이 준비되어 있다고 하셨기 때문에, 일단 쉬운 프로젝트라도 무작정 덤벼들어 보자는 마음으로 참가를 결심하였다(결과적으로, 탁월한 선택이었다!). 다행히 페이스북 그룹 내 반응을 살펴보니 양자컴퓨팅 입문자가 나만은 아닌 것 같아 위안이 많이 되었고, 해커톤 시작일이 가까워질수록 두려움보다는 새로운 것을 배운다는 기대감이 더 커졌다.

### pre-3. 입문자용 강의 & 사전 행사
Quantum Computing KR 그룹 내에 계신 배준현 교수님께서 정말 감사하게도 입문자용 강의 영상들을 유튜브에 올려주셨다. 해커톤 사전행사에서 제공해주신 강연 역시 유튜브 라이브 방송으로 업로드되어 있다.  
[주니온TV 아무거나연구소 - 어서와! 양자컴퓨팅은 처음이지?](https://youtube.com/playlist?list=PLHqxB9kMLLaMS6F5RSA973qptBlFsk5RE)

## 1. 1~2일차 오리엔테이션 & 특별 강연