import cv2

cap = cv2.VideoCapture(0)
exit = cv2.VideoWriter('VideodeSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow('Video',frame)
        exit.write(frame)
        if cv2.waitKey(1) &0xFF == ord('s'):
            break

cap.release()
exit.release()
cv2.destroyAllWindows()