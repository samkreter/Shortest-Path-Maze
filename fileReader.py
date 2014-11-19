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
    self.graph = {}



  #prints the matrix given to it on the screen
  def printMatrix(self):
    for array in self.matrix:
      for elem in array:
        print elem,
      print


  #creates the graph from the matrix and finds the start and end points
  def createGraph(self):
    for indm, array in enumerate(self.matrix):
      for inda, elem in enumerate(array):       ############check this weird -2 thing#######
        if inda != 0 and indm != 0 and indm < len(self.matrix)-2 and inda < len(array):
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

m = Matrix("hey.txt")
m.createGraph()
pprint(m.graph)
