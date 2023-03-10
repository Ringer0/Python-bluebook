import stddraw
from vector import Vector
import sys

class Body:
    def __init__(self, r, v, mass):
        self._r = r
        self._v = v
        self._mass = mass
    def move(self, f, dt):
        a = f.scale(1.0 / self._mass)
        self._v = self._v + a.scale(dt)
        self._r = self._r + self._v.scale(dt)
    def forceFrom(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        m1 = self._mass
        m2 = other._mass
        magnitude = G * m1 * m2 / (dist *dist)
        return delta.direction().scale(magnitude)
    def draw(self):
        stddraw.setPenRadius(0.0125)
        stddraw.point(self._r[0], self._r[1])
        
def main():
    r = Vector([.1, .15])
    v = Vector([.15, .1])
    m = .5
    stddraw.setXscale(-1000, 1000)
    stddraw.setYscale(-1000, 1000)
    body = Body(r,v,m)
    body1 = Body(v,r,m)
    f = body.forceFrom(body1)
    for i in range(1000000):
        body.move(f, 10)
        body.draw()
        body1.move(f,10)
        body1.draw()
        stddraw.show(10)
    stddraw.show()
if __name__ == '__main__' : main()
