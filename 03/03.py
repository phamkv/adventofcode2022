ans = 0

""" with open("rucksack.txt") as f:
    for line in f.readlines():
        type = ""
        mid = len(line) // 2
        count = set()
        for c in line[:mid]:
            count.add(c)
        for c in line[mid:]:
            if c in count:
                type = c
                break
        priority = 0
        if type.islower():
            priority = ord(type) - 96
        else:
            priority = ord(type) - 64 + 26
        ans += priority """

group = 1
first = set()
second = set()
type = ""
with open("rucksack.txt") as f:
    for line in f.readlines():
        if group == 1:
            for c in line:
                first.add(c)
            group += 1
        elif group == 2:
            for c in line:
                if c in first:
                    second.add(c)
            group += 1
        else:
            for c in line:
                if c in second:
                    type = c
                    break
            if type.islower():
                ans += ord(type) - 96
            else:
                ans += ord(type) - 64 + 26
            group = 1
            first = set()
            second = set()

print(ans)