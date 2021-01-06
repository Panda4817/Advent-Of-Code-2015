def part1(data):
  floor = 0
  for i in data:
    if i == '(':
      floor += 1
    elif i == ')':
      floor -= 1
  return floor

def part2(data):
  floor = 0
  for i in range(len(data)):
    if data[i] == '(':
      floor += 1
    elif data[i] == ')':
      floor -= 1
    if floor == -1:
      return i + 1