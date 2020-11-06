#include <stdlib.h>
#include <iostream>
#include <typeinfo>
#include "GameState.h"
#include <fstream>
#include <stdio.h>
#include <ctype.h>

using namespace std;

int main(int argc, char* argv[])
{
    // Inicio: Leer archivo
    int filas = 0;
    int columnas = 0;
    int datos = 0;
    ifstream file(argv[1]);
    if(file.is_open()) {
        string line;
        getline(file, line);
        columnas = line.length();
        file.close();
    }
    ifstream file2(argv[1]);
    if(file2.is_open()) {
        string line;
        while(getline(file2, line)) {
            if(line.length() != 3)
            {
                filas++;
            }
            if(line.length() == 3)
            {
                datos++;
            } 
        }
        file.close();
    }
    char tablero[filas][columnas];
    int coordenadas[datos-1][2];
    int posicion[2];
    ifstream file3(argv[1]);
    int contador = 0;
    int contador2 = 0;
    int contador3 = 0;
    if(file3.is_open()) {
        string line;
        while(getline(file3, line)) {
            if(line.length() != 3)
            {
                for(int i = 0; i < line.length(); i++)
                {
                    tablero[contador][i] = line[i];
                } 
                contador++;
            } else if(line.length() == 3 && contador2 == 0)
            {
                posicion[0] = line[0] - '0';
                posicion[1] = line[2] - '0';
                contador2++;
            } else if(line.length() == 3 && contador2 != 0)
            {
                coordenadas[contador3][0] = line[0] - '0';
                coordenadas[contador3][1] = line[2] - '0';
                contador3++;
            }
        }
        file3.close();
    }
    // Fin: Leer archivo
    // Tablero de juego almacenado en matriz "tablero"
    // Coordenadas iniciales de las cajas guardadas en "coordenadas"
    // Posicion inicial del jugador en "posicion"
    GameState juego(filas, columnas);
    juego.gimme();
}