import cv2
import smtplib
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def alerta():
	mensajeAlerta = "El aula sobrepasa el aforo maximo permitido"
	asunto = "Mensaje alerta aforo"

	mensajeAlerta = "Subject: {}\n\n{}".format(asunto, mensajeAlerta)

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("lfvallejo61922@umanizales.edu.co", "supervideos1")


	server.sendmail("lfvallejo61922@umanizales.edu.co", "lkrios62840@umanizales.edu.co", mensajeAlerta)

	server.quit()

	print("Correo de alerta enviado exitosamente")


cap = cv2.VideoCapture(0)
aforoAula702=2
contador = 0
while True:
	# la funcion video.read() retorna un boleando y el fotograma
	ret, frame = cap.read()
	if ret == False: break

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30,30),
		maxSize=(100,100))
	#eyes = eye_cascade.detectMultiScale(roi_gray)

	counter=len(faces)
	
	cv2.rectangle(frame,(0,0),(frame.shape[1],30),(0,0,0),-2)
	color = (0, 255, 255)
	font = cv2.FONT_HERSHEY_SIMPLEX

	
	#para visualizar el anterior texto se utiliza la funcion cv.putTex() 
	cv2.putText(frame, str(counter), (5,25), font, 1, (0,255,0), 2)
	
	for (x,y,w,h) in faces:
	    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	    #roi_gray = gray[y:y+h, x:x+w]
	    #roi_color = frame[y:y+h, x:x+w]
	    #eyes = eye_cascade.detectMultiScale(roi_gray)

	    #for (ex,ey,ew,eh) in eyes:
	     #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	if counter>aforoAula702:
		alerta()

				
	cv2.imshow('frame', frame)

	if cv2.waitKey(80) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()

