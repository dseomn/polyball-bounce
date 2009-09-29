import os, math
import pygame
import util

class Hazard(pygame.sprite.Sprite):
  TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT, OTHER = range(5)
  ALL = TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT
  
  def __init__(self, config, type=OTHER, rect=None, image=None, update=None):
    pygame.sprite.Sprite.__init__(self)
    self.config = config

    if image is None:
      self.image = pygame.Surface(self.config.hazard['size'])
      self.image.fill(self.config.colors['bg'])
      self.image.set_colorkey(self.config.colors['bg'])
    else:
      self.image = image

    if rect is None:
      self.rect = self.image.get_rect()
    else:
      self.rect = pygame.Rect(rect)

    if update is not None:
      self._update = update

    if type == Hazard.TOP_LEFT:
      self.normal = 7*math.pi/4
      self.rect = pygame.draw.polygon(self.image, self.config.colors['fg'], ((0,0), (self.config.hazard['size'][0],0), (0,self.config.hazard['size'][1])))
    elif type == Hazard.TOP_RIGHT:
      self.normal = 5*math.pi/4
      self.rect = pygame.draw.polygon(self.image, self.config.colors['fg'], ((0,0), (self.config.hazard['size'][0],0), self.config.hazard['size']))
      self.rect = self.rect.move((self.config.size[0] - self.config.hazard['size'][0], 0))
    elif type == Hazard.BOTTOM_LEFT:
      self.normal = math.pi/4
      self.rect = pygame.draw.polygon(self.image, self.config.colors['fg'], ((0,0), self.config.hazard['size'], (0,self.config.hazard['size'][1])))
      self.rect = self.rect.move((0, self.config.size[1] - self.config.hazard['size'][1]))
    elif type == Hazard.BOTTOM_RIGHT:
      self.normal = 3*math.pi/4
      self.rect = pygame.draw.polygon(self.image, self.config.colors['fg'], (self.config.hazard['size'], (self.config.hazard['size'][0],0), (0,self.config.hazard['size'][1])))
      self.rect = self.rect.move((self.config.size[0] - self.config.hazard['size'][0], self.config.size[1] - self.config.hazard['size'][1]))
  
  bounce_angle = util.bounce_angle

  def update(self):
    try:
      self._update(self)
    except AttributeError:
      pass
