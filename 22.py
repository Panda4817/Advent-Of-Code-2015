import math
import copy

def part1(data):
  wizard_spells = {
    'poison': {'c': 173, 'd': 3, 'h': 0, 'a': 0, 't': 6, 'm': 0, 'od': 12 },
    'magic_missile': {'c': 53, 'd': 4, 'h': 0, 'a': 0, 't': 1, 'm': 0, 'od': 4},
    'drain': {'c': 73, 'd': 2, 'h': 2, 'a': 0, 't': 1, 'm': 0, 'od': 2 },
    'recharge': {'c': 229, 'd': 0, 'h': 0, 'a': 0, 't': 5, 'm': 101, 'od': 0 },
    'shield': {'c': 113, 'd': 0, 'h': 0, 'a': 7, 't': 6, 'm': 0, 'od': 0 },  
  }

  boss_action = 8

  my_stats = [50, 0, 500]
  boss_stats = [55, 0, 8]


  player = 'player'
  boss = 'boss'
  def initial_state():
    
    return {
      player: [50, 0, 500, {'shield': 0, 'recharge': 0, 'poison': 0}, 0, False],
      boss: [55, 8, True]
    }
  
  def player(stats):
    if stats[player][-1] == False:
      return player
    elif stats[boss][-1] == False:
      return boss
  
  def actions(stats, pl):
    actions = []
    if pl == player:
      for s, v in wizard_spells.items():
        if stats[player][2] < v['m']:
          continue
        if v['t'] > 1:
          if stats[player][3][s] > 1:
            continue
        actions.append(s)
    elif pl == boss:
      if stats[player][3]['shield'] > 1:
        dam = boss_action - stats[player][1]
      else:
        dam = boss_action
      if dam < 0:
        dam = 1
      actions.append(dam)
    print(actions)
    return actions
  
  def result(stats, action):
    cp = copy.deepcopy(stats)
    for e in cp[player][3]:
      if cp[player][3][e] > 0:
        cp[boss][0] -= wizard_spells[e]['d']
        cp[player][3][e] -= 1
        if e == 'shield' and cp[player][3][e] == 0:
          cp[player][1] -= wizard_spells[e]['a']
    
    if isinstance(action, int):
      cp[player][0] -= action
      cp[boss][-1] == True
      cp[player][-1] = False
    elif isinstance(action, str):
      
      cp[player][2] -= wizard_spells[action]['c']
      cp[player][4] += wizard_spells[action]['c']
      cp[player][1] += wizard_spells[action]['a']
      cp[player][0] += wizard_spells[action]['h']
      cp[player][2] += wizard_spells[action]['m']
      cp[player][-1] = True
      cp[boss][-1] = False
      
      if action == 'magic_missile' or action == 'drain':
        cp[boss][0] -= wizard_spells[action]['d']   
      elif action == 'posion' or action == 'shield' or action == 'recharge':
        cp[player][3][action] = wizard_spells[action]['t']
    return cp
  
  def winner(stats):
    if stats[player][0] <= 0:
      winner = boss
    elif stats[boss][0] <= 0:
      winner = player
    elif stats[player][2] <= 0:
      winner = boss
    else:
      winner = None
    
    return (winner, stats[player][4])
  
  def terminal(stats):
    if winner(stats) != None:
      if stats[player][0] > 0 and stats[boss][0] > 0 and stats[player][2] > 0:
        return False
      else:
        return True
    else:
      return False
  
  def utility(stats):
    win = winner(stats)
    if win[0] == boss:
      return -1
    elif win[0] == player:
      return 1
    else:
      return 0
    
  
  def maxValue(stats, alpha, beta):
    """
    Returns the best utility for an action with alpha beta pruning for a max-player.
    """
    # Check the board is not terminal, if so, return utility
    if terminal(stats):
        return utility(stats)
    # Initiate a variable to store bestv utility, which for a max player is the lowest value possible
    pl = player(stats)
    bestv = float("-inf")

    # Loop through actions, calculating the minimum value, uses recursion
    for action in actions(stats, pl):
        v = minValue(result(stats, action), alpha, beta)
        # Find the max value between current v and bestv and update bestv
        bestv = max(bestv, v)
        # Find max between alpha and bestv and update alpha
        alpha = max(alpha, bestv)
        # Check if beta is less than or = to alpha, if so stop searching tree and return bestv
        if beta <= alpha:
            break
    return bestv

  def minValue(stats, alpha, beta):
    """
    Returns the best utility for an action with alpha beta pruning for a min-player.
    """
    # Check the board is not terminal, if so, return utility
    if terminal(stats):
        return utility(stats)
    # Initiate a variable to store bestv utility, which for a min player is the highest value possible

    pl = player(stats)
    bestv = float("inf")
    
    # Loop through actions, calculating the maximum value, uses recursion
    for action in actions(stats, pl):
        v = maxValue(result(stats, action), alpha, beta)
        # Find the min value between current v and bestv and update bestv
        bestv = min(bestv, v)
        # Find min between beta and bestv and update beta
        beta = min(beta, bestv)
        # Check if beta is less than or = to alpha, if so stop searching tree and return bestv
        if beta <= alpha:
            break
    return bestv
  
  def minimax(stats):
    """
    Returns the optimal action for the current player on the stats.
    """
    # Check if board is terminal, if so return None
    if terminal(stats):
        return None
    
    # Workout whose turn it is using the player function
    pl = player(stats)

    # Workout all the possible moves from the board
    moves = actions(stats, pl)

    # Initiate a list, which will store {"moves": action, "v": best utility value}
    utility = []

    # Inititate a explored list to keep track of the actions already explored
    explored = set()

    # Initiate the best alpha and beta variables (alpha is for the max-player and beta is for the min-player)
    alpha = float("-inf")
    beta = float("inf")

    # If next player is player, use the minValue function
    if pl == player:
        # Loop through actions
        for move in moves:
            # Check the move is not in explored
            if not move in explored:
                # Add to list the (row, cell) pair as move and call minValue function, to find opponents best value and from that find your best value
                utility.append({'move': move, 'v': minValue(result(stats, move), alpha, beta)})
                # Add the move to explored
                explored.add(move)
        # Find the max value from all actions
        optimal = max(utility, key=lambda x: x['v'])
        return optimal['move']
    
    # If the next player is boss, use the max-value function
    if pl == boss:
        # Loop through actions
        for move in moves:
            # Check the move is not in explored
            if not move in explored:
                # Add to list the (row, cell) pair as move and call maxValue function, to find opponents best value and from that find your best value
                utility.append({'move': move, 'v': maxValue(result(stats, move), alpha, beta)})
                # Add the move to explored
                explored.add(move)
        # Find the min value from all actions 
        optimal = min(utility, key=lambda x: x['v'])
        return optimal['move']
  
  stats = initial_state()
  while(terminal(stats) == False):
    move = minimax(stats)
    print(move) 
    stats = result(stats, move)
    print(stats)






    




