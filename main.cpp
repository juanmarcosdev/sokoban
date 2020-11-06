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
    int largoTablero = 0;
    int anchoTablero = 0;
    ifstream file(argv[1]);
    if(file.is_open()) {
        string line;
        while(getline(file, line)) {
            cout << line.length() << endl;
        }
        file.close();
    }
}