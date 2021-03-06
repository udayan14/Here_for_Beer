#go to opencv/build/lib directory for using this code
import sys
sys.path.append("/Users/udayanjoshi/opencv/build/lib")
import cv2
from pyimagesearch.transform import four_point_transform
import numpy as np
import sys
import argparse
x=raw_input('enter filename: ')+('.jpg')
gray=cv2.imread(x,0)
image=cv2.imread(x)
output=image.copy()




circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 400, np.array([]), 100, 5, 12, 16)
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
        
        # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    
        
    
cornercircles=[]

for ( x , y, r ) in circles :
    cornercircles.append([x,y])


pts = np.array(cornercircles, dtype = "float32")
print pts
# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)

# show the original and warped images

cv2.imwrite("b1.jpg", warped)