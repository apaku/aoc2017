import sys

def parse(input):
    return dict([(int(line.split(": ")[0]), int(line.split(": ")[1])) for line in input.split("\n")])

def nextState(oldstate, firewallconfig):
    for key in firewallconfig.keys():
        oldstate[key] = (oldstate[key][0] + oldstate[key][1], oldstate[key][1])
        if oldstate[key][0] == firewallconfig[key]:
            oldstate[key] = (oldstate[key][0] - 2, -1)
        elif oldstate[key][0] == -1:
            oldstate[key] = (oldstate[key][0] + 2, 1)
    return oldstate

def initialState(config):
    return dict([(k, (0, 1)) for k in config.keys()])

def part1(input):
    firewallconfig = parse(input)
    state = initialState(firewallconfig)
    caughtLayers = []
    packetPos = -1
    while packetPos < max(firewallconfig.keys()):
        packetPos += 1
        if packetPos in state.keys() and state[packetPos][0] == 0:
            caughtLayers.append(packetPos)
        state = nextState(state, firewallconfig)
    return caughtLayers, sum([k*firewallconfig[k] for k in caughtLayers])
if __name__ == "__main__":
    print(part1(sys.stdin.read().strip()))
