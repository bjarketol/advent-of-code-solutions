#!/usr/bin/env python
import json
import re

# Question 1
with open("input.txt", "r") as f:
    dstr = f.read()

print sum(map(int, re.findall(r"-?[0-9]+", dstr)))


# Question 2

def hook(d):
    if "red" in d.values():
        return {}
    else:
        return d

with open("input.txt", "r") as f:
    dstr = str(json.load(f, object_hook=hook))

print sum(map(int, re.findall(r"-?[0-9]+", dstr)))

