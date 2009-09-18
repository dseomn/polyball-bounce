import math

class Velocity:
  _angle = None

  def get_angle(self):
    return self._angle
  def set_angle(self, value):
    self._angle = value
    self.normalize()
  def del_angle(self):
    del self._angle
  angle = property(get_angle, set_angle, del_angle)

  def __init__(self, speed, angle):
    "angle = angle CCW of the x+ axis in radians, 0 < angle < 2*pi"
    self.speed = speed
    self.angle = angle
    self.normalize()

  def normalize(self):
    "make sure speed and angle are within parameters"
    while self.angle < 0:
      self.angle += 2 * math.pi
    self.angle %= 2 * math.pi
    if self.speed < 0:
      self.speed = abs(self.speed)
      self.angle += self.math.pi
      self.normalize()

  def delta(self, time):
    "return (change from top, change from left) for given time"
    return (-1*time*self.speed*math.sin(self.angle), time*self.speed*math.cos(self.angle))
