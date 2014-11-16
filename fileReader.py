def makeMatrix():

  matrix = []


  for line in open("maze.txt"):
    temp = []
    for c in line:
      temp.append(c);
    matrix.append(temp);

  return matrix;



matrix = makeMatrix()
for array in matrix:
  print array
