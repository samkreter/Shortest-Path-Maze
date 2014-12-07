#recursive function to find a path through a maze
#takes a matrix, and nedds startx and starty

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
