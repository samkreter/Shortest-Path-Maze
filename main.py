from Matrix import Matrix
import time

#used to find the execution time of the program 
start_time = time.time()

m = Matrix("maze.txt")
m.dfs()

print "Execution Time = ",time.time() - start_time
