import operator
from itertools import count, ifilter, imap
import sys

def parse(inputlines):
    return [map(int, line.split(": ")) for line in inputlines]

def scannerPositionAfter(scanner, initialDelay):
    return (initialDelay + scanner[0]) % ((scanner[1] - 1) * 2)

def scannerHitsMeTest(delay):
    def scannerHitsMe(scanner):
        return scannerPositionAfter(scanner, delay) == 0
    return scannerHitsMe

def scannersHittingMe(scannerConfig, delay):
    return ifilter(scannerHitsMeTest(delay), scannerConfig)

def delaysToPass(config):
    for delay in count():
        try:
            next(scannersHittingMe(config, delay))
        except StopIteration:
            yield delay

def product(iterable):
    return reduce(operator.mul, iterable, 1)

def doit(input):
    firewallconfig = parse(input)
    part1 = sum(imap(product, scannersHittingMe(firewallconfig, 0)))
    part2 = next(delaysToPass(firewallconfig))
    return part1, part2

if __name__ == "__main__":
    print(doit(sys.stdin.readlines()))
