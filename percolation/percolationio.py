import sys
import stddraw
import stdio
import stdrandom
import stdarray

def random(n, p):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    return a

def draw(a, which):
    n = len(a)
    stddraw.setXscale(-0.5, n-0.5)
    stddraw.setYscale(-0.5, n-0.5)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, n-i-1, 0.5)

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    test = random(n, p)
    draw(test, False)
    stddraw.show()

if __name__ == '__main__' : main()
