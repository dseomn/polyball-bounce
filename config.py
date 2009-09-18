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

score_zone = {
  Player.TOP: (100, 0, 200, 10),
  Player.LEFT: (0, 100, 10, 200),
  Player.RIGHT: (390, 100, 10, 200),
  Player.BOTTOM: (100, 390, 200, 10),
}

colors = {
  'bg': (255, 255, 255),
  'fg': (  0,   0,   0),
}
