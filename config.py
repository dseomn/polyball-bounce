from player import Player

size = (400, 400)

speed = 3

sleep = 0.01

ball = {
  'start': (200, 200),
  'speed': 1.0, # ratio relative to config.speed above
}

hazard = {
  'size': (100, 100),
  'width': 5,
}

paddle = {
  'size_horizontal': (75, 10),
  'size_vertical': (10, 75),
  'center': {
    Player.TOP: (200, 15),
    Player.LEFT: (15, 200),
    Player.RIGHT: (385, 200),
    Player.BOTTOM: (200, 385),
  }
}

score_zone = {
  Player.TOP: {'center': (200, 5), 'size': (200, 10)},
  Player.LEFT: {'center': (5, 200), 'size': (10, 200)},
  Player.RIGHT: {'center': (395, 200), 'size': (10, 200)},
  Player.BOTTOM: {'center': (200, 395), 'size': (200, 10)},
}

colors = {
  'bg': (255, 255, 255),
  'fg': (  0,   0,   0),
}
