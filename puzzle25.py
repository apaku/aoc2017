import cProfile as profile
import pstats as stats
import re
import sys

def createrule(writevalue, movevalue, contvalue):
    def doit(tape, cursor):
        tape[cursor] = int(writevalue)
        if movevalue == "left":
            move = -1
        else:
            move = +1
        newcursor = cursor + move
        if newcursor < 0:
            for i in range(500):
                tape.insert(0, 0)
            newcursor += 500
        if newcursor == len(tape):
            for i in range(500):
                tape.append(0)
        return (newcursor, contvalue)
    return doit


def parse(lines):
    statere = re.compile(r"Begin in state ([A-Z])")
    state = statere.match(lines[0]).group(1)
    iterationsre = re.compile(r"Perform a diagnostic checksum after (\d+) steps")
    iterations = int(iterationsre.match(lines[1]).group(1))
    rules = {}
    rulestartre = re.compile(r"In state ([A-Z])")
    writere = re.compile(r"Write the value ([0-1])")
    movere = re.compile(r"Move one slot to the (right|left)")
    contre = re.compile(r"Continue with state ([A-Z])")
    for i in range(3, len(lines), 10):
        curstate = rulestartre.match(lines[i]).group(1)
        zerorule = createrule(writere.search(lines[i+2]).group(1),movere.search(lines[i+3]).group(1),contre.search(lines[i+4]).group(1))
        onerule = createrule(writere.search(lines[i+6]).group(1),movere.search(lines[i+7]).group(1),contre.search(lines[i+8]).group(1))
        rules[curstate] = (zerorule, onerule)
    return (state, iterations, rules)

def part1(program):
    (state, iterations, rules) = parse(program)
    tape = 100000 * [0]
    cursor = int(len(tape)/2)
    for i in range(iterations):
        (cursor, state) = rules[state][tape[cursor]](tape, cursor)
    return sum(tape)

if __name__ == "__main__":
    program = sys.stdin.readlines()
    print part1(program)
