import sys, time, random, string, os
import pygame
import config, levels

levels.ALL['Simple'].init(config)

def run_game():
  pygame.init()
  
  pygame.display.set_caption(config.name)
  pygame.display.set_icon(config.icon)
  
  # set up screen and layout
  game_area_rect = pygame.Rect(config.border_size, config.border_size, config.size[0], config.size[1])
  border_rect = game_area_rect.inflate(2*config.border_size, 2*config.border_size)
  font = pygame.font.Font(None, config.font_size)
  status_rect = pygame.Rect(config.border_size, border_rect.bottom+config.margin_size, config.size[0], config.font_size)
  help_rect = pygame.Rect(border_rect.right+config.margin_size, config.margin_size, config.help_width, status_rect.bottom - 2*config.margin_size)
  screen = pygame.display.set_mode((help_rect.right, status_rect.bottom))
  
  
  import ball, hazard, player
  
  
  def play():
    "returns true if the game should quit, false if another game should be played"
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
    for i in hazard.Hazard.ALL:
      hazards.add(hazard.Hazard(i))
    for i in config.hazard['custom']:
      hazards.add(hazard.Hazard(**i))
    for i in config.PLAYER_ALL:
      players.append(player.Player(i, paddles, score_zones, hazards, balls, paddle_type=config.paddle['paddle_type'][i]))
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
      balls.add(ball.Ball(collideables, score_zones))
    for i in collideables:
      i.balls = balls
      
    
    # run the game
    while True:
      ticks = pygame.time.get_ticks()
  
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return True
        elif event.type == pygame.KEYDOWN:
          try:
            keys_down[event.key]()
          except KeyError:
            pass
          if event.key == pygame.K_PAUSE or (event.key == pygame.K_p and event.mod & pygame.KMOD_CTRL):
            paused = not paused
          elif event.key == pygame.K_n and event.mod & pygame.KMOD_CTRL:
            return False
          elif event.key == pygame.K_q and event.mod & pygame.KMOD_CTRL:
            return True
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
          balls.add(ball.Ball(collideables, score_zones))
    
      # draw everything
      screen.fill(config.colors['bg'])
      screen.fill(config.colors['border'], border_rect)
      game_area.fill(config.colors['bg'])
      balls.draw(game_area)
      paddles.draw(game_area)
      hazards.draw(game_area)
      screen.blit(game_area, game_area_rect)
      screen.blit(font.render(get_status_string(players), True, config.colors['fg']), status_rect)
      line_num = 0
      for line in string.split(config.help_string, '\n'):
        screen.blit(font.render(line, True, config.colors['fg']), \
          (help_rect.left, help_rect.top + line_num*font.get_linesize(), help_rect.width, help_rect.height))
        line_num += 1
      pygame.display.flip()
  
      pygame.time.wait(max(0, config.sleep - (pygame.time.get_ticks() - ticks)))
  
  
  while not play():
    pass

  pygame.quit()
