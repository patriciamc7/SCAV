import numpy as np

def encode(sequence,n):
    aux_seq = sequence;
    aux = 0;
    for i in range (0,n):
        count = 1;
        enter = 0;
        if (i + 1 != n):
            if (sequence[i] == sequence[i+1]):
                count += 1;
                aux = sequence[i];
                enter = 1;
        if (enter == 1):
            aux_seq[i] = aux;
            aux_seq[i+1] = count;
            i += 2;
        else:
            aux_seq[i] = sequence[i];

    return  aux_seq;

if __name__ == '__main__':

    sequence = []
    n = int(input("Introduce una longitud para la cadena : "))
    print("Introduce una cadena: ");
    for i in range(0, n):
        value = int(input())
        sequence.append(value);

    aux_seq = encode(sequence,n);
    print(aux_seq)