#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations

nbr_val = defaultdict(defaultdict)
people = set()
def parse_line():
    person, _, sign, value, _, _, _, _, _, _, neighbour = line
    neighbour = neighbour.replace(".","")
    if sign == "lose":
        change = -1.0 * float(value)
    else:
        change = float(value)
    return person, change, neighbour

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        person, change, neighbour = parse_line()
        people.add(person)
        nbr_val[person][neighbour] = change 

#---------------------------------------#
# This makes the answer for part2
for person in people:
    nbr_val[person]["You"] = 0.0
    nbr_val["You"][person] = 0.0
people.add("You")
#---------------------------------------#

values = []
for permu in permutations(people, len(people)):
    value = 0
    for i, person in enumerate(permu):
        ipnb = i+1
        imnb = i-1
        if ipnb > len(permu) - 1:
            ipnb = 0
        pnb = permu[ipnb]
        mnb = permu[imnb]
        value += nbr_val[person][pnb]
        value += nbr_val[person][mnb]
    values.append(value)

print int(max(values))
        

         
        




