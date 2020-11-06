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
    char **tableroJuego;
  
  public:
    GameState(int filas_, int columnas_, char **tablero_);
    void gimme();
    void action();
};

#endif