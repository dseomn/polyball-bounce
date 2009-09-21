# margin of error for various floating point comparisons
margin = 0.01
pixel_margin = 1.5

size = (400, 400)
font_size = 16
border_size = 3

speed = 3

sleep = 25 # in milliseconds

num_balls = 2

ball = {
  'start': (200, 200),
  'speed': 1.0, # ratio relative to config.speed above
}

hazard = {
  'size': (75, 75),
  'width': 4,
}

paddle = {
  'speed': 1, # ratio relative to config.speed above
  'size_horizontal': (60, 4),
  'size_vertical': (4, 60),
}
from player import Player
paddle['center']= {
  Player.TOP: (200, 6),
  Player.LEFT: (6, 200),
  Player.RIGHT: (394, 200),
  Player.BOTTOM: (200, 394),
}

score_zone = {
  Player.TOP: {'center': (200, 2), 'size': (250, 4)},
  Player.LEFT: {'center': (2, 200), 'size': (4, 250)},
  Player.RIGHT: {'center': (398, 200), 'size': (4, 250)},
  Player.BOTTOM: {'center': (200, 398), 'size': (250, 4)},
}

colors = {
  'bg':     (255, 255, 255),
  'fg':     (  0,   0,   0),
  'border': (127, 127, 127),
}
