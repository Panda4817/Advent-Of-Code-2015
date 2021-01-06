import itertools
# part 2 in part 1
def part1(data):
  lst = data.split("\n")
  ings = {}
  for l in lst:
    parts = l.split()
    ings[parts[0][:-1]] = {
      'capacity': int(parts[2][:-1]),
      'durability': int(parts[4][:-1]),
      'flavour': int(parts[6][:-1]),
      'texture': int(parts[8][:-1]),
      'calories': int(parts[-1]),
    }
  
  print(ings)
  ingredients = list(ings.keys())
  print(ingredients)
  l = len(ingredients)
  cookie_total = {}
  combi = list(itertools.permutations(range(l), l))
  print(combi)
  total_teaspoon = 100
  teaspoons_combo = [
    gp for gp in itertools.combinations_with_replacement(range(101) , l) if sum(gp) == total_teaspoon
  ]
  for t in teaspoons_combo:
    assert sum(t) == total_teaspoon
    cookie_total[t] = {}
    for c in combi:
      t_vals = {}
      for n, v in zip(c, t):
        t_vals[ingredients[n]] = v
      
      capacity = 0
      durability = 0
      flavour = 0
      texture = 0
      calories = 0
      for i in range(l):
        capacity += ings[ingredients[i]]['capacity'] * t_vals[ingredients[i]]
        durability += ings[ingredients[i]]['durability'] * t_vals[ingredients[i]]
        flavour += ings[ingredients[i]]['flavour'] * t_vals[ingredients[i]]
        texture += ings[ingredients[i]]['texture'] * t_vals[ingredients[i]]
        calories += ings[ingredients[i]]['calories'] * t_vals[ingredients[i]]
      
      if capacity < 0:
        capacity = 0
      if durability < 0:
        durability = 0
      if flavour < 0:
        flavour = 0
      if texture < 0:
        texture = 0
      
      total = capacity * durability * flavour * texture
      # Calories is part of part 2
      if calories != 500 or total == 0:
        continue

      cookie_total[t][c] = total
      print(t, c, total, calories)
      print()
  
  highest = 0
  teaspoons = None
  indices = None
  for k, v in cookie_total.items():
    for ke, ve in v.items():
      if ve > highest:
        highest = ve
        teaspoons = k
        indices = ke

  return highest, teaspoons, indices

    
