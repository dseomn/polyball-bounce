import math

class Velocity:
  _angle = None
  _speed = None

  def get_angle(self):
    return self._angle
  def set_angle(self, value):
    self._angle = value
    self.normalize()
  def del_angle(self):
    del self._angle
  angle = property(get_angle, set_angle, del_angle)

  def get_speed(self):
    return self._speed
  def set_speed(self, value):
    self._speed = value
    self.normalize()
  def del_speed(self):
    del self._speed
  speed = property(get_speed, set_speed, del_speed)

  def __init__(self, speed, angle):
    "angle = angle CCW of the x+ axis in radians, 0 < angle < 2*pi"
    self._speed = speed
    self._angle = angle
    self.normalize()

  def normalize(self):
    "make sure speed and angle are within parameters"
    while self._angle < 0:
      self._angle += 2 * math.pi
    self._angle %= 2 * math.pi
    if self._speed < 0:
      self._speed = abs(self._speed)
      self._angle += self.math.pi
      self.normalize()

  def delta(self, time):
    "return (change from top, change from left) for given time"
    return (-1*time*self.speed*math.sin(self.angle), time*self.speed*math.cos(self.angle))
