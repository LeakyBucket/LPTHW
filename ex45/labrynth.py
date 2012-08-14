from room import Room

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