from __future__ import print_function
from imutils.object_detection import non_max_suppression
import numpy as np 
import cv2 
import imutils

image = cv2.imread("students.jpg")
cv2.imshow('students', image)

w = int(image.shape[1] / 2)
image = imutils.resize(image, width=w)

# inicializar el descriptor HOG

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

org = image.copy()

#detectar estudiantes en la imagen

(rects, weights) = hog.detectMultiScale(image, winStride=(3, 3), padding=(8, 8), scale=1.05)

# dibujar los cuadros delimitadores originales

for (x, y, w, h) in rects:
           cv2.rectangle(org, (x, y), (x + w, y + h), (0, 0, 255 ), 2)

# aplicar supresión no máxima a los cuadros delimitadores utilizando un umbral de superposición 
# grande para tratar de mantener la superposición
# cajas que siguen siendo personas


rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

# dibuja los cuadros delimitadores finales


for (xA, yA, xB, yB) in pick:
			cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

cv2.imshow("Output", org)
cv2.imshow("OutputNMS", image)
cv2.waitKey(0)
cv2.destroyAllWindows()