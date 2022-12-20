import stddraw
import sys
import stdarray
from instream import InStream
from vector import Vector
from body import Body

class Universe:
    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.readInt()
        radius = instream.readFloat()

        stddraw.setXscale(-radius, radius)
        stddraw.setYscale(-radius, radius)
        self._bodies = stdarray.create1D(n)
        for i in range(n):
            rx = instream.readFloat()
            ry = instream.readFloat()
            vx = instream.readFloat()
            vy = instream.readFloat()
            mass = instream.readFloat()
            r = Vector([rx,ry])
            v = Vector([vx,vy])
            self._bodies[i] = Body(r, v, mass)
    def increaseTime(self, dt):
        n = len(self._bodies)
        f = stdarray.create1D(n, Vector([0, 0]))
        for i in range(n):
            for j in range(n):
                if i != j:
                    bodyi = self._bodies[i]
                    bodyj = self._bodies[j]
                    f[i] = f[i] + bodyi.forceFrom(bodyj)
        for i in range(n):
            self._bodies[i].move(f[i], dt)
    def draw(self):
        for body in self._bodies:
            body.draw()

def main():
    universe = Universe(sys.argv[1])
    dt = float(sys.argv[2])
    while True:
        universe.increaseTime(dt)
        universe.draw()
        stddraw.show(10)
        stddraw.clear()

if __name__ == '__main__' : main()
    
