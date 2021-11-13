import rgb_yuv, Encode, dct
import sys

def RGBYUV():
    r_ori = int(input("Introduce un valor R: "));
    g_ori = int(input("Introduce un valor G: "));
    b_ori = int(input("Introduce un valor B: "));

    y, u, v = rgb_yuv.rgb_to_yuv(r_ori, g_ori, b_ori)
    r, g, b = rgb_yuv.yuv_to_rgb(y, u, v)

    print("YUV valores son", y, u, v);
    print("RGB valores son", r, g, b);

def run_lengt():
    sequence = []
    n = int(input("Introduce una longitud para la cadena : "))
    print("Introduce una cadena: ");
    for i in range(0, n):
        value = int(input())
        sequence.append(value);

    aux_seq = Encode.encode(sequence, n);
    print(aux_seq);

def ex():
    print("Has decidido salir");
    sys.exit(0);


if __name__ == '__main__':
    while True:
        print("Escoge el script que quieres ejecutar:");
        print("1- RGB a YUV");
        print("2- Encoder run-length");
        print("3- DCT");
        print("4- Exit");
        opcion = int(input());
        if (opcion == 1):
            RGBYUV();
        elif (opcion == 2):
            run_lengt();
        elif(opcion == 3):
            dct.dct();
        elif(opcion == 4):
            exit();
        else:
            print("opcion no valida");
