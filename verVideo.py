import cv2

cap = cv2.VideoCapture('VideodeSalida.avi')

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow('Video',frame)
        if cv2.waitKey(30) &0xFF == ord('s'):
            break
    else: break

cap.release()

cv2.destroyAllWindows()