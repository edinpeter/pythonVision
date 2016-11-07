# import the necessary packages
from __future__ import print_function
import cv2
import numpy as np
import robosub
 
lower_green = np.array([50,100,100])
upper_green = np.array([90,255,255])

lower_red = np.array([100,20,45])
upper_red = np.array([105,255,255])

frame = cv2.imread("bouys_small.png")

overlay = frame.copy()

robosub.findColorBuoy(frame, lower_green, upper_green, "Green", overlay)
robosub.findColorBuoy(frame, lower_red, upper_red, "Red", overlay)

cv2.imshow("Output", overlay)
cv2.waitKey(0)