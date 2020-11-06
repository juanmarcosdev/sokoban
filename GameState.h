#ifndef HH_GameState
#define HH_GameState

#include <stdlib.h>
#include <iostream>
using namespace std;

class GameState
{
  private:
  int x;
  int y;
  
  public:
  GameState(int x1, int y1);
  int getX();
  void sumX();

};

#endif