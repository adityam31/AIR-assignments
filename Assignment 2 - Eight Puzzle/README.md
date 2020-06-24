# Eight Puzzle Problem

## Explanation, Links, References

You can implement this using BFS or A*

Solving using BFS:
In our 8-Puzzle problem, we can define the h-score as the number of misplaced tiles by comparing the current state and the goal state<br>
or<br>
summation of the Manhattan distance between misplaced nodes.<br>

Solving using A star:
h-score same as above.<br>
g-score will be number of nodes traversed from start node to get to the current node.<br>
https://www.youtube.com/watch?v=PTqN_Qe2_zQ

import copy
use deepcopy function to create copy of 2D array<br>
https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
