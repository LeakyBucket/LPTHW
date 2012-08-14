from inventory import Inventory

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