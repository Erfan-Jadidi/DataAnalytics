import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("F:\\DA\\DA 09\\DA 09\\brain.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Thresholding
# gray[gray > 50] = 255
# gray[gray <= 50] = 0

contours, hierarchy = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

i = 1
for contour in contours:
    x,y,w,h = cv.boundingRect(contour)

    z = gray[y:y+h, x:x+w]
    z = cv.resize(z,(50,50))

    # img = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    # print(x,y,w,h)
    # z = np.zeros_like(img)
    # z = cv.drawContours(z, contour, -1, (0, 0, 255),thickness= cv.FILLED)
    img = cv.drawContours(img, contour, -1, (0, 255, 0), 1)
    # print(cv.contourArea(contour))
    #
    # cv.imshow("Contour", z)
    cv.imshow("Image", img)
    # cv.imwrite(f"Contour{i}.jpg", z)
    cv.waitKey(1)
    i += 1