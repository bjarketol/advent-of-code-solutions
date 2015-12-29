#!/usr/bin/env python
import re

instr = "hepxcrrq"

def increment(s):
    
    alpha = "abcdefghijklmnopqrstuvwxyz"

    try:
        return s[0:-1] + alpha[alpha.index(s[-1]) + 1]
    except IndexError:
        return increment(s[0:-1]) + "a"

def valid(s):

    if any(x in s for x in ["i","l","o"]):
        return False

    for i in xrange(len(s)-2):
        if ord(s[i]) == ord(s[i+1]) - 1 and ord(s[i+1]) == ord(s[i+2]) - 1:
            break 
    else:
        return False

    if len(re.findall(r'(.)\1+', s)) < 2:
        return False

    return True

def gen_new(instr):
    while True:
        instr = increment(instr)
        if valid(instr):
           return instr 

new1 = gen_new(instr)
new2 = gen_new(new1)

print new1, new2




