import cv2 as cv

img = cv.imread('page2.jpg')
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)

_,result=cv.threshold(img,35,255,cv.THRESH_BINARY)

adaptive=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,81,2)

cv.imshow('Image',img)
cv.imshow('Result',result)
cv.imshow('Adaptive Result',adaptive)

cv.waitKey(0)
cv.destroyAllWindows()