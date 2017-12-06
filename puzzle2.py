import sys

def part1(input):
    sum = 0;
    for row in input.split('\n'):
        l = [int(x) for x in row.split('\t')]
        sum += max(l) - min(l)
    return "%s" % sum

def part2(input):
    sum = 0
    for row in input.split('\n'):
        l = [int(x) for x in row.split('\t')]
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                num1 = l[i]
                num2 = l[j]
                if num1 < num2:
                    num1, num2 = num2, num1
                if num1 % num2 == 0:
                    sum += num1 / num2
    return "%s" % sum

if __name__ == "__main__":
    sys.stdout.write(part2(sys.stdin.read().strip())+"\n")
