import sys

def parseGarbage(input):
    assert len(input) > 1
    assert input[0] == '<'
    index = 1
    garbagechars = 0
    while index < len(input):
        if input[index] == '!':
            index += 2
        elif input[index] == '>':
            return (index + 1, garbagechars)
        else:
            garbagechars += 1
            index += 1
    return (index, garbagechars)

def parseGroup(input, nestingLevel):
    assert len(input) > 1
    assert input[0] == '{'
    sum = nestingLevel + 1
    garbagesum = 0
    index = 1
    while index < len(input):
        subsum = 0
        garbagesubsum = 0
        if input[index] == '}':
            return (index+1, sum, garbagesum)
        elif input[index] == '{':
            (endindex, subsum, garbagesubsum) = parseGroup(input[index:], nestingLevel + 1)
            index += endindex
        elif input[index] == '<':
            (endindex, garbagesubsum) = parseGarbage(input[index:])
            index += endindex
        else:
            assert index == len(input) or input[index] == ','
            index += 1
        garbagesum += garbagesubsum
        sum += subsum
    return (index, sum, garbagesum)

def part1and2(input):
    groupsum = parseGroup(input, 0)
    return groupsum

if __name__ == "__main__":
    print(part1and2(sys.stdin.read().strip()))
