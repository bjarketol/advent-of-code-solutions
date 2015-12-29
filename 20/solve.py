#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import math
from itertools import chain
import numpy as np
from calculate_presents import calculate_presents

goal = 29000000



BIG_NUM = 1000000  # try larger numbers until solution found

#goal = 33100000
houses_a = np.zeros(BIG_NUM)
houses_b = np.zeros(BIG_NUM)

for elf in xrange(1, BIG_NUM):
    houses_a[elf::elf] += 10 * elf
    houses_b[elf:(elf+1)*50:elf] += 11 * elf

print(np.nonzero(houses_a >= goal)[0][0])
print(np.nonzero(houses_b >= goal)[0][0])



#presents = calculate_presents(target)
#print presents



#for house_no in xrange(1, target):
#
#    presents = sum(set(
#
#               chain.from_iterable(
#                   (i, house_no // i)
#                   for i in xrange(1, int(math.ceil(math.sqrt(house_no) + 1)))
#                   if house_no == 0)))
#
#    if presents >= target:
#        break

#print house_no





#for house_no in xrange(1,target):
#    s = 0
#
#    for i in xrange(1,target):
#        if (house_no % i == 0) and (house_no >= i):
#            s += i
#
#    if s >= target:
#        print house_no
#        break

    



    








