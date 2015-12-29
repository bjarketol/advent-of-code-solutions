#!/usr/bin/env python

input = "1321131112"

from itertools import groupby

def look_and_say(input_string, num_iterations):
    for i in xrange(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    return input_string

print len(look_and_say(input, 50))


