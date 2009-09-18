import pygame

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

class HumanPaddle(Paddle):

class AIPaddle(Paddle):

class ScoreZone(pygame.sprite.Sprite):
  def __init__(self, owner):
    pygame.sprite.Sprite.__init__(self)
    self.owner = owner
    self.rect = pygame.rect(config.score_zone[self.owner.type])

