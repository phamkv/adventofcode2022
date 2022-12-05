from copy import deepcopy
# Parsing: https://www.reddit.com/r/adventofcode/comments/zcxid5/comment/iz01qpy/?utm_source=share&utm_medium=web2x&context=3
def part1(crates, moves):
    for move in moves:
        amount, where, to = move
        for _ in range(amount):
            x = crates[where-1].pop()
            crates[to-1].append(x)
    return crates

def part2(crates, moves):
    for move in moves:
        amount, where, to = move
        stack = []

        for _ in range(amount):
            x = crates[where-1].pop()
            stack.append(x)
        for _ in range(amount):
            crates[to-1].append(stack.pop())
    return crates

with open("crates.txt") as f:
    crates, moves = f.read().split("\n\n")
    moves = [[int(c) for c in move.split() if c.isdigit()] for move in moves.splitlines()]

    arr = []
    for x in crates.splitlines()[:-1][::-1]:
        arr.append((x[1::4]))
    crates = list(zip(*arr))
    #crates = list(zip(*[x[1::4] for x in crates.splitlines()[:-1][::-1]]))
    crates = [[crate for crate in stack if crate != " "] for stack in crates]

    ans = part1(deepcopy(crates),moves)
    print([x[-1] for x in ans])

    ans = part2(deepcopy(crates),moves)
    print([x[-1] for x in ans])
