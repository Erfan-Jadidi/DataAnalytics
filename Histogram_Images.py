import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("images.jpg")

cv2.imshow("Image", img)


# cv2.imshow("Image1", img[100:200,100:200, :])

# cv2.waitKey(0)

r,g,b = cv2.split(img)

plt.hist(np.ravel(r),color="red",  bins=256)
plt.hist(np.ravel(g),color="green", bins=256)
plt.hist(np.ravel(b),color="blue", bins=256)
plt.show()