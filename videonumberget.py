import numpy as np
import cv2
from PIL import Image
import pytesseract
video_filename = '/Users/xuexianbin/Desktop/untitled/12345.mp4'
videoCap = cv2.VideoCapture(video_filename)
# 帧频
fps = videoCap.get(cv2.CAP_PROP_FPS)
# 视频总帧数
total_frames = int(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))
# 图像尺寸
image_size = (int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print(fps)
print(total_frames)
print(image_size)
# 图像尺寸
for i in range(40):
 ret, frame = videoCap.read()
 #im = frame[:, :, (2,1,0)]
img = Image.fromarray(frame)
img.show()
#im = frame[:, :, 2]
im = frame[660:700,150 :220, (2,1,0)]
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
np.set_printoptions(threshold=np.inf)
#print(im)
#边缘检测
#edges = cv2.Canny(im,20,83)
#cv2.imwrite("canny.jpg", edges)
#cv2.imshow("canny", cv2.imread("canny.jpg"))
#cv2.waitKey()
#cv2.destroyAllWindows()
#ret, thresh = cv2.threshold(im, 84, 225,cv2.THRESH_BINARY)
#im1.save(r"C:\Users\Owner\PycharmProjects\untitled\a.jpg")
text = pytesseract.image_to_string('4.jpg', lang='eng')
print(text)