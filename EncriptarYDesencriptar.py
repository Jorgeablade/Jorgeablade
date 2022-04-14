# archivo = open('texto.txt', 'a') #crear un archivo y lo abre en modo escritura
# a = >> hablando de Linux (que no sobreponga la info)
# w = > (que pise la info anterior)
#archivo.write('Prueba de guardado en el archivo')
# Meter algo en el archivo
# archivo.close()
# Cerrar la cualquier accion que estemos haciendo en el archivo

#archivo = open('texto.txt', 'r')
# Abrimos el archivo en modo lectura
# print(archivo.read())

def encriptar(texto):
    print('Texto para encriptar: ' + texto)
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra) #ord te devuelve el ascii del caracter que le pases
        ascii += 1
        textoFinal += chr(ascii) #chr toma un numero de la tabla ascii y lo transforma en el caracter que corresponda
    return textoFinal
    # return para sacar el contenido fuera de la funcion


def desencriptar(texto):
    print('Texto encriptado: ' + texto)
    textoFinal = ''
    #contador = 0
    for letra in texto:
        ascii = ord(letra) #ord te devuelve el ascii del caracter que le pases
        ascii -= 1
        textoFinal += chr(ascii) #chr toma un numero de la tabla ascii y lo transforma en el caracter que corresponda
            #if contador % 2 == 0:
            # Vamos a ignorar las letras que esten en posiciones inpares
            #textoFinal += letra
            # Y solo nos quedamos con las pares
            # Ya que los arrays empiezan en 0 (par)
        #contador += 1
    return textoFinal

#desencriptar('Pxrxuxexbxax xdxex xtxexxxtxox')

#archivo = open('texto.txt', 'a')


def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    # guardamos la info del archivo en la variable texto
    archivo.close
    # luego lo cerramos
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    # volvemos a abrirlo con >
    archivo.write(textoEncriptado)
    # volcamos el texto encriptado en el archivo
    archivo.close()
    # cerramos
    print("El archivo se encripto correctamente")


def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    # guardamos la info del archivo en la variable texto
    archivo.close
    # luego lo cerramos
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    # volvemos a abrirlo con >
    archivo.write(textoDesencriptado)
    # volcamos el texto encriptado en el archivo
    archivo.close()
    # cerramos
    print("El archivo se desencripto correctamente")


#desencriptarArchivo()

opcionEoD = input('Presione "E" para encriptar, o "D" para desencriptar: ')
rutaArchivo = input('Ingrese la ruta del archivo: ')

if opcionEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)