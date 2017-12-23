import sys

def part1(numbers):
    cnt = 0
    l = list(numbers)
    idx = 0
    while idx < len(l):
        jmp = l[idx]
        l[idx] += 1
        idx += jmp
        cnt += 1
    return cnt

def part2(numbers):
    cnt = 0
    l = list(numbers)
    idx = 0
    while idx < len(l):
        jmp = l[idx]
        if jmp >= 3:
            l[idx] -= 1
        else:
            l[idx] += 1
        idx += jmp
        cnt += 1
    return cnt

if __name__ == "__main__":
    lines = [int(line.strip()) for line in sys.stdin.readlines()]
    print part1(lines)
    print part2(lines)
