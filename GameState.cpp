#include <stdlib.h>
#include <iostream>
#include "GameState.h"

using namespace std;

GameState::GameState(int filas_, int columnas_)
{
    this->filas = filas_;
    this->columnas = columnas_;
}

void GameState::gimme()
{
    cout << this->filas << endl;
    cout << this->columnas << endl;
}
