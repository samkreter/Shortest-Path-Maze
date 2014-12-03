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
    self.count = 0



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

    self.printMatrix()##############print the matrix with each iteration

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
            if self.matrix[indm-1][inda] == " ":
              self.graph[(indm,inda)].append((indm-1,inda))
            if self.matrix[indm][inda-1] == " ":
              self.graph[(indm,inda)].append((indm,inda-1))
            if self.matrix[indm+1][inda] == " ":
              self.graph[(indm,inda)].append((indm+1,inda))
            if self.matrix[indm][inda+1] == " ":
              self.graph[(indm,inda)].append((indm,inda+1))
          if elem == "E":
            self.end = (indm,inda)
          if elem == "S":
            self.start = (indm,inda)
