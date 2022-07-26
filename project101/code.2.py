import cv2

def takePictures():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("image2.png", frame)
        result = False
    
    videoCaptureObject.release()
    cv2.destroyAllWindows()

takePictures() 