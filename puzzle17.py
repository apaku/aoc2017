import time
from cProfile import Profile as P
from pstats import Stats as S
import sys

def doit(steps, numIterations):
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
        if i < 8:
            print curpos, buf
        buf.insert(curpos + 1, i + 1)
        curpos += 1
        i += 1
        if i % 100000 == 0:
            print time.time(), "1K"
    return curpos, buf

if __name__ == "__main__":
    steps = int(sys.stdin.read().strip())
    part1 = (curpos, buf) = doit(steps, 2017)
    part1 = buf[curpos + 1] if curpos < (len(buf) - 1) else buf[0]
    print part1
    p = P()
    p.enable()
    (_, part2buf) = doit(steps, 200000)
    p.disable()
    s = S(p)
    s.sort_stats("cumtime")
    s.print_stats()
    idx = part2buf.index(0)
    print part2buf[idx + 1] if idx < (len(part2buf) - 1) else part2buf[0]
