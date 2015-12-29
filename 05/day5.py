#!/usr/bin/env python
import re

infile = "day5_data.txt"


#Q1
if (0):
    vowels = ["a", "e", "i", "o", "u"]
    omit = ["ab", "cd", "pq", "xy"]

    repeat_matcher = re.compile(r'((\w)\2{1,})')
    count = 0
    with open(infile, "r") as f:
        for line in f:
            line = line.strip()
            if not [match[0] for match in re.findall(repeat_matcher, line)]:
                continue
            if sum(line.count(c) for c in vowels) < 3:
                continue
            if any(c in line for c in omit):
                print "Omit", line
                continue
            count +=1
    print "Count:", count


#Q2
count = 0
with open(infile, "r") as f:
    for line in f:
        line = line.strip()
        print line
        print [match for match in re.findall(r"([a-z])", line)]
        print [match for match in re.findall(r"([a-z]).", line)]
        print [match for match in re.findall(r"([a-z]).\1", line)]
        print [match for match in re.findall(r"([a-z]{2}).*\1", line)]

        if not [match for match in re.findall(r"([a-z]).\1", line)]:
            continue
        if not [match for match in re.findall(r"([a-z]{2}).*\1", line)]:
            continue

        count += 1
print "Count:", count




