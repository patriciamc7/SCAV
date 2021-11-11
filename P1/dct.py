from PIL import Image
import cv2
import numpy as np

if __name__ == '__main__':
    image = Image.open("bw2.png");
    image = np.float32(image);
    dct = cv2.dct(image);
    image_out = np.uint8(dct)*255;