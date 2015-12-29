#!/usr/bin/env python
import numpy as np
import pandas as pd
from itertools import permutations
import sys

def parse_line(line):
    _, sue_nr, key1, val1, key2, val2, key3, val3 = line
    data = {key1 : int(val1),
            key2 : int(val2),
            key3 : int(val3)}
    return sue_nr, data

tape = {"children" : 3,
        "cats" : 7,
        "samoyeds" : 2,
        "pomeranians" : 3,
        "akitas" : 0,
        "vizslas" : 0,
        "goldfish" : 5,
        "trees" : 3,
        "cars" : 2,
        "perfumes" : 1}

with open("input.txt", "r") as f:
    for line in f:    
        line = line.replace(":","").replace(",","")
        line = line.strip().split()
        sue_nr, data = parse_line(line)

        nt = 0
        for k, v in data.iteritems():

            if k in ["cats", "trees"]:
            #if k in []:
                if v > tape[k]:
                    nt += 1
            #elif k in []:
            elif k in ["pomeranians", "goldfish"]:
                if v < tape[k]:
                    nt += 1
            elif  v == tape[k]:
                nt += 1
        if nt == 3:
            print sue_nr
            




sys.exit()
# OLD STUFF

def parse_line(line):
    _, sue_nr, key1, val1, key2, val2, key3, val3 = line
    data = {"sue_nr" : [int(sue_nr)],
            key1 : [int(val1)],
            key2 : [int(val2)],
            key3 : [int(val3)]}
    return data

tape = {"children" : 3,
        "cats" : 7,
        "samoyeds" : 2,
        "pomeranians" : 3,
        "akitas" : 0,
        "vizslas" : 0,
        "goldfish" : 5,
        "trees" : 3,
        "cars" : 2,
        "perfumes" : 1}


#df = pd.DataFrame({"sue_nr" : [1]})
#print df
with open("input.txt", "r") as f:
    for line in f:    
        line = line.replace(":","").replace(",","")
        line = line.strip().split()
        data = parse_line(line)
        if not "df" in locals():
            df = pd.DataFrame(data)
        else:  
            df_temp = pd.DataFrame(data)
            df = df.append(df_temp)

for per in permutations(tape.keys(), 3):
    
    #if per[0] in ["cats", "trees"]
    df_check = df[(df[per[0]] == tape[per[0]]) &
                  (df[per[1]] == tape[per[1]]) & 
                  (df[per[2]] == tape[per[2]])] 

    if len(df_check) > 0:
        print df_check["sue_nr"]

        
