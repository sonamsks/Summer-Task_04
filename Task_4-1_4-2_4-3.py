import cv2
import numpy as np
sk = np.zeros((600,800,3))
sk.shape

sk = cv2.circle(sk,(450,120),(10),(255,255,255),2)
sk = cv2.circle(sk,(450,130),(15),(255,255,255),2)
sk = cv2.circle(sk,(450,140),(20),(255,255,255),2)

sk = cv2.circle(sk,(350,120),(10),(255,255,255),2)
sk = cv2.circle(sk,(350,130),(15),(255,255,255),2)
sk = cv2.circle(sk,(350,140),(20),(255,255,255),2)

sk = cv2.circle(sk,(400,200),(60),(255,0,0),2) #1
sk = cv2.circle(sk,(400,200),(50),(0,0,255),2)

sk = cv2.circle(sk,(400,330),(90),(255,0,255),2)  #2
sk = cv2.circle(sk,(400,330),(80),(255,0,0),2)
sk = cv2.circle(sk,(400,330),(70),(255,255,0),2)
sk = cv2.circle(sk,(400,330),(60),(255,0,255),2)
sk = cv2.circle(sk,(400,330),(50),(255,255,255),2)
sk = cv2.circle(sk,(400,330),(40),(0,0,255),2)
sk = cv2.circle(sk,(400,330),(30),(255,255,255),2)
sk = cv2.circle(sk,(400,330),(20),(0,255,0),2)
sk = cv2.circle(sk,(400,330),(10),(0,0,0),2)
sk = cv2.circle(sk,(400,330),(5),(255,0,255),2)

sk = cv2.circle(sk,(370,180),(3),(255,255,0),2) #eye1
sk = cv2.circle(sk,(430,180),(3),(255,255,0),2) #eye2

sk = cv2.line(sk,(390,210),(410,210),(255,255,0),2) #mo
sk = cv2.line(sk,(390,200),(410,200),(255,255,0),2)

sk = cv2.line(sk,(220,230),(360,250),(255,255,0),4)
sk = cv2.line(sk,(440,250),(590,220),(255,255,0),4)

position = (80,30)
cv2.putText(
     sk, #numpy array on which text is written
     "Aatm Namaste Everyone", #text
     position, #position at which writing has to start
     cv2.FONT_HERSHEY_SIMPLEX, #font family
     1, #font size
     (255, 0, 255), #font color
     3)
     
     position = (80,500)
cv2.putText(
     sk, 
     "Sonam Teja Ishan Aakash Gagan",  
     position, 
     cv2.FONT_HERSHEY_SIMPLEX, 
     1, #font size
     (255, 255, 0), 
     3)
     
cv2.imshow('my photo',sk)
cv2.waitKey()
cv2.destroyAllWindows()
