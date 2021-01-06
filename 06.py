import numpy as np

def part1(data):
  lights = np.zeros((1000, 1000), dtype=int)

  def turn_on(start_row, end_row, start_col, end_col):
    lights[start_row:end_row, start_col:end_col] = np.ones((end_row - start_row, end_col - start_col), dtype=int)
  
  def toggle(start_row, end_row, start_col, end_col):
    for i in range(start_row, end_row):
      for j in range(start_col, end_col):
        if lights[i:i+1, j:j+1] == 1:
          lights[i:i+1, j:j+1] = 0
        else:
          lights[i:i+1, j:j+1] = 1
  
  def turn_off(start_row, end_row, start_col, end_col):
    lights[start_row:end_row, start_col:end_col] = np.zeros((end_row - start_row, end_col - start_col), dtype=int)
  
  instructions = data.split("\n")
  for i in instructions:
    splitter = ''
    if 'toggle' in i:
      splitter = 'toggle '
    else:
      splitter = " ".join(i.split()[0:2]) + ' '
    second_parts = i.split(splitter)
    num_parts = second_parts[1].split(" through ")
    
    coord = []
    for n in num_parts:
      coord.extend([int(j) for j in n.split(",")])

    start_row = coord[1]
    end_row = coord[3] + 1
    start_col = coord[0]
    end_col = coord[2] + 1
    if splitter == 'toggle ':
      toggle(start_row, end_row, start_col, end_col)
    elif splitter == 'turn off ':
      turn_off(start_row, end_row, start_col, end_col)
    elif splitter == 'turn on ':
      turn_on(start_row, end_row, start_col, end_col)
  
  return dict(zip(*np.unique(lights, return_counts=True)))[1]

def part2(data):
  lights = np.zeros((1000, 1000), dtype=int)

  def turn_on(start_row, end_row, start_col, end_col):
    lights[start_row:end_row, start_col:end_col] += 1
  
  def toggle(start_row, end_row, start_col, end_col):
    lights[start_row:end_row, start_col:end_col] += 2
  
  def turn_off(start_row, end_row, start_col, end_col):
    lights[start_row:end_row, start_col:end_col]  -= 1
    for i in range(start_row, end_row):
      for j in range(start_col, end_col):
        if lights[i:i+1, j:j+1] < 0:
          lights[i:i+1, j:j+1] = 0
  
  instructions = data.split("\n")
  for i in instructions:
    splitter = ''
    if 'toggle' in i:
      splitter = 'toggle '
    else:
      splitter = " ".join(i.split()[0:2]) + ' '
    second_parts = i.split(splitter)
    num_parts = second_parts[1].split(" through ")
    
    coord = []
    for n in num_parts:
      coord.extend([int(j) for j in n.split(",")])

    start_row = coord[1]
    end_row = coord[3] + 1
    start_col = coord[0]
    end_col = coord[2] + 1
    if splitter == 'toggle ':
      toggle(start_row, end_row, start_col, end_col)
    elif splitter == 'turn off ':
      turn_off(start_row, end_row, start_col, end_col)
    elif splitter == 'turn on ':
      turn_on(start_row, end_row, start_col, end_col)
  
  return np.sum(lights)
