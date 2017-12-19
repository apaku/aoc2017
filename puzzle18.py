import sys
from collections import defaultdict

def snd(val):
    def snddoit(registers, messages):
        if messages is None:
            #Part1
            registers["snd"] = getRegisterOrValue(val, registers)
            return (1, None, 'snd')
        else:
            #Part2
            return (1, getRegisterOrValue(val,  registers), 'snd')
    return snddoit

def rcv(register):
    def rcvdoit(registers, messages):
        if messages is None:
            #Part1
            if getRegisterOrValue(register, registers) != 0:
                return (1, registers['snd'], 'rcv')
            return (1, None, 'rcv')
        else:
            #Part2
            if len(messages) == 0:
                return (0, None, 'rcv')
            registers[register] = messages.pop(0)
            return (1, None, 'rcv')
    return rcvdoit

def getRegisterOrValue(val, registers):
    if val in registers:
        return registers[val]
    else:
        return int(val)

def setval(lvalue, rvalue):
    def setdoit(registers, messages):
        registers[lvalue] = getRegisterOrValue(rvalue, registers)
        return (1, None, 'set')
    return setdoit

def add(lvalue, rvalue):
    def muldoit(registers, messages):
        registers[lvalue] = registers[lvalue] + getRegisterOrValue(rvalue, registers)
        return (1, None, 'add')
    return muldoit

def mul(lvalue, rvalue):
    def muldoit(registers, messages):
        registers[lvalue] = registers[lvalue] * getRegisterOrValue(rvalue, registers)
        return (1, None, 'mul')
    return muldoit

def mod(lvalue, rvalue):
    def moddoit(registers, messages):
        registers[lvalue] = registers[lvalue] % getRegisterOrValue(rvalue, registers)
        return (1, None, 'mod')
    return moddoit

def jgz(lvalue, rvalue):
    def jgzdoit(registers, messages):
        jumpval = getRegisterOrValue(rvalue, registers)
        condval = getRegisterOrValue(lvalue, registers)
        if condval > 0:
            return (jumpval, None, 'jgz')
        return (1, None, 'jgz')
    return jgzdoit

def parse(lines):
    instructionlist = []
    for line in lines:
        instructions = line.strip().split(" ")
        if instructions[0] == 'snd':
            instructionlist.append(snd(instructions[1]))
        elif instructions[0] == 'set':
            instructionlist.append(setval(instructions[1], instructions[2]))
        elif instructions[0] == 'add':
            instructionlist.append(add(instructions[1], instructions[2]))
        elif instructions[0] == 'mul':
            instructionlist.append(mul(instructions[1], instructions[2]))
        elif instructions[0] == 'mod':
            instructionlist.append(mod(instructions[1], instructions[2]))
        elif instructions[0] == 'rcv':
            instructionlist.append(rcv(instructions[1]))
        elif instructions[0] == 'jgz':
            instructionlist.append(jgz(instructions[1], instructions[2]))
    return instructionlist

def part1(instructions):
    i = 0
    registers = defaultdict(int)
    while i < len(instructions) and i >= 0:
        (jump, sndValue, cmd) = instructions[i](registers, None)
        if sndValue is not None:
            return sndValue
        i += jump
    return None

def part2(instructions):
    i0 = 0
    i1 = 0
    registers0 = defaultdict(int)
    registers0['p'] = 0
    registers1 = defaultdict(int)
    registers1['p'] = 1
    messagequeue = {"prog0": [], "prog1": []}
    prog0sndcnt = 0
    prog1sndcnt = 0
    while i0 < len(instructions) and i0 >= 0 and \
          i1 < len(instructions) and i1 >= 0:
        (jump0, sndValue0, cmd0) = instructions[i0](registers0, messagequeue['prog0'])
        (jump1, sndValue1, cmd1) = instructions[i1](registers1, messagequeue['prog1'])
        if cmd0 == 'rcv' and cmd1 == 'rcv' and jump0 == 0 and jump1 == 0:
            return prog1sndcnt
        if cmd0 == 'snd' and sndValue0 is not None:
            prog0sndcnt += 1
            messagequeue['prog1'].append(sndValue0)
        if cmd1 == 'snd' and sndValue1 is not None:
            prog1sndcnt += 1
            messagequeue['prog0'].append(sndValue1)
        i0 += jump0
        i1 += jump1
    return prog1sndcnt

if __name__ == "__main__":
    instructions = parse(sys.stdin.readlines())
    print part1(instructions)
    print part2(instructions)
