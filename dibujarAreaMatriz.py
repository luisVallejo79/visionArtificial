import cv2
import numpy as np
import imutils

#cargando un video en la variable cap
cap = cv2.VideoCapture('personas.mp4')

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

	
	#visualizar los puntos extremosq
	cv2.drawContours(frame, [ptsArea], -1, color, 2)

	#para visualizar el anterior texto se utiliza la funcion cv.putTex() 
	cv2.putText(frame,textoEstado,(10,30), font,1,(0,0,255),2)

	cv2.imshow('frame', frame)
	#cv2.imshow('imAux', imAux)

	if cv2.waitKey(80) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()