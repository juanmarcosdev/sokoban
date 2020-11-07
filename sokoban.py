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
            tablero.append(Lines[i])
        if(Lines[i][0] != 'W' and Lines[i][0] != '0' and contador != 0):
            ubicaciones_cajas.append([int(Lines[i][0]), int(Lines[i][2])])
        if(Lines[i][0] != 'W' and Lines[i][0] != '0' and contador == 0):
            posicion.append(int(Lines[i][0]))
            posicion.append(int(Lines[i][2]))
            contador = contador + 1

    columnas = len(Lines[0])

    return filas, columnas, posicion, ubicaciones_cajas, tablero

class State:
    def __init__(self, filas, columnas, posicion, ubicaciones_cajas, tablero, movimientos, cache):
        self.filas = filas
        self.columnas = columnas
        self.posicion = posicion
        self.ubicaciones_cajas = ubicaciones_cajas
        self.tablero = tablero
        self.movimientos = movimientos
        self.cache = cache
    
    def jugadasValidas(self):
        jugadas_validas = []

        if(self.tablero[self.posicion[0]-1][self.posicion[1]] != 'W'):
            jugadas_validas.append('U')
        if(self.tablero[self.posicion[0]+1][self.posicion[1]] != 'W'):
            jugadas_validas.append('D')
        if(self.tablero[self.posicion[0]][self.posicion[1]-1] != 'W'):
            jugadas_validas.append('L')
        if(self.tablero[self.posicion[0]][self.posicion[1]+1] != 'W'):
            jugadas_validas.append('R')
        
        if(([self.posicion[0]-1, self.posicion[1]] in self.ubicaciones_cajas and self.tablero[self.posicion[0]-2][self.posicion[1]] == 'W') or ([self.posicion[0]-1, self.posicion[1]] in self.ubicaciones_cajas and self.posicion[0]-1 == 0)):
            jugadas_validas.remove('U')
        if(([self.posicion[0]+1, self.posicion[1]] in self.ubicaciones_cajas and self.tablero[self.posicion[0]+2][self.posicion[1]] == 'W') or ([self.posicion[0]+1, self.posicion[1]] in self.ubicaciones_cajas and self.posicion[0]+1 == self.filas-1)):
            jugadas_validas.remove('D')
        if(([self.posicion[0], self.posicion[1]-1] in self.ubicaciones_cajas and self.tablero[self.posicion[0]][self.posicion[1]-2] == 'W') or ([self.posicion[0], self.posicion[1]-1] in self.ubicaciones_cajas and self.posicion[1]-1 == 0)):
            jugadas_validas.remove('L')
        if(([self.posicion[0], self.posicion[1]+1] in self.ubicaciones_cajas and self.tablero[self.posicion[0]][self.posicion[1]+2] == 'W') or ([self.posicion[0], self.posicion[1]+1] in self.ubicaciones_cajas and self.posicion[1]+1 == self.columnas-1)):
            jugadas_validas.remove('R')
        
        if(str(self.posicion[0]) + "," + str(self.posicion[1]) in self.cache):
            jugadas_validas.remove(self.cache[str(self.posicion[0]) + "," + str(self.posicion[1])])

        return jugadas_validas
    
    def lugaresCajaIdeales(self):
        lugares_ideales = []
        for i in range(0,self.filas):
            for j in range(0,self.columnas):
                if(self.tablero[i][j] == 'X'):
                    lugares_ideales.append([i,j])
        return lugares_ideales
    
    def ganeElJuego(self):
        return self.ubicaciones_cajas == self.lugaresCajaIdeales()

    def estoyEnUnDeadlock(self):
        flag = False
        for i in range(len(self.ubicaciones_cajas)):
            if(self.tablero[self.ubicaciones_cajas[i][0]-1][self.ubicaciones_cajas[i][1]] == 'W' and self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]-1] == 'W'):
                flag = True
            if(self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]-1] == 'W' and self.tablero[self.ubicaciones_cajas[i][0]+1][self.ubicaciones_cajas[i][1]] == 'W'):
                flag = True
            if(self.tablero[self.ubicaciones_cajas[i][0]+1][self.ubicaciones_cajas[i][1]] == 'W' and self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]+1] == 'W'):
                flag = True
            if(self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]+1] == 'W' and self.tablero[self.ubicaciones_cajas[i][0]-1][self.ubicaciones_cajas[i][1]] == 'W'):
                flag = True
        return flag
    
    def nuevoEstado(self, movimiento):
        if(movimiento == 'U'):
            newPosicion = [self.posicion[0]-1, self.posicion[1]]
            if(newPosicion in self.ubicaciones_cajas):
                nuevasCajas = self.ubicaciones_cajas
                nuevasCajas.remove(newPosicion)
                nuevasCajas.append([newPosicion[0]-1, newPosicion[1]])
            nuevosMovimientos = self.movimientos
            nuevosMovimientos.append('U')
            nuevoCache = self.cache
            nuevoCache[str(self.posicion[0]) + "," + str(self.posicion[1])] = "U"
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos, nuevoCache)
        
        if(movimiento == 'D'):
            newPosicion = [self.posicion[0]+1, self.posicion[1]]
            if(newPosicion in self.ubicaciones_cajas):
                nuevasCajas = self.ubicaciones_cajas
                nuevasCajas.remove(newPosicion)
                nuevasCajas.append([newPosicion[0]+1, newPosicion[1]])
            nuevosMovimientos = self.movimientos
            nuevosMovimientos.append('D')
            nuevoCache = self.cache
            nuevoCache[str(self.posicion[0]) + "," + str(self.posicion[1])] = "D"
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos, nuevoCache)
        
        if(movimiento == 'L'):
            newPosicion = [self.posicion[0], self.posicion[1]-1]
            if(newPosicion in self.ubicaciones_cajas):
                nuevasCajas = self.ubicaciones_cajas
                nuevasCajas.remove(newPosicion)
                nuevasCajas.append([newPosicion[0], newPosicion[1]-1])
            nuevosMovimientos = self.movimientos
            nuevosMovimientos.append('L')
            nuevoCache = self.cache
            nuevoCache[str(self.posicion[0]) + "," + str(self.posicion[1])] = "L"
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos, nuevoCache)
        
        if(movimiento == 'R'):
            newPosicion = [self.posicion[0], self.posicion[1]+1]
            if(newPosicion in self.ubicaciones_cajas):
                nuevasCajas = self.ubicaciones_cajas
                nuevasCajas.remove(newPosicion)
                nuevasCajas.append([newPosicion[0], newPosicion[1]+1])
            nuevosMovimientos = self.movimientos
            nuevosMovimientos.append('R')
            nuevoCache = self.cache
            nuevoCache[str(self.posicion[0]) + "," + str(self.posicion[1])] = "R"
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos, nuevoCache)

rows, columns, position, boxes_positions, board = leerArchivo()

initialState = State(rows, columns, position, boxes_positions, board, [], {})

print(initialState.posicion)
print(initialState.jugadasValidas())
print(initialState.ubicaciones_cajas)
print(initialState.lugaresCajaIdeales())
print(initialState.ganeElJuego())
print(initialState.estoyEnUnDeadlock())

newState = initialState.nuevoEstado('D')

print("----------------------------------------")

print(newState.posicion)
print(newState.jugadasValidas())
print(newState.ubicaciones_cajas)
print(newState.lugaresCajaIdeales())
print(newState.ganeElJuego())
print(newState.estoyEnUnDeadlock())

