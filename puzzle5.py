import sys

def part1(input):
    cnt = 0
    l = [int(x) for x in input.split('\n')]
    idx = 0
    while idx < len(l):
        jmp = l[idx]
        l[idx] += 1
        idx += jmp
        cnt += 1
    return "%s" % cnt

def part2(input):
    cnt = 0
    l = [int(x) for x in input.split('\n')]
    idx = 0
    while idx < len(l):
        jmp = l[idx]
        if jmp >= 3:
            l[idx] -= 1
        else:
            l[idx] += 1
        idx += jmp
        cnt += 1
    return "%s" % cnt

if __name__ == "__main__":
    sys.stdout.write(part2(sys.stdin.read().strip())+"\n")
