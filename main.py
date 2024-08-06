import cv2
import numpy as np
import os
import time
import hand_tracking as ht 

folderpath = r"C:/Users/nandi/OneDrive/Desktop/nandini/Program/virtual_painter/headers"
myList = os.listdir(folderpath)
overLay = []
for imPath in myList:
    image= cv2.imread(os.path.join(folderpath, imPath))
    overLay.append(image)

header =  overLay[0]
drawColor = (0,0,0)
brushThickness = 20
eraserThickness = 100
xp = 0
yp = 0

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 72)

imgCanvas = np.zeros((720,1280,3), np.uint8)

pTime=0

detector = ht.handDetector()
while True: 
    r,frame = cap.read(0)
    frame=cv2.flip(frame,1)

    frame= detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)

    if len(lmList)!= 0: 

        #tip of index and middle finger
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]

        fingers=detector.fingerUps()    

        if fingers[1] and fingers[2] : 
            xp,yp = 0,0
            print('Selection Mode')
            if y1 < 125:
                if len(overLay) < 65:
                    header=overLay[0]
                drawColor=(255,255,255)
                if 71<x1<175: 
                    header = overLay[1]
                    drawColor=(0,0,255)
                
                elif 263<x1<367: 
                    header = overLay[2]
                    drawColor= (255,0,0)

                elif 455<x1<561: 
                    header = overLay[3]
                    drawColor= (0,255,0)
                
                elif 649<x1<755: 
                    header = overLay[4]
                    drawColor= (0,255,255)
                
                elif 837<x1<947: 
                    header = overLay[5]
                    drawColor=(0,0,0)

                elif 1036<x1<1049 :
                    header= overLay[6]
                    drawColor
                    brushThickness= 30

                elif 1064<x1<1083 :
                    header= overLay[7]
                    drawColor
                    brushThickness= 40

                elif 1099<x1<1124 :
                    header=overLay[8]
                    drawColor
                    brushThickness = 50  

            cv2.rectangle(frame, (x1,y1-20), (x2, y2+20), drawColor, 2)



        if fingers[1] and not fingers[2]: 
            cv2.circle(frame, (x1,y1), 20, (255,255,255), 2)
            print('Drawing Mode')    
            if xp == 0 and yp==0:
                xp,yp = x1,y1
            
            
            cv2.line(frame, (xp,yp), (x1,y1), drawColor, brushThickness)
            cv2.line(imgCanvas, (xp,yp), (x1,y1), drawColor, brushThickness)

            xp,yp = x1,y1 

    fgray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    q, finv= cv2.threshold(fgray, 50,255, cv2.THRESH_BINARY_INV)
    finv = cv2.cvtColor(finv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, finv)
    frame = cv2.bitwise_or(frame, imgCanvas)        

    frame[0:125, 0:1280] = header

    cTime= time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.imshow("Virtual_Painter", frame)
    if cv2.waitKey(1) & 0xff==ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
