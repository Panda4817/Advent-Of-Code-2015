import numpy as np

def part1(data):
  grid = np.zeros((3030*2, 3030*2), dtype=float)
  print(grid.shape)
  for d in range(3030*2):
      if d == 0:
          grid[0:1, 0:1] = 20151125
          continue
      elif d == 1:
          n = grid[0:1, 0:1]
          num = (n * 252533) % 33554393
          grid[1: 2, 0: 1] = num

          n = grid[1:2, 0:1]
          num = (n * 252533) % 33554393
          grid[0: 1, 1: 2] = num
          continue
      u = 0
      for r in range(d, -1, -1):
          if u == 0:
              n = grid[0:1, u + d - 1: (u+d)]
              num = (n * 252533) % 33554393
              grid[r: r + 1, u: u + 1] = num
          elif u > 0:
              n = grid[r + 1: r + 2, u - 1: u]
              num = (n * 252533) % 33554393
              grid[r: r + 1, u: u + 1] = num
          u += 1
          if u > d:
              break
        
            

  print(grid)
  return grid[2946: 2947, 3028:3029]