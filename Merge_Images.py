#🔅 Task 35.3
#📌 Take 2 images and combine it to form a single image. For example, collage 

#import cv2 
import cv2

#read images
photo1 = cv2.imread('1.jpg')
photo2 = cv2.imread('2.jpg')

#show images
cv2.imshow('1',photo1)
cv2.imshow('2',photo2)
cv2.waitKey()
cv2.destroyAllWindows()

#Merge Images Vertically
new_v = cv2.vconcat([photo1, photo2])

#Show Vertically Merged Images
cv2.imshow('conbine_vertical',new_v)
cv2.waitKey()
cv2.destroyAllWindows()

#Merge Images Horizontally
new_h = cv2.hconcat([photo1, photo2])

#Show Horizontally Merged Images
cv2.imshow('conbine_vertical',new_h)
cv2.waitKey()
cv2.destroyAllWindows()