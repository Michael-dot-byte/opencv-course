import cv2 as cv

#resizing and rescaling
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_LINEAR)

#change resolution
def changeResolution(width)

#reading images
'''
img = cv.imread('../Resources/Photos/cat.jpg')
img_resized = rescaleFrame(img, 0.4)
cv.imshow('cat', img)
cv.imshow('cat_resized', img_resized)
cv.waitKey(0)
'''

#reading videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    #end video when pressing letter d
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
