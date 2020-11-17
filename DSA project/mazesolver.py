from collections import deque
class Solution:
      
  def Maze(self,matrix):
#making a solution-matrix whose size is equal to the given matrix
    m=len(matrix[0])
    n=len(matrix)
    solution=[[0] * m for _ in range(n)]
#using deque module to create a queue and appending(0,0)
    q=deque() 
    q.append((0, 0))
    #initializing count  
    count=0
    while (len(q) > 0):     
        p = q.pop() 
#When program reaches end, count is incremented and resultant solution is printed.
        if (p[0] == n - 1 and p[1] == m - 1):
            solution[p[0]][p[1]]=1 
            count+=1
            return sol.PrintSolution(solution)
            
            
#if the path is 1 on given matrix then marking them on solution matrix
        if p[0]>=0 and p[1]>=0 and p[0]<n and p[1]<m and solution[p[0]][p[1]]==0 and matrix[p[0]][p[1]]==1:
          solution[p[0]][p[1]]=1
          
          #finding the next path
          #right
          if (p[0] + 1 < n and
              matrix[p[0]+1][p[1]] == 1): 
              q.append((p[0]+1, p[1]))
          #finding the next path
          #down
          if (p[1] + 1 < m and 
              matrix[p[0]][p[1]+1] == 1): 
              q.append((p[0], p[1] + 1))
#for count value zero it prints -1 i.e. there are no solutions. 
    if count==0:
      print(-1)         
  
#for printing the Solution matrix
  def PrintSolution(self,solution):
    for i in solution:
      print(i)  
#*******************************************************************
sol=Solution()

import fileinput
matrix=[]
for line in fileinput.input(files=('inputfile.txt')):
    c=list(map(int,line.split())) 
    matrix.append(c)
sol.Maze(matrix) 


