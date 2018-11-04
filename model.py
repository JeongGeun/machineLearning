#vcg16모델 사용
from keras.models import Sequential
import keras
import numpy as np
from keras.applications import vgg16, inception_v3, resnet50, mobilenet

# VGG 모델을 로딩함
vgg_model = vgg16.VGG16(weights='imagenet')

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt

filename = 'C:\P_workspace\workspace\개발과제\images\card\card0.jpg'
# 이미지 로딩. PIL format
original = load_img(filename, target_size=(224, 224))
print('PIL image size', original.size)
plt.imshow(original)
plt.show()

# PIL 이미지를 numpy 배열로 변환
# Numpy 배열 (height, width, channel)
numpy_image = img_to_array(original)
plt.imshow(np.uint8(numpy_image))
plt.show()
print('numpy array size', numpy_image.shape)

# 이미지를 배치 포맷으로 변환
# 데이터 학습을 위해 특정 축에 차원 추가
# 네트워크 형태는 batchsize, height, width, channels 이 됨
image_batch = np.expand_dims(numpy_image, axis=0)
print('image batch size', image_batch.shape)
plt.imshow(np.uint8(image_batch[0]))

# 모델 준비
processed_image = vgg16.preprocess_input(image_batch.copy())

# 각 클래스 속할 확률 예측
predictions = vgg_model.predict(processed_image)

# 예측된 확률을 클래스 라벨로 변환. 상위 5개 예측된 클래스 표시
label = decode_predictions(predictions)
print(label)
