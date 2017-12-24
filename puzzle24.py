import sys

def parse(line):
    return tuple([int(x.strip()) for x in line.split('/')])

def findcandidates(connectors, knownside):
    return [connector for connector in connectors if
            connector[0] == knownside or connector[1] == knownside]

def openside(connector, usedsidenum):
    return connector[0] if connector[1] == usedsidenum else connector[1]

def strengths(opensidenum, connectors):
    candidates = findcandidates(connectors, opensidenum)
    candidatesstrengths = []
    for candidate in candidates:
        candidateopenside = openside(candidate, opensidenum)
        leftoverconnectors = set(connectors) - set([candidate])
        substrengths = strengths(candidateopenside, leftoverconnectors)
        if len(substrengths) == 0:
            newstrengths = [(1, candidate[0] + candidate[1])]
        else:
            newstrengths = [(substrength[0] + 1, candidate[0] + candidate[1] + substrength[1]) for substrength in substrengths]
        candidatesstrengths += newstrengths
    return candidatesstrengths

def part1(bridgestrengths):
    return max([strength[1] for strength in bridgestrengths])

def part2(bridgestrengths):
    maxlen = max([strength[0] for strength in bridgestrengths])
    return max([strength[1] for strength in bridgestrengths if strength[0] == maxlen])

if __name__ == "__main__":
    connectors = [parse(line) for line in sys.stdin.readlines()]
    bridgestrengths = strengths(0, connectors)
    print part1(bridgestrengths)
    print part2(bridgestrengths)
