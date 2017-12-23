import sys

def part1(numbers):
    blocks = list(numbers)
    seenConfigurations = []
    iterationcnt = 1
    while True:
        nextSplitIdx = blocks.index(max(blocks))
        banksize = blocks[nextSplitIdx]
        blocks[nextSplitIdx] = 0
        nextBlock = nextSplitIdx + 1
        while banksize > 0:
            if nextBlock == len(blocks):
                nextBlock = 0
            blocks[nextBlock] += 1
            banksize -= 1
            nextBlock += 1
        if blocks in seenConfigurations:
            break
        seenConfigurations.append(list(blocks))
        iterationcnt += 1

    return iterationcnt

def part2(numbers):
    blocks = list(numbers)
    seenConfigurations = {}
    iterationcnt = 1
    while True:
        nextSplitIdx = blocks.index(max(blocks))
        banksize = blocks[nextSplitIdx]
        blocks[nextSplitIdx] = 0
        nextBlock = nextSplitIdx + 1
        while banksize > 0:
            if nextBlock == len(blocks):
                nextBlock = 0
            blocks[nextBlock] += 1
            banksize -= 1
            nextBlock += 1
        blockstr = ' '.join(map(str, blocks))
        if blockstr in seenConfigurations:
            return iterationcnt - seenConfigurations[blockstr]
            break
        seenConfigurations[blockstr] = iterationcnt
        iterationcnt += 1

    return None

if __name__ == "__main__":
    data = [int(x) for x in sys.stdin.read().split('\t')]
    print part1(data)
    print part2(data)
