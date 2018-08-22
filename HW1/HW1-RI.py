from sys import argv #Poner archivos como argumentos a la hora de correrlo
from collections import deque #Importacion para utilizar linked lists
from os.path import exists #Verificar si existe la palabra (Funcion alterna que se puede utilizar)


#Ciclo para seguir preguntando por palabras
#Las palabras meterlas en una lista


#Forma alterna de correr el programa

#archivo = argv
# ******************************************************************************************
# A la hora de ejecutar el programa, dar como argumento los archivos que se quieren examinar
# ******************************************************************************************

#Funcion para encontrar la palabra
def encontrarPalabra():
    #Leer datos del teclado (Palabra)
    palabra = raw_input("Ingrese la palabra que desea buscar > ")
    print ""
    lista = deque([palabra])
    #Un arreglo de archivos vacios
    files = []
    #Arreglo de archivos encontrados, esto es para saber en cual se encuentra
    filesEncontrados = []
    # prueba = open("test1.txt")
    # lista1 = list(prueba)
    # print lista1

    if palabra == "":
        print "Ingrese palabra valida"
        exit()

    #Agregar los archivos
    for i in range (1,6):
        archivo = "test%r.txt" %i
        files.append(archivo)
        #Abrir el archivo
        open(archivo)

        #Abrir todos los archivos en la iteracion
        for line in open(archivo):
            #print line
            archivoLista = open(archivo)
            list(archivoLista)


            #Buscar en las palabras de los archivos (iterar sobre la lista de archivos)
            for i in range (len(files)):
                list(archivo)
                #Confirmar que exista una palabra


                #Revisar si la palabra se encuentra en alguna de las lineas
                if palabra in line:
                    #print True, "En archivo ", archivo
                    filesEncontrados.append(archivo)
                    break

                #La palabra no se encuentra
                else:
                    #print False, "En el archivo", archivo
                    break

    print ""

#Formato de impresion, en caso de que sea mayor a uno es plural, menor singular, 0 no ha encontrado
    if len(filesEncontrados) > 1:
        print "Los archivos en donde se encuentra la palabra son", filesEncontrados

    elif len(filesEncontrados) == 1:
        print "El archivo en donde se encuentra la palabra es", filesEncontrados

    else:
        print "No hemos encontrado la palabra ===>", palabra


    print "Aqui estan los archivos"
    print ""

    for elemento in filesEncontrados:
        nuevaLista = open(elemento)
        print list(nuevaLista)



#Ejecutar la funcion
encontrarPalabra()
