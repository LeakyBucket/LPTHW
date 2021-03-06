from sys import exit
from random import randint
import re
from re import match
from re import split
from re import findall
from re import search

monsters = ['Troll', 'Goblin', 'Ogre', 'Hobgoblin', 'Politician', 'Grue']
enemy_levels = [['Tough', 200, 20], ['Average', 100, 10], ['Wimpy', 50, 5]]
treasure = [['Garbage', 0], ['Penny', 100], ['Cash Money', 500], ['Car', 10000]]
weapons = [['Rock', 10], ['Stick', 15], ['Sharp Wit', 5], ['Sword', 50], ['Foul Odor', 25]]

HELP = """
attack <monster>
get <item>
go <direction>
look
inventory
quit
"""

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

  def last_room(self):
    return(self.the_map[-1])



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


class Monster:
  """Monster represents a monster"""
  def __init__(self, name, args):
    self.type = name
    self.alive = True
    self.state = 'Healthy'
    self.title = args[0]
    self.life = args[1]
    self.damage = args[2]
    self.max_health = args[1]

  def state(self):
    self.state

  def take_damage(self, damage):
    self.life -= damage

    if self.life >= self.max_health/2:
      self.state = "Injured"
    elif self.life >= self.max_health/4:
      self.state = "Maimed"
    elif self.life <= 0:
        self.state = "Dead"
        self.alive = False

    return self.state




class Treasure:
  """Treasure represents a collectible Item in the Game"""
  def __init__(self, args):
    self.name = args[0]
    self.value = args[1]




class Weapon:
  """Weapon represents a weapon in the Game"""
  def __init__(self, args):
    self.name = args[0]
    self.damage = args[1]




class Inventory:
  """The players Inventory"""
  def __init__(self):
    self.items = []

  def add(self, item):
    self.items.append(item)




class Player:
  """The Player"""
  def __init__(self):
    self.inventory = Inventory()
    self.life = 100
    self.alive = True
    self.damage = 25

  def take_damage(self, amount):
    self.life -= amount
    if self.life <= 0:
      self.die()

  def die(self):
    print "You died!"
    exit(0)

  def add_item(self, item):
    self.inventory.add(item)

  def add_weapon(self, weapon):
    self.inventory.add(weapon)
    self.damage += weapon.damage

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
    self.labrynth = labrynth
    self.room = labrynth.first_room()

  def next_room(self):
    self.room = self.labrynth.next_room(self.room)

  def previous_room(self):
    self.room = self.labrynth.previous_room(self.room)

  def current_room(self):
    return(self.room)

  def last_room(self):
    return(self.room is self.labrynth.last_room())

  def first_room(self):
    return(self.room is self.labrynth.first_room())



class Action():
  """Process Player Action"""
  def __init__(self, player, state):
    self.player = player
    self.state = state

  def move(self, state, command):
    exit_direction = state.current_room().exit
    enter_direction = state.current_room().enter

    direction = ' '.join(split(' ', command)[1::])

    if search(direction, exit_direction, re.I):
      if state.last_room():
        print "Hooray, freedom!"
        exit(0)
      else:
        state.next_room()
        return True
    elif search(direction, enter_direction, re.I):
      if state.first_room():
        print "Sorry, you can't actually go that way."
        return True
      else:
        state.previous_room()
        return True
    else:
      return(False)


  def check_clear(self, state, command):
    if state.current_room().monster and state.current_room().monster.alive:
      print "The %s won't let you!" % state.current_room().monster.type
      return(False)
    else:
      return self.move(state, command)


  def pick_up(self, command):
    room = self.state.current_room()
    target = ' '.join(split(' ', command)[1::])

    if room.treasure and match(room.treasure.name, target, re.I):
      self.player.add_item(room.treasure)
      print "You shove the %s into your pocket." % room.treasure.name
      room.treasure = False
    elif room.weapon and match(room.weapon.name, target, re.I):
      self.player.add_weapon(room.weapon)
      print "You now have a wonderful %s to hurt things with." % room.weapon.name
      room.weapon = False


  def show_inventory(self):
    if len(player.inventory.items) > 0:
      print "You rummage around in your pockets and find:"
      for item in player.inventory.items:
        print item.name
    else:
      print "Your pockets are empty."


  def check_enemy(self, command):
    return match(split(' ', command)[-1], self.state.current_room().monster.type, re.I) and self.state.current_room().monster.alive

  def attack(self, command):
    monster = self.state.current_room().monster

    if self.check_enemy(command):
      if randint(1, 20) > 8:
        print 'A hit!'
        print 'The %s appears to be %s.' % (monster.type, monster.take_damage(self.player.damage))
      else:
        print 'You missed.'
        if randint(1, 20) > 12:
          self.player.take_damage(monster.damage)
          print 'And it hurt!'
    else:
      if self.state.current_room().monster.alive:
        print "I don't see one of those here?"
      else:
        print "It looks to be dead already."



labrynth = Labrynth(randint(1, 10))
state = State(labrynth)
player = Player()
action = Action(player, state)

print "You enter the Labrynth..."
print "You find yourself in a room.  %s" % state.current_room().describe()

while True:
  command = raw_input('What do you do?> ')

  if match('go', command):
    if action.check_clear(state, command):
      print "Another room.  %s" % state.current_room().describe()
      command = ''
  elif match('attack', command):
    action.attack(command)
  elif match('look', command):
    print state.current_room().describe()
  elif match('inventory', command):
    action.show_inventory()
  elif match('get', command):
    action.pick_up(command)
  elif match('help', command):
    print HELP
  elif match('quit', command):
    exit(0)
  else:
    print 'What?'
