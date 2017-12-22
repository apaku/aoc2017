import sys

def parse(lines):
    infected = set()
    numlines = len(lines)
    axislen = (numlines-1)/2
    pos = (-axislen,axislen)
    for line in lines:
        for c in line:
            if c == '#':
                infected.add(pos)
            pos = (pos[0]+1,pos[1])
        pos = (-axislen,pos[1]-1)
    return infected

def turnLeft(olddir):
    print "turning left on", olddir
    if olddir == (0,0) or olddir == (0,1):
        return (-1,0)
    elif olddir == (-1,0):
        return (0,-1)
    elif olddir == (0,-1):
        return (1,0)
    elif olddir == (1,0):
        return (0,1)
    assert not "Should not happen %s" % olddir

def turnRight(olddir):
    print "turning right on", olddir
    if olddir == (0,0) or olddir == (0,1):
        return (1,0)
    elif olddir == (1,0):
        return (0,-1)
    elif olddir == (0,-1):
        return (-1,0)
    elif olddir == (-1,0):
        return (0,1)
    assert not "Should not happen %s" % olddir

def doit(lines):
    infected = parse(lines)
    curpos = (0,0)
    direction = (0,0)
    infectcount = 0
    for i in range(10000):
        direction = turnRight(direction) if curpos in infected else turnLeft(direction)
        print "direction", direction
        if curpos in infected:
            infected.remove(curpos)
        else:
            infected.add(curpos)
            infectcount += 1
        curpos = (curpos[0]+direction[0], curpos[1]+direction[1])
    print infected
    return infectcount
if __name__ == "__main__":
    print doit(sys.stdin.readlines())
