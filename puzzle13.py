import cProfile as profile
import pstats
import StringIO
import sys

def parse(input):
    return dict([(int(line.split(": ")[0]), int(line.split(": ")[1])) for line in input.split("\n")])

def scannersAtZeroWhenPassingWithDelay(delay, scannerConfig, firstOnly):
    scannersAtZero = []
    for (scannerPos, scannerMax) in scannerConfig.items():
        positionAtPass2 = (delay + scannerPos) % ((scannerMax - 1) * 2)
        if positionAtPass2 == 0:
            if firstOnly:
                return [(scannerPos, scannerMax)]
            scannersAtZero.append((scannerPos, scannerMax))
    return scannersAtZero

def findDelay(config):
    delay = 0
    while True:
        scannersAtZero = scannersAtZeroWhenPassingWithDelay(delay, config, True)
        if len(scannersAtZero) == 0:
            return delay
        delay += 1


def doit(input):
    firewallconfig = parse(input)
    part1 = sum([x * y for (x,y) in scannersAtZeroWhenPassingWithDelay(0, firewallconfig, False)])
    profiler = profile.Profile()
    profiler.enable()
    part2 = findDelay(firewallconfig)
    profiler.disable()
    stats = StringIO.StringIO()
    ps = pstats.Stats(profiler, stream=stats).sort_stats('pcalls')
    ps.print_stats()
    print stats.getvalue()
    return part1, part2

if __name__ == "__main__":
    print(doit(sys.stdin.read().strip()))
