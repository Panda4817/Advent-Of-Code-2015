import copy
import itertools
# Part 2 in part 1
def part1(data):
  shop = {
    'weapons': {
      'Greataxe': {'c': 74, 'd': 8, 'a': 0},
      'Longsword': {'c': 40, 'd': 7, 'a': 0},
      'Warhammer': {'c': 25, 'd': 6, 'a': 0},
      'Shortsword': {'c': 10, 'd': 5, 'a': 0},
      'Dagger': {'c': 8, 'd': 4, 'a': 0},
      
    },
    'armour': {
      'Platemail': {'c': 102, 'd': 0, 'a': 5},
      'Bandedmail': {'c': 75, 'd': 0, 'a': 4},
      'Splitmail': {'c': 53, 'd': 0, 'a': 3},
      'Chainmail': {'c': 31, 'd': 0, 'a': 2},
      'Leather': {'c': 13, 'd': 0, 'a': 1},
      'None': {'c': 0, 'd': 0, 'a': 0}  
    },
    'rings1': {
      'dam+3': {'c': 100, 'd': 3, 'a': 0},
      'dam+2': {'c': 50, 'd': 2, 'a': 0},
      'dam+1': {'c': 25, 'd': 1, 'a': 0}, 
      'def+3': {'c': 80, 'd': 0, 'a': 3},
      'def+2': {'c': 40, 'd': 0, 'a': 2},
      'def+1': {'c': 20, 'd': 0, 'a': 1},
      'None': {'c': 0, 'd': 0, 'a': 0}    
    },
    'rings2': {
      'dam+3': {'c': 100, 'd': 3, 'a': 0},
      'dam+2': {'c': 50, 'd': 2, 'a': 0},
      'dam+1': {'c': 25, 'd': 1, 'a': 0}, 
      'def+3': {'c': 80, 'd': 0, 'a': 3},
      'def+2': {'c': 40, 'd': 0, 'a': 2},
      'def+1': {'c': 20, 'd': 0, 'a': 1},
      'None': {'c': 0, 'd': 0, 'a': 0} 
    }
  }

  my_dict = {
    'w': list(shop['weapons'].keys()), 
    'a': list(shop['armour'].keys()),
    'r1': list(shop['rings1'].keys()),
    'r2': list(shop['rings2'].keys())
  }

  allNames = sorted(my_dict)
  combinations = list(itertools.product(*(my_dict[Name] for Name in allNames)))
  combi = []
  for c in combinations:
    eliminate_duplicates = set()
    for v in c:
      eliminate_duplicates.add(v)
    combi.append(eliminate_duplicates)
  print(combi)
  
  my_stats = [100, 0, 0]
  boss_stats = [int(i.split(": ")[1]) for i in data.split("\n")]

  def play(player, boss):
    turn = 1
    def playerTurn():
      dam = player[1] - boss[2]
      if dam < 0:
        dam = 1
      boss[0] -= dam
      if boss[0] < 0:
        boss[0] = 0
      
    def bossTurn():
      dam = boss[1] - player[2]
      if dam < 0:
        dam = 1
      player[0] -= dam
      if player[0] < 0:
        player[0] = 0

    while(player[0] > 0 and boss[0] > 0):
      if turn == 1:
        playerTurn()
        turn = 2
      elif turn == 2:
        bossTurn()
        turn = 1
      
      if player[0] == 0:
        return 2
      elif boss[0] == 0:
        return 1
  
  winners = []
  for c in combi:
    cpplayer = copy.deepcopy(my_stats)
    cpboss = copy.deepcopy(boss_stats)
    cost = 0
    chosen = [0, 0]
    for k in c:
      for key, value in shop.items():
        if k in value:
          cpplayer[1] += value[k]['d']
          cpplayer[2] += value[k]['a']
          cost += value[k]['c']
          chosen[0] += value[k]['d']
          chosen[1] += value[k]['a']
          break
    ans = play(cpplayer, cpboss)
    winners.append({'c': cost, 'd': chosen[0], 'a': chosen[1], 'w':ans})


  
  lowest = 400
  highest = 0
  for w in winners:
    # Part 1
    if w['c'] < lowest and w['w'] == 1:
      lowest = w['c']
    # Part 2
    if w['c'] > highest and w['w'] == 2:
      highest = w['c']
   
  return lowest, highest

  
    
      


