#!/usr/bin/env python
import re
from collections import defaultdict

# PART 1

pathways = defaultdict(list)
with open("input.txt") as f:
    pathway_lines, instr = f.read().split("\n\n")
    #print pathway_lines
    instr = instr.strip()
    for line in pathway_lines.split("\n"):
        line = line.strip().split()
        a, _, b = line
        pathways[a].append(b)

pattern = re.compile(r"[A-Z][a-z]*")
parts = pattern.findall(instr)
unique_molecules = set()

for i, part in enumerate(parts):
    for pathway in pathways[part]:
        
        l = parts[:]
        l[i] = pathway

        unique_molecules.add("".join(l))

#print len(unique_molecules)


# PART 2

rules = {}
with open("input.txt") as f:
    rules_block, string = map(str.strip, f.read().split("\n\n"))
    lines = rules_block.split("\n")
    for line in lines:
        a, _, b = line.split()
        rules[a] = b

sorted_rules = sorted(rules.keys(), reverse = True, key = len)

def search_and_replace(s):
    if s == "e":
        return 0
    return 1 + next(search_and_replace(s.replace(t, rules[t], 1))
                    for t in sorted_rules if t in s)


print search_and_replace(string)




