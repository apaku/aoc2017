import sys

def parse(input):
    return [map(int, line.split(": ")) for line in input.split("\n")]

def scannerPositionAfter(scanner, initialDelay):
    return (initialDelay + scanner[0]) % ((scanner[1] - 1) * 2)

def scannersHittingMe(scannerConfig, delay):
    for scanner in scannerConfig:
        if scannerPositionAfter(scanner, delay) == 0:
            yield scanner

def findDelay(config):
    delay = 0
    while True:
        try:
            next(scannersHittingMe(config, delay))
        except StopIteration:
            return delay
        delay += 1

def doit(input):
    firewallconfig = parse(input)
    part1 = sum(map(lambda (x,y): x * y, scannersHittingMe(firewallconfig, 0)))
    part2 = findDelay(firewallconfig)
    return part1, part2

if __name__ == "__main__":
    print(doit(sys.stdin.read().strip()))
