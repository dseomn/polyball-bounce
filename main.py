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
hazards = pygame.sprite.Group()
paddles = pygame.sprite.Group()
collideables = pygame.sprite.Group()
score_zones = pygame.sprite.Group()
balls = pygame.sprite.Group()
for i in Hazard.ALL:
  hazards.add(Hazard(i))
for i in Player.ALL:
  players.append(Player(i, paddles, score_zones, hazards, paddle_type=ComputerPaddle))
collideables.add(hazards)
collideables.add(paddles)
for i in xrange(config.num_balls):
  balls.add(Ball(collideables, score_zones))
for i in collideables:
  i.balls = balls

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  balls.update()
  while len(balls) < config.num_balls:
    balls.add(Ball(collideables, score_zones))
  screen.fill(config.colors['bg'])
  balls.draw(screen)
  paddles.draw(screen)
  hazards.draw(screen)
  pygame.display.flip()
  time.sleep(config.sleep)
