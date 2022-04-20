import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    name=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("NewPicture.jpg",frame)
        result=False

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()