#!/usr/bin/env python

def parse_line():
    name     = line[0]
    speed    = int(line[3])
    duration = int(line[6])
    rest     = int(line[13])
    return name, speed, duration, rest

class Flight(object):

    def __init__(self, name, speed, duration, rest):

        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self.seconds = 0
        self.distance = 0
        self.sleep = False
        self.countdown_swapstate = duration
        self.wincount = 0

    def advance(self):
        
        if not self.sleep:
            self.distance += self.speed
            self.countdown_swapstate -= 1
        elif self.sleep:
            self.countdown_swapstate -= 1

        if self.countdown_swapstate == 0:
            if self.sleep:
                self.sleep = False
                self.countdown_swapstate = self.duration
            elif not self.sleep:
                self.sleep = True
                self.countdown_swapstate = self.rest

        return self

def get_max(d):
    vals = {}
    winners = []
    for k, v in d.iteritems():
        vals[k] = v.distance
    max_val = max(vals.values())
    print max_val
    for k, v in d.iteritems():
        if v.distance == max_val:
            winners.append(k)
    return winners


reindeers = {}
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        name, speed, duration, rest = parse_line()
        reindeers[name] = Flight(name, speed, duration, rest)

for it in xrange(2503):
    for reindeer in reindeers:
        reindeers[reindeer].advance()
    winners = get_max(reindeers)
    for winner in winners:
        reindeers[winner].wincount += 1

for reindeer in reindeers:
    print reindeer, reindeers[reindeer].distance, reindeers[reindeer].wincount
    


#result[name] = distance(2503, speed, duration, rest)


#print max(result, key=result.get)


