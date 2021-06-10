import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt

img = cv.imread('road.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# plt.imshow(gray)
# plt.show()
cv.imshow('Image', gray)
cv.waitKey(0)
cv.destroyAllWindows()
