def part1(data):
  houses = []
  visited = []
  currentx = 0
  currenty = 0
  
  for d in data:
    visited.append((currentx, currenty))
    if d == '>':
      currentx += 1
    elif d == '<':
      currentx -= 1
    elif d == '^':
      currenty += 1
    elif d == 'v':
      currenty -= 1
    visited.append((currentx, currenty))
  
  for v in visited:
    if v in houses:
      continue
    houses.append(v)
    
  
  return len(houses)

def part2(data):
  houses = []
  visited = []
  santa_currentx = 0
  santa_currenty = 0
  robo_currentx = 0
  robo_currenty = 0

  santa = True
  
  for d in data:
    if santa:
      visited.append((santa_currentx, santa_currenty))
      if d == '>':
        santa_currentx += 1
      elif d == '<':
        santa_currentx -= 1
      elif d == '^':
        santa_currenty += 1
      elif d == 'v':
        santa_currenty -= 1
      visited.append((santa_currentx, santa_currenty))
      santa = False
    else:
      visited.append((robo_currentx, robo_currenty))
      if d == '>':
        robo_currentx += 1
      elif d == '<':
        robo_currentx -= 1
      elif d == '^':
        robo_currenty += 1
      elif d == 'v':
        robo_currenty -= 1
      visited.append((robo_currentx, robo_currenty))
      santa = True
  
  for v in visited:
    if v in houses:
      continue
    houses.append(v)
    
  
  return len(houses)
