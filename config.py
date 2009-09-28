import pygame

name = 'Polyball Bounce'

# margin of error for various floating point comparisons
margin = 0.01
pixel_margin = 1.5

size = (400, 400)
font_size = 16
border_size = 2
margin_size = 2

speed = 3

sleep = 25 # in milliseconds

num_balls = 2

ball = {
  'start': (200, 200),
  'speed': 1.5, # ratio relative to config.speed above
}

hazard = {
  'size': (75, 75),
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

colors = {
  'bg':     (255, 255, 255),
  'fg':     (  0,   0,   0),
  'border': (127, 127, 127),
}
