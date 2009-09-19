import sys, time, random
import pygame
import config

pygame.init()
random.seed()

screen = pygame.display.set_mode(config.size)

from ball import Ball
from hazard import Hazard
from player import Player

collideables = pygame.sprite.Group()
scoreables = pygame.sprite.Group()
for i in Hazard.ALL:
  collideables.add(Hazard(i))

players = []
for i in Player.ALL:
  players.append(Player(i, collideables, scoreables))

balls = pygame.sprite.Group(Ball(collideables, scoreables))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  balls.update()
  screen.fill(config.colors['bg'])
  balls.draw(screen)
  collideables.draw(screen)
  pygame.display.flip()
  time.sleep(config.sleep)
