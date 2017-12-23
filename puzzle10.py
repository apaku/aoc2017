import sys
from itertools import cycle, islice

def tie(thelist, lengths, position = 0, skip = 0):
    for length in lengths:
        if length + position > len(thelist):
            #wrapping case
            endoflistlen = len(thelist) - position
            startoflistlen = abs(len(thelist) - (position + length))
            sublist = thelist[position:position+endoflistlen] + thelist[0:startoflistlen]
            sublist.reverse()
            thelist = sublist[endoflistlen:] + thelist[startoflistlen:position] + sublist[:endoflistlen]
        else:
            sublist = thelist[position:position+length]
            sublist.reverse()
            thelist = thelist[:position] + sublist  + thelist[position+length:]
#         sublist = list(islice(cycle(thelist), position, position + length))
#         print "sublist: ", sublist
#         sublist.reverse()
#         print "reversed: ", sublist
#         firstpartoflistlen = abs(len(thelist) - (position - length))
#         firstpartoflist = list(islice(cycle(thelist), 0, firstpartoflistlen))
#         print "first part of list", firstpartoflist
#         secondpartofliststart = position + length
#         secondpartoflistlen = len(thelist) - length - len(firstpartoflist)
#         print "restlen:", secondpartoflistlen
#         print "second part of list:", list(islice(cycle(thelist), secondpartofliststart, secondpartofliststart + secondpartoflistlen))
#         thelist = firstpartoflist + sublist + list(islice(cycle(thelist), secondpartofliststart, secondpartofliststart + secondpartoflistlen))
#         print "thelist:", thelist
        position = (position + length + skip) % len(thelist)
        skip += 1

    return thelist[0] * thelist[1], position, skip, thelist

def part1(input):
    return tie(range(0,256), map(int, input.split(",")))
    #return tie(range(0,5), map(int, input.split(",")))

def part2(input):
    lengths = map(ord, input) + [17, 31, 73, 47, 23]
    position = 0
    skip = 0
    sparseHash = range(0,256)
    for i in range(64):
        (_, position, skip, sparseHash) = tie(sparseHash, lengths, position, skip)
    blocks = [sparseHash[x:x+16] for x in range(0, len(sparseHash), 16)]
    densehash = [reduce(lambda x,y: x ^ y, block) for block in blocks]
    return ''.join(["{:02X}".format(num) for num in densehash])

if __name__ == "__main__":
    data = sys.stdin.read().strip()
    print(part1(data))
    print(part2(data))
