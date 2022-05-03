import cv2
import math


point1 = []
point2 = []
def drawRectangle (action, x, y, flags, param):
    global point1, point2
    if action == cv2.EVENT_LBUTTONDOWN:
        point1 = [(x,y)]
    elif action == cv2.EVENT_LBUTTONUP:
        point2 = [(x,y)]
        cv2.rectangle(img, point1[0], point2[0], (200,100,0),3, lineType=cv2.LINE_AA)
        cv2.imshow('Window', img)
        crop = img[point1[0][1]:point2[0][1],point1[0][0]:point2[0][0]]
        cv2.imwrite('face.png',crop)
img = cv2.imread('sample.jpg',1)
dummy = img.copy()
cv2.namedWindow('Window')
cv2.setMouseCallback('Window',drawRectangle)
k = 0
while k!=27:
    cv2.imshow('Window',img)
    cv2.putText(img,"Choose center, and drag, Press ESC to exit and c to clear",
                (10,30), cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
    k = cv2.waitKey(20) & 0xFF
    if k==99:
        img = dummy.copy()

cv2.destroyAllWindows()
