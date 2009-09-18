import os, pygame

class Ball(pygame.sprite.DirtySprite):
  vel = [1,1]
  image = pygame.image.load(os.path.join('data', 'ball.png')).convert_alpha()
  rect = image.get_rect() 

  def update(self):
    self.dirty = 1
    self.rect = self.rect.move(self.vel)
