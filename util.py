import math

def bounce_angle(self, other):
  "compute the angle other should bounce off self"
  return 2*self.normal - other.vel.angle + math.pi
