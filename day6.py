#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def toggle(subset):
    mask_one = subset == 1
    mask_zero = subset == 0
    subset[mask_one] = 0
    subset[mask_zero] = 1
    return subset

def turn_on(subset):
    subset = 1
    return subset

def turn_off(subset):
    subset = 0
    return subset

def parse_line(line):

    for act in ["turn on", "turn off", "toggle"]:
        if act in line:
            action = act

    line = line.replace(action+" ","").replace("through","")
    line = line.split("  ")

    llx, lly = line[0].split(",")
    llx, lly = int(llx), int(lly)

    urx, ury = line[1].split(",")
    urx, ury = int(urx)+1, int(ury)+1

    ll = (llx, lly)
    ur = (urx, ury)

    return action, ll, ur

infile = "day6_data.txt"

status = np.zeros([1000,1000], dtype=np.int)

with open(infile, "r") as f:

    for line in f:
        line = line.strip()

        action, ll, ur = parse_line(line)

        if "turn on" in action:
            status[ll[0]:ll[1], ur[0]:ur[1]] = 1# turn_on(status[ll[0]:ll[1], ur[0]:ur[1]])
        if "turn off" in action:
            status[ll[0]:ll[1], ur[0]:ur[1]] = 0# turn_off(status[ll[0]:ll[1], ur[0]:ur[1]])
        if "toggle" in action:
            status[ll[0]:ll[1], ur[0]:ur[1]] = toggle(status[ll[0]:ll[1], ur[0]:ur[1]])


        #plt.contourf(status)
        #plt.pause(0.0001)
print np.sum(status)






