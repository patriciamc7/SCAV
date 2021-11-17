import cv2
import cut, resize, histogram
if __name__ == '__main__':
    # change audio into mono and in dif audio codec, decidir a que queremos pasar

    while True:
        print("Escoge el script que quieres ejecutar:");
        print("0- Ver video");
        print("1- Cortar un video");
        print("2- Historgrama YUV");
        print("3- Cambiar el tamaño");
        print("4- Cambiar el audio");
        print("5- Exit");
        opcion = int(input());
        if (opcion == 1):
            N = int(input("Introduce la longitud en segundos, a la que quieres recortar el video"));
            cut.cut(N)
        elif (opcion == 2):
            histogram.read_video();
        elif (opcion == 3):
            print("Escoge la resolucion a la que quieres cambiar:");
            print("0- 720p");
            print("1- 480p");
            print("2- 360x240");
            print("3- 160x120");
            res = int(input());
            resize.resize(res);
        elif (opcion == 4):

        elif (opcion == 5):
            exit();
        else:
            print("opcion no valida");

