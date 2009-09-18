import sys, pygame

pygame.init()

size = (400, 400)
center = (200, 200)

screen = pygame.display.set_mode(size)

from ball import Ball
from hazard import Hazard

hazards = pygame.sprite.Group(Hazard(Hazard.BOTTOM_RIGHT))

balls = pygame.sprite.Group(Ball(center, hazards))

background = (255, 255, 255)

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  balls.update()
  screen.fill(background)
  balls.draw(screen)
  hazards.draw(screen)
  pygame.display.flip()
