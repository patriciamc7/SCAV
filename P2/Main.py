import Cut, resize, histogram, audio
import subprocess

if __name__ == '__main__':
    while True:
        print("Escoge el script que quieres ejecutar:")
        print("1- Cortar un video")
        print("2- Historgrama YUV")
        print("3- Cambiar la resolucion")
        print("4- Cambiar el audio")
        print("5- Exit")
        opcion = int(input())
        if (opcion == 1):
            print("Introduce la longitud en segundos, a la que quieres recortar el video")
            N = int(input())
            Cut.cut(N)
        elif (opcion == 2):
            histogram.histogram()
        elif (opcion == 3):
            print("Escoge la resolucion a la que quieres cambiar:")
            print("0- 720p")
            print("1- 480p")
            print("2- 360x240")
            print("3- 160x120")
            res = int(input())
            resize.resize(res)
        elif (opcion == 4):
            print("En que codec quieres cambiar el audio a mono:")
            print("0- ac")
            print("1- aac")
            modo = int(input())
            audio.audio(modo)
        elif (opcion == 5):
            print("Has decidido salir")
            exit()
        else:
            print("Opcion no valida")

