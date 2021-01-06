def part1(data):
  presents = int(data)//10
  print(presents)
  houses = [0] * presents
  for e in range(1, presents):
    for h in range(e, presents, e):
      houses[h] += e

  for h in range(len(houses)):
    if houses[h] >= presents:
      print(h, houses[h])
      return h
      break

def part2(data):
  presents = int(data)//11
  print(presents)
  houses = [0] * presents
  for e in range(1, presents):
    for h in range(e, presents, e):
      if h == 50 * e:
        break
      houses[h] += e

  for h in range(len(houses)):
    if houses[h] >= presents:
      print(h, houses[h])
      return h
      break