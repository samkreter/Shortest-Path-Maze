
#makes the map matrix from the file
def makeMatrix():

  matrix = []


  for line in open("maze.txt"):
    temp = []
    for c in line:
      temp.append(c);
    matrix.append(temp);

  return matrix;

#prints the matrix given to it on the screen
def printMatrix(matrix):
  for array in matrix:
    for elem in array:
      print elem,
    print

def findE(matrix):
   for index, array in enumerate(matrix):
     if "E" in array:
       coords = [index,array.index("E")]
