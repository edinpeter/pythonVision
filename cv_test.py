# import the necessary packages
from __future__ import print_function
import cv2
import numpy
 
# load the image and convert it to grayscale
image = cv2.imread("bouys.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# initialize the AKAZE descriptor, then detect keypoints and extract
# local invariant descriptors from the image
detector = cv2.AKAZE_create()
(kps, descs) = detector.detectAndCompute(gray, None)
print("keypoints: {}, descriptors: {}".format(len(kps), descs.shape))


# draw the keypoints and show the output image
#cv2.drawKeypoints(image, kps, image, (0, 255, 0))
dst = cv2.resize(image, (600, 400)) 

cv2.imshow("Output", dst)
cv2.waitKey(0)