import sys
from itertools import islice, izip

def parse(lines):
    return [int(line.split(" ")[-1]) for line in lines]

def generator(startValue, factor, multiple):
    prevValue = startValue
    while True:
        prevValue = ( factor * prevValue ) % 2147483647
        if prevValue % multiple == 0:
            yield prevValue

def lowerBits(value):
    return value & 0xffff

def sameLowerBits(valueA, valueB):
    return lowerBits(valueA) == lowerBits(valueB)

def doit(lines):
    generatorStarts = parse(lines)
    generatorA = generator(generatorStarts[0], 16807, 4)
    generatorB = generator(generatorStarts[1], 48271, 8)
    return sum(1 for a, b in islice(izip(generatorA, generatorB), 5000000) if sameLowerBits(a, b))

if __name__ == "__main__":
    print(doit(sys.stdin.readlines()))
