import string
import sys

def doSpin(spinlen):
    def dospin(programs):
        return programs[-spinlen:] + programs[:-spinlen]
    return dospin

def doExchange(pos_one, pos_two):
    def doexchange(programs):
        programs[pos_one], programs[pos_two] = programs[pos_two], programs[pos_one]
        return programs
    return doexchange

def doSwap(prog_one, prog_two):
    def doswap(programs):
        prog_one_index = programs.index(prog_one)
        prog_two_index = programs.index(prog_two)
        return doExchange(prog_one_index, prog_two_index)(programs)
    return doswap

def parseMove(move):
    if move[0] == 's':
        return doSpin(int(move[1:]))
    elif move[0] == 'x':
        swapPlaces = move[1:].split('/')
        return doExchange(int(swapPlaces[0]), int(swapPlaces[1]))
    else:
        assert move[0] == 'p'
        swapPlaces = move[1:].split('/')
        return doSwap(swapPlaces[0], swapPlaces[1])

def doit(numiterations, moveFuncs):
    #programs = list(string.ascii_lowercase)[:5]
    programs = list(string.ascii_lowercase)[:16]
    seen = []
    for i in xrange(numiterations):
        programsstr = "".join(programs)
        if programsstr in seen:
            return seen[numiterations % i]
        seen.append(programsstr)
        for moveFunc in moveFuncs:
            programs = moveFunc(programs)
    return "".join(programs)

if __name__ == "__main__":
    moves = sys.stdin.read().strip().split(",")
    moveFuncs = []
    for move in moves:
        moveFuncs.append(parseMove(move))
    print("".join(doit(1, moveFuncs)))
    print("".join(doit(1000000000, moveFuncs)))
