import sys
from collections import deque 

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1

def ubicacionesCajaToString(arreglo):
    string = ""
    for i in range(0,len(arreglo)):
        string = string + "(" + str(arreglo[i][0]) + "," + str(arreglo[i][1]) + ")"
    return string

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
    def __init__(self, filas, columnas, posicion, ubicaciones_cajas, tablero, movimientos, profundidad):
        self.filas = filas
        self.columnas = columnas
        self.posicion = posicion
        self.ubicaciones_cajas = ubicaciones_cajas
        self.tablero = tablero
        self.movimientos = movimientos
        self.lugares_ideales = self.lugaresCajaIdeales()
        self.profundidad = profundidad
    
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

        if([self.posicion[0]-1,self.posicion[1]] in self.ubicaciones_cajas and (self.tablero[self.posicion[0]-2][self.posicion[1]] == 'W' or [self.posicion[0]-2,self.posicion[1]] in self.ubicaciones_cajas)):
            jugadas_validas.remove('U')
        if([self.posicion[0]+1,self.posicion[1]] in self.ubicaciones_cajas and (self.tablero[self.posicion[0]+2][self.posicion[1]] == 'W' or [self.posicion[0]+2,self.posicion[1]] in self.ubicaciones_cajas)):
            jugadas_validas.remove('D')
        if([self.posicion[0],self.posicion[1]-1] in self.ubicaciones_cajas and (self.tablero[self.posicion[0]][self.posicion[1]-2] == 'W' or [self.posicion[0],self.posicion[1]-2] in self.ubicaciones_cajas)):
            jugadas_validas.remove('L')
        if([self.posicion[0],self.posicion[1]+1] in self.ubicaciones_cajas and (self.tablero[self.posicion[0]][self.posicion[1]+2] == 'W' or [self.posicion[0],self.posicion[1]+2] in self.ubicaciones_cajas)):
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
                for i in range(0,len(nuevasCajas)):
                    if(nuevasCajas[i] == newPosicion):
                        nuevasCajas[i] = [newPosicion[0]-1, newPosicion[1]]
            nuevosMovimientos = self.movimientos.copy()
            nuevosMovimientos.append('U')
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos, self.profundidad + 1)
        
        elif(movimiento == 'D'):
            newPosicion = [self.posicion[0]+1, self.posicion[1]]
            nuevasCajas = self.ubicaciones_cajas.copy()
            if(newPosicion in nuevasCajas):
                for i in range(0,len(nuevasCajas)):
                    if(nuevasCajas[i] == newPosicion):
                        nuevasCajas[i] = [newPosicion[0]+1, newPosicion[1]]
            nuevosMovimientos = self.movimientos.copy()
            nuevosMovimientos.append('D')
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos, self.profundidad + 1)
        
        elif(movimiento == 'L'):
            newPosicion = [self.posicion[0], self.posicion[1]-1]
            nuevasCajas = self.ubicaciones_cajas.copy()
            if(newPosicion in nuevasCajas):
                for i in range(0,len(nuevasCajas)):
                    if(nuevasCajas[i] == newPosicion):
                        nuevasCajas[i] = [newPosicion[0], newPosicion[1]-1]
            nuevosMovimientos = self.movimientos.copy()
            nuevosMovimientos.append('L')
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos, self.profundidad + 1)
        
        elif(movimiento == 'R'):
            newPosicion = [self.posicion[0], self.posicion[1]+1]
            nuevasCajas = self.ubicaciones_cajas.copy()
            if(newPosicion in nuevasCajas):
                for i in range(0,len(nuevasCajas)):
                    if(nuevasCajas[i] == newPosicion):
                        nuevasCajas[i] = [newPosicion[0], newPosicion[1]+1]
            nuevosMovimientos = self.movimientos.copy()
            nuevosMovimientos.append('R')
            return State(self.filas, self.columnas, newPosicion, nuevasCajas, self.tablero, nuevosMovimientos, self.profundidad + 1,)

rows, columns, position, boxes_positions, board = leerArchivo()

initialState = State(rows, columns, position, boxes_positions, board, [], 0)

def BFS():
    queue = deque()
    queue.append(initialState)
    visited = set()
    while queue:
        currentState = queue.popleft()
        if(currentState.profundidad > 64):
            continue
        visited.add(str(currentState.posicion[0]) + "," + str(currentState.posicion[1]) + ubicacionesCajaToString(currentState.ubicaciones_cajas))
        if(currentState.estoyEnUnDeadlock()):
            continue
        else:
            if(currentState.ganeElJuego()):
                break
            jugadas_validas = currentState.jugadasValidas()
            for item in jugadas_validas:
                tempState = currentState.nuevoEstado(item)
                if(str(tempState.posicion[0]) + "," + str(tempState.posicion[1]) + ubicacionesCajaToString(tempState.ubicaciones_cajas) in visited):
                    continue
                else:
                    queue.append(tempState)
    return currentState

def DFS():
    stack = deque([initialState])
    visited = set()
    while stack:
        currentState = stack.pop()
        if(currentState.profundidad > 64):
            continue
        visited.add(str(currentState.posicion[0]) + "," + str(currentState.posicion[1]) + ubicacionesCajaToString(currentState.ubicaciones_cajas))
        if(currentState.estoyEnUnDeadlock()):
            continue
        else:
            if(currentState.ganeElJuego()):
                break
            jugadas_validas = currentState.jugadasValidas()
            jugadas_validas.reverse()
            for item in jugadas_validas:
                tempState = currentState.nuevoEstado(item)
                if(str(tempState.posicion[0]) + "," + str(tempState.posicion[1]) + ubicacionesCajaToString(tempState.ubicaciones_cajas) in visited):
                    continue
                else:
                    stack.append(tempState)
    return currentState

def IDFS():
    stack = deque()
    stack.append(initialState)
    visited = set()
    while stack:
        currentState = stack.pop()
        if(currentState.profundidad > 64):
            continue
        visited.add(str(currentState.posicion[0]) + "," + str(currentState.posicion[1]) + ubicacionesCajaToString(currentState.ubicaciones_cajas))
        if(currentState.estoyEnUnDeadlock()):
            continue
        else:
            if(currentState.ganeElJuego()):
                break
            jugadas_validas = currentState.jugadasValidas()
            jugadas_validas.reverse()
            for item in jugadas_validas:
                tempState = currentState.nuevoEstado(item)
                if(str(tempState.posicion[0]) + "," + str(tempState.posicion[1]) + ubicacionesCajaToString(tempState.ubicaciones_cajas) in visited):
                    continue
                else:
                    stack.append(tempState)
    return currentState


algoritmo = sys.argv[2]
if(algoritmo == "BFS"):
    bfsResponse = BFS()
    print(listToString(bfsResponse.movimientos))
if(algoritmo == "DFS"):
    dfsResponse = DFS()
    print(listToString(dfsResponse.movimientos))
if(algoritmo == "IDFS"):
    idfsResponse = IDFS()
    print(listToString(idfsResponse.movimientos))
