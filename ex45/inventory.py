class Inventory:
  """The players Inventory"""
  def __init__(self):
    self.items = []

  def add(self, item):
    self.items.append(item)