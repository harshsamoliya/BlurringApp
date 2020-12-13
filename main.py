import cv2
import numpy as np
img =cv2.imread('1_TUqC3XRqvzErhnFC4h1Rcw@2x.png')

# kernel = np.array([[0.0625,0.125,0.0625]
#                   ,[0.125,0.25,0.125],
#                    [0.0625,0.125,0.0625]])


# dst = cv2.filter2D(img,-1,kernel)
windowName ="Harsh Bot"
cv2.namedWindow(windowName)

LCondition_clic =False

def blur_project(event,x,y,flag,param):
    global LCondition_clic
    if event==cv2.EVENT_LBUTTONDOWN:
        LCondition_clic = True
        part = img[y:y+20,x:x+20]       #from x to X+20 and y to y+20
        blur= cv2.blur(part,(5,5))
        img[y:y+20,x:x+20] = blur
        # cv2.circle(img,(x,y),30,(255,0,255),1)

    elif event == cv2.EVENT_MOUSEMOVE and LCondition_clic==True:
        part = img[y:y+20,x:x+20]  # from x to X+20 and y to y+20
        blur = cv2.blur(part,(5, 5))
        img[y:y+20,x:x+20] = blur
        # cv2.circle(img, (x, y), 30, (255, 0, 255), 1)
        # cv2.line(img,(x,y),(x+50,y+50),(255,0,0),5)
    else:
        LCondition_clic =False

cv2.setMouseCallback(windowName,blur_project)

# dst = cv2.blur(img,(5,9))
while True:
    cv2.imshow(windowName,img)
    # cv2.imshow('Image Output',dst)
    if cv2.waitKey()==ord('c'):
        break

cv2.destroyWindow()
# image will display

# CNN- convioutonal neural network

