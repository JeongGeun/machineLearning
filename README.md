# machinerunning
머신러닝과제
웹캠을 이용한 사물 및 사람 인식 프로그램

#camtoavi.py
웹캠에 사물이나 사람얼굴을 보여주면서 웹캠영상을 띄우고 esc키를 누르면 동영상파일로 저장한다

#cardtojpg,humantojpg,papertojpg.py
-저장된 동영상을 읽어서 시간마다 프레임 단위로 자르고 그 프레임을 선택해서 jpg파일로 저장한다

#labeling.py
- 각 프레임마다 컴퓨터가 알고리즘 모델이 인식할 수 있도록 정수 형태로 라벨링을 한다.

#model2.py실행
-cnn모델을 사용하여 내가 만든 데이터셋을 학습시키고 그 내용을 바탕으로 테스트를 수행한다

#model1.py(가산점)
-vcg16모델을 통해 object detection을 구현하였다.
