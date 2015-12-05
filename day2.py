#!/usr/bin/env python
import numpy as np
import pandas as pd
from datetime import datetime 
infile = "day2_data.txt"


time = datetime.now()

#Q1

with open(infile, "r") as f: 
    datalist = [[float(c) for c in f.readline().strip().split("x")] for n in xrange(1000)]

data = np.array(datalist)

datadict = {"h" : data[:, 0],
            "w" : data[:, 1],
            "l" : data[:, 2]}

df = pd.DataFrame(datadict)

df["min"]         = df.loc[:, ["h", "l", "w"]].min(axis=1)
df["median"]      = df.loc[:, ["h", "l", "w"]].median(axis=1)
df["max"]         = df.loc[:, ["h", "l", "w"]].max(axis=1)
df["hl"]          = df["h"]*df["l"]
df["hw"]          = df["h"]*df["w"]
df["wl"]          = df["w"]*df["l"]
df['area_min']    = df.loc[:, ['hl', 'hw', 'wl']].min(axis=1)
df["paper_area"]  = 2*df["hl"]+2*df["hw"]+2*df["wl"]+df["area_min"]
df["cumsum_area"] = df["paper_area"].cumsum()

total_area = df["cumsum_area"].iloc[-1]
print df[-10:]
print "Total area:", int(total_area)

#Q2 

df["ribbon"] = 2*df["min"] + 2*df["median"]
df["bow"] = df["h"]*df["w"]*df["l"]
df["ribbon_total"] = df["ribbon"] + df["bow"]
df["cumsum_ribbon"] = df["ribbon_total"].cumsum()

print "Total ribbon", int(df["cumsum_ribbon"].iloc[-1])

print datetime.now() - time

#GOOD EXAMPLE 

time = datetime.now()

import itertools
def paper(x, y, z):
    sides = [a*b for a, b in itertools.permutations([x, y, z], 2)]
    return sum(sides + [min(sides)])

def ribbon(x, y, z):
    return x*y*z + 2*(sum([x, y, z]) - max(x, y, z))

def presents(filename):
    return [map(int, line.split('x')) for line in open(filename)]

paper_needed = sum(paper(x, y, z) for x, y, z in presents(infile))
ribbon_needed = sum(ribbon(x, y, z) for x, y, z in presents(infile))

print "paper needed", paper_needed
print "ribbon_needed", ribbon_needed

print datetime.now() - time

















