#SCAV P1:Hay 4 diferentes scripts:

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

#SCAV P2: Hay 5 diferentes scripts:

-Main: Donde pedimos por consola que script queremos ejecutar y pedimos los
paramteros de los siguientes scripts.

-Cut: Cortamos N segundos (por consola), el video y es el que vamos a utilizar 
siempre, ya que tardara menos.

-Histogram: Creamos un histograma en YUV y lo solapamos con ayuda de ffmpeg.

-Resize: Pedimos al usuario por consola que resolucion quiere, y aplicamos
la escala en esa resolucion.

-Audio: Leemos el audio del video y lo pasamos a lo que el usuario ha escogido
por consola.

Por otra parte tambien he añadido los videos de las ejecuciones, y los audios.

###SCAV S2: 5 diferentes scrpits:###

-Main: Donde pedimos por consola que script queremos ejecutar y pedimos los
paramteros de los siguientes scripts.

-Motion vectors: En este script ejecutamos por ffmpeg un comando donde se nos genera
el video original con los motion vectors de fondo.

-Container: Aqui generamos un contenedor donde añadimos el video sin audio, y audios 
en aac y en mp3.

-Information: Scamos la informacion de un comando de ffmpeg y le damos al usuario 
informacion que puede ser util.

-Subtitles: Aqui descargamos subtitulos de internet a partir de un link, y los añadimos
al video con tal de que se vean en pantalla.

#SCAV S3: 4 diferentes script

-Main: Donde pedimos por consola que script queremos ejecutar y pedimos los
paramteros de los siguientes scripts.

-Converter: convertimos un video a la resolucion que el usuario quiera
en formatos que el usuario quiera, entre ellos estan vp8, vp9, av1, h265.

-Comparision: Comparamos los videos en formato vp8 y vp9 y tambien su diferencia.

-Streaming: Generamos un streaming de nuestro video en la ip que el usuario desee.
