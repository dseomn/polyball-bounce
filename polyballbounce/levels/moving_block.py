import pygame

name = 'Moving Block'

def init(config):
  config.level_name = name
  square = pygame.Surface((30,30))
  square.fill(config.colors['fg'])
  square.set_colorkey(config.colors['bg'])
  def update(self):
    if not hasattr(self, 'dir'):
      self.dir = (1,0)
    if self.rect.centery < 120:
      self.rect.centery = 120
      self.dir = (1,0)
    elif self.rect.centerx > 280:
      self.rect.centerx = 280
      self.dir = (0,1)
    elif self.rect.centery > 280:
      self.rect.centery = 280
      self.dir = (-1,0)
    elif self.rect.centerx < 120:
      self.rect.centerx = 120
      self.dir = (0,-1)
    self.rect.centerx += self.dir[0]
    self.rect.centery += self.dir[1]
  

  config.hazard['custom'] = [{'rect': (110, 110, 30, 30), 'image': square, 'update': update}]
