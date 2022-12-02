elves = [0]

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


with open("./01/input.txt", "r") as f:
  for line in f.readlines():
    if line == '\n':
      elves.append(0)
      continue
    elves[-1] += int(line)

print(max(elves))
top3 = sorted(elves, reverse=True)[:3]
print(sum(top3))