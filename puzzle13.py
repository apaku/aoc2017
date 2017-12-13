import sys

def parse(input):
    return dict([(int(line.split(": ")[0]), int(line.split(": ")[1])) for line in input.split("\n")])

def nextState(oldstate, firewallconfig):
    newstate = dict(oldstate)
    for key in firewallconfig.keys():
        newstate[key] = (newstate[key][0] + newstate[key][1], newstate[key][1])
        if newstate[key][0] == firewallconfig[key]:
            newstate[key] = (newstate[key][0] - 2, -1)
        elif newstate[key][0] == -1:
            newstate[key] = (newstate[key][0] + 2, 1)
    return newstate

def initialState(config):
    return dict([(k, (0, 1)) for k in config.keys()])

def tryTravel(initialState, firewallconfig):
    state = dict(initialState)
    caughtLayers = []
    packetPos = -1
    while packetPos < max(firewallconfig.keys()):
        packetPos += 1
        if packetPos in state.keys() and state[packetPos][0] == 0:
            caughtLayers.append(packetPos)
        state = nextState(state, firewallconfig)
    return caughtLayers, sum([k*firewallconfig[k] for k in caughtLayers])

def findDelay(initState, config):
    state = dict(initState)
    delay = 0
    while True:
        print "1", state
        (caught, severity) = tryTravel(state, config)
        print "2", caught, severity
        if len(caught) == 0:
            return delay
        delay += 1
        state = nextState(state, config)

def doit(input):
    firewallconfig = parse(input)
    state = initialState(firewallconfig)
    part1 = tryTravel(state, firewallconfig)
    print "------------------------------"
    part2 = findDelay(state, firewallconfig)
    return part1, part2

if __name__ == "__main__":
    print(doit(sys.stdin.read().strip()))
