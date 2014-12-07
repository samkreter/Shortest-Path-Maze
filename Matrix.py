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
    self.parentMap = {}
    self.sPath = []


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
          print "Start = ",self.start
        if elem == "E":
          self.end = (indm,inda)
          print "End = ",self.end


  #dfs using a stack to find paths
  def dfs(self):
    stack = []
    visited = []
    stack.append(self.start)
    while stack:
      parent = stack.pop()
      print parent
      if parent in visited:
        continue
      visited.append(parent)
      children = self.getChildren(parent)
      for child in children:
        stack.append(child)
        if child in self.parentMap:
          print "#########################################"
        self.parentMap[child] = parent

    self.returnPath()


  def getChildren(self,parent):
    indm = parent[0]
    inda = parent[1]
    children = []
    #check child to the left of parent
    try:
      if self.matrix[indm-1][inda] == " " or self.matrix[indm-1][inda] == "E":
        children.append((indm-1,inda))
    except IndexError:
      pass

    try:
      if self.matrix[indm][inda-1] == " " or self.matrix[indm][inda-1] == "E":
        children.append((indm,inda-1))
    except IndexError:
      pass

    try:
      if self.matrix[indm+1][inda] == " " or self.matrix[indm+1][inda] == "E":
        children.append((indm+1,inda))
    except IndexError:
      pass

    try:
      if self.matrix[indm][inda+1] == " " or self.matrix[indm][inda+1] == "E":
        children.append((indm,inda+1))
    except IndexError:
      pass

    return children


  def returnPath(self):
    pprint(self.parentMap)
    # curr = self.end
    # while curr:
    #   self.sPath.append(curr)
    #   curr = self.parentMap[curr]
    # self.showPath()




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
