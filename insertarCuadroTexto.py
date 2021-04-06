import cv2
import numpy as np
import imutils

#cargando un video en la variable cap
cap = cv2.VideoCapture('personas.mp4')

bgs = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

while True:
	# la funcion video.read() retorna un boleando y el fotograma
	ret, frame = cap.read()
	if ret == False: break

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#dubujar rectangulo con mensaje dentro del video
	cv2.rectangle(frame,(0,0),(frame.shape[1],80),(0,0,0),-2)
	color = (0, 255, 0)
	textoEstado = "Sin Movimiento"
	font = cv2.FONT_HERSHEY_SIMPLEX

	#para visualizar el anterior texto se utiliza la funcion cv.putTex() 
	cv2.putText(frame,textoEstado,(600,70), font,3,(0,0,255),2)

	#redimencionar el video, ya que estaba muy grande el formayo
	frame = imutils.resize(frame, width=640)

	cv2.imshow('Video Inicial', frame)

	if cv2.waitKey(80) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()