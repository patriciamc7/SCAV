import cv2
import numpy as np

def dct():
    image = cv2.imread("food.jpg",0);
    im = np.float32(image)/255;
    dct = cv2.dct(im);
    image_dct = np.uint8(dct)*255;
    cv2.imwrite("dct.jpg", image_dct);
    inverse = cv2.idct(np.float32(image_dct));
    cv2.imwrite("inverse.jpg", inverse);
    print("Se han generado las imagenes en la carpeta");