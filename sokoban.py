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
    aux = []
    visited = set()
    while queue:
        currentState = queue.popleft()
        if(currentState.profundidad > 64):
            continue
        aux.append(currentState)
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
    return currentState, aux

def DFS():
    stack = deque()
    stack.append(initialState)
    aux = []
    visited = set()
    while stack:
        currentState = stack.pop()
        # if(currentState.posicion == [5,4] and currentState.profundidad == 52 and currentState.ubicaciones_cajas == [[4,4],[2,3]]):
        #         print("----------------------")
        #         print(currentState.posicion)
        #         print(currentState.ubicaciones_cajas)
        #         print(currentState.jugadasValidas())
        #         break
        if(currentState.profundidad > 64):
            continue
        aux.append(currentState)
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
                    # if(currentState.posicion == [5,4] and currentState.profundidad == 52 and currentState.ubicaciones_cajas == [[4,4],[2,3]]):
                    #     print("----------------------")
                    #     print("Me chulie a " + str(tempState.posicion) + " , movimiento: " + item + " isDeadlock: " + str(tempState.estoyEnUnDeadlock()))
                    continue
                else:
                    stack.append(tempState)
                    # if(currentState.posicion == [5,4] and currentState.profundidad == 52 and currentState.ubicaciones_cajas == [[4,4],[2,3]]):
                    #     print("----------------------")
                    #     print("Explorare " + str(tempState.posicion) + " , movimiento: " + item + " isDeadlock: " + str(tempState.estoyEnUnDeadlock()))
                    #     print(listToString(stack[len(stack)-1].movimientos))
    return currentState, aux


# bfsResponse, auxiliarBFS = BFS()
# print(listToString(bfsResponse.movimientos) + " " + str(bfsResponse.profundidad))

# DFS Level 3
# DDDRRURDRUULDDLLLUUURRURDULDDUURDDUULDDLULDDDRRUUDDRURULULDLLUR
dfsResponse, auxiliarDFS = DFS()
print(listToString(dfsResponse.movimientos) + " " + str(dfsResponse.profundidad) + " " + str(dfsResponse.ganeElJuego()) + " " + str(dfsResponse.jugadasValidas()))

# newState1 = dfsResponse.nuevoEstado('U')
# print(listToString(newState1.movimientos) + " " + str(newState1.profundidad) + " " + str(newState1.ganeElJuego()) + " " + str(newState1.jugadasValidas()))

# newState2 = newState1.nuevoEstado('R')
# print(listToString(newState2.movimientos) + " " + str(newState2.profundidad) + " " + str(newState2.ganeElJuego()) + " " + str(newState2.jugadasValidas()))

# newState3 = newState2.nuevoEstado('U')
# print(listToString(newState3.movimientos) + " " + str(newState3.profundidad) + " " + str(newState3.ganeElJuego()) + " " + str(newState3.jugadasValidas()))

# newState4 = newState3.nuevoEstado('L')
# print(listToString(newState4.movimientos) + " " + str(newState4.profundidad) + " " + str(newState4.ganeElJuego()) + " " + str(newState4.jugadasValidas()))

# newState5 = newState4.nuevoEstado('U')
# print(listToString(newState5.movimientos) + " " + str(newState5.profundidad) + " " + str(newState5.ganeElJuego()) + " " + str(newState5.jugadasValidas()))

# newState6 = newState5.nuevoEstado('L')
# print(listToString(newState6.movimientos) + " " + str(newState6.profundidad) + " " + str(newState6.ganeElJuego()) + " " + str(newState6.jugadasValidas()))

# newState7 = newState6.nuevoEstado('D')
# print(listToString(newState7.movimientos) + " " + str(newState7.profundidad) + " " + str(newState7.ganeElJuego()) + " " + str(newState7.jugadasValidas()))

# newState8 = newState7.nuevoEstado('L')
# print(listToString(newState8.movimientos) + " " + str(newState8.profundidad) + " " + str(newState8.ganeElJuego()) + " " + str(newState8.jugadasValidas()))

# newState9 = newState8.nuevoEstado('L')
# print(listToString(newState9.movimientos) + " " + str(newState9.profundidad) + " " + str(newState9.ganeElJuego()) + " " + str(newState9.jugadasValidas()))

# newState10 = newState9.nuevoEstado('U')
# print(listToString(newState10.movimientos) + " " + str(newState10.profundidad) + " " + str(newState10.ganeElJuego()) + " " + str(newState10.jugadasValidas()))

# newState11 = newState10.nuevoEstado('R')
# print(listToString(newState11.movimientos) + " " + str(newState11.profundidad) + " " + str(newState11.ganeElJuego()) + " " + str(newState11.jugadasValidas()))


# algoritmo = sys.argv[2]
# if(algoritmo == "BFS"):
#     bfsResponse, auxiliarBFS = BFS()
#     print(listToString(bfsResponse.movimientos))
# if(algoritmo == "DFS"):
#     dfsResponse, auxiliarDFS = DFS()
#     print(listToString(dfsResponse.movimientos))