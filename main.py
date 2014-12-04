from Matrix import Matrix


m = Matrix("hey.txt")
m.createGraph()
# m.printGraph()
m.dfs(m.start)
print " "
m.findShortestPath()
print m.sPath
