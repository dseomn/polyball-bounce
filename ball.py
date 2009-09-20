import os, random, math, copy
import pygame
import config, velocity

class Ball(pygame.sprite.DirtySprite):
  def get_edge_destination(self):
    ret = Ball(None, None, start=self.rect.center, angle=self.vel.angle)

    # move the ret to one edge
    if math.pi/4 <= ret.vel.angle < 3*math.pi/4: # up
      dx, dy = ret.vel.delta(ret.y/math.sin(ret.vel.angle), speed=1)
      ret.x += dx
      ret.y += dy
      assert ret.y == 0
    elif 3*math.pi/4 <= ret.vel.angle < 5*math.pi/4: # left
      dx, dy = ret.vel.delta(-ret.x/math.cos(ret.vel.angle), speed=1)
      ret.x += dx
      ret.y += dy
      assert ret.x == 0
    elif 5*math.pi/4 <= ret.vel.angle < 7*math.pi/4: # down
      dx, dy = ret.vel.delta((ret.y - config.size[1])/math.sin(ret.vel.angle), speed=1)
      ret.x += dx
      ret.y += dy
      assert ret.y == config.size[1]
    else: # right
      dx, dy = ret.vel.delta((config.size[0] - ret.x)/math.cos(ret.vel.angle), speed=1)
      ret.x += dx
      ret.y += dy
      assert ret.x == config.size[0]

    # if ret is out of bounds, move it back in
    if ret.x < 0:
      dx, dy = ret.vel.delta(ret.x/math.cos(ret.vel.angle), speed=-1)
      ret.x += dx
      ret.y += dy
    elif ret.x > config.size[0]:
      dx, dy = ret.vel.delta((ret.x - config.size[0])/math.cos(ret.vel.angle), speed=-1)
      ret.x += dx
      ret.y += dy
    if ret.y < 0:
      dx, dy = ret.vel.delta(-ret.y/math.sin(ret.vel.angle), speed=-1)
      ret.x += dx
      ret.y += dy
    elif ret.y > config.size[1]:
      dx, dy = ret.vel.delta((config.size[1] - ret.y)/math.sin(ret.vel.angle), speed=-1)
      ret.x += dx
      ret.y += dy

    ret.rect.center = (ret.x, ret.y)
    return ret
  def get_edge_destination_cache(self):
    def cmp_state(state1, state2):
      if state1 == state2:
        return True
      if state1[0] == state2[0]:
        dx = state2[1] - state1[1]
        dy = state1[2] - state2[2]
        dist = math.sqrt(dx*dx + dy*dy)
        return (dx, dy) == (dist*math.cos(state1[0]), dist*math.sin(state1[0]))
      return False
    cur_state = (self.vel.angle, self.rect.centerx, self.rect.centery)
    try:
      if cmp_state(self._edge_destination_state, cur_state):
        return self._edge_destination
    except AttributeError:
      pass
    self._edge_destination = self.get_edge_destination()
    self._edge_destination_state = cur_state
    return self._edge_destination
  edge_destination = property(get_edge_destination_cache)

  def __init__(self, collideables, scoreables, start=config.ball['start'], speed=config.ball['speed'], angle=None):
    pygame.sprite.DirtySprite.__init__(self)
    if angle is None:
      angle = random.uniform(0, 2*math.pi)
    self.vel = velocity.Velocity(speed, angle)
    self.image = pygame.image.load(os.path.join('data', 'ball.png')).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.center = start
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
