import subprocess
import  motion_vector, container, information, subtitles
if __name__ == '__main__':
    while True:
        print("Escoge el script que quieres ejecutar:")
        print("1- Mostrar motion vectors")
        print("2- Crear contenedor BBB")
        print("3- Informacion sobre contendor")
        print("4- Añadir subtitulos")
        print("5- Exit")
        opcion = int(input())
        if (opcion == 1):
            motion_vector.motion_vectors()
        elif (opcion == 2):
            container.create_container()
        elif (opcion == 3):
            information.information()
        elif(opcion ==4):
            subtitles.subtitulos()
        elif (opcion == 5):
            print("Has decidido salir")
            exit()
        else:
            print("Opcion no valida")