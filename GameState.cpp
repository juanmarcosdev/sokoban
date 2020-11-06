#include <stdlib.h>
#include <iostream>
#include "GameState.h"

GameState::GameState(int x1, int y1)
{
    this->x = x1;
    this->y = y1;
}

int GameState::getX()
{
    return this->x;
}

void GameState::sumX()
{
    this->x = this->x + 1;
} 