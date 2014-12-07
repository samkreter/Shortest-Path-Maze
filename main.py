from Matrix import Matrix


m = Matrix("hey.txt")
m.createGraph()
#m.printGraph()
m.dfs()
print " "
m.findShortestPath()
print m.sPath
m.showPath()
m.printMatrix()
