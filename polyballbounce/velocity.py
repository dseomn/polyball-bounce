import math

class Velocity(object):
  def get_angle(self):
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
    self.angle = angle
    self.speed = speed

  def delta(self, time, speed=None):
    "return (change in left, change from top) for given time"
    if speed is None:
      speed = self.speed
    return (time*speed*math.cos(self.angle), -1*time*speed*math.sin(self.angle))
