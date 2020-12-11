#import cv2

"""
#imagenes
# cargar el archivo PNG indicado
img = cv2.imread('C:/Git/TipsPython/camara_web/Imagenes/43_spherespirals.jpg', cv2.IMREAD_GRAYSCALE)

# guardar la imagen en formato JPG
#cv2.imwrite('save.jpg', img)

# mostrar la imagen en una ventana
cv2.imshow('IMAGEN', img)


# esperar hasta que se presiona una tecla
cv2.waitKey(0)
#print("hola Mundo")

#VIDEOS

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    if ret:
        cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""
"""
cap = cv2.VideoCapture('C:/Git/TipsPython/camara_web/Videos/Pro.mp4')

# Definir el codec y crear el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc('M','S','V','C')
out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (720, 528))

while(True):
    # capturar el cuadro
    ret, frame = cap.read()

    if ret:
        # procesar la captura, convertir a grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # escribir el cuadro procesado
        out.write(gray)

        # mostar la captura actual
        cv2.imshow('video', gray)

    # esperar, si se presiona la tecla ESC salir
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()

cv2.destroyAllWindows()



************

from cv2 import *

namedWindow("webcam")
vc = VideoCapture(0);

#while True:
#    next, frame = vc.read()
#    imshow("webcam", frame)
#    if waitKey(50) >= 0:
#        break;

while True:
    next, frame = vc.read()

    gray = cvtColor(frame, COLOR_BGR2GRAY)
    gauss = GaussianBlur(gray, (7,7), 1.5, 1.5)
    can = Canny(gauss, 0, 30, 3)

    imshow("webcam", can)

    if waitKey(5) >= 0:

        break;
#http://acodigo.blogspot.com/2013/06/acceso-la-webcam.html



******


#El script simplemente define la captura de vídeo, genera un ciclo donde se captura el vídeo y se muestra en pantalla. Cuando se presiona la tecla espaciadora se hace una captura de una imagen y se salva, al presionar la tecla Escape se finaliza el ciclo de captura de vídeo.

#!/usr/bin/env python

#Se importa cv2.

import cv2


# se crea la instancia de la captura de Video.

video = cv2.VideoCapture(0)

#Se define un ciclo.

while True:

    #Se captura el video de la webcam

    ret,im = video.read()

    #Se muestra el video  donde se pasa im que es la lectura del video de la webcam.

    cv2.imshow('Prueba de video',im)

    #Se captura la tecla de escape del teclado

    tecla = cv2.waitKey(10)

    if tecla == 27:

        #Si es la tecla escape se termina el ciclo

        break

    #Si la tecla es el espacio en blanco se captura una imagen del video.

    if tecla == ord(' '):

        cv2.imwrite('captura_img.jpg',im)
#FIN

"""



import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Define el codec y crea el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)  # invierte el cuadro

        # escribe el cuadro invertido
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Libera todo si la tarea ha terminado
cap.release()
out.release()
cv2.destroyAllWindows()