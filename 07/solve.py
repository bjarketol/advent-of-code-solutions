#!/usr/bin/env python
import sys
import re

# Regular expression patterns
get_cmd = re.compile("[A-Z]+")
get_args = re.compile("[a-z0-9]+")

# Store functions
funcs = {
        "AND"    : lambda a,b: a & b,
        "OR"     : lambda a,b: a | b,
        "LSHIFT" : lambda a,b: a << b,
        "RSHIFT" : lambda a,b: a >> b,
        "NOT"    : lambda a: ~a
        }

def resolve(symbol):
    if isinstance(symbol, int):
        return symbol
    value = wires[symbol]
    if not isinstance(value, tuple):
        return value
    command, args = value
    if not command:
        result = resolve(args[0])
        wires[symbol] = result
        return result
    else:
        resolved_args = [resolve(x) for x in args]
        result = funcs[command](*resolved_args)
        wires[symbol] = result
        return result

wires = {}
with open("input.txt") as f:
    for line in f:
        command = get_cmd.search(line)
        args = get_args.findall(line)
        args = [int(x) if x.isdigit() else x for x in args]
        if command:
            command = command.group()
        to_wire = args.pop()
        wires[to_wire] = (command, tuple(args))

initial_wires = wires.copy()
result_a = resolve("a")
print "Part1:",result_a
wires = initial_wires
wires["b"] = result_a
result_b = resolve("a")
print "Part2:",result_b



sys.exit()

# OLD STUFF

def _binary2int(binary):
    return int(binary, 2)

def _int2binary(int_):
    return "{0:b}".format(int_)

def _parse_line(line):
    operation, target = line.strip().split("->")
    return operation, target 

def rshift(target, wire, shift):
    pass
    

values = {}
operations = []

with open("input.txt") as f:
    for line in f:
        operation, target = _parse_line(line)
        
        try:
            val = int(operation)
            values[str(target)] = val
        except ValueError:
            operations.append((operation, target))

rshifts = []
lshifts = []
nots = []
ands = []
ors = []
for item in operations:
    operation, target = item
    print operation
    if "RSHIFT" in operation:
        wire, opr, shift = operation.split()
        rshifts.append((target, wire, int(shift)))
    if "LSHIFT" in operation:
        wire, opr, shift = operation.split()
        lshifts.append((target, wire, int(shift)))
    if "NOT" in operation:
        opr, wire = operation.split()
        nots.append((target, wire))
    if "AND" in operation:
        wire1, opr, wire2 = operation.split()
        ands.append((target, wire1, wire2))
    if "OR" in operation:
        wire1, opr, wire2 = operation.split()
        ors.append((target, wire1, wire2))

print rshifts
print lshifts
print nots
print ands
print ors

while True:
    
    for command in rshifts:
        pass
    for command in lshifts:
        pass
    for command in nots:
        pass
    for command in ands:
        pass
    for command in ors:
        pass

    break






