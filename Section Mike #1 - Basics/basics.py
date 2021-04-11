import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('cat', img)

# Converting into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# Edge Cascade --> get the edges within an image
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Image', canny)

# Dilating the image (Erweiterung)
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('dilated', dilated)

# Eroding (reverse the previous step)
eroded = cv.erode(dilated, (7,7), iterations=1)
# cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)