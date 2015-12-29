#!/usr/bin/env python
import sys
from itertools import permutations

places = set()
distances = dict()
for line in open('input.txt'):
    print line
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest] = int(distance)
    distances.setdefault(dest, dict())[source] = int(distance)

for k, v in distances.iteritems():
    print k, v

shortest = sys.maxsize
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("shortest: %d" % (shortest))
print("longest: %d" % (longest))








