import json

#part 2 in part 1
def part1(data):
  d = json.loads(data)
  
  def recurse_search(data):
    num = 0
    if isinstance(data, str) or isinstance(data, int):
      try:
        num += int(data)
      except ValueError:
        num += 0
    elif isinstance(data, list):
      for d in data:
        num += recurse_search(d)
    elif isinstance(data, dict):
      # part of part 2
      if 'red' in data.values():
        return num
      
      else:
        for v in data.values():
          num += recurse_search(v)
   
    
    return num
  
  ans =  recurse_search(d)
  return ans
      