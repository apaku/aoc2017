import sys
from puzzle10 import part2

def rowHash(input):
    for row in range(0, 128):
        yield part2("%s-%s" % (input, row))

def toBinary(hexstring):
    for d in hexstring:
        yield "{0:04b}".format(int(d, 16))

def findAdjacents(grid, pos):
    adjacents = []
    if pos[0] > 0 and grid[pos[0] - 1][pos[1]] == 1:
        adjacents.append((pos[0] - 1, pos[1]))
    if pos[1] > 0 and grid[pos[0]][pos[1] - 1] == 1:
        adjacents.append((pos[0], pos[1] - 1))
    if pos[0] < len(grid) - 1 and grid[pos[0] + 1][pos[1]] == 1:
        adjacents.append((pos[0] + 1, pos[1]))
    if pos[1] < len(grid[pos[0]]) - 1 and grid[pos[0]][pos[1] + 1] == 1:
        adjacents.append((pos[0], pos[1] + 1))
    return adjacents

def markAndFind(grid, group, pos):
    grid[pos[0]][pos[1]] = group
    for adjacent in findAdjacents(grid, pos):
        markAndFind(grid, group, adjacent)

def findFirstBit(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return (i,j)

    return None

def findRegions(grid):
    curgroup = 2
    groupStartPos = findFirstBit(grid)
    while groupStartPos is not None:
        markAndFind(grid, curgroup, groupStartPos)
        groupStartPos = findFirstBit(grid)
        curgroup += 1
    return curgroup - 2

def doit(input):
    grid = []
    for hashStr in rowHash(input):
        hashBits = ""
        for bits in toBinary(hashStr):
            assert len(bits) == 4
            hashBits += bits
        assert len(hashBits) == 128
        grid.append([int(x) for x in hashBits])
    overallsum = sum([sum(x) for x in grid])
    regions = findRegions(grid)
    return overallsum, regions

if __name__ == "__main__":
    print(doit(sys.stdin.read().strip()))
