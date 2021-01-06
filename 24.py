import itertools
def part1(data):
  
  weights = set([int(i) for i in data.split("\n")])
  print(weights)
  total = sum(weights)
  each = total // 3
  # part 2 - total // 4
  print(total, each)
  length = len(weights)
  print(length)


  combi = []

  for i in range(1, length):
      combi.extend([ gr for gr in itertools.combinations(weights, i) if sum(gr) == each])
      if len(combi) > 0:
          break

  print(len(combi))

  def prod(a):
      s=1
      for n in a:
          s *= n
      return s

  em = float('inf')
  group1 = set()
  for c in combi:
      s = set(c)
      r = weights - s
      e = prod(s)
      if e < em:
          em = e
          group1 = s
      else:
          continue
  return (em, group1, r)