import copy
wizard_spells = {
    'poison': {'c': 173, 'd': 3, 'h': 0, 'a': 0, 't': 6, 'm': 0, 'od': 12 },
    'magic_missile': {'c': 53, 'd': 4, 'h': 0, 'a': 0, 't': 0, 'm': 0, 'od': 4},
    'drain': {'c': 73, 'd': 2, 'h': 2, 'a': 0, 't': 0, 'm': 0, 'od': 2 },
    'recharge': {'c': 229, 'd': 0, 'h': 0, 'a': 0, 't': 5, 'm': 101, 'od': 0 },
    'shield': {'c': 113, 'd': 0, 'h': 0, 'a': 7, 't': 6, 'm': 0, 'od': 0 },  
}

min_mana_spent = float('inf')

class GameState(object):
    ongoing = 0
    win = 1
    loss = 2

class Character(object):
    
    def __init__(self, hp):
        self.hp = hp
    


class Player(Character):

    def __init__(self, hp, armour, mana, shield=0, recharge=0, poison=0):
        super().__init__(hp)
        self.mana = mana
        self.armour = armour
        self.effects = {
            'shield': shield,
            'recharge': recharge,
            'poison': poison,
        }

    def __str__(self):
        return f'<Player(hp={self.hp}, mana={self.mana}, armour={self.armour}, effects={self.effects})>'


class Boss(Character):

    def __init__(self, hp, damage):
        super().__init__(hp)
        self.damage = damage
    
    def __str__(self):
        return f'<Boss(hp={self.hp}, damage={self.damage})>'


class Node(object):

    def __init__(self, mana_spent, player, boss, state):
        self.mana_spent = mana_spent
        self.player = player
        self.boss = boss
        self.state = state  # type: GameState
        self.children = []

        self.make_children()
    
    def __str__(self):
        return f'<Node(mana_spent={self.mana_spent}, player={str(self.player)}, boss={self.boss}, state={self.state}, num_children={len(self.children)})>'
    
    @staticmethod
    def apply_effects(player, boss):
        for k, v in player.effects.items():
            if v > 0:
                player.effects[k] -= 1
                boss.hp -= wizard_spells[k]['d']
                player.mana += wizard_spells[k]['m']
                if k == 'shield' and player.effects[k] == 0:
                    player.armour -= wizard_spells[k]['a']
        return player, boss

    
    def player_turn(self, player, boss, spell):
        player, boss = self.apply_effects(player, boss)

        player.mana -= wizard_spells[spell]['c']
        player.armour += wizard_spells[spell]['a']
        player.hp += wizard_spells[spell]['h']
        
        if spell in ('magic_missile', 'drain'):
            boss.hp -= wizard_spells[spell]['d']   
        elif spell in ('poison', 'shield', 'recharge'):
            player.effects[spell] = wizard_spells[spell]['t']
        return player, boss
    
    def boss_turn(self, player, boss):
        player, boss = self.apply_effects(player, boss)
        player.hp -= max(boss.damage - player.armour, 1)
        return player, boss


    def turn(self, spell):
        new_player = copy.deepcopy(self.player)
        new_boss = copy.deepcopy(self.boss)
        
        # Part 2 - Hard mode (player loses hp at start of each turn)
        new_player.hp -= 1
        if new_player.hp <= 0:
            game_state = GameState.loss
            new_mana = self.mana_spent
        else:
            new_mana = self.mana_spent + wizard_spells[spell]['c']
            new_player, new_boss = self.player_turn(new_player, new_boss, spell)
            new_player, new_boss = self.boss_turn(new_player, new_boss)

            game_state = GameState.ongoing
            if new_boss.hp <= 0:
                game_state = GameState.win
                global min_mana_spent
                if new_mana < min_mana_spent:
                    min_mana_spent = new_mana
            elif new_player.hp <= 0:
                game_state = GameState.loss
        
        child = Node(
            mana_spent=new_mana,
            player=new_player,
            boss=new_boss,
            state=game_state,
        )
        return child



    def make_children(self):
        if self.state != GameState.ongoing:
            return

        for k, v in wizard_spells.items():
            # Check which spells we can cast based on mana and current effects
            if self.player.mana < v['c']:
                continue
            if self.mana_spent + v['c'] > min_mana_spent:
                continue
            if k in self.player.effects and self.player.effects[k] > 1:
                continue

            self.children.append(
                self.turn(k)
            )

def part1(data):

  pl = Player(50, 0, 500)
  b = Boss(55, 8)

  tree = Node(0, pl, b, GameState.ongoing)
  print(min_mana_spent)
  return min_mana_spent






    




