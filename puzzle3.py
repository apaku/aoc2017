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

def main(input):
    distance = ""
    for i, (x,y) in enumerate(indices()):
        if i == int(input)-1:
            distance = "%s" %(abs(x) + abs(y))
            break
    return distance
if __name__ == "__main__":
    sys.stdout.write(main(sys.stdin.read().strip())+"\n")
