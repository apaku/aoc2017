import sys
import re

def parse(input):
    nodes = []
    for line in input.split('\n'):
        weightidx = line.find('(')+1
        name = line[:line.find(' ')]
        weight = int(line[weightidx:line.find(')')])
        childidx = line.find('->')
        if childidx > 0:
            childs = [x.strip() for x in line[childidx+2:].split(',')]
        else:
            childs = []
        nodes.append(((name, weight), childs))
    return nodes

def reduceTree(tree):
    leaves = [x[0][0] for x in filter(lambda x: len(x[1]) == 0, tree)]
    nonleaves = filter(lambda x: len(x[1]) > 0, tree)
    newtree = map(lambda x: (x[0], filter(lambda y: y not in leaves, x[1])), nonleaves)
    if len(newtree) == 1:
        return newtree
    return reduceTree(newtree)

def part1(input):
    return "%s" % (reduceTree(parse(input))[0][0][0],)

if __name__ == "__main__":
    sys.stdout.write(part1(sys.stdin.read().strip()) + '\n')
