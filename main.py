import os
import cv2
import numpy        #multidimensional arrays

columns= 3
rows= 2

horizontal_margin= 40
vertical_margin= 20

images= os.listdir("images")
image_object= [cv2.imread(f"images/{filename}") for filename in images]
print(images)

shape= cv2.imread("images/1.jpeg").shape
print(shape)

big_image= numpy.zeros((shape[0] * rows + horizontal_margin * (rows+1),

shape[1] * columns + vertical_margin * (columns+1), shape[2]), numpy.uint8)
big_image.fill(255)             #makes image white

position= [(x,y) for x in range (columns) for y in range (rows)]
print(position)

for (pos_x, pos_y), image in zip(position, image_object):
    x= pos_x * (shape[1]+ vertical_margin) + vertical_margin
    y= pos_y * (shape[0] + horizontal_margin) + horizontal_margin
    big_image[y:y+shape[0], x:x+shape[1]] = image

cv2.imwrite("grid.jpeg", big_image)
