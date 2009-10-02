import math
import pygame
import velocity, util


class Paddle(pygame.sprite.DirtySprite):
  def __init__(self, config, owner, hazards, balls, speed=None):
    pygame.sprite.DirtySprite.__init__(self)
    self.config = config
    if speed is None:
      speed = self.config.paddle['speed']

    self.owner = owner
    self.hazards = hazards
    self.balls = balls

    if self.owner.type in (self.config.PLAYER_TOP, self.config.PLAYER_BOTTOM):
      self.pos_angle = 0
      self.image = pygame.Surface(self.config.paddle['size_horizontal'])
      self.image.fill(self.config.colors['bg'])
      pygame.draw.ellipse(self.image, self.config.colors['fg'], (0, -self.config.paddle['size_horizontal'][1], self.config.paddle['size_horizontal'][0], 2*self.config.paddle['size_horizontal'][1]))
    elif self.owner.type in (self.config.PLAYER_LEFT, self.config.PLAYER_RIGHT):
      self.pos_angle = 3*math.pi/2
      self.image = pygame.Surface(self.config.paddle['size_vertical'])
      self.image.fill(self.config.colors['bg'])
      pygame.draw.ellipse(self.image, self.config.colors['fg'], (-self.config.paddle['size_vertical'][0], 0, 2*self.config.paddle['size_vertical'][0], self.config.paddle['size_vertical'][1]))
    self.image = pygame.transform.flip(self.image, self.owner.type == self.config.PLAYER_RIGHT, self.owner.type == self.config.PLAYER_BOTTOM)
    self.image.set_colorkey(self.config.colors['bg'])

    self.vel = velocity.Velocity(0, 0)
    self.speed = speed
    self.rect = self.image.get_rect()
    self.rect.center = self.config.paddle['center'][owner.type]
    self.x = self.rect.centerx
    self.y = self.rect.centery
    self.dirty = 1

  bounce_angle = util.bounce_angle

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
    deltax, deltay = self.vel.delta(self.config.speed)
    self.x += deltax
    self.y += deltay
    self.rect.center = (self.x, self.y)
    if pygame.sprite.spritecollide(self, self.hazards, False, pygame.sprite.collide_mask):
      self.rect.center = self.x, self.y = old_x, old_y
    else:
      dirty = 1


class HumanPaddle(Paddle):
  def __init__(self, config, owner, hazards, balls, speed=None):
    Paddle.__init__(self, config, owner, hazards, balls, speed=speed)
    self.key_pos = self.config.paddle['key_pos'][self.owner.type]
    self.key_neg = self.config.paddle['key_neg'][self.owner.type]


class ComputerPaddle(Paddle):
  def update(self):
    ball = self.find_closest()
    if ball is None:
      to_x = self.config.size[0]/2
      to_y = self.config.size[1]/2
    else:
      to_x = ball.edge_destination.x
      to_y = ball.edge_destination.y
    if self.owner.type in (self.config.PLAYER_TOP, self.config.PLAYER_BOTTOM):
      if -self.config.pixel_margin < self.x - to_x < self.config.pixel_margin:
        self.move_stop()
      elif self.x > to_x:
        self.move_neg()
      else:
        self.move_pos()
    elif self.owner.type in (self.config.PLAYER_LEFT, self.config.PLAYER_RIGHT):
      if -self.config.pixel_margin < self.y - to_y < self.config.pixel_margin:
        self.move_stop()
      elif self.y > to_y:
        self.move_neg()
      else:
        self.move_pos()
    Paddle.update(self)

  def find_closest(self):
    "returns the Ball heading towards this Player's score zone that's closest to this Paddle"
    min_dist = math.sqrt(self.config.size[0]**2 + self.config.size[1]**2)
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
  def __init__(self, config, owner):
    pygame.sprite.Sprite.__init__(self)
    self.config = config
    self.owner = owner
    self.image = pygame.Surface(self.config.score_zone[self.owner.type]['size'])
    self.rect = self.image.get_rect()
    self.rect.center = self.config.score_zone[self.owner.type]['center']





class Player:
  def __init__(self, config, type, paddles, score_zones, hazards, balls, paddle_type=Paddle):
    self.config = config
    _paddle_class = {
      self.config.PLAYER_COMPUTER: ComputerPaddle,
      self.config.PLAYER_HUMAN: HumanPaddle,
    }
    self.score = 0
    self.type = type
    self.name = self.config.player['name'][self.type]
    self.score_zone = ScoreZone(config, self)
    self.paddle = _paddle_class[paddle_type](config, self, hazards, balls)
    paddles.add(self.paddle)
    score_zones.add(self.score_zone)
