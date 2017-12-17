import sys

def part1(steps, numIterations):
    buf = [0]

    curpos = 0
    i = 0
    while i < numIterations:
        bufsize = len(buf)
        reststeps = steps % bufsize
        if curpos + reststeps > bufsize - 1:
            curpos = reststeps - (bufsize - curpos)
        else:
            curpos = curpos + reststeps
        buf.insert(curpos + 1, i + 1)
        curpos += 1
        i += 1
    return buf[curpos + 1] if curpos < len(buf) -1  else buf[0]

def part2(steps, numIterations):
    curpos = 0
    i = 0
    while i < numIterations:
        bufsize = i + 1
        reststeps = steps % bufsize
        if curpos + reststeps > i:
            curpos = reststeps - (bufsize - curpos)
        else:
            curpos = curpos + reststeps
        curpos += 1
        if curpos == 1:
            value_after_zero = bufsize
        i += 1
    return value_after_zero

if __name__ == "__main__":
    steps = int(sys.stdin.read().strip())
    print part1(steps, 2017)
    print part2(steps, 50000000)
