import cv2
import numpy as np


click_count = 0
max_clicks = 2
lst = []

def click_event(event, x, y, flags, params):
    global click_count,lst
    if event == cv2.EVENT_LBUTTONDOWN:
        if click_count < max_clicks:
            x = int(x)
            y = int(y)

            strXY = str(x) + " " + str(y)
            
  
            cv2.putText(img, strXY, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
            cv2.imshow('image', img)
            
       
            click_count += 1
            lst.append((x,y))
           
            if click_count >= max_clicks:
                print(lst)
                cv2.rectangle(img,lst[0],lst[1],(255,0,0),2)
                cv2.imshow('image',img)
        else:
            print("No more clicks allowed.")


img = np.zeros((500, 500), np.uint8)
cv2.imshow('image', img)


cv2.setMouseCallback('image', click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()
