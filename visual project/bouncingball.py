import stddraw
import sys
import stdrandom
import stdarray

class Ball:
    def __init__(self):
        self._a = stdrandom.uniformFloat(-0.98,0.98)
        self._b = stdrandom.uniformFloat(-0.98,0.98)
        self._c = stdrandom.uniformFloat(-0.5e-5, 0.5e-5)
        self._d = stdrandom.uniformFloat(-0.5e-5, 0.5e-5)
    def move(self, dt):
        self._a = self._a + self._c * dt
        self._b = self._b + self._d * dt
        if abs(self._a + self._c) + 0.02 > 1.0:
            self._c *= -1
        if abs(self._b + self._d) + 0.02 > 1.0:
            self._d *= -1
    def draw(self):
        stddraw.setPenRadius(0.02)
        stddraw.point(self._a, self._b)
        
def main():
    n = int(sys.argv[1])
    stddraw.setXscale(-1.0, 1.0)
    stddraw.setYscale(-1.0, 1.0)
    stddraw.setCanvasSize(800,800)
    BallBax = stdarray.create1D(n)
    for i in range(n):
        BallBax[i] = Ball()
    while True:
        for i in range(n):
            BallBax[i].move(5000)
        for i in range(n):
            BallBax[i].draw()
        stddraw.show(12)
        stddraw.clear()

if __name__ == '__main__' : main()
