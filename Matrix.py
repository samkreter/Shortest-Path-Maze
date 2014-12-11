from pprint import pprint
import sys
import os.path
import random 

class Matrix:

  #takes in a filepath and creates the self.matrix from the text file
  def __init__(self,filePath):
    matrix = []
    while not os.path.exists(filePath):
      filePath = raw_input("File Does not exist, Please enter again: ")
    for line in open(filePath):
      temp = []
      for c in line:
        temp.append(c)
      matrix.append(temp)
    self.matrix = matrix
    self.getPoints()
    self.parentMap = {} #used to hold parents and the number of steps from the start
    self.sPath = [] #holds the shortest path
    self.countTime = 0


  #prints the matrix given to it on the screen
  def printMatrix(self):
    for array in self.matrix:
      for elem in array:
        print elem,
      print


  #gets the start and end points from the matrix, if they don't exist
  #if will exit the program
  def getPoints(self):
    self.start = "%"
    self.end = "%"
    for indm, array in enumerate(self.matrix):
      for inda, elem in enumerate(array):
        if elem == "S":
          self.start = (indm,inda)
          print "Start = ",self.start
        if elem == "E":
          self.end = (indm,inda)
          print "End = ",self.end

    #check if start and end exists in the matrix
    if self.start == "%" or self.end == "%":
      print "Either Start or End was not in maze"
      sys.exit()


  #dfs using a stack to find paths
  def dfs(self):
    stack = []
    visited = []
    stack.append(self.start)
    self.parentMap[self.start] = ["start",0]
    while stack:
      parent = stack.pop()
      if parent in visited:
        continue
      visited.append(parent)
      children = self.getChildren(parent)
      for child in children:
        stack.append(child)
        #checks if there is already a parent to replace if step count is lower
        if child in self.parentMap and self.parentMap[parent][1]+1 > self.parentMap[child][1]:
          continue
        else:
          self.parentMap[child] = [parent,self.parentMap[parent][1]+1]
          stack.append(parent)

    self.countTime = self.countTime + 1
    #check if there is no path from the start to the end
    if self.end not in self.parentMap:
      print "There is not path to the End"
      sys.exit()
    self.returnPath()
    if(self.countTime < 4):
      self.dfs()
    



  #used to get the connect children of the parent passed in
  #used try statments to catch out of index exceptions and treats them as walls
  def getChildren(self,parent):
    indm = parent[0]
    inda = parent[1]
    children = []
    funcList = []

      #checks to the top of the parent
    def checkTop(): 
      try:
        if self.matrix[indm+1][inda] == " " or self.matrix[indm+1][inda] == "E":
          children.append((indm+1,inda))
      except IndexError:
        pass

    def checkBottom():
      try:
        if self.matrix[indm-1][inda] == " " or self.matrix[indm-1][inda] == "E":
          children.append((indm-1,inda))
      except IndexError:
        pass
    
    #checks to the left of the parent
    def checkLeft():
      try:
        if self.matrix[indm][inda+1] == " " or self.matrix[indm][inda+1] == "E":
          children.append((indm,inda+1))
      except IndexError:
        pass

    #checks to the right of the parent
    def checkRight():
      try:
        if self.matrix[indm][inda-1] == " " or self.matrix[indm][inda-1] == "E":
          children.append((indm,inda-1))
      except IndexError:
        pass

    random.seed()
    funcOption1 = [checkBottom,checkTop,checkRight,checkLeft] 
    funcOption2 =  [checkLeft,checkBottom,checkTop,checkRight]
    funcOption3 = [checkRight,checkLeft,checkBottom,checkTop]
    funcOption4 = [checkTop,checkRight,checkLeft,checkBottom]

    funcList = [funcOption1,funcOption2,funcOption3,funcOption4]
  
    for f in funcList[self.countTime]:
      f()

    #return the children
    return children

  #returns the shorts path from the end
  def returnPath(self):
    curr = self.end
    temp = []
    print self.parentMap[curr][1]
    while curr != "start":
      temp.append(curr)
      curr = self.parentMap[curr][0]
    if(self.countTime == 1):
      self.sPath = temp[:]
    elif(len(temp) < len(self.sPath)):
      self.sPath = temp[:]


  #puts the paths on the matrix to display to the user
  def showPath(self):
    print "Step count for path is ",len(self.sPath)
    for steps in self.sPath:
      self.matrix[steps[0]][steps[1]] = "+"
    self.matrix[self.start[0]][self.start[1]] = "S"
    self.matrix[self.end[0]][self.end[1]] = "E"
    self.printMatrix()
