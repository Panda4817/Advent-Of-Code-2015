import itertools

# Part 2 in part 1
def part1(data):
  lst = data.split("\n")
  next_to = {}
  names = []
  for l in lst:
    parts = l.split()
    if parts[0] not in names:
      names.append(parts[0])
    if parts[10][:-1] not in names:
      names.append(parts[10][:-1])
    if parts[0] not in next_to:
      next_to[parts[0]] = {}
    if parts[10][:-1] not in next_to[parts[0]]:
      next_to[parts[0]][parts[10][:-1]] = {}
    if parts[2] not in next_to[parts[0]][parts[10][:-1]]:
      next_to[parts[0]][parts[10][:-1]][parts[2]] = int(parts[3])

  # Part 2 - Include me with gain and loss of 0
  for k, v in next_to.items():
    v['me'] = {}
    v['me']['gain'] = 0
    v['me']['lose'] = 0
  next_to['me'] = {}
  for k in next_to:
     next_to['me'][k] = {}
     next_to['me'][k]['gain'] = 0
     next_to['me'][k]['lose'] = 0
  
  names.append('me')
  print(names)
  length = len(names)
  combo = list(itertools.permutations(names))
  total_happiness = []
  for c in combo:
    total = 0
    for i in range(length):
      p1 = c[i]
      if i == length - 1:
        p2 = c[0]
      else:
        p2 = c[i + 1]
      
      try:
        total += next_to[p1][p2]['gain']
        
      except KeyError:
        total -= next_to[p1][p2]['lose']
        
      
      try:
        total -= next_to[p2][p1]['lose']
      except KeyError:
        total += next_to[p2][p1]['gain']

    total_happiness.append(total)

  maxi = max(total_happiness)
  index = total_happiness.index(maxi)
  return combo[index], maxi