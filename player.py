import pygame
import velocity

class Player:
  ALL = TOP, LEFT, RIGHT, BOTTOM = range(4)

  def __init__(self, type, paddles, score_zones):
    self.score = 0
    self.type = type
    paddles.add(Paddle(self))
    score_zones.add(ScoreZone(self))


class Paddle(pygame.sprite.DirtySprite):
  def __init__(self, owner):
    pygame.sprite.DirtySprite.__init__(self)
    self.owner = owner
    if self.owner.type in (Player.TOP, Player.BOTTOM):
      self.vel = velocity.Velocity(0, 0)
      self.image = pygame.Surface(config.paddle['size_horizontal'])
    elif self.owner.type in (Player.LEFT, Player.RIGHT):
      self.vel = velocity.Velocity(0, math.pi/2)
      self.image = pygame.Surface(config.paddle['size_vertical'])
    self.image.fill(config.colors['fg'])
    self.rect = self.image.get_rect()
    self.rect.center = config.paddle['center'][owner.type]
    self.dirty = 1

class HumanPaddle(Paddle):
  def update(self):
    pass

class AIPaddle(Paddle):
  def update(self):
    pass

class ScoreZone(pygame.sprite.Sprite):
  def __init__(self, owner):
    pygame.sprite.Sprite.__init__(self)
    self.owner = owner
    self.rect = pygame.rect(config.score_zone[self.owner.type])

