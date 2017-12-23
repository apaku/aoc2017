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

def calculate(instructions, registers, debug=False):
    i = 0
    cmds = []
    print registers
    while i < len(instructions) and i >= 0:
        (jump, cmd) = instructions[i](registers)
        if debug:print "ran", cmd, "to get\n", registers
        cmds.append(cmd)
        i += jump
        if debug and 'g' in registers and registers['g'] == 0:
            print 'register g is 0', registers
        if debug and 'h' in cmd:
            print "Changed h", registers
    return cmds

if __name__ == "__main__":
    instructions = parse(sys.stdin.readlines())
    registers = defaultdict(int)
    cmds = calculate(instructions, registers)
    print "part1", len([cmd for cmd in cmds if 'mul' in cmd])
    registers = defaultdict(int)
    registers['a'] = 1
    print calculate(instructions, registers, True), registers
