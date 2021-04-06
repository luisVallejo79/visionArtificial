import cv2

captura = cv2.VideoCapture(0)

while (captura.isOpened()):
  video, imagen = captura.read()
  if video == True:
    cv2.imshow('video', imagen)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()