import copy

def part1(data):
  seq = [int(i) for i in list(data)]
  print(seq)
  rounds = 50
  for i in range(rounds):
    current_num = None
    count = 0
    cp = copy.deepcopy(seq)
    seq = []
    for s in cp:
      if s == current_num and current_num != None:
        count += 1
      else:
        if current_num != None:
          seq.append(count)
          seq.append(current_num)
        current_num = s
        count = 1
    seq.append(count)
    seq.append(current_num)

 
  return len(seq)
