import math
import pygame

def bounce_angle(self, other):
  "compute the angle other should bounce off self"

  if hasattr(self, 'normal'):
    # really simple approximation
    normal = self.normal
  else:
    # more complex approximation
    for o in (self, other):
      if not hasattr(o, 'mask'):
        o.mask = pygame.mask.from_surface(o.image)
    x = other.rect.left - self.rect.left
    y = other.rect.top - self.rect.top
    dx = self.mask.overlap_area(other.mask,(x-1,y)) - self.mask.overlap_area(other.mask,(x+1,y))
    dy = self.mask.overlap_area(other.mask,(x,y+1)) - self.mask.overlap_area(other.mask,(x,y-1))
    if dx == 0:
      if dy > 0:
        normal = math.pi/2
      else:
        normal = 3*math.pi/2
    else:
      normal = math.atan(float(dy)/dx)
      if dx < 0:
        normal += math.pi
      if normal < 0:
        normal += 2*math.pi

  return 2*normal - other.vel.angle + math.pi
