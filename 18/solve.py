#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

corners = {(0, 0), (0, 99), (99, 0), (99,99)}

with open("input.txt") as f:
    lights = corners | set((x, y) for y, line in enumerate(f)
                                  for x, char in enumerate(line.strip())
                                  if char == "#" )

neighbours = lambda x, y: sum((_x, _y) in lights for _x in (x-1, x, x+1)
                                                for _y in (y-1, y, y+1)
                                                if (_x, _y) != (x, y))

for c in xrange(100):
    lights = corners | set((x, y) for x in xrange(100)
                                  for y in xrange(100)
                                  if (x, y) in lights and 2 <= neighbours(x, y) <= 3
                                  or (x, y) not in lights and neighbours(x, y) == 3)

print len(lights)
print type(corners)
sys.exit()

# OLD STUFF
sns.set_style("white")

def advance(data):

    neighbours = count_neighbours(data)

    three = neighbours == 3
    two = neighbours == 2
    dataon = data == 1
    on_opr = three + two*dataon
    #on_opr = (((neighbours == 2) & (data == 1)) | (neighbours == 3))
    off_opr = np.invert(on_opr)
  
    data[off_opr] = 0
    data[on_opr] = 1

    return data

def count_neighbours(data):
    nx, ny = data.shape
    
    neighbours = np.zeros([nx,ny])

    for ix in xrange(nx):
        ixm = max(0, ix-1)
        ixp = min(nx-1, ix+1)
        for iy in xrange(ny):

            iym = max(0, iy-1)
            iyp = min(ny-1, iy+1)
            
            neighbours[ix, iy] = np.sum(data[ixm:ixp, iym:iyp])

    return neighbours

with open("input.txt", "r") as f:
    string = f.read().replace("\n","").replace("#","1").replace(".","0")
    data = np.array(list(string),dtype=np.float64)
    data = data.reshape(100,100)

#data = np.array([
#                 [0,0,1,0,1,0,1,1],
#                 [0,1,1,1,1,1,0,0],
#                 [0,1,0,1,1,0,0,0],
#                 [0,1,1,1,1,1,0,0],
#                 [0,1,1,0,1,0,0,0],
#                 [0,1,0,1,1,1,0,0],
#                 [0,1,1,1,0,1,0,0],
#                 [0,1,1,0,1,1,0,0]
#                 ])



for it in xrange(5):
    data = advance(data)
    plt.imshow(data)
    plt.pause(1)

print np.sum(data)
    


