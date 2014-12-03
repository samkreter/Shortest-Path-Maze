from Matrix import Matrix


m = Matrix("hey.txt")
m.createGraph()
m.dfs(m.start)
print " "
m.findShortestPath()
print m.sPath
