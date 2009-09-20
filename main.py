import sys, time, random
import pygame
import config

pygame.init()

screen = pygame.display.set_mode(config.size)

from ball import Ball
from hazard import Hazard
from player import Player, ComputerPaddle

# set up objects on the game board
players = []
collideables = pygame.sprite.Group()
scoreables = pygame.sprite.Group()
balls = pygame.sprite.Group()
for i in Hazard.ALL:
  collideables.add(Hazard(i))
for i in Player.ALL:
  players.append(Player(i, collideables, scoreables, paddle_type=ComputerPaddle))
for i in xrange(config.num_balls):
  balls.add(Ball(collideables, scoreables))
for i in collideables:
  i.balls = balls

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  balls.update()
  while len(balls) < config.num_balls:
    balls.add(Ball(collideables, scoreables))
  screen.fill(config.colors['bg'])
  balls.draw(screen)
  collideables.draw(screen)
  pygame.display.flip()
  time.sleep(config.sleep)
