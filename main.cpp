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
    cout << filas << endl;
    cout << columnas << endl;
    cout << datos << endl;
    char tablero[filas][columnas];
    int coordenadas[datos][2];
    ifstream file3(argv[1]);
    int contador = 0;
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
            }
        }
        file3.close();
    }
    for(int i = 0; i < filas; i++)
    {
        for(int j = 0; j < columnas; j++)
        {
            cout << tablero[i][j];
        }
        cout << endl;
    }
}