import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
   ret, frame= cap.read()
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   #boundary for RED color range values
   lower_bound = np.array([0,100,100])
   upper_bound = np.array([20,255,255])

   mask = cv2.inRange(hsv, lower_bound, upper_bound) 

   contours,_ = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   for dim in contours:
      x, y, w, h = cv2.boundingRect(dim)
      area = cv2.contourArea(dim)
      if area > 2500:
         cv2.rectangle(frame, (x , y), (x + w, y + h), (0, 255, 0), 2)
       
   cv2.imshow("mask", mask)
   cv2.imshow('bounding box', frame)
   key = cv2.waitKey(1) 
   if key == 27:
     break

cap.release()
cv2.destroyAllWindows()