import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 1080)
fc = 20.0
codec = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
out = cv2.VideoWriter('data.avi', codec, fc, (int(cap.get(3)), int(cap.get(4))))
while True:
    ret, frame = cap.read()
    cv2.imshow('Object Detection', frame)
    out.write(frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
