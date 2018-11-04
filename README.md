# machinerunning
머신러닝과제
웹캠을 이용한 사물 및 사람 인식 프로그램

먼저 디렉토리에 image,train,test폴더를 만든다
# camtoavi.py

웹캠에 사물이나 사람얼굴을 보여주면서 웹캠영상을 띄우고 esc키를 누르면 동영상파일로 저장한다
동영상은 esc키를 누르면 꺼지고 다른 사물을 찍기 위해서는 다시 한번 코드를 실행하고 동영상명을 다르게 해주어 구분이 가게 해야한다.

# cardtojpg,humantojpg,papertojpg.py
-저장된 동영상을 읽어서 시간마다 프레임 단위로 자르고 그 프레임을 선택해서 '분류할이름'.jpg파일로 image폴더에 저장한다

# labeling.py
- 각 프레임마다 컴퓨터가 알고리즘 모델이 인식할 수 있도록 정수 형태로 라벨링을 하여 train폴더에 저장될 수 있도록 한다.

# model2.py실행
-train폴더 중에 몇 개를 골라 test폴더로 옮기고 나중에 train폴더와 비교할 수 있게 한다.
-cnn모델을 사용하여 내가 만든 데이터셋을 학습시키고 그 내용을 바탕으로 테스트를 수행한다

# model1.py(가산점)
-vcg16모델을 통해 object detection을 구현하였다.
