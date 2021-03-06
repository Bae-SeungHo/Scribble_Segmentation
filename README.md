Scribble Training Project 
==============================

modified from [ScribbleSup](https://github.com/meng-tang/rloss)
edited by Bae-SeungHo



### 0. Before Start
----------

1. pipenv 설치 후 python 3.7으로 가상환경을 생성해주세요.

```cmd
pipenv --python 3.7
pipenv shell
```

2. bilateralfilter 를 빌드해주세요.

```cmd
cd rloss/pytorch/wrapper/bilateralfilter
swig -python -c++ bilateralfilter.i
python setup.py install
```

3. requirements.txt 를 설치해주세요 

```cmd
pip install -r requirements.txt
```

4. input/ 폴더에 새로운 폴더를 만들고, **JPEGImages** 폴더에는 원본 이미지, **JSONScribble** 폴더에는 라벨 데이터를 json 파일로 저장해주세요.


### 1. Script Description
-----

* _01_json_to_image.py : Json 형태의 라벨 데이터를 이미지 형태로 변환하고, classes.txt 파일을 생성합니다.  
* _02_split_train_test.py : 학습 데이터와 검증 데이터를 분류하고, train.txt , val.txt 파일을 생성합니다.
* _03_train.py : 모델을 학습하고 model/ (기본값) 폴더에 최적의 모델을 생성합니다. 
* _04_inference.py : 학습된 모델을 통해 Segmentation 을 수행합니다.
* _05_show_result.py : 테스트 이미지를 통해 원본과 세그멘테이션 결과를 비교합니다.


