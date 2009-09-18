import os, random, math
import pygame
import config, velocity

class Ball(pygame.sprite.DirtySprite):
  def __init__(self, collidables, scoreables, start=config.ball['start'], speed=config.ball['speed'], angle=random.uniform(0, 2*math.pi)):
    pygame.sprite.DirtySprite.__init__(self)
    self.vel = velocity.Velocity(speed, angle)
    self.image = pygame.image.load(os.path.join('data', 'ball.png')).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = config.ball['start']
    self.collidables = collidables
    self.scoreables = scoreables
    self.owner = None

  def update(self):
    self.dirty = 1
    for collided in pygame.sprite.spritecollide(self, self.collidables, False, pygame.sprite.collide_mask):
      self.vel.angle = collided.bounceAngle(self.vel.angle)
      try:
        self.owner = collided.owner
      except AttributeError:
        pass
    for scored in pygame.sprite.spritecollide(self, self.scoreables, True, pygame.sprite.collide_mask):
      scored.owner.score--
    self.rect = self.rect.move(self.vel.delta(config.speed))
