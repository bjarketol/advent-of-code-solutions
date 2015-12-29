#!/usr/bin/env python
from hashlib import md5
import itertools

key = "iwrupvqb"
target = "00000"
for i in itertools.count():
    if md5(key+str(i)).hexdigest().startswith(target):
        print(i)
        break

