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