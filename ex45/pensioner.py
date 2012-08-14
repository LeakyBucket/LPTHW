from sys import exit
from random import randint
from re import match
from room import Room
from state import State
from player import Player
from labrynth import Labrynth
from action import Action



HELP = """
attack <monster>
get <item>
go <direction>
look
inventory
quit
"""


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
