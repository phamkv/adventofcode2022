import collections

characters = collections.defaultdict(int)
with open("packetmarker.txt", "r") as f:
  packet = f.read()
  left = ans = 0
  for right in range(len(packet)):
    characters[packet[right]] += 1
    if right > 12:
      if len(set(characters)) == 14:
        ans = right + 1
        break
      characters[packet[left]] -= 1
      if characters[packet[left]] == 0:
        del characters[packet[left]]
      left += 1
  print(str(ans))