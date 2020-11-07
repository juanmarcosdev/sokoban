import sys

def leerArchivo():
    filas = 0
    columnas = 0
    contador = 0
    posicion = []
    ubicaciones_cajas = []
    tablero = []


    file = open(sys.argv[1], 'r')
    Lines = file.readlines()

    for i in range(0,len(Lines)):
        Lines[i] = Lines[i].replace("\n","")

    for i in range(0,len(Lines)):
        if(Lines[i][0] == 'W' or Lines[i][0] == '0'):
            filas = filas + 1
            tablero.append([Lines[i]])
        if(Lines[i][0] != 'W' and Lines[i][0] != '0' and contador != 0):
            ubicaciones_cajas.append([int(Lines[i][0]), int(Lines[i][2])])
        if(Lines[i][0] != 'W' and Lines[i][0] != '0' and contador == 0):
            posicion.append(int(Lines[i][0]))
            posicion.append(int(Lines[i][2]))
            contador = contador + 1

    columnas = len(Lines[0])

    print(filas)
    print(columnas)
    print(posicion)
    print(ubicaciones_cajas)
    print(tablero)

leerArchivo()