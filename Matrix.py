from pprint import pprint

class Matrix:

  #takes in a filepath and creates the self.matrix from the text file
  def __init__(self,filePath):
    matrix = []
    for line in open(filePath):
      temp = []
      for c in line:
        temp.append(c)
      matrix.append(temp)
    self.matrix = matrix
    self.getPoints()


  #prints the matrix given to it on the screen
  def printMatrix(self):
    for array in self.matrix:
      for elem in array:
        print elem,
      print

  def getPoints(self):
    for indm, array in enumerate(self.matrix):
      for inda, elem in enumerate(array):
        if elem == "S":
          self.start = (indm,inda)
        if elem == "E":
          self.end = (indm,inda)


  #dfs using a stack to find paths
  def dfs(self):
    path=[]
    stack = []
    visited = []
    stack.append(self.start)
    while stack:
      parent = stack.pop()
      if parent in visited:
        continue
      visited.append(parent)
      children = self.getChildren(parent)
      for child in children:
        stack.append(child)


  def getChildren(self,parent):
    try:
      if()
    except IndexError:
      gotdata = 'null'



  #from the paths found from the DFS will pick the shortest path
  def findShortestPath(self):
    self.sPath = self.paths[0]
    sLength = len(self.paths[0]);
    for path in self.paths:
      if len(path) < sLength:
        sLength = len(path)
        self.sPath = path

  #puts the paths on the matrix to display to the user
  def showPath(self):
    for steps in self.sPath:
      self.matrix[steps[0]][steps[1]] = "+"
