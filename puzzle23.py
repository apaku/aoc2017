import sys
from collections import defaultdict

def getRegisterOrValue(val, registers):
    try:
        return int(val)
    except ValueError:
        return registers[val]

def setval(lvalue, rvalue):
    def setdoit(registers):
        registers[lvalue] = getRegisterOrValue(rvalue, registers)
        return (1, 'set %s %s' % (lvalue, rvalue))
    return setdoit

def sub(lvalue, rvalue):
    def muldoit(registers):
        registers[lvalue] = registers[lvalue] - getRegisterOrValue(rvalue, registers)
        return (1, 'sub %s %s' % (lvalue, rvalue))
    return muldoit

def mul(lvalue, rvalue):
    def muldoit(registers):
        registers[lvalue] = registers[lvalue] * getRegisterOrValue(rvalue, registers)
        return (1, 'mul %s %s' % (lvalue, rvalue))
    return muldoit

def jnz(lvalue, rvalue):
    def jnzdoit(registers):
        jumpval = getRegisterOrValue(rvalue, registers)
        condval = getRegisterOrValue(lvalue, registers)
        if condval != 0:
            return (jumpval, 'jnz %s %s' % (lvalue, rvalue))
        return (1, 'jnz')
    return jnzdoit

def parse(lines):
    instructionlist = []
    for line in lines:
        instructions = line.strip().split(" ")
        if instructions[0] == 'set':
            instructionlist.append(setval(instructions[1], instructions[2]))
        elif instructions[0] == 'sub':
            instructionlist.append(sub(instructions[1], instructions[2]))
        elif instructions[0] == 'mul':
            instructionlist.append(mul(instructions[1], instructions[2]))
        elif instructions[0] == 'jnz':
            instructionlist.append(jnz(instructions[1], instructions[2]))
        else:
            assert not "Unknown instruction %s" % instructions
    return instructionlist

def part1():
    instructions = parse(sys.stdin.readlines())
    i = 0
    cmds = []
    registers = defaultdict(int)
    while i < len(instructions) and i >= 0:
        (jump, cmd) = instructions[i](registers)
        cmds.append(cmd)
        i += jump
    return len([cmd for cmd in cmds if 'mul' in cmd])

def part2():
    def isprime(n):
        '''check if integer n is a prime'''

        # make sure n is a positive integer
        n = abs(int(n))

        # 0 and 1 are not primes
        if n < 2:
            return False

        # 2 is the only even prime number
        if n == 2:
            return True

        # all other even numbers are not primes
        if not n & 1:
            return False

        # range starts with 3 and only needs to go up
        # the square root of n for all odd numbers
        for x in range(3, int(n**0.5) + 1, 2):
            if n % x == 0:
                return False

        return True
    start = 108100
    end = 125100
    step = 17
    primecnt = 0
    nonprimecnt = 0
    while start <= end:
        if not isprime(start):
            nonprimecnt += 1
        start += step
    return nonprimecnt

if __name__ == "__main__":
    print "part1", part1()
    print "part2", part2()
