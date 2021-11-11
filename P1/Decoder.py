from PIL import Image
import cv2
import numpy as np

if __name__ == '__main__':
    image = Image.open("bw2.png");
    image = np.float32(image);
    dct = cv2.dct(image);
    print(dct);
    image_out = Image.fromarray(dct);
    image_out.save("out.jpg");