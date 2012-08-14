import re
from re import match
from re import split
from re import findall
from re import search
from random import randint

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