class Weapon:
  """Weapon represents a weapon in the Game"""
  def __init__(self, args):
    self.name = args[0]
    self.damage = args[1]