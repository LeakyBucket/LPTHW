from sys import exit
from random import randrange   



class Labrynth:
  """This is the place where the things happen"""
  def __init__(rooms):
    self.the_map = []

    for x in range(1, rooms):
      if x%2 > 0:
        the_map << Room('horizontal')
      else:
        the_map << Room('vertical')



class Room:
  """Room represents a room in the game"""
  def __init__(type):
    if type == 'horizontal':
      self.exit = 'left'
      self.enter = 'right'
    else:
      self.exit = 'top'
      self.enter = 'bottom'

  def generate_monster():
  monsters[randrange(0, monsters.length, 1)]

  def generate_treasure():
  treasure[randrange(0, treasure.length, 1)]

  def generate_weapon():
  weapons[randrange(0, weapons.length, 1)]



class Monster:
  """Monster represents a monster"""
  def __init__(arg):
    self.type = arg
    self.alive = True




class Treasure:
  """Treasure represents a collectible Item in the Game"""
  def __init__(arg):
    self.name = arg




class Weapon:
  """Weapon represents a weapon in the Game"""
  def __init__(arg):
    self.name = arg




class Inventory:
  """The players Inventory"""
  def __init__():
    self.items = []

  def add(item):
    self.items << item




class Player:
  """The Player"""
  def __init__(name):
    self.name = name
    self.inventory = Inventory()
    self.life = 100
    self.alive = True

  def take_damage(amount):
    self.life -= amount
    if self.life <= 0:
      die()

  def die():
    print "You died!"
    exit(0)

  def add_item(item):
    self.inventory.add(item)

  def check_inventory():
    print "You have"

  def equip_weapon(weapon):
    for item in inventory:
      if item.name == weapon:
        self.weapon = item
      else:
        return(False)




monsters = ['Troll', 'Goblin', 'Ogre', 'Hobgoblin', 'Politician']
enemy_levels = [['Tough', 200, 20], ['Medium', 100, 10], ['Wimpy', 50, 5]]
treasure = ['Garbage', 'Penny', 'Cash Money', 'Car']
weapons = ['Rock', 'Stick', 'Sharp Whit', 'Sword', 'Foul Odor']
