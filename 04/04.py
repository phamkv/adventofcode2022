ans = 0
with open("assignments.txt", "r") as f:
    for line in f.readlines():
        line = line.split(",")
        first, second = line[0], line[1].strip()
        a1 = list(map(lambda section: int(section) ,first.split("-")))
        a2 = list(map(lambda section: int(section) ,second.split("-")))
        #if a1[0] <= a2[0] and a2[1] <= a1[1] or a2[0] <= a1[0] and a1[1] <= a2[1]:
        #    ans += 1
        if a1[0] <= a2[1] and a2[0] <= a1[1]:
            ans += 1

print(ans)