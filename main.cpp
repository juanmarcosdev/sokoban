#include <stdlib.h>
#include <iostream>
#include "GameState.h"

using namespace std;

int main()
{
    GameState G(1, 2);
    cout << G.getX() << endl;
    G.sumX();
    cout << G.getX() << endl;
}