import sys

def part1(lines):
    sum = 0;
    for row in lines:
        l = [int(x) for x in row.split('\t')]
        sum += max(l) - min(l)
    return sum

def part2(input):
    sum = 0
    for row in lines:
        l = [int(x) for x in row.split('\t')]
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                num1 = l[i]
                num2 = l[j]
                if num1 < num2:
                    num1, num2 = num2, num1
                if num1 % num2 == 0:
                    sum += num1 / num2
    return sum

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    print part1(lines)
    print part2(lines)
