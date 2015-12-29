#!/usr/bin/env python

with open("input.txt", "r") as f:
    content = f.readlines()

print sum(len(line.strip()) - len(eval(line)) for line in content)

print sum(line.strip().count("\\") + line.strip().count('"') + 2 for line in content)



