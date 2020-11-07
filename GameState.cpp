#include <stdlib.h>
#include <iostream>
#include "GameState.h"
#include <memory>

using namespace std;

GameState::GameState(int filas_, int columnas_, int numerocajas_, char **tablero_, int *posJugador, int **posInicialesBoxes_)
{
    this->filas = filas_;
    this->columnas = columnas_;
    this->numero_cajas = numerocajas_;
    this->tableroJuego = tablero_;
    this->posicionJugador = posJugador;
    this->posicionesInicialesCajas = posInicialesBoxes_;
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
    cout << this->posicionJugador[0] << this->posicionJugador[1] << endl;
    for(int i = 0; i < this->numero_cajas; ++i)
    {
        for(int j = 0; j < 2; ++j)
        {
            cout << this->posicionesInicialesCajas[i][j];
        }
        cout << endl;
    }
}

void GameState::action()
{
    this->tableroJuego[0][0] = 'S';
}

GameState GameState::copy()
{
    GameState copia(this->filas, this->columnas, this->numero_cajas, this->tableroJuego, this->posicionJugador, this->posicionesInicialesCajas);
    return copia;
}