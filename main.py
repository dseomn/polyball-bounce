import sys, pygame
pygame.init()

screen = pygame.display.set_mode(resolution=(400,400))

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
