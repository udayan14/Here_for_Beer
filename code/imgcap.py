import sys
sys.path.append("/Users/udayanjoshi/opencv/build/lib")
import cv2

vidcap=cv2.VideoCapture()
vidcap.open(1) #this can be 0,1,2 .just experiment
retval, image = vidcap.retrieve()
vidcap.release()
cv2.imwrite("capimage.jpg",image)