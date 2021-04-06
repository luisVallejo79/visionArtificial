import cv2
import imutils

#cargando un video en la variable cap
cap = cv2.VideoCapture('personas.mp4')

while True:
	# la funcion video.read() retorna un boleando y el fotograma
	ret, frame = cap.read()
	if ret == False: break

	#redimencionar el video, ya que estaba muy grande el formayo
	frame = imutils.resize(frame, width=640)

	cv2.imshow('Video Inicial', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()