import copy

def part1(data):
  lst = data.split("\n")
  var = {}
  var_lst = []
  ops = ['NOT', 'OR', 'AND', 'LSHIFT', 'RSHIFT', '->']

  def isInt(n):
    try:
      int(n)
      return True
    except ValueError:
      return False

  cp = copy.deepcopy(lst)
  for c in cp:
    parts = c.split(" -> ")
    other_parts = c.split()
    for o in other_parts:
      if o not in ops and o not in var_lst:
        if isInt(o) == False:
          var_lst.append(o)
    
    if isInt(parts[0]):
      var[parts[1]] = int(parts[0])
      lst.remove(c)

  print(var)


  def returnVals(nums):
    vals = []
    for n in nums:
      if isInt(n):
        vals.append(int(n))
      elif n != '':
        vals.append(var[n])
    return vals
  
  
  while(len(var.keys()) != len(var_lst)):
    cp = copy.deepcopy(lst)
    for c in cp:
      parts = c.split(" -> ")
      ans = None
      try:
        if 'AND' in parts[0]:
          nums = parts[0].split(" AND ")
          vals = returnVals(nums)
          ans = vals[0] & vals[1]
        elif 'OR' in parts[0]:
          nums = parts[0].split(" OR ")
          vals = returnVals(nums)
          ans = vals[0] | vals[1]
        elif 'LSHIFT' in parts[0]:
          nums = parts[0].split(" LSHIFT ")
          vals = returnVals(nums)
          ans = vals[0] << vals[1]
        elif 'RSHIFT' in parts[0]:
          nums = parts[0].split(" RSHIFT ")
          vals = returnVals(nums)
          ans = vals[0] >> vals[1]
        elif 'NOT' in parts[0]:
          nums = parts[0].split("NOT ")
          vals = returnVals(nums)
          ans = ~vals[0]
        else:
          vals = returnVals([parts[0]])
          ans = vals[0]
        
        if ans != None and ans < 0:
          ans += 2**16
        if ans != None:
          var[parts[1]] = ans
          lst.remove(c)
      except KeyError:
        continue
  
  return var['a']

def part2(data):
  overide = 3176
  lst = data.split("\n")
  var = {}
  var_lst = []
  ops = ['NOT', 'OR', 'AND', 'LSHIFT', 'RSHIFT', '->']

  def isInt(n):
    try:
      int(n)
      return True
    except ValueError:
      return False

  cp = copy.deepcopy(lst)
  for c in cp:
    parts = c.split(" -> ")
    other_parts = c.split()
    for o in other_parts:
      if o not in ops and o not in var_lst:
        if isInt(o) == False:
          var_lst.append(o)
    
    if isInt(parts[0]):
      if parts[1] == 'b':
        var[parts[1]] = overide
      else:
        var[parts[1]] = int(parts[0])
      lst.remove(c)

  
  def returnVals(nums):
    vals = []
    for n in nums:
      if isInt(n):
        vals.append(int(n))
      elif n != '':
        vals.append(var[n])
    return vals
  
  
  while(len(var.keys()) != len(var_lst)):
    cp = copy.deepcopy(lst)
    for c in cp:
      parts = c.split(" -> ")
      ans = None
      try:
        if 'AND' in parts[0]:
          nums = parts[0].split(" AND ")
          vals = returnVals(nums)
          ans = vals[0] & vals[1]
        elif 'OR' in parts[0]:
          nums = parts[0].split(" OR ")
          vals = returnVals(nums)
          ans = vals[0] | vals[1]
        elif 'LSHIFT' in parts[0]:
          nums = parts[0].split(" LSHIFT ")
          vals = returnVals(nums)
          ans = vals[0] << vals[1]
        elif 'RSHIFT' in parts[0]:
          nums = parts[0].split(" RSHIFT ")
          vals = returnVals(nums)
          ans = vals[0] >> vals[1]
        elif 'NOT' in parts[0]:
          nums = parts[0].split("NOT ")
          vals = returnVals(nums)
          ans = ~vals[0]
        else:
          vals = returnVals([parts[0]])
          ans = vals[0]
        
        if ans != None and ans < 0:
          ans += 2**16
        if ans != None:
          var[parts[1]] = ans
          lst.remove(c)
      except KeyError:
        continue

  return var['a']

        