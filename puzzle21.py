from itertools import chain
import math
import sys

start = [[False,True,False],[False,False,True],[True,True,True]]

def rotate(grid, degree):
    newgrid = list(grid)
    cnt = degree/90
    for i in range(cnt):
    # deque of 'outer' elements, rotate by grid-size
    # or reverse + transpose of grid, transpose being doable via zip with *: zip(*grid)
    # + map(list, transpose)
        newgrid = map(list, zip(*newgrid[::-1]))
    return newgrid

def flipVertical(grid):
    # grid[0] <-> grid[len-1] or grid[0][0]..grid[0][len-1] <-> grid[len-1][0]..grid[len-1][len-1]
    return reversed(grid)

def flipHorizontal(grid):
    return zip(*reversed(zip(*grid)))

def toStr(grid):
    return '\n'.join(''.join('#' if b else '.' for b in line) for line in grid)

def parsePattern(lines):
    return [[x == '#' for x in line] for line in lines]

def matchPattern(grid, rules):
    return [rule[1] for rule in rules if rule[0] == grid][0]

def subgrid(grid, offset, size):
    startline = offset[0] * size
    startcol = offset[1] * size
    subgrid = []
    for i in range(size):
        subgrid.append(grid[startline+i][startcol:startcol+size])
    return subgrid

def divide(grid, size):
    assert len(grid) % size == 0
    numsubgridsinline = len(grid) / size
    grids = []
    for i in range(numsubgridsinline):
        for j in range(numsubgridsinline):
            grids.append(subgrid(grid, (i,j), size))
    return grids

def merge(grids):
    numsubgridstomerge = int(math.sqrt(len(grids)))
    grid = []
    for i in range(0, numsubgridstomerge):
        merged = [list(chain(*k)) for k in zip(*grids[i:i + numsubgridstomerge])]
        grid += merged
    return grid

def parse(line):
    mapping = line.strip().split(" => ")
    inputgrid = parsePattern(mapping[0].split('/'))
    outputgrid = parsePattern(mapping[1].split('/'))
    return (inputgrid, outputgrid)

def explode(rules):
    explodedrules = []
    for rule in rules:
        for rotation in [0, 90, 180, 270]:
            explodedrules.append((list(rotate(rule[0], rotation)), rule[1]))
        flipped = list(flipVertical(rule[0]))
        for rotation in [0, 90, 180, 270]:
            explodedrules.append((rotate(flipped, rotation), rule[1]))
    return explodedrules

def doit(lines):
    grid = start
    print "original\n", toStr(grid)
    rules = explode([parse(line) for line in lines])
    print "rules", len(rules)
    for i in range(5):
        if len(grid) % 2 == 0:
            subgrids = divide(grid, 2)
        else:
            subgrids = divide(grid, 3)
        for i, subgrid in enumerate(subgrids):
            subgrids[i] = matchPattern(subgrid, rules)
            assert subgrids[i] is not None
        grid = merge(subgrids)
        print toStr(grid)
        print "----------------"
    print "Final grid\n", toStr(grid)
    return len([y for x in grid for y in x if y])

if __name__ == "__main__":
    print doit(sys.stdin.readlines())
