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
        getline(file, line);
        anchoTablero = line.length();
        file.close();
    }
    ifstream file2(argv[1]);
    if(file2.is_open()) {
        string line;
        while(getline(file2, line)) {
            if(line.length() != 3)
            {
                largoTablero++;
            }
        }
        file.close();
    }
    cout << largoTablero << endl;
    cout << anchoTablero << endl;
}