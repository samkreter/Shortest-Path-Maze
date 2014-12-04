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
    self.getStart()
    self.graph = {}
    self.paths = []
    self.sPath = []



  def printGraph(self):
    pprint(self.graph)

  #prints the matrix given to it on the screen
  def printMatrix(self):
    for array in self.matrix:
      for elem in array:
        print elem,
      print

  def getStart(self):
    for indm, array in enumerate(self.matrix):
      for inda, elem in enumerate(array):
        if elem == "S":
          self.startx = indm
          self.starty = inda
          print "found start at ",indm," ",inda

  def findPath(self,x,y):
    #should never be used but check bounds
    if(x >= len(self.matrix) or x < 0):
      return False
    if(y >= len(self.matrix[x]) or y < 0):
      return False

    if(self.matrix[x][y] == "#" or self.matrix[x][y] == "+"):
      return False
    #check if found the end
    if(self.matrix[x][y] == "E"):
      return True

    #mark the path
    self.matrix[x][y] = "+"
    if(self.findPath(x+1,y)):
      return True
    if(self.findPath(x,y-1)):
      return True
    if(self.findPath(x-1,y)):
      return True
    if(self.findPath(x,y+1)):
      return True

    #if all directions are face
    self.matrix[x][y] = " "
    return False


  #creates the graph from the matrix and finds the start and end points
  def createGraph(self):
    for indm, array in enumerate(self.matrix):
      for inda, elem in enumerate(array):       ############check this weird -2 thing#######
        if inda != 0 and indm != 0 and indm < len(self.matrix)-1 and inda < len(array)-1:
          if elem == " " or elem == "E" or elem == "S":
            self.graph[(indm,inda)] = []
            if self.matrix[indm-1][inda] == " " or self.matrix[indm-1][inda] == "E":
              self.graph[(indm,inda)].append((indm-1,inda))
            if self.matrix[indm][inda-1] == " " or self.matrix[indm][inda-1] == "E":
              self.graph[(indm,inda)].append((indm,inda-1))
            if self.matrix[indm+1][inda] == " " or self.matrix[indm+1][inda] == "E":
              self.graph[(indm,inda)].append((indm+1,inda))
            if self.matrix[indm][inda+1] == " " or self.matrix[indm][inda+1] == "E":
              self.graph[(indm,inda)].append((indm,inda+1))
          if elem == "E":
            self.end = (indm,inda)
            self.graph
          if elem == "S":
            self.start = (indm,inda)

  #Rescusive DFS that finds all paths from start to the end
  def dfs(self,start,path=[]):
    print start
    path = path+[start]
    if start == self.end:
      self.paths.append(path)
      return
    for node in self.graph[start]:
      if node not in path:
        self.dfs(node,path)

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
