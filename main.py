from Matrix import Matrix


m = Matrix("maze.txt")
m.createGraph()
m.printGraph()
print m.start ,m.end
