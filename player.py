import math
import pygame
import config, velocity


class Paddle(pygame.sprite.DirtySprite):
  def __init__(self, owner, hazards, balls, speed=config.paddle['speed']):
    pygame.sprite.DirtySprite.__init__(self)
    self.owner = owner
    self.hazards = hazards
    self.balls = balls

    if self.owner.type in (Player.TOP, Player.BOTTOM):
      self.pos_angle = 0
      self.image = pygame.Surface(config.paddle['size_horizontal'])
    elif self.owner.type in (Player.LEFT, Player.RIGHT):
      self.pos_angle = 3*math.pi/2
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
    self.speed = speed
    self.image.fill(config.colors['fg'])
    self.image.set_colorkey(config.colors['bg'])
    self.rect = self.image.get_rect()
    self.rect.center = config.paddle['center'][owner.type]
    self.x = self.rect.centerx
    self.y = self.rect.centery
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

  def update(self):
    """Move the paddle based on self.vel, but don't actually compute self.vel.
    This should be called by all sub-classes."""
    old_x, old_y = self.x, self.y
    deltax, deltay = self.vel.delta(config.speed)
    self.x += deltax
    self.y += deltay
    self.rect.center = (self.x, self.y)
    if pygame.sprite.spritecollide(self, self.hazards, False, pygame.sprite.collide_mask):
      self.rect.center = self.x, self.y = old_x, old_y
    else:
      dirty = 1


class HumanPaddle(Paddle):
  def update(self):
    pass


class ComputerPaddle(Paddle):
  def update(self):
    ball = self.find_closest()
    if ball is None:
      to_x = config.size[0]/2
      to_y = config.size[1]/2
    else:
      to_x = ball.edge_destination.x
      to_y = ball.edge_destination.y
    if self.owner.type in (Player.TOP, Player.BOTTOM):
      if self.x > to_x:
        self.move_neg()
      else:
        self.move_pos()
    elif self.owner.type in (Player.LEFT, Player.RIGHT):
      if self.y > to_y:
        self.move_neg()
      else:
        self.move_pos()
    Paddle.update(self)

  def find_closest(self):
    "returns the Ball heading towards this Player's score zone that's closest to this Paddle"
    min_dist = math.sqrt(config.size[0]**2 + config.size[1]**2)
    min_ball = None
    for ball in self.balls:
      if not pygame.sprite.collide_mask(ball.edge_destination, self.owner.score_zone):
        continue
      dist = math.sqrt( (self.x - ball.x)**2 + (self.y - ball.y)**2 )
      if dist < min_dist:
        min_dist = dist
        min_ball = ball
    return min_ball


class ScoreZone(pygame.sprite.Sprite):
  def __init__(self, owner):
    pygame.sprite.Sprite.__init__(self)
    self.owner = owner
    self.image = pygame.Surface(config.score_zone[self.owner.type]['size'])
    self.rect = self.image.get_rect()
    self.rect.center = config.score_zone[self.owner.type]['center']


class Player:
  ALL = TOP, LEFT, RIGHT, BOTTOM = range(4)
  type_name = {
    TOP: 'Top',
    LEFT: 'Left',
    RIGHT: 'Right',
    BOTTOM: 'Bottom',
  }

  def __init__(self, type, paddles, score_zones, hazards, balls, paddle_type=Paddle):
    self.score = 0
    self.type = type
    self.name = Player.type_name[self.type]
    self.score_zone = ScoreZone(self)
    paddles.add(paddle_type(self, hazards, balls))
    score_zones.add(self.score_zone)
