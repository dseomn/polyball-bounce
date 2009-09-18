import os, pygame
import config, velocity

import math

class Ball(pygame.sprite.DirtySprite):
  def __init__(self, collidables, start=config.ball['start'], speed=config.ball['speed'], angle=7*math.pi/4):
    pygame.sprite.DirtySprite.__init__(self)
    self.vel = velocity.Velocity(speed, angle)
    self.image = pygame.image.load(os.path.join('data', 'ball.png')).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = config.ball['start']
    self.collidables = collidables

  def update(self):
    self.dirty = 1
    collided = pygame.sprite.spritecollide(self, self.collidables, False, pygame.sprite.collide_mask)
    for i in collided:
      self.vel.angle += math.pi
    self.rect = self.rect.move(self.vel.delta(config.speed))
