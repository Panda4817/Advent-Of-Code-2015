import itertools
import math

# part 2 in part 1
def part1(data):
  lst = data.split("\n")
  places = []
  from_to = {}
  for l in lst:
    parts = l.split()
    print(parts)
    if parts[0] not in places:
      places.append(parts[0])
    if parts[2] not in places:
      places.append(parts[2])
    if parts[0] not in from_to:
      from_to[parts[0]] = {}
    if parts[2] not in from_to[parts[0]]:
      from_to[parts[0]][parts[2]] = int(parts[4])
  
  for k, v in from_to.items():
    print(k, v)
  

  length = len(places)
  print(length)
  combo = list(itertools.permutations(places))
  totals = []
  for c in combo:
    dis = 0
    
    for i in range(0, length - 1):
      try:
        dis += from_to[c[i]][c[i + 1]]
      except KeyError:
        dis += from_to[c[i+1]][c[i]]
    
    totals.append(dis)
    
    
  mini = min(totals)
  index = totals.index(mini)

  print(combo[index], mini)

  maxi = max(totals)
  index = totals.index(maxi)

  print(combo[index], maxi)

  return mini, maxi