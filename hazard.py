import os, pygame
import config

class Hazard(pygame.sprite.Sprite):
  TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT = range(4)
  
  def __init__(self, type):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface(config.hazard['size'])
    self.image.fill(config.colors['bg'])
    self.image.set_colorkey(config.colors['bg'])
    self.rect = self.image.get_rect()
    if type == Hazard.BOTTOM_RIGHT:
      self.rect = pygame.draw.line(self.image, config.colors['fg'], (0,config.hazard['size'][1]), (config.hazard['size'][0],0), config.hazard['width'])
      self.rect = self.rect.move((config.size[0] - config.hazard['size'][0], config.size[1] - config.hazard['size'][1]))
