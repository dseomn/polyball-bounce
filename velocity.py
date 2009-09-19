import math

class Velocity:
  _angle = None
  _speed = None

  def get_angle(self):
    if self._angle > 2*math.pi or self._angle < 0:
    return self._angle
  def set_angle(self, value):
    self._angle = value % (2*math.pi)
  def del_angle(self):
    del self._angle
  angle = property(get_angle, set_angle, del_angle)

  def get_speed(self):
    return self._speed
  def set_speed(self, value):
    self._speed = abs(value)
    if value < 0:
      self.angle += math.pi
  def del_speed(self):
    del self._speed
  speed = property(get_speed, set_speed, del_speed)

  def __init__(self, speed, angle):
    "angle = angle CCW of the x+ axis in radians, 0 < angle < 2*pi"
    self.speed = speed
    self.angle = angle

  def delta(self, time):
    "return (change from top, change from left) for given time"
    return (-1*time*self.speed*math.sin(self.angle), time*self.speed*math.cos(self.angle))
