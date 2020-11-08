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
    def __init__(self, filas, columnas, posicion, ubicaciones_cajas, tablero, movimientos):
        self.filas = filas
        self.columnas = columnas
        self.posicion = posicion
        self.ubicaciones_cajas = ubicaciones_cajas
        self.tablero = tablero
        self.movimientos = movimientos
        self.lugares_ideales = self.lugaresCajaIdeales()
    
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
        
        for item in jugadas_validas:
            if(item == 'U'):
                if([self.posicion[0]-1, self.posicion[1]] in self.ubicaciones_cajas):
                    if([self.posicion[0]-2, self.posicion[1]] in self.ubicaciones_cajas or self.tablero[self.posicion[0]-2][self.posicion[1]] == 'W'):
                        jugadas_validas.remove('U')
            if(item == 'D'):
                if([self.posicion[0]+1, self.posicion[1]] in self.ubicaciones_cajas):
                    if([self.posicion[0]+2, self.posicion[1]] in self.ubicaciones_cajas or self.tablero[self.posicion[0]+2][self.posicion[1]] == 'W'):
                        jugadas_validas.remove('D')
            if(item == 'L'):
                if([self.posicion[0], self.posicion[1]-1] in self.ubicaciones_cajas):
                    if([self.posicion[0], self.posicion[1]-2] in self.ubicaciones_cajas or self.tablero[self.posicion[0]][self.posicion[1]-2] == 'W'):
                        jugadas_validas.remove('L')
            if(item == 'R'):
                if([self.posicion[0], self.posicion[1]+1] in self.ubicaciones_cajas):
                    if([self.posicion[0], self.posicion[1]+2] in self.ubicaciones_cajas or self.tablero[self.posicion[0]][self.posicion[1]+2] == 'W'):
                        jugadas_validas.remove('R')
                

        return jugadas_validas
    
    def lugaresCajaIdeales(self):
        lugares_ideales = []
        for i in range(0,self.filas):
            for j in range(0,self.columnas):
                if(self.tablero[i][j] == 'X'):
                    lugares_ideales.append([i,j])
        return lugares_ideales
    
    def ganeElJuego(self):
        flag = True
        for i in range(0,len(self.lugares_ideales)):
            if(self.lugares_ideales[i] in self.ubicaciones_cajas):
                continue
            else:
                flag = False
        return flag

    def estoyEnUnDeadlock(self):
        for i in range(0,len(self.ubicaciones_cajas)):
            if(self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]+1] == 'W' and self.tablero[self.ubicaciones_cajas[i][0]+1][self.ubicaciones_cajas[i][1]] == 'W'):
                return True
            elif(self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]-1] == 'W' and self.tablero[self.ubicaciones_cajas[i][0]+1][self.ubicaciones_cajas[i][1]] == 'W'):
                return True
            elif(self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]-1] == 'W' and self.tablero[self.ubicaciones_cajas[i][0]-1][self.ubicaciones_cajas[i][1]] == 'W'):
                return True
            elif(self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]+1] == 'W' and self.tablero[self.ubicaciones_cajas[i][0]-1][self.ubicaciones_cajas[i][1]] == 'W'):
                return True
            elif((self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]+1] == 'W' or [self.ubicaciones_cajas[i][0],self.ubicaciones_cajas[i][1]+1] in self.ubicaciones_cajas) and (self.tablero[self.ubicaciones_cajas[i][0]+1][self.ubicaciones_cajas[i][1]] == 'W' or [self.ubicaciones_cajas[i][0]+1,self.ubicaciones_cajas[i][1]] in self.ubicaciones_cajas) and (self.tablero[self.ubicaciones_cajas[i][0]+1][self.ubicaciones_cajas[i][1]+1] == 'W' or [self.ubicaciones_cajas[i][0]+1,self.ubicaciones_cajas[i][1]+1] in self.ubicaciones_cajas)):
                return True
            elif((self.tablero[self.ubicaciones_cajas[i][0]][self.ubicaciones_cajas[i][1]-1] == 'W' or [self.ubicaciones_cajas[i][0],self.ubicaciones_cajas[i][1]-1] in self.ubicaciones_cajas) and (self.tablero[self.ubicaciones_cajas[i][0]-1][self.ubicaciones_cajas[i][1]] == 'W' or [self.ubicaciones_cajas[i][0]-1,self.ubicaciones_cajas[i][1]] in self.ubicaciones_cajas) and (self.tablero[self.ubicaciones_cajas[i][0]-1][self.ubicaciones_cajas[i][1]-1] == 'W' or [self.ubicaciones_cajas[i][0]-1,self.ubicaciones_cajas[i][1]-1] in self.ubicaciones_cajas)):
                return True
            else:
                return False

    
    def nuevoEstado(self, movimiento):
        if(movimiento == 'U'):
            newPosicion = [self.posicion[0]-1, self.posicion[1]]
            nuevasCajas = self.ubicaciones_cajas.copy()
            if(newPosicion in nuevasCajas):
                nuevasCajas.remove(newPosicion)
                nuevasCajas.append([newPosicion[0]-1, newPosicion[1]])
            nuevosMovimientos = self.movimientos.copy()
            nuevosMovimientos.append('U')
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos)
        
        elif(movimiento == 'D'):
            newPosicion = [self.posicion[0]+1, self.posicion[1]]
            nuevasCajas = self.ubicaciones_cajas.copy()
            if(newPosicion in nuevasCajas):
                nuevasCajas.remove(newPosicion)
                nuevasCajas.append([newPosicion[0]+1, newPosicion[1]])
            nuevosMovimientos = self.movimientos.copy()
            nuevosMovimientos.append('D')
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos)
        
        elif(movimiento == 'L'):
            newPosicion = [self.posicion[0], self.posicion[1]-1]
            nuevasCajas = self.ubicaciones_cajas.copy()
            if(newPosicion in nuevasCajas):
                nuevasCajas.remove(newPosicion)
                nuevasCajas.append([newPosicion[0], newPosicion[1]-1])
            nuevosMovimientos = self.movimientos.copy()
            nuevosMovimientos.append('L')
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos)
        
        elif(movimiento == 'R'):
            newPosicion = [self.posicion[0], self.posicion[1]+1]
            nuevasCajas = self.ubicaciones_cajas.copy()
            if(newPosicion in nuevasCajas):
                nuevasCajas.remove(newPosicion)
                nuevasCajas.append([newPosicion[0], newPosicion[1]+1])
            nuevosMovimientos = self.movimientos.copy()
            nuevosMovimientos.append('R')
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos)

rows, columns, position, boxes_positions, board = leerArchivo()

initialState = State(rows, columns, position, boxes_positions, board, [])

# print(initialState.posicion)
# print(initialState.jugadasValidas())
# print(initialState.ubicaciones_cajas)

# newState = initialState.nuevoEstado('D')

# print(newState.posicion)
# print(newState.jugadasValidas())
# print(newState.ubicaciones_cajas)

# newState2 = newState.nuevoEstado('R')

# print(newState2.posicion)
# print(newState2.jugadasValidas())
# print(newState2.ubicaciones_cajas)




