import sys

Up = "Up"
Down = "Down"
Left = "Left"
Right = "Right"

def findStart(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == '|':
            return (0, i)
    assert False

def charAt(pos, grid):
    if pos[0] < 0  or pos[1] < 0 or pos[0] >= len(grid) or pos[1] >= len(grid[pos[0]]):
        return ' '
    return grid[pos[0]][pos[1]]

def findNextPos(direction, pos, grid):
    curChar = charAt(pos, grid)
    assert curChar != ' '
    if curChar == '+':
        leftChar = charAt((pos[0], pos[1]-1), grid)
        rightChar = charAt((pos[0], pos[1]+1), grid)
        upChar = charAt((pos[0]-1, pos[1]), grid)
        downChar = charAt((pos[0]+1, pos[1]), grid)

        if direction in [Up, Down]:
            if leftChar != ' ':
                return (Left, (pos[0], pos[1]-1))
            else:
                return (Right, (pos[0], pos[1]+1))
        else:
            if upChar != ' ':
                return (Up, (pos[0]-1, pos[1]))
            else:
                return (Down, (pos[0]+1, pos[1]))
    elif direction == Down:
        assert pos[0] + 1 < len(grid)
        return (direction, (pos[0] + 1, pos[1]))
    elif direction == Up:
        assert pos[0] - 1 >= 0
        return (direction, (pos[0] - 1, pos[1]))
    elif direction == Right:
        assert pos[1] + 1 < len(grid[0])
        return (direction, (pos[0], pos[1] + 1))
    elif direction == Left:
        assert pos[1] - 1 >= 0
        return (direction, (pos[0], pos[1] - 1))

def doit(grid):
    characters = ""
    pos = findStart(grid)
    lines = '|-+'
    direction = Down
    count = 1
    while True:
        (direction, pos) = findNextPos(direction, pos, grid)
        char = charAt((pos[0], pos[1]), grid)
        if char == ' ':
            break
        if char not in lines:
            characters += char
        count += 1
    return (characters, count)

if __name__ == "__main__":
    print doit(sys.stdin.readlines())
