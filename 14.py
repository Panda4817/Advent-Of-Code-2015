
# part 2 in part1 
def part1(data):
  lst = data.split("\n")
  info = {}
  for l in lst:
    parts = l.split()
    info[parts[0]] = {
      'dist': int(parts[3]),
      'fly': int(parts[6]),
      'rest': int(parts[13]),
      'rest_started': None,
      'fly_started': 0,
      'total_dist': 0,
      'points': 0
    }
  
  print(info)
  seconds = 2503

  # part 2 - keep track of highest total distance per second
  current_highest = 0
  
  for i in range(seconds):
    for r, v in info.items():
      if v['rest_started'] != None and i - v['rest_started'] != v['rest']:
        continue
      if v['fly_started'] != None and i - v['fly_started'] == v['fly']:
        v['rest_started'] = i
        v['fly_started'] = None
        continue
      if v['rest_started'] != None and i - v['rest_started'] == v['rest']:
        v['fly_started'] = i
        v['rest_started'] = None
      
      v['total_dist'] += v['dist']
      if v['total_dist'] > current_highest:
        current_highest = v['total_dist']
    
    # Part 2-  award points based on highest total distance per second
    for r, v in info.items():
      if v['total_dist'] == current_highest:
        v['points'] += 1

  totals = {}
  for i in info:
    print(i)
    print(info[i])
    totals[i] = info[i]['points']
  
  maxi = max(totals, key=lambda key: totals[key])
  print(maxi)

  return totals[maxi]
  

      
      

