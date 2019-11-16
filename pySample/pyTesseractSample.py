import cv2
import os, sys, webbrowser, platform
import pytesseract

app_carpeta = os.getcwd()
img_carpeta = app_carpeta + os.sep + "img" + os.sep
file1 = img_carpeta + "example_02.png"
file2 = img_carpeta + "example_02.jpg"
texto = "Sin Imagen"
texto2 = "Sin Imagen"
if not os.path.exists(file1):
    print('Imagen no encontrada:', file1)
else:
    im = cv2.imread(file1)
    texto = pytesseract.image_to_string(im)
if not os.path.exists(file2):
    print('Imagen no encontrada:', file2)
else:
    im2 = cv2.imread(file2)
    texto2 = pytesseract.image_to_string(im2)
print(img_carpeta)
print(texto)
print(texto2)