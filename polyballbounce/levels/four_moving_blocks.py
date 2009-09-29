import pygame

name = 'Four Moving Blocks'

def init(config):
  config.level_name = name
  square = pygame.Surface((30,30))
  square.fill(config.colors['fg'])
  square.set_colorkey(config.colors['bg'])
  def update(self):
    if not hasattr(self, 'dir'):
      self.dir = (2,0)
    if self.rect.centery < 120:
      self.rect.centery = 120
      self.dir = (2,0)
    elif self.rect.centerx > 280:
      self.rect.centerx = 280
      self.dir = (0,2)
    elif self.rect.centery > 280:
      self.rect.centery = 280
      self.dir = (-2,0)
    elif self.rect.centerx < 120:
      self.rect.centerx = 120
      self.dir = (0,-2)
    self.rect.centerx += self.dir[0]
    self.rect.centery += self.dir[1]
  

  config.ball['num'] = 4
  config.ball['speed'] = 1.5
  config.hazard['custom'] = [
    {'rect': (110, 110, 30, 30), 'image': square, 'update': update},
    {'rect': (110, 390, 30, 30), 'image': square, 'update': update},
    {'rect': (390, 110, 30, 30), 'image': square, 'update': update},
    {'rect': (390, 390, 30, 30), 'image': square, 'update': update},
  ]
  config.paddle['speed'] = 1.25
