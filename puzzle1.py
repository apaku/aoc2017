import sys

def part1(input):
    sum = 0;
    if input[0] == input[-1]:
        sum += int(input[0])
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            sum += int(input[i])

    return sum

def part2(input):
    sum = 0
    inputlen = len(input)
    for i in range(inputlen):
        targetidx = i + inputlen / 2
        if targetidx > inputlen - 1:
            targetidx = targetidx - inputlen
        if input[i] == input[targetidx]:
            sum += int(input[i])
    return sum

if __name__ == "__main__":
    numbers = sys.stdin.read().strip()
    print part1(numbers)
    print part2(numbers)
