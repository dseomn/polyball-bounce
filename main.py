import sys, time, random, string
import pygame
import config

pygame.init()

screen = pygame.display.set_mode((config.size[0], config.size[1]+config.border_size+config.font_size))


from ball import Ball
from hazard import Hazard
from player import Player


def get_score_string(players):
  return string.join([str.format('{0.name: >8}: {0.score: <4}', i) for i in players], '  ')


# set up objects on the game board
players = []
keys_up = {}
keys_down = {}
hazards = pygame.sprite.Group()
paddles = pygame.sprite.Group()
collideables = pygame.sprite.Group()
score_zones = pygame.sprite.Group()
balls = pygame.sprite.Group()
for i in Hazard.ALL:
  hazards.add(Hazard(i))
for i in Player.ALL:
  players.append(Player(i, paddles, score_zones, hazards, balls, paddle_type=config.paddle['paddle_type'][i]))
for i in players:
  try:
    keys_down[i.paddle.key_pos] = i.paddle.move_pos
    keys_down[i.paddle.key_neg] = i.paddle.move_neg
    keys_up[i.paddle.key_pos] = i.paddle.move_stop
    keys_up[i.paddle.key_neg] = i.paddle.move_stop
  except AttributeError:
    pass
collideables.add(hazards)
collideables.add(paddles)
for i in xrange(config.num_balls):
  balls.add(Ball(collideables, score_zones))
for i in collideables:
  i.balls = balls


# set up score reporting and border(s)
borders = [pygame.Rect(0, config.size[1], config.size[0], config.border_size)]
font = pygame.font.Font(None, config.font_size)
score_report = pygame.Rect(0, config.size[1]+config.border_size, config.size[0], config.font_size)

while True:
  ticks = pygame.time.get_ticks()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      try:
        keys_down[event.key]()
      except KeyError:
        pass
    elif event.type == pygame.KEYUP:
      try:
        keys_up[event.key]()
      except KeyError:
        pass

  balls.update()
  paddles.update()
  while len(balls) < config.num_balls:
    balls.add(Ball(collideables, score_zones))
  screen.fill(config.colors['bg'])
  for i in borders:
    screen.fill(config.colors['border'], i)
  balls.draw(screen)
  paddles.draw(screen)
  hazards.draw(screen)
  screen.blit(font.render(get_score_string(players), True, config.colors['fg']), score_report)
  pygame.display.flip()
  pygame.time.wait(max(0, config.sleep - (pygame.time.get_ticks() - ticks)))
