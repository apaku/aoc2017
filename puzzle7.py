import sys
import re
from collections import defaultdict

def parse(input):
    nodes = {}
    for line in input.split('\n'):
        weightidx = line.find('(')+1
        name = line[:line.find(' ')]
        weight = int(line[weightidx:line.find(')')])
        childidx = line.find('->')
        if childidx > 0:
            childs = [x.strip() for x in line[childidx+2:].split(',')]
        else:
            childs = []
        nodes[name] = (weight, childs)
    return nodes

def reduceTree(tree):
    leaves = dict(filter(lambda x: len(x[1][1]) == 0, tree.items()))
    nonleaves = dict(filter(lambda x: len(x[1][1]) > 0, tree.items()))
    newtree = dict(map(lambda x: (x[0], (x[1][0], filter(lambda y: y not in leaves, x[1][1]))), nonleaves.items()))
    if len(newtree) == 1:
        return newtree
    return reduceTree(newtree)

def part1(input):
    return "%s" % (reduceTree(parse(input)))

def nodeWeight(node, tree):
    return tree[node][0] + sum(map(lambda x: nodeWeight(x, tree), tree[node][1]))

def determineBalance(startNode, tree):
    weights = defaultdict(lambda: [])
    for child in tree[startNode][1]:
        weight = nodeWeight(child, tree)
        weights[weight].append(child)
    return (filter(lambda x: len(x[1]) > 1, weights.items()),
            filter(lambda x: len(x[1]) == 1, weights.items())
    )

def unbalancedChild(node, tree):
    (_, unbalanced) = determineBalance(node, tree)
    if len(unbalanced) == 0:
        return None
    return unbalanced[0][1][0]

def findImbalance(node, tree):
    (balanced, unbalanced) = determineBalance(node, tree)

    (unbalWeight, unbalNames) = unbalanced[0]
    (balWeight, balNames) = balanced[0]

    childNode = unbalancedChild(unbalNames[0], tree)
    if childNode:
        return findImbalance(childNode, tree)

    diff = balWeight - unbalWeight
    return (unbalNames[0], diff, tree[unbalNames[0]][0] + diff)

def part2(input):
    tree = parse(input)
    rootNode = reduceTree(tree)
    print findImbalance(rootNode.keys()[0], tree)
    return ""

if __name__ == "__main__":
    sys.stdout.write(part2(sys.stdin.read().strip()) + '\n')
