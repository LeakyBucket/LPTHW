from sys import exit
from random import randint   

monsters = ['Troll', 'Goblin', 'Ogre', 'Hobgoblin', 'Politician', 'Grue']
enemy_levels = [['Tough', 200, 20], ['Average', 100, 10], ['Wimpy', 50, 5]]
treasure = ['Garbage', 'Penny', 'Cash Money', 'Car']
weapons = ['Rock', 'Stick', 'Sharp Whit', 'Sword', 'Foul Odor']


class Labrynth:
  """This is the place where the things happen"""
  def __init__(self, rooms):
    self.the_map = []

    for x in range(0, rooms - 1):
      if x % 2 > 0:
        self.the_map.append(Room('horizontal'))
      else:
        self.the_map.append(Room('vertical'))

  def first_room(self):
    return(self.the_map[0])

  def next_room(self, room):
    return(self.the_map[self.the_map.index(room) + 1])

  def previous_room(self, room):
    return(self.the_map[self.the_map.index(room) - 1])



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
      self.description = 'Amazingly empty here, there is a door ' + self.exit + ' and another one ' + self.enter
    elif number == 1:
      self.generate_monster()
      self.treasure = False
      self.weapon = False
      self.description = 'Some rubble here, also a %s %s %s.' % (self.monster.state, self.monster.title, self.monster.type)
      self.description += '  You see a door %s and another one %s.' % (self.exit, self.enter)
    elif number == 2:
      self.generate_monster()
      self.generate_treasure()
      self.weapon = False
      self.description = 'Pillars, Piles of junk, and a %s %s %s.  Oh look! %s.' % (self.monster.state, self.monster.title, self.monster.type, self.treasure.name)
      self.description += '  You see a door %s and another one %s.' % (self.exit, self.enter)
    elif number == 3:
      self.generate_monster()
      self.generate_treasure()
      self.generate_weapon()
      self.description = 'Fancy schmancy!  All kinds of wonderful things here.  A %s %s %s.  In the corner we have %s. There is also a %s in the middle of the room.' % (self.monster.state, self.monster.title, self.monster.type, self.treasure.name, self.weapon.name)
      self.description += '  You see a door %s and another one %s.' % (self.exit, self.enter)

  def monster(self):
    self.monster

  def treasure(self):
    self.treasure

  def weapon(self):
    self.weapon

  def describe(self):
    return(self.description)


class Monster:
  """Monster represents a monster"""
  def __init__(self, name, args):
    self.type = name
    self.alive = True
    self.state = 'Healthy'
    self.title = args[0]
    self.life = args[1]
    self.damage = args[2]

  def state(self):
    self.state

  def title():
    return(self.title + ' ' + self.name)




class Treasure:
  """Treasure represents a collectible Item in the Game"""
  def __init__(self, arg):
    self.name = arg




class Weapon:
  """Weapon represents a weapon in the Game"""
  def __init__(self, arg):
    self.name = arg




class Inventory:
  """The players Inventory"""
  def __init__(self):
    self.items = []

  def add(self, item):
    self.items << item




class Player:
  """The Player"""
  def __init__(self, name):
    self.name = name
    self.inventory = Inventory()
    self.life = 100
    self.alive = True

  def take_damage(self, amount):
    self.life -= amount
    if self.life <= 0:
      die()

  def die(self):
    print "You died!"
    exit(0)

  def add_item(self, item):
    self.inventory.add(item)

  def check_inventory(self):
    return(self.inventory)

  def equip_weapon(self, weapon):
    for item in inventory:
      if item.name == weapon:
        self.weapon = item
      else:
        return(False)



class State():
  """Game State"""
  def __init__(self, labrynth):
    self.room = labrynth.first_room()

  def next_room(self, labrynth):
    self.room = labrynth.next_room(self.room)

  def previous_room(self, labrynth):
    self.room = labrynth.previous_room(self.room)

  def current_room(self):
    return(self.room)



labrynth = Labrynth(randint(1, 10))
state = State(labrynth)

print "You enter the Labrynth..."
print "You find yourself in a room.  %s" % state.current_room().describe()