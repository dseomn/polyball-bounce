import os, pygame

class Hazard(pygame.sprite.Sprite):
  BOTTOM_RIGHT = 1
  
  def __init__(self, type):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((100,100))
    self.image.fill((0,0,0,255))
    self.rect = self.image.get_rect()
    if type == Hazard.BOTTOM_RIGHT:
      self.rect = pygame.draw.line(self.image, (0,0,0), (0,100), (100,0), 5)
    self.rect.move((300,300))
