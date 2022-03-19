Scribble Segmentation
==============================

modified from [ScribbleSup](https://github.com/meng-tang/rloss)

edited by Bae-SeungHo



### 0. Before Start
----------

1. venv 를 통해 rloss 폴더 내의 'v-env' 이름의 가상환경을 생성하고 activate 해 주세요.

```cmd
ppython3 -m venv rloss/v-env
```

2. rloss/ 폴더의 requirements-bsh.txt 를 설치해주세요 

```cmd
pip install -r requirements-bsh.txt
```

3. input/ 폴더에 새로운 폴더를 만들고, **JPEGImages** 폴더에는 원본 이미지, **JSONScribble** 폴더에는 라벨 데이터를 json 파일로 저장해주세요.


### 1. Script Description
-----

* _01_json_to_image.py : Json 형태의 라벨 데이터를 이미지 형태로 변환하고, classes.txt 파일을 생성합니다.  
* _02_split_train_test.py : 학습 데이터와 검증 데이터를 분류하고, train.txt , val.txt 파일을 생성합니다.
* _03_train.py : 모델을 학습하고 model/ (기본값) 폴더에 최적의 모델을 생성합니다. 
* _04_inference.py : 학습된 모델을 통해 Segmentation 을 수행합니다.


