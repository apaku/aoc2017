import sys

def parse(input):
    return dict([(int(line.split(": ")[0]), int(line.split(": ")[1])) for line in input.split("\n")])

def nextPositionOfScanner(scannerIdx, direction, scannerMax):
    print "    nextPos:", scannerIdx, direction, scannerMax
    if scannerIdx + direction < 0:
        return (1, -1 * direction)
    elif scannerIdx + direction == scannerMax:
        return (scannerIdx - 1, -1 * direction)
    return (scannerIdx + direction, direction)

def positionOfScannerAt(picoSeconds, scannerLength):
    scannerIdx = 0
    direction = 1
    for i in range(0, picoSeconds):
        (scannerIdx, direction) = nextPositionOfScanner(scannerIdx, direction, scannerLength)
    return scannerIdx

def scannersAtZeroWhenPassingWithDelay(delay, scannerConfig):
    scannersAtZero = []
    for (scannerPos, scannerMax) in scannerConfig.items():
        print "Scanner at ", scannerPos, "calculating for", delay, "scanner's size", scannerMax
        positionAtPass = positionOfScannerAt(delay + scannerPos, scannerMax)
        print "Position of scanner:", positionAtPass
        if positionAtPass == 0:
            scannersAtZero.append((scannerPos, scannerMax))
    return scannersAtZero

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
        (caught, severity) = tryTravel(state, config)
        if len(caught) == 0:
            return delay
        delay += 1
        state = nextState(state, config)

def findDelay2(config):
    delay = 0
    while True:
        scannersAtZero = scannersAtZeroWhenPassingWithDelay(delay, config)
        if len(scannersAtZero) == 0:
            return delay
        delay += 1


def doit(input):
    firewallconfig = parse(input)
    state = initialState(firewallconfig)
    part1 = sum([x * y for (x,y) in scannersAtZeroWhenPassingWithDelay(0, firewallconfig)])
    part2 = findDelay2(firewallconfig)
    return part1, part2

if __name__ == "__main__":
    print(doit(sys.stdin.read().strip()))
