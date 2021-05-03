<h1>TL;DR for this repo:</h1>
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" height="100" width="100">
<ul>
  <li><h4>Programming Language used:</h4>Python</li>
  <li><h4>Approximate date:</h4>Second semester of 2020</li>
  <li><h4>Purpose:</h4>This repository corresponds to the implementation of different search algorithms such as Breadth First Search, Depth First Search and Iterative deepening depth-first search for solving the Sokoban game. The input is a text file of the configuration of the Sokoban game map, and the program gives you the opportunity of choosing from what algorithm you want to use to solve the problem. The output is a string of L,D,U,R (left, down, up and right) which are the movements that the player has to do in order to solve the game. To run the program, you must execute the run.sh script, the first argument should be the text file of the level game and the second argument the algorithm (DFS, BFS or IDFS), i.e.:
  <code>
./run.sh nivel1.txt BFS
</code>
  And the output (the number at the end of the string corresponds to the number of steps to solve the game, the depth of the tree at the solution):
  <code>
RDLDDRRRUULLRRDDLLUDRRUULULLDRDDLU 34
</code></li>
  <li><h4>Preview:</h4></li>
</ul>
<p align="center">
    <img src="https://www.numuki.com/game/img/sokoban-1735.jpg">
</p>
<p align="center">
    <img src="https://i.ibb.co/LnWxWwm/Screenshot-from-2021-05-03-11-53-36.png">
</p>
<p align="center">
    <img src="https://i.ibb.co/Zg0bysH/Screenshot-from-2021-05-03-11-53-36.png">
</p>
