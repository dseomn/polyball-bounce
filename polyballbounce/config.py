import os
import pygame

name = 'Polyball Bounce'

datadir = 'data'

# margin of error for various floating point comparisons
margin = 0.01
pixel_margin = 1.5

size = (400, 400)
font_size = 20
border_size = 2
margin_size = 4

speed = 3

sleep = 25 # in milliseconds

icon_file = os.path.join(datadir, 'icon.png')
icon = pygame.image.load(icon_file)

colors = {
  'bg':     (255, 255, 255),
  'fg':     (  0,   0,   0),
  'border': (127, 127, 127),
}

ball = {
  'start': (200, 200),
  'image': pygame.image.load(os.path.join(datadir, 'ball.png')),
  'num_max': 999,
}

hazard = {
  'size': (75, 75),
}

PLAYER_ALL = PLAYER_TOP, PLAYER_LEFT, PLAYER_RIGHT, PLAYER_BOTTOM = range(4)
PLAYER_COMPUTER, PLAYER_HUMAN = range(2)
player = {
  'name': {
    PLAYER_TOP: 'Top',
    PLAYER_LEFT: 'Left',
    PLAYER_RIGHT: 'Right',
    PLAYER_BOTTOM: 'Bottom',
  },
}
paddle = {
  'size_horizontal': (60, 4),
  'size_vertical': (4, 60),
  'center': {
    PLAYER_TOP: (200, 6),
    PLAYER_LEFT: (6, 200),
    PLAYER_RIGHT: (394, 200),
    PLAYER_BOTTOM: (200, 394),
  },
  'key_pos': {
    PLAYER_TOP: pygame.K_6,
    PLAYER_LEFT: pygame.K_z,
    PLAYER_RIGHT: pygame.K_DOWN,
    PLAYER_BOTTOM: pygame.K_SLASH,
  },

  'key_neg': {
    PLAYER_TOP: pygame.K_5,
    PLAYER_LEFT: pygame.K_a,
    PLAYER_RIGHT: pygame.K_UP,
    PLAYER_BOTTOM: pygame.K_PERIOD,
  },
  'paddle_type': {
    PLAYER_TOP: PLAYER_COMPUTER,
    PLAYER_LEFT: PLAYER_HUMAN,
    PLAYER_RIGHT: PLAYER_COMPUTER,
    PLAYER_BOTTOM: PLAYER_COMPUTER,
  },
}

score_zone = {
  PLAYER_TOP: {'center': (200, -7), 'size': (400, 10)},
  PLAYER_LEFT: {'center': (-7, 200), 'size': (10, 400)},
  PLAYER_RIGHT: {'center': (407, 200), 'size': (10, 400)},
  PLAYER_BOTTOM: {'center': (200, 407), 'size': (400, 10)},
}

help_string = """\
Ctrl-N: New game
Ctrl-P: Pause
Ctrl-Q: Quit

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
  if first.score - second.score >= 5:
    return first
  if first.score < 5:
    return None
  if second is None:
    return first
  if first.score - second.score >= 2:
    return first
  return None
