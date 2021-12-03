import subprocess
import  converter, comparision, streaming
if __name__ == '__main__':
    while True:
        print("Escoge el script que quieres ejecutar:")
        print("1- Convertir video")
        print("2- Comparación")
        print("3- Streaming")
        print("4- Exit")
        opcion = int(input())
        if (opcion == 1):
           converter.converter()
        elif (opcion == 2):
            comparision.comparision()
        elif (opcion == 3):
            streaming.streaming()
        elif (opcion == 4):
            print("Has decidido salir")
            exit()
        else:
            print("Opcion no valida")