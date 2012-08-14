from random import randint
from monster import Monster
from treasure import Treasure
from weapon import Weapon

monsters = ['Troll', 'Goblin', 'Ogre', 'Hobgoblin', 'Politician', 'Grue']
enemy_levels = [['Tough', 200, 20], ['Average', 100, 10], ['Wimpy', 50, 5]]
treasure = [['Garbage', 0], ['Penny', 100], ['Cash Money', 500], ['Car', 10000]]
weapons = [['Rock', 10], ['Stick', 15], ['Sharp Wit', 5], ['Sword', 50], ['Foul Odor', 25], ['Bazooka', 125]]

class Room:
  """Room represents a room in the game"""
  def __init__(self, type):
    if type == 'horizontal':
      self.exit = 'to the left'
      self.enter = 'to the right'
    else:
      self.exit = 'straight ahead'
      self.enter = 'back behind you'

    self.generate_content(randint(0, 3))

  def __eq__(self, other):
    return self.__dict__ == other.__dict__


  def generate_monster(self):
    self.monster = Monster(monsters[randint(0, len(monsters) - 1)], enemy_levels[randint(0, len(enemy_levels) - 1)])


  def generate_treasure(self):
    self.treasure = Treasure(treasure[randint(0, len(treasure) - 1)])


  def generate_weapon(self):
    self.weapon = Weapon(weapons[randint(0, len(weapons) - 1)])


  def generate_content(self, number):
    if number == 0:
      self.monster = False
      self.treasure = False
      self.weapon = False
      self.description = 'Amazingly empty here.'
    elif number == 1:
      self.generate_monster()
      self.treasure = False
      self.weapon = False
      self.description = 'Some rubble here.'
    elif number == 2:
      self.generate_monster()
      self.generate_treasure()
      self.weapon = False
      self.description = 'Pillars and Piles of junk.'
    elif number == 3:
      self.generate_monster()
      self.generate_treasure()
      self.generate_weapon()
      self.description = 'Fancy schmancy!  All kinds of wonderful things here.'

  def monster(self):
    self.monster

  def treasure(self):
    self.treasure

  def weapon(self):
    self.weapon

  def describe(self):
    current_state = self.description

    if self.monster:
      current_state += '  You see a %s %s %s.' % (self.monster.state, self.monster.title, self.monster.type)
    if self.treasure:
      current_state += '  Oh look!  %s.' % self.treasure.name
    if self.weapon:
      current_state += '  A %s sits in the middle of the room.' % self.weapon.name

    return(current_state + '  You see a door %s and another one %s.' % (self.exit, self.enter))
