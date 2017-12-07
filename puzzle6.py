import sys

def part1(input):
    blocks = [int(x) for x in input.split("\t")]
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

    return "%s" % iterationcnt

if __name__ == "__main__":
    sys.stdout.write(part1(sys.stdin.read().strip()) + "\n")
