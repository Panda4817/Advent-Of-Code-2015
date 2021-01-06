# part 2 in part 1
def part1(data):
  lst = data.split("\n")
  aunts = {}
  for l in lst:
    parts = l.split()
    aunts[parts[1][:-1]] = {
      parts[2][:-1] : int(parts[3][:-1]),
      parts[4][:-1] : int(parts[5][:-1]),
      parts[6][:-1] : int(parts[7]),
    }
  
  ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
  }

  def check_aunt(v):
    for ke, ve in v.items():
      # The conditions are part pf part 2
      if ke == 'cats' or ke == 'trees':
        if ve <= ticker_tape[ke]:
          return False
      elif ke == 'pomeranians' or ke == 'goldfish':
        if ve >= ticker_tape[ke]:
          return False
      elif ticker_tape[ke] != ve:
        return False
    return True
  
  possible_aunt = []
  for k, v in aunts.items():
    if check_aunt(v):
      possible_aunt.append(k)
  
  return possible_aunt[0]

