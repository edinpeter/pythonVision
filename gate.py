from __future__ import print_function
import cv2
import numpy as np
import robosub

frame = cv2.imread("gate_sample_rotated.png")

overlay = frame.copy()

robosub.findGate(frame.copy(), None, None, True, overlay)

cv2.imshow("Output", overlay)
cv2.waitKey(0)