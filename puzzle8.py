from collections import defaultdict
import sys

ops = {'inc': '+', 'dec': '-'}

def part1(input):
    registers = defaultdict(lambda: 0)
    for line in input.split('\n'):
        (reg, op, value, _, left, condition, right) = tuple(line.split(' '))

        if eval("registers['%s'] %s %s" % (left, condition, right)):
            registers[reg] = eval("registers['{}'] {} {}".format(reg, ops[op], value))
    return "%s" % max(registers.values())

def part2(input):
    registers = defaultdict(lambda: 0)
    maximums = []
    for line in input.split('\n'):
        (reg, op, value, _, left, condition, right) = tuple(line.split(' '))

        if eval("registers['%s'] %s %s" % (left, condition, right)):
            registers[reg] = eval("registers['{}'] {} {}".format(reg, ops[op], value))
        maximums.append(max(registers.values()))
    return "%s" % max(maximums)
if __name__ == "__main__":
    sys.stdout.write(part2(sys.stdin.read().strip()) + "\n")
