import itertools

# Part 2 in part 1
def part1(data):
  containers = [int(i) for i in data.split("\n")]
  print(containers)
  l = len(containers)
  combi = []
  for i in range(1, l + 1):
    combi.extend([gr for gr in itertools.combinations(containers, i) if sum(gr) == 150])
  
  lowest = l
  count = 0
  for c in combi:
    temp = len(c)
    if temp < lowest:
      lowest = temp
      count = 1
    elif temp == lowest:
      count += 1
  
  return len(combi), count