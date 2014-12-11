##Finding the Shortest Path##

To run the program type: python main.py < inputfile(optional) >
- The input file is the file that contains the maze
- The input file is option at the end, if not enter you will be prompted

###Specifications###
The Project uses:
- Modified DFS which finds the paths and marks the parents of the child from the start
- If the algorithm comes across a child with a parent of larger step count it will replace
with the new parent
- This method is reported four times for the different combinations of which child to search first. In many cases all four iterations find the same path, but if there is a difference then the algorithm will choose the shortest. 
- The step count of the shortest along with a visual representation of the maze with the correct path steps marked with "+"
