import numpy as np
import copy

# Part 2 in part 1
def part1(data):
  rows = [list(r) for r in data.split("\n")]
  grid = np.array(rows)
  grid = np.where(grid == '#', 1, 0)
  steps = 100
  
  # Part 2
  corners = [
    (0, 0),
    (99, 99),
    (0, 99),
    (99, 0)
  ]
  for c in corners:
    grid[c[0]:c[0] + 1, c[1]:c[1] +1] = 1
    
  print(grid)
  def get_neighbors(i, j):
    n = []
    for a in range(i - 1, i + 2):
      for b in range(j - 1, j + 2):
        if (a, b) == (i, j) or a < 0 or b < 0 or a > 100 or j > 100:
          continue
        n.append((a, b))
    
    return n
  
  for s in range(steps):
    cp = copy.deepcopy(grid)
    for i in range(100):
      for j in range(100):
        # Part 2
        if (i, j) in corners:
          continue
        neigh = get_neighbors(i, j)
        how_many_on = 0
        for n in neigh:
          if cp[n[0]:n[0] + 1, n[1]: n[1] + 1] == 1:
            how_many_on += 1
        
        if how_many_on == 3 and cp[i: i + 1, j: j + 1] == 0:
          grid[i: i + 1, j: j + 1] = 1
        elif cp[i: i + 1, j: j + 1] == 1 and (how_many_on < 2 or how_many_on > 3):
          grid[i: i + 1, j: j + 1] = 0
  
  return (grid == 1).sum()
  
  
