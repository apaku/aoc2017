from collections import defaultdict
import sys

ops = {'inc': '+', 'dec': '-'}

def maximums(lines):
    registers = defaultdict(int)
    maximums = []
    for line in lines:
        (reg, op, value, _, left, condition, right) = tuple(line.split(' '))

        if eval("registers['%s'] %s %s" % (left, condition, right)):
            registers[reg] = eval("registers['{}'] {} {}".format(reg, ops[op], value))
        maximums.append(max(registers.values()))
    return maximums

def part1(maximums):
    return maximums[-1]

def part2(maximums):
    return max(maximums)

if __name__ == "__main__":
    maximums = maximums(sys.stdin.readlines())
    print part1(maximums)
    print part2(maximums)
