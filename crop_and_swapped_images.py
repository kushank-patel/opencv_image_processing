#🔅 Task 35.2
#📌 Take 2 images, crop some part of both the images and swap them.

import cv2

#Read images
photo1 = cv2.imread('1.jpg')
photo2 = cv2.imread('2.jpg')

#show images
cv2.imshow('1',photo1)
cv2.imshow('2',photo2)
cv2.waitKey()
cv2.destroyAllWindows()

#Crop images
crop1 = photo1[30:145,120:165]
crop2 = photo2[30:145,112:174]

#Store cropped images in one file 
cv2.imshow('1',crop1)
cv2.imshow('2',crop2)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('crop1.jpg',crop1)
cv2.imwrite('crop2.jpg',crop2)

#Paste croped image in different image
photo2[30:145,60:105] = crop1
photo1[32:147,52:114] = crop2

# Show updated image
cv2.imshow('1',photo2)
cv2.imshow('2',photo1)
cv2.waitKey()
cv2.destroyAllWindows()