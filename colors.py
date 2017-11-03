#!usr/bin/python
import random # random number generator library
import delegator

numColors = 16 # the total number of colors
rgb = 3       # the number of variables needed to define the color (r,g,b)
t = 4         # time in seconds that each color will be displayed

# define our list of colors (c)olors (l)ist = "cl"
cl = [[0 for x in range(rgb)] for y in range(numColors)] # initialize the outer list with lists
cl[0][0] = 255 # Red (r)
cl[0][1] = 0   # Red (g)
cl[0][2] = 0   # Red (b)
cl[1][0] = 0   # Green (r)
cl[1][1] = 255 # Green (g)
cl[1][2] = 0   # Green (b)
cl[2][0] = 0   # Blue (r)
cl[2][1] = 0   # Blue (g)
cl[2][2] = 255 # Blue (b)
cl[3][0] = 255 # Yellow (r)
cl[3][1] = 255 # Yellow (g)
cl[3][2] = 0   # Yellow (b)
cl[4][0] = 153 # Purple (r)
cl[4][1] = 0   # Purple (g)
cl[4][2] = 153 # Purple (b)
cl[5][0] = 255 # Orange (r)
cl[5][1] = 153 # Orange (g)
cl[5][2] = 0   # Orange (b)
cl[6][0] = 255 # Pink (r)
cl[6][1] = 192 # Pink (g)
cl[6][2] = 203 # Pink (b)
cl[7][0] = 220 # Crimson (r)
cl[7][1] = 20  # Crimson (g)
cl[7][2] = 60  # Crimson (b)
cl[8][0] = 255 # Magenta (r)
cl[8][1] = 0   # Magenta (g)
cl[8][2] = 255 # Magenta (b)
cl[9][0] = 75  # Indigo (r)
cl[9][1] = 0   # Indigo (g)
cl[9][2] = 130 # Indigo (b)
cl[10][0] = 64  # Turquoise (r)
cl[10][1] = 224 # Turquoise (g)
cl[10][2] = 208 # Turquoise (b)
cl[11][0] = 0   # Emerald (r)
cl[11][1] = 201 # Emerald (g)
cl[11][2] = 87  # Emerald (b)
cl[12][0] = 139 # Brown (r)
cl[12][1] = 69  # Brown (g)
cl[12][2] = 19  # Brown (b)
cl[13][0] = 220 # Gray (r)
cl[13][1] = 220 # Gray (g)
cl[13][2] = 220 # Gray (b)
cl[14][0] = 198 # Salmon (r)
cl[14][1] = 113 # Salmon (g)
cl[14][2] = 113 # Salmon (b)
cl[15][0] = 238 # Tan (r)
cl[15][1] = 197 # Tan (g)
cl[15][2] = 145 # Tan (b)

# iterate the list, calling the paint program
for z in range(numColors):
    s = random.randint(1,4) # picks a random integer in the range (inclusive)
    delegator.delegate(cl[z][0],cl[z][1],cl[z][2],t,s)