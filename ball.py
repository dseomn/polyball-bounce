import os, random, math
import pygame
import config, velocity

class Ball(pygame.sprite.DirtySprite):
  def __init__(self, collideables, scoreables, start=config.ball['start'], speed=config.ball['speed'], angle=None):
    pygame.sprite.DirtySprite.__init__(self)
    if angle is None:
      angle = random.uniform(0, 2*math.pi)
    self.vel = velocity.Velocity(speed, angle)
    self.image = pygame.image.load(os.path.join('data', 'ball.png')).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = config.ball['start']
    self.x = self.rect.centerx
    self.y = self.rect.centery
    self.collideables = collideables
    self.scoreables = scoreables
    self.prev_collided = []
    self.owner = None

  def update(self):
    self.dirty = 1
    cur_collided = pygame.sprite.spritecollide(self, self.collideables, False, pygame.sprite.collide_mask)
    for collided in cur_collided:
      if collided in self.prev_collided:
        continue
      self.vel.angle = collided.bounce_angle(self.vel.angle)
      try:
        self.owner = collided.owner
      except AttributeError:
        pass
    self.prev_collided = cur_collided
    for scored in pygame.sprite.spritecollide(self, self.scoreables, False, pygame.sprite.collide_mask):
      scored.owner.score -= 1
      self.kill()
      return
    deltax, deltay = self.vel.delta(config.speed)
    self.x += deltax
    self.y += deltay
    self.rect.center = (self.x, self.y)
