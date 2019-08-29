import numpy as np
import cv2

cap = cv2.VideoCapture(0)#cap仅仅是摄像头的一个对象
while True:
    ret,frame = cap.read()#一帧一帧的捕获视频,ret返回的是否读取成功，frame返回的是帧

#gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#对帧的操作,这里是把彩色图像转为灰度图像
#cv2.imshow('frame',gray)

    cv2.imshow('frame',frame)
#if cv2.waitKey(1) == ord('q'):#key值写的太高，会导致视频帧数很低
    c=cv2.waitKey(1)
    if  c==27:
     break

print(ret)
cap.release()
cv2.destroyAllWindows()