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