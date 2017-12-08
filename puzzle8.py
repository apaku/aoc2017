from collections import defaultdict
import sys

ops = {'inc': '+', 'dec': '-'}

def maximums(input):
    registers = defaultdict(int)
    maximums = []
    for line in input.split('\n'):
        (reg, op, value, _, left, condition, right) = tuple(line.split(' '))

        if eval("registers['%s'] %s %s" % (left, condition, right)):
            registers[reg] = eval("registers['{}'] {} {}".format(reg, ops[op], value))
        maximums.append(max(registers.values()))
    return maximums

def part1(input):
    return "%s" % maximums(input)[-1]

def part2(input):
    return "%s" % max(maximums(input))

if __name__ == "__main__":
    sys.stdout.write(part2(sys.stdin.read().strip()) + "\n")
