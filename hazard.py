import os, math
import pygame
import config

class Hazard(pygame.sprite.Sprite):
  ALL = TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT = range(4)
  
  def __init__(self, type):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface(config.hazard['size'])
    self.image.fill(config.colors['bg'])
    self.image.set_colorkey(config.colors['bg'])
    self.rect = self.image.get_rect()

    if type in (Hazard.TOP_LEFT, Hazard.BOTTOM_RIGHT):
      self.rect = pygame.draw.line(self.image, config.colors['fg'], (0,config.hazard['size'][1]), (config.hazard['size'][0],0), config.hazard['width'])
    elif type in (Hazard.TOP_RIGHT, Hazard.BOTTOM_LEFT):
      self.rect = pygame.draw.line(self.image, config.colors['fg'], (0,0), config.hazard['size'], config.hazard['width'])

    if type == Hazard.TOP_LEFT:
      self.normal = 7*math.pi/4
    elif type == Hazard.TOP_RIGHT:
      self.normal = 5*math.pi/4
      self.rect = self.rect.move((0, config.size[1] - config.hazard['size'][1]))
    elif type == Hazard.BOTTOM_LEFT:
      self.normal = math.pi/4
      self.rect = self.rect.move((config.size[0] - config.hazard['size'][0], 0))
    elif type == Hazard.BOTTOM_RIGHT:
      self.normal = 3*math.pi/4
      self.rect = self.rect.move((config.size[0] - config.hazard['size'][0], config.size[1] - config.hazard['size'][1]))
  
  def bounceAngle(self, angle):
    "compute the angle something should bounce off of this hazard"
    return 2*self.normal - angle + math.pi
