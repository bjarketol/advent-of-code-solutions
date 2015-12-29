#!/usr/bin/env python
import numpy as np
from itertools import combinations
from collections import Counter

with open("input.txt", "r") as f:
    containers = np.genfromtxt(f)

for c in containers:
    print c
counter = Counter(len(c) for i in xrange(len(containers)) for c in combinations(containers, i) if sum(c) == 150)

print sorted(counter.items(), key = lambda x: x[0])[0][1]








