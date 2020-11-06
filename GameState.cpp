#include <stdlib.h>
#include <iostream>
#include "GameState.h"
#include <memory>

using namespace std;

GameState::GameState(int filas_, int columnas_, char **tablero_)
{
    this->filas = filas_;
    this->columnas = columnas_;
    this->tableroJuego = tablero_;
}

void GameState::gimme()
{
    cout << this->filas << endl;
    cout << this->columnas << endl;
    for(int i = 0; i < this->filas; ++i)
    {
        for(int j = 0; j < this->columnas; ++j)
        {
            cout << this->tableroJuego[i][j];
        }
        cout << endl;
    }
}

void GameState::action()
{
    this->tableroJuego[0][0] = 'S';
}