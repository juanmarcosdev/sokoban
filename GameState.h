#ifndef HH_GameState
#define HH_GameState

#include <stdlib.h>
#include <iostream>

using namespace std;

class GameState
{
  private:
    int filas;
    int columnas;
    int numero_cajas;
    char **tableroJuego;
    int *posicionJugador;
    int **posicionesInicialesCajas;
  
  public:
    GameState(int filas_, int columnas_, int numerocajas_, char **tablero_, int *posJugador, int **posInicialesBoxes);
    void gimme();
    void action();
    GameState copy();
};

#endif