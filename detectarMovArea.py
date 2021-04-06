import cv2
import numpy as np
import imutils

#cargando un video en la variable cap
cap = cv2.VideoCapture(1)

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

while True:
	# la funcion video.read() retorna un boleando y el fotograma
	ret, frame = cap.read()
	if ret == False: break

	#redimencionar el video, ya que estaba muy grande el formayo
	frame = imutils.resize(frame, width=640)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#dubujar rectangulo con mensaje dentro del video
	cv2.rectangle(frame,(0,0),(frame.shape[1],40),(0,0,0),-1)
	color = (0, 255, 0)
	textoEstado = "Sin Movimiento"
	font = cv2.FONT_HERSHEY_SIMPLEX

	#especificar puntos extremos del area a analizar, iniciando punto superior izquiero
	ptsArea = np.array([[190,320], [450,320], [550,frame.shape[0]], [70,frame.shape[0]]])

	#con la ayuda de una imagen auxiliar determinamos el area sobre la cual actuara el detector
	imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8) 
	imAux = cv2.drawContours(imAux, [ptsArea], -1, (255), -1)
	imagenArea = cv2.bitwise_and(gray, gray, mask=imAux)

	#visualizar los puntos extremosq
	

		# obtener imagen binaria donde la region en blanco representa la existencia de movimiento
	fgmask = fgbg.apply(imagenArea)

	#para reducir el ruido de la imagen
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
	fgmask = cv2.dilate(fgmask, None, iterations=2)

	# luego de encontrar los contornos presentes de fgmask determinar si existe movimiento
	cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

	for cnt in cnts:
	    if cv2.contourArea(cnt) > 600:
	        x, y, w, h = cv2.boundingRect(cnt)
	        cv2.rectangle(frame, (x,y), (x+w, y+h),(255,2550,0), 2)
	        textoEstado = "Movimiento Detectado"
	        color = (0, 0, 255)  
	        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
	cv2.drawContours(frame, [ptsArea], -1, color, 2) 
	cv2.putText(frame,textoEstado,(10,30), font,1,(0,255,0),2)


	cv2.imshow('frame', frame)
	#cv2.imshow('imAux', imagenArea)
	cv2.imshow('fgmask', fgmask)

	if cv2.waitKey(80) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()