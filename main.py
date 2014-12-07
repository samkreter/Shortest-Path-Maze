from Matrix import Matrix
import time
import sys

#used to find the execution time of the program
start_time = time.time()

try:
  file = sys.argv[1]
except IndexError:
  file = raw_input("Please enter a file name with the maze: ")

m = Matrix(file)
m.dfs()

print "Execution Time = ",time.time() - start_time
