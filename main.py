import sys, time, random, string, os
import pygame
import config

pygame.init()

pygame.display.set_caption(config.name)
pygame.display.set_icon(pygame.image.load(os.path.join('data', 'icon.png')))

# set up screen and layout
game_area_rect = pygame.Rect(config.border_size, config.border_size, config.size[0], config.size[1])
border_rect = game_area_rect.inflate(2*config.border_size, 2*config.border_size)
font = pygame.font.Font(None, config.font_size)
status_rect = pygame.Rect(config.border_size, border_rect.bottom+config.margin_size, config.size[0], config.font_size)
help_rect = pygame.Rect(border_rect.right+config.margin_size, config.margin_size, config.help_width, status_rect.bottom - 2*config.margin_size)
screen = pygame.display.set_mode((help_rect.right, status_rect.bottom))


from ball import Ball
from hazard import Hazard
from player import Player


def play():
  def get_status_string(players):
    parts = [str.format('{0.name: >8}: {0.score: <4}', i) for i in players]
    if winner is not None: parts += ['Winner: ' + winner.name]
    elif paused: parts += ['***PAUSED***']
    return string.join(parts, '  ')

  # set up objects on the game board
  game_area = pygame.Surface(config.size)
  paused = False
  winner = None
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
  for i in config.hazard['custom']:
    hazards.add(Hazard(**i))
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
  for i in xrange(config.ball['num']):
    balls.add(Ball(collideables, score_zones))
  for i in collideables:
    i.balls = balls
    
  
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
        if event.key == pygame.K_PAUSE or (event.key == pygame.K_p and event.mod & pygame.KMOD_CTRL):
          paused = not paused
        if event.key == pygame.K_n and event.mod & pygame.KMOD_CTRL:
          return
      elif event.type == pygame.KEYUP:
        try:
          keys_up[event.key]()
        except KeyError:
          pass
  
    winner = config.get_winner(players)
  
    if not paused and winner is None:
      hazards.update()
      paddles.update()
      balls.update()
      while len(balls) < config.ball['num']:
        balls.add(Ball(collideables, score_zones))
  
    screen.fill(config.colors['bg'])
    screen.fill(config.colors['border'], border_rect)
    game_area.fill(config.colors['bg'])
    balls.draw(game_area)
    paddles.draw(game_area)
    hazards.draw(game_area)
    screen.blit(game_area, game_area_rect)
    screen.blit(font.render(get_status_string(players), True, config.colors['fg']), status_rect)
    screen.blit(font.render(config.help_string, True, config.colors['fg']), help_rect)
    pygame.display.flip()
    pygame.time.wait(max(0, config.sleep - (pygame.time.get_ticks() - ticks)))


while True:
  play()
