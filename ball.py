import os, pygame

class Ball(pygame.sprite.DirtySprite):
  def __init__(self, start, collidables):
    pygame.sprite.DirtySprite.__init__(self)
    self.vel = [1,1]
    self.image = pygame.image.load(os.path.join('data', 'ball.png')).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = start
    self.collidables = collidables

  def update(self):
    self.dirty = 1
    collided = pygame.sprite.spritecollide(self, self.collidables, False, pygame.sprite.collide_mask)
    for i in collided:
      self.vel = -self.vel
    self.rect = self.rect.move(self.vel)
