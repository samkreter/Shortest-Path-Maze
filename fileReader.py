
#makes the map matrix from the file
class qObj:
  def _init_(self,coords,steps):
    self.coord1 = coord1
    self.coord2 = coord2
    self.steps = steps


class Matrix:

  #takes in a filepath and creates the self.matrix from the text file
  def _init_(self,filePath):
    matrix = []
    for line in open(filePath):
      temp = []
      for c in line:
        temp.append(c);
      matrix.append(temp);
    self.matrix = matrix


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


m = Matrix()
m.printMatrix()
