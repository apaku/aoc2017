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
    text = ""
    for line in grid:
        for b in line:
            if b:
                text += "#"
            else:
                text += "."

        text += "\n"
    return text

def parsePattern(lines):
    grid = []
    for line in lines:
        grid.append([x == '#' for x in line])

    return grid

def matchPattern(grid, rules):
    for rule in rules:
        if len(rule[0]) != len(grid[0]):
            continue
        for rotation in (0, 90,180,270):
            if rotate(rule[0], rotation) == grid:
                return rule[1]
            if flipVertical(rule[0]) == grid:
                return rule[1]
            if flipHorizontal(rule[0]) == grid:
                return rule[1]
            if flipVertical(flipHorizontal(rule[0])) == grid:
                return rule[1]
    return None

def divide(grid, size):
    assert len(grid) % size == 0
    numsubgrids = (len(grid) / size) * (len(grid) / size)
    grids = [[] for i in xrange(0, numsubgrids)]
    gridrow = 0
    for i, line in enumerate(grid):
        sublines = [line[k:k+size] for k in range(0, len(line), size)]
        for j, subline in enumerate(sublines):
            grid[gridrow+j].append(subline)
        if i == size-1:
            gridrow += 1
    return grids

def merge(grids):
    gridlinelen = math.sqrt(len(grids))
    supergrid = [[[] for i in range(0,gridlinelen)] for j in range(0, gridlinelen)]
    supergridrows = [[] for i in range(0,gridlinelen)]
    for i, grid in enumerate(grids):
        for j, line in enumerate(grid):
            supergridrows[j] += line
        if i + gridlinelen == 0:
            supergrid += supergridrows
            supergridrows = [[] for i in range(0,gridlinelen)]
    return supergrid

def parse(line):
    mapping = line.split(" => ")
    inputgrid = parsePattern(mapping[0].split('/'))
    outputgrid = parsePattern(mapping[1].split('/'))
    return (inputgrid, outputgrid)

def doit(lines):
    grid = start
    print "original\n", toStr(grid)
    print "rotated 0\n", toStr(rotate(grid, 0))
    print "rotated 90\n", toStr(rotate(grid, 90))
    print "rotated 180\n", toStr(rotate(grid, 180))
    print "rotated 270\n", toStr(rotate(grid, 270))
    print "rotated 270\n", toStr(rotate(grid, 360))
    print "flipped vertically\n", toStr(flipVertical(grid))
    print "flipped horizontally\n", toStr(flipHorizontal(grid))
    rules = [parse(line) for line in lines]
    for i in range(5):
        print "dividing\n", toStr(grid)
        if len(grid) % 2 == 0:
            subgrids = divide(grid, 2)
        else:
            subgrids = divide(grid, 3)
        for i, grid in enumerate(subgrids):
            print "matching\n", toStr(subgrid)
            subgrids[i] = matchPattern(grid, rules)
            assert subgrids[i] is not None
        grid = merge(subgrids)
    return len([y for x in grid for y in x if y == 1])

if __name__ == "__main__":
    print doit(sys.stdin.readlines())
