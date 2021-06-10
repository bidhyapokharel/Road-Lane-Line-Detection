import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img,mask)
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(blank_image, (x1,y1), (x2,y2), (0,255,0), thickness=3)




img = cv.imread('road.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# plt.imshow(gray)
# plt.show()
cv.imshow('Image', gray)
cv.waitKey(0)
cv.destroyAllWindows()
