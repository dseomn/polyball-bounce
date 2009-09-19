import math
import pygame
import config, velocity

class Player:
  ALL = TOP, LEFT, RIGHT, BOTTOM = range(4)
  type_name = {
    TOP: 'Top',
    LEFT: 'Left',
    RIGHT: 'Right',
    BOTTOM: 'Bottom',
  }

  def __init__(self, type, paddles, score_zones):
    self.score = 0
    self.type = type
    self.name = Player.type_name[self.type]
    paddles.add(Paddle(self))
    score_zones.add(ScoreZone(self))


class Paddle(pygame.sprite.DirtySprite):
  def __init__(self, owner, speed=config.paddle['speed']):
    pygame.sprite.DirtySprite.__init__(self)
    self.owner = owner

    if self.owner.type in (Player.TOP, Player.BOTTOM):
      self.pos_angle = 0
      self.image = pygame.Surface(config.paddle['size_horizontal'])
    elif self.owner.type in (Player.LEFT, Player.RIGHT):
      self.pos_angle = math.pi/2
      self.image = pygame.Surface(config.paddle['size_vertical'])

    if self.owner.type == Player.TOP:
      self.normal = 3*math.pi/2
    elif self.owner.type == Player.LEFT:
      self.normal = 0
    elif self.owner.type == Player.RIGHT:
      self.normal = math.pi
    elif self.owner.type == Player.BOTTOM:
      self.normal = math.pi/2

    self.vel = velocity.Velocity(0, 0)
    self.image.fill(config.colors['fg'])
    self.image.set_colorkey(config.colors['bg'])
    self.rect = self.image.get_rect()
    self.rect.center = config.paddle['center'][owner.type]
    self.dirty = 1

  def bounce_angle(self, angle):
    "compute the angle something should bounce off of this hazard"
    return 2*self.normal - angle + math.pi

  def move_pos(self):
    self.vel.speed = self.speed
    self.vel.angle = self.pos_angle

  def move_neg(self):
    self.vel.speed = self.speed
    self.vel.angle = self.pos_angle + math.pi

  def move_stop(self):
    self.vel.speed = 0


class HumanPaddle(Paddle):
  def update(self):
    pass


class ComputerPaddle(Paddle):
  def update(self):
    pass

  def find_closest(self):
    "returns the Ball  heading towards this Player's score zone that's closest to this Paddle"
    for ball in balls:


class ScoreZone(pygame.sprite.Sprite):
  def __init__(self, owner):
    pygame.sprite.Sprite.__init__(self)
    self.owner = owner
    self.image = pygame.Surface(config.score_zone[self.owner.type]['size'])
    self.rect = self.image.get_rect()
    self.rect.center = config.score_zone[self.owner.type]['center']

