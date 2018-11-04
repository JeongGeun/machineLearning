import cv2
import numpy as np
import os

# set video file path of input video with name and extension
vid = cv2.VideoCapture('C:\P_workspace\workspace\개발과제\data.avi')


if not os.path.exists('images/human'):
    os.makedirs('images/human')

#for frame identity
index = 0
while(True):
    # Extract images
    ret, frame = vid.read()
    # end of frames
    if not ret:
        break
    # Saves images
    name = './images/human/human' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # next frame
    index += 1
