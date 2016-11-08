import numpy as np
import cv2

import robosub

pool_lower_green = np.array([50,100,100])
pool_upper_green = np.array([90,255,255])

lower_green = np.array([40,45,45])
upper_green = np.array([90,255,255])

lower_red = np.array([170,100,60])
upper_red = np.array([179,255,255])


cap = cv2.VideoCapture('output-videos/battelle_video_11-5-16-MP4.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('battelle_output.avi',fourcc, 20.0, (960,720))


while(cap.isOpened()):
	ret, frame = cap.read()
    
	overlay = frame.copy()
	robosub.findColorBuoy(frame.copy(), lower_green, upper_green, "Green",overlay)
	robosub.findColorBuoy(frame.copy(), lower_red, upper_red, "Red",overlay)

	out.write(overlay)
	#height, width, channels = overlay.shape
	#print height, width, channels
	cv2.imshow('frame',overlay)

    #####################################
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()