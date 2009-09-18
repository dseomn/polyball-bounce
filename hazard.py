import os, pygame
import config

class Hazard(pygame.sprite.Sprite):
  BOTTOM_RIGHT = 1
  
  def __init__(self, type):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((100,100))
    self.image.fill(config.colors['bg'])
    self.image.set_colorkey(config.colors['bg'])
    self.rect = self.image.get_rect()
    if type == Hazard.BOTTOM_RIGHT:
      self.rect = pygame.draw.line(self.image, config.colors['fg'], (0,100), (100,0), 5)
      self.rect = self.rect.move((300,300))
