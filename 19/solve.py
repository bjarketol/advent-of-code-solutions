import random
import re
from collections import defaultdict

# !! PART 1 !!

pathways = defaultdict(list)
with open("input.txt") as f:
    pathway_lines, string = f.read().split("\n\n")
    string = string.strip()
    for line in pathway_lines.split("\n"):
        line = line.strip().split()
        a, _, b = line
        pathways[a].append(b)

pattern = re.compile(r"[A-Z][a-z]*")
parts = pattern.findall(string)
unique_mols = set()

for i, part in enumerate(parts):
    for pathway in pathways[part]:
        
        l = parts[:]
        l[i] = pathway

        unique_mols.add("".join(l))

print "part1:",len(unique_mols)


# !! PART 2 !!

def backtrack(s, rules):
    count = 0
    old_s = ""
    keys = list(rules.keys())
    random.shuffle(keys)
    while old_s != s:
        old_s = s
        for key in keys:
            while key in s:
                count += s.count(key)
                s = s.replace(key, rules[key])
    return int(s == "e") * count

rules = {}
with open("input.txt") as f:
    rules_block, string = map(str.strip, f.read().split("\n\n"))
    lines = rules_block.split("\n")
    for line in lines:
        a, _, b = line.split()
        rules[b] = a

num = 0
while num == 0:
    num = backtrack(string, rules)

print "part2:", num



