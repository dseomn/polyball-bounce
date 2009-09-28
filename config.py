import pygame

name = 'Polyball Bounce'

# margin of error for various floating point comparisons
margin = 0.01
pixel_margin = 1.5

size = (400, 400)
font_size = 20
border_size = 2
margin_size = 4

speed = 3

sleep = 25 # in milliseconds

colors = {
  'bg':     (255, 255, 255),
  'fg':     (  0,   0,   0),
  'border': (127, 127, 127),
}

ball = {
  'num': 2,
  'start': (200, 200),
  'speed': 1.5, # ratio relative to config.speed above
}

_hazard_square = pygame.Surface((30,30))
_hazard_square.fill(colors['fg'])
_hazard_square.set_colorkey(colors['bg'])
def _hazard_update(self):
  if not hasattr(self, 'dir'):
    self.dir = (1,0)
  if self.rect.centery < 120:
    self.rect.centery = 120
    self.dir = (1,0)
  elif self.rect.centerx > 280:
    self.rect.centerx = 280
    self.dir = (0,1)
  elif self.rect.centery > 280:
    self.rect.centery = 280
    self.dir = (-1,0)
  elif self.rect.centerx < 120:
    self.rect.centerx = 120
    self.dir = (0,-1)
  self.rect.centerx += self.dir[0]
  self.rect.centery += self.dir[1]
hazard = {
  'size': (75, 75),

  # additional hazards
  'custom': [
    {'rect': pygame.Rect(110, 110, 30, 30), 'image': _hazard_square, 'update': _hazard_update},
  ],
}

paddle = {
  'speed': 1, # ratio relative to config.speed above
  'size_horizontal': (60, 4),
  'size_vertical': (4, 60),
}
from player import Player, ComputerPaddle, HumanPaddle
paddle['center']= {
  Player.TOP: (200, 6),
  Player.LEFT: (6, 200),
  Player.RIGHT: (394, 200),
  Player.BOTTOM: (200, 394),
}
paddle['key_pos'] = {
  Player.TOP: pygame.K_6,
  Player.LEFT: pygame.K_z,
  Player.RIGHT: pygame.K_DOWN,
  Player.BOTTOM: pygame.K_SLASH,
}
paddle['key_neg'] = {
  Player.TOP: pygame.K_5,
  Player.LEFT: pygame.K_a,
  Player.RIGHT: pygame.K_UP,
  Player.BOTTOM: pygame.K_PERIOD,
}
paddle['paddle_type'] = {
  Player.TOP: ComputerPaddle,
  Player.LEFT: HumanPaddle,
  Player.RIGHT: ComputerPaddle,
  Player.BOTTOM: ComputerPaddle,
}

score_zone = {
  Player.TOP: {'center': (200, -7), 'size': (400, 10)},
  Player.LEFT: {'center': (-7, 200), 'size': (10, 400)},
  Player.RIGHT: {'center': (407, 200), 'size': (10, 400)},
  Player.BOTTOM: {'center': (200, 407), 'size': (400, 10)},
}

help_string = """\
Ctrl-N: new game
Ctrl-P: pause

Controls
  Top: 5 6
  Left: A Z
  Right: Up Down
  Bottom: . /"""
help_width = 120

# return the winner of the game, or None if there is no winner
def get_winner(players):
  second = None
  first = None
  for p in players:
    if first is None:
      first = p
    elif p.score > first.score:
      second = first
      first = p
    elif second is None or p.score > second.score:
      second = p
  if first.score < 5:
    return None
  if second is None:
    return first
  if first.score - second.score >= 2:
    return first
  return None
