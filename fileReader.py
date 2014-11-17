
#makes the map matrix from the file
class qObj:
  def _init_(self,coords,steps):
    self.coord1 = coord1
    self.coord2 = coord2
    self.steps = steps


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
    self.graph = {}
    self.start = 


  #prints the matrix given to it on the screen
  def printMatrix(self):
    for array in self.matrix:
      for elem in array:
        print elem,
      print

  def findE(self):
    for index, array in enumerate(self.matrix):
      if "E" in array:
        coords = [index,array.index("E")]
        return coords
    print "couldn't find E"

  def createGraph(self):
    for indm, array in enumerate(self.matrix):
      for inda, elem in enumerate(array):
        if elem == " ":
          self.graph[(indm,inda)] = [];



m = Matrix("maze.txt")
m.printMatrix()
