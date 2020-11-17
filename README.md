The Maze Problem

A python program that runs as a command-line tool. It takes the input and output file name as command-line arguments. Using the square matrix present in the input file it generates a path to reach the end of the maze and put it in the output file. If the maze is unsolvable, it returns -1 as the only value in the output file.

Given a mxn matrix where each element can either be 0 or 1. The path can only be created out of a cell if its value is 1. 0 will be considered as dead-end and 1 means the block can be used in the path from source to destination.
Approach-
1)The program uses queue and breadth first search application(bfs) to check if a path exists between the starting and ending points and print them with the total number of paths that are possible with that matrix
2)It uses Object oriented programming(OOPs) format.

Input-
First, we enter no. of rows in the matrix and then no. of columns in the terminal, followed by the matrix (integers with 1 space distance and next row in next line)

Output-
It prints one of the possible paths.


Code implementation-
summary-It first makes a solution matrix equal to the size of the given matrix, initially all values are kept 0 inside it. A queue is made using deque() function, Deque (Doubly Ended Queue) in Python is implemented using the module “collections“ and (0, 0) is inserted into the queue.
 *(Deque is preferred over list where we need quicker append and pop operations from both either ends, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. )
 
Now it keeps popping pairs from the queue and storing them in variable p, if the popped value is the end of the matrix then increment count and print the possible path, otherwise mark all the points we have visited while traversing the path as 1.

And then check if the next column can give a valid move or the next row can give a valid move and according to that, insert the corresponding row, column pair into the queue.when the queue is empty it comes out of the loop.
At last count is returned.
given sample input # 1 0 0 0
                    # 1 1 0 1
                    # 0 1 0 0
                    # 1 1 1 1
given sample output # 1 0 0 0
                     # 1 1 0 0
                     # 0 1 0 0
                     # 0 1 1 1
No. of possible paths are 1
It prints -1 when there are no possible paths between the start and end points and return no. of possible paths as 0.
Code:
There is a class Solution which contains two functions Maze and printSolution.
Maze function takes m (no. of rows) and n (no. of columns) and matrix and printSolution prints the solution matrix.
