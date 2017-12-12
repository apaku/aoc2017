import sys
from collections import defaultdict

def parse(input):
    connections = {}
    for line in input.split("\n"):
        left = int(line[:line.index("<->")].strip())
        right = [int(x.strip()) for x in line[line.index("<->")+3:].strip().split(",")]
        connections[left] = set(right)
    return connections

def getTargets(start, connectedToGroup, connections):
    connectedTargets = connections[start]
    unknownTargets = connectedTargets - connectedToGroup
    connectedToGroup |= connectedTargets
    for target in unknownTargets:
        getTargets(target, connectedToGroup, connections)

def doit(input):
    connections = parse(input)
    groups = {}
    for entry in connections.keys():
        if len(filter(lambda key: entry in groups[key], groups.keys())) > 0:
            continue
        connectedToGroup = set([0])
        getTargets(entry, connectedToGroup, connections)
        groups[entry] = connectedToGroup

    return groups[0], len(groups[0]), len(groups.keys())

if __name__ == "__main__":
    print(doit(sys.stdin.read().strip()))
