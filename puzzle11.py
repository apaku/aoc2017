import sys
from math import copysign

def distance(pos1, pos2):
    (xstart, ystart) = pos1
    (xend, yend) = pos2
    dx = xend - xstart
    dy = yend - ystart
    if copysign(1, dx) == copysign(1, dy):
        return abs(dx + dy)
    else:
        return max(abs(dx), abs(dy))

def doit(input):
    way = [((0,0),0)]
    for x in input.split(','):
        newpos = None
        if x == 'n':
            newpos = (way[-1][0][0], way[-1][0][1] + 1)
        elif x == 'ne':
            newpos = (way[-1][0][0]+1, way[-1][0][1])
        elif x == 'se':
            newpos = (way[-1][0][0]+1, way[-1][0][1] - 1)
        elif x == 's':
            newpos = (way[-1][0][0], way[-1][0][1] - 1)
        elif x == 'sw':
            newpos = (way[-1][0][0]-1, way[-1][0][1])
        else:
            assert x == 'nw'
            newpos = (way[-1][0][0]-1, way[-1][0][1] + 1)
        way.append((newpos, distance(way[0][0], newpos)))
    return max([x[1] for x in way]), way[-1]

if __name__ == "__main__":
    print(doit(sys.stdin.read().strip()))
