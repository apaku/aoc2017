import sys

from itertools import chain, count

NORTH = "north"
WEST = "west"
SOUTH = "south"
EAST = "east"


def spiral():
    for i in count(0, 2):
        l = list(chain.from_iterable(i * [x] for x in [NORTH, WEST, SOUTH, EAST]))
        for e in l[1:]:
            yield e
        yield EAST

def move(where, pos):
    x, y = pos
    if where == NORTH: return x, y - 1
    if where == WEST: return x - 1, y
    if where == SOUTH: return x, y + 1
    if where == EAST: return x + 1, y

def indices():
    pos = (0,0)
    for where in spiral():
        yield pos
        pos = move(where, pos)

def part1(input):
    distance = ""
    for i, (x,y) in enumerate(indices()):
        if i == int(input)-1:
            distance = "%s" %(abs(x) + abs(y))
            break
    return distance
def part2(input):
    values = {(0,0): 1}
    for i, (x,y) in enumerate(indices()):
        curvalue = 0
        if i != 0:
            for entry in [(x-1,y), (x-1,y-1), (x, y-1), (x+1,y), (x+1, y+1), (x, y+1), (x+1, y-1), (x-1, y+1)]:
                curvalue += values[entry] if entry in values.keys() else 0
            values[(x,y)] = curvalue
        if curvalue > int(input):
            return curvalue
    assert False
if __name__ == "__main__":
    print(part2(sys.stdin.read().strip()))
