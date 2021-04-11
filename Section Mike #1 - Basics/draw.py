import cv2 as cv
import numpy as np

# blank image (black)
blank = np.zeros((500,500,3), dtype='uint8')    # creates an array with 500 with the dimensions of 500,500,3
# cv.imshow('blank',blank)
#
# # 1.Paint the image a certain color
# blank[200:300, 300:400] = 0,255,0
#
# # 2.Draw a rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
#
# # 3. Draw a circle
# cv.circle(blank, (250, 250), 40, (0,0,255), thickness=3)    # fill by using thickness=-1
#
# # 4. Draw a line
# cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
# cv.imshow('Green', blank)

# 5. Write text on an image
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
