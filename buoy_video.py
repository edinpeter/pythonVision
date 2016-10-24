import numpy as np
import cv2

lower_green = np.array([40,45,45])
upper_green = np.array([90,255,255])



cap = cv2.VideoCapture('output.mp4')

while(cap.isOpened()):
	ret, frame = cap.read()
    
    #ret, mask = cv2.threshold(frame, 10, 255, cv2.THRESH_BINARY)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
	mask = cv2.inRange(hsv, lower_green, upper_green)

	(_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	if(len(cnts) > 0):
		c = max(cnts, key=cv2.contourArea)
		peri = cv2.arcLength(c, True)

		contours_x = 0
		contours_y = 0
		contours_count = 0
		for line in c:
			contours_count = contours_count + 1
			contours_x = contours_x + line[0][0]
			contours_y = contours_y + line[0][1]
			# print(contours_x)
		if(contours_count > 0):
			print(contours_count)

			contours_x = contours_x / contours_count
			contours_y = contours_y / contours_count

			center = (contours_x,contours_y)
			cv2.circle(frame,center,10,(255,0,255),-1)

		approx = cv2.approxPolyDP(c, 0.1 * peri, True)
		cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)

		x,y,w,h = cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)

		(x,y),radius = cv2.minEnclosingCircle(c)
		center = (int(x),int(y))
		radius = int(radius)
		cv2.circle(frame,center,radius,(255,0,255),2)

	cv2.imshow('frame',frame)

    #####################################
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()