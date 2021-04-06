import cv2
import numpy as np 
import imutils

cap = cv2.VideoCapture('autos.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
carCounter = 0


while True:
	ret, frame = cap.read()
	if ret == False:
		break
	frame = imutils.resize(frame, width=640)
	color = (0, 255, 0)

	# espeficiar los puntos extermos sobre los cuales se dibujara el area a analizar

	ptsArea = np.array([[330, 162], [frame.shape[1]-80, 162], [frame.shape[1]-80, 267], [330, 267]])
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#visualizacion
	cv2.drawContours(frame, [ptsArea], -1, color, 2)
	cv2.line(frame, (450, 162), (450, 267), color, 2)

	imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8) 
	imAux = cv2.drawContours(imAux, [ptsArea], -1, (255), -1)
	#imagenArea = cv2.bitwise_and(gray, gray, mask=imAux)
	imagen_Area = cv2.bitwise_and(frame, frame, mask=imAux)

	# Para aplicar sustraccion de fondo
	fgmask = fgbg.apply(imagen_Area)

	#para reducir el ruido de la imagen
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
	fgmask = cv2.dilate(fgmask, None, iterations=5)

	# luego de encontrar los contornos presentes de fgmask determinar si existe movimiento
	cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

	for cnt in cnts:
	    if cv2.contourArea(cnt) > 1200:
	        x, y, w, h = cv2.boundingRect(cnt)
	        cv2.rectangle(frame, (x,y), (x+w, y+h),(255,2550,0), 2)

	        # si el auto ha cruzado entre 440 y 460 abierto en x, se incrememtara contador
	        if 440 < (x + w) < 460:
	        	carCounter = carCounter + 1
	        	cv2.line(frame, (450, 162), (450, 267), (0, 0, 255), 3)	     
	cv2.rectangle(frame, (frame.shape[1] -70, 215), (frame.shape[1]-5, 270), (0, 255, 255), 2) 
	cv2.putText(frame, str(carCounter), (frame.shape[1]-55, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)

	
	cv2.imshow("Video inicial", frame)
	#cv2.imshow("Video imAux", imAux)
	#cv2.imshow("imagen Area ", imagenArea)
	cv2.imshow("imagen Area", fgmask)
	if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
