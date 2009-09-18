import sys, time, random, pygame
import config

pygame.init()
random.seed()

screen = pygame.display.set_mode(config.size)

from ball import Ball
from hazard import Hazard

hazards = pygame.sprite.Group(Hazard(Hazard.BOTTOM_RIGHT))

balls = pygame.sprite.Group(Ball(hazards))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  balls.update()
  screen.fill(config.colors['bg'])
  balls.draw(screen)
  hazards.draw(screen)
  pygame.display.flip()
  time.sleep(config.sleep)
