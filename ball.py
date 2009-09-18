from pygame.sprite import DirtySprite

class Ball(DirtySprite):
  vel = [1,1]

  def update():
    dirty = 1
    source_rect.move(vel)
