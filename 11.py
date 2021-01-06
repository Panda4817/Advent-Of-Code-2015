
# Part 2 in part 1
def part1(data):
  old = list(data)
  print(old)
  length = len(old)
  def isValid(p):
    
    # Part 1 solution, and also part of part 2
    if "".join(p) == "hxbxxyzz":
      return False
    
    straight = 0
    different_pairs = 0
    pairs = []
    for c in range(length):
      if p[c] == 'i' or p[c] == 'o' or p[c] == 'l':
        return False
      try:
        if p[c] == p[c + 1] and p[c - 1] != p[c] and p[c] not in pairs:
          different_pairs += 1
          pairs.append(p[c])
        if p[c + 1] == chr(ord(p[c]) + 1) and p[c + 2] == chr(ord(p[c]) + 2):
          straight += 1
      except IndexError:
        continue
    if straight >= 1 and different_pairs >= 2:
      return True
    return False
  
  def incrememnt(l):
    if l != 'z':
      return chr(ord(l) + 1)
    return 'a'
  
  def adjust(p, isChanged):
    changed = isChanged
    for c in reversed(range(1, length)):
      if p[c] == 'a' and changed:
        p[c - 1] = incrememnt(p[c - 1])
        changed = True
      else:
        changed = False
  
  while(isValid(old) == False):
    old[length - 1] = incrememnt(old[length - 1])
    adjust(old, True)
  
  return "".join(old)


    
      
