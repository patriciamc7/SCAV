SCAV
P1:
Hay 4 diferentes scripts:

-Main: Donde pedimos por consola que script queremos ejecutar y pedimos los paramteros
de los siguientes scripts.

-rgb_yuv: Donde lo que hacemos es pasar valores rgb de 0 a 255, para pasarlos a YUV, 
y tambien al mismo momento hacemos la conversión de YUV a rgb, para comprobar que
lo tenemos bien.

-Encode:  Aqui lo que hacemos es aplicar el codificador run-length, lo que hacemos
es mirar si dos numeros seguidos salen repetidos y si es asi, la nueva sequencia
sera el valor con las veces que sale repetido. Por consola pedimos al usuario que
longitud de la cadena quiere y luego introduce el valor de la cadena.

-DCT: Aqui lo que hacemos es la implementacion de la DCT a partir de la libreria
opencv.

Por otra parte tambien he añadido las imagenes de los comandos de escala, y la imagen
en blanco y negro, he subido dos ya que he probado de aplicar un threshold desde 
ffmpeg con la imagen original y con una imagen que sea grayscale, y para el ejercicio
de la DCT utilizo la conversion con la grayscale ya que pesa menos.
