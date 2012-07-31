from sys import exit
from random import randint
from re import match
from re import split
from re import findall

monsters = ['Troll', 'Goblin', 'Ogre', 'Hobgoblin', 'Politician', 'Grue']
enemy_levels = [['Tough', 200, 20], ['Average', 100, 10], ['Wimpy', 50, 5]]
treasure = [['Garbage', 0], ['Penny', 100], ['Cash Money', 500], ['Car', 10000]]
weapons = [['Rock', 10], ['Stick', 15], ['Sharp Wit', 5], ['Sword', 50], ['Foul Odor', 25]]


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
      self.description = 'Some rubble here, also a %s %s %s.' % (self.monster.state, self.monster.title, self.monster.type)
    elif number == 2:
      self.generate_monster()
      self.generate_treasure()
      self.weapon = False
      self.description = 'Pillars, Piles of junk, and a %s %s %s.  Oh look! %s.' % (self.monster.state, self.monster.title, self.monster.type, self.treasure.name)
    elif number == 3:
      self.generate_monster()
      self.generate_treasure()
      self.generate_weapon()
      self.description = 'Fancy schmancy!  All kinds of wonderful things here.  A %s %s %s.  In the corner we have %s. There is also a %s in the middle of the room.' % (self.monster.state, self.monster.title, self.monster.type, self.treasure.name, self.weapon.name)

  def monster(self):
    self.monster

  def treasure(self):
    self.treasure

  def weapon(self):
    self.weapon

  def describe(self):
    return(self.description + '  You see a door %s and another one %s.' % (self.exit, self.enter))


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
      die()

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
    self.room is self.labrynth.last_room()

  def first_room(self):
    self.room is self.labrynth.first_room()



class Action():
  """Process Player Action"""
  def __init__(self, player, state):
    self.player = player
    self.state = state

  def move(self, state, direction):
    exit_direction = split(' ', state.current_room().exit)[-1]
    enter_direction = split(' ', state.current_room().enter)[-1]

    if findall(exit_direction, direction):
      if state.last_room():
        print "Hooray, freedom!"
        exit(0)
      else:
        state.next_room()
        return True
    elif findall(split(' ', state.current_room().enter)[-1], direction):
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
    if room.treasure and match(room.treasure.name, ' '.join(split(' ', command)[1::])):
      self.player.add_item(room.treasure)
      print "You shove the %s into your pocket." % room.treasure.name
    elif room.weapon and match(room.weapon.name, ' '.join(split(' ', command)[1::])):
      self.player.add_weapon(room.weapon)
      print "You now have a wonderful %s to hurt things with." % room.weapon.name

  def check_enemy(self, command):
    return match(split(' ', command)[-1], self.state.current_room().monster.type) and self.state.current_room().monster.alive

  def attack(self, command):
    if self.check_enemy(command):
      if randint(1, 20) > 8:
        print 'The %s looks %s.' % (self.state.current_room().monster.type, self.state.current_room().monster.take_damage(self.player.damage))
      else:
        print 'You missed.'
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
  command = raw_input('What do you do> ')

  if match('go', command):
    if action.check_clear(state, command):
      print "Another room.  %s" % state.current_room().describe()
      command = ''
  elif match('attack', command):
    action.attack(command)
  elif match('look', command):
    print state.current_room().describe()
  elif match('get', command):
    action.pick_up(command)
  elif match('quit', command):
    exit(0)
  else:
    print 'What?'
