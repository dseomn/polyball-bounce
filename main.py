import sys, pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

from ball import Ball


ball = Ball()
sprites = pygame.sprite.Group(ball)

background = (255, 255, 255)

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  sprites.update()
  screen.fill(background)
  sprites.draw(screen)
  pygame.display.flip()
