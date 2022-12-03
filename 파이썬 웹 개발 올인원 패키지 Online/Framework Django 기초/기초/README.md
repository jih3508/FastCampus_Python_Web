# 기초

## 프레임워크
- 자주 사용되는 코드를 체계화하여 쉽게 사용할 수 있도록 도와주는 코드 집합
- 라이브러리와 혼동될 수 있지만 좀 더 규모가 크고 프로젝트의 기반이 됨
- 건축에 비유하면 구조를 만드는 골조가 프레임워크라면 그 외 자재들이 라이브러리가 됨

## 웹 프레임워크
- 웹 개발에 필요한 기본적인 구조와 코드(클래스, 함수 등)가 만들어져 있음

## 장고 프로젝트 만들기
### 1. 가상환경 만들기
```
> mkdir 3rd
> pip install --upgrade pip # 관리자 모드 실행
> pip3 install virtualenv # 가상환경 패키지 만들기
> virtualenv fcdjango_venv # 가상환경 만들기
> fcdjango_venv\Scripts\activate // 가상환경 실행
```

### 2. 장고 프로젝트 생성
```
> pip install Django==2.1.7 # 장고 설치 하기
> django-admin startproject fc_community # 프로젝트 생성
> cd fc_community
> django-admin startapp board 
```