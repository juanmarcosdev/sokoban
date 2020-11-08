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

def DFS(state):
    visited = set()
    stack = []
    stack.append(state)
    while(len(stack) != 0):
        currentState = stack[0]
        visited.add(str(currentState.posicion[0]) + "," + str(currentState.posicion[1]))
        if(currentState.ganeElJuego()):
            break
        else:
            if(currentState.estoyEnUnDeadlock()):
                stack.pop(0)
                continue
            else:
                validMoves = currentState.jugadasValidas()
                for i in range(0,len(validMoves)):
                    temporalState = currentState.nuevoEstado(validMoves[i])
                    if(str(temporalState.posicion[0]) + "," + str(temporalState.posicion[1]) in visited):
                        continue
                    else:
                        stack.append(temporalState)
                stack.pop(0)
    print(currentState.lugares_ideales)
    print(currentState.ubicaciones_cajas)
    return currentState.movimientos

# print(DFS(initialState))

print(initialState.posicion)
print(initialState.movimientos)
print(initialState.jugadasValidas())
print(initialState.lugares_ideales)
print(initialState.ubicaciones_cajas)

# print("------------------------------")

# newState = initialState.nuevoEstado('D')

# print(newState.posicion)
# print(newState.movimientos)
# print(newState.jugadasValidas())

# print("------------------------------")

# newState2 = initialState.nuevoEstado('R')

# print(newState2.posicion)
# print(newState2.movimientos)
# print(newState2.jugadasValidas())