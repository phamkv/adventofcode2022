ans = 0
#points = { "A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3 }
#result = { 0: 3, -1: 6, 2: 6, -2: 0, 1: 0}

points = { "A": 1, "B": 2, "C": 3}
lose = { "A": 3, "B": 1, "C": 2}
win = { "A": 2, "B": 3, "C": 1}

with open("02/strategy.txt", "r") as f:
  for line in f.readlines():
    test = line.split(" ")
    first, second = test[0], test[1].strip()
    # ans += result[points[first] - points[second]] + points[second]
    if second == "X":
      ans += lose[first]
    elif second == "Y":
      ans += points[first] + 3
    else:
      ans += win[first] + 6

print(ans)