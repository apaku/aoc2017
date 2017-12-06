import sys

def part1(input):
    valid_phrases = 0;
    for row in input.split('\n'):
        words = row.split(' ')
        words.sort()
        valid = True
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                valid = False
                break
        if valid:
            valid_phrases += 1
    return "%s" % valid_phrases

def part2(input):
    valid_phrases = 0;
    for row in input.split('\n'):
        words = row.split(' ')
        words.sort()
        valid = True
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                word1list = list(words[i])
                word2list = list(words[j])
                word1list.sort()
                word2list.sort()
                if word1list == word2list:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valid_phrases += 1
    return "%s" % valid_phrases

if __name__ == "__main__":
    sys.stdout.write(part2(sys.stdin.read().strip())+"\n")
