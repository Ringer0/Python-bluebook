import stdio
import stddraw
import stdarray
import sys

def draw(pole):

    POLE_WIDTH = 0.01
    POLE_COLOR = stddraw.RED
    DISC_COLOR = stddraw.BLUE

    n = len(pole) - 1

    stddraw.clear()
    stddraw.setPenColor(POLE_COLOR)
    stddraw.setPenRadius(POLE_WIDTH)
    for i in range(3):
        stddraw.line(i, 0, i, n)

    discs = stdarray.create1D(3, 0)  
    for i in range(n, 0, -1):
        stddraw.setPenColor(DISC_COLOR)
        stddraw.setPenRadius(0.035)  
        size = 0.5 * i / n
        p = pole[i]
        stddraw.line(p-size/2, discs[p], p + size/2, discs[p])
        discs[p] += 1

    stddraw.show(500.0)

def hanoiHelp(n, fromDisc, tempDisc, toDisc, pole):
    if n == 0:
        return
    hanoiHelp(n-1, fromDisc, toDisc, tempDisc, pole)
    stdio.writeln("Move disc " + str(n) + " from pole " + \
        str(fromDisc) + " to pole " + str(toDisc))
    pole[n] = toDisc
    draw(pole)
    hanoiHelp(n-1, tempDisc, fromDisc, toDisc, pole)

def hanoi(n):
    pole = stdarray.create1D(n+1, 0)
    draw(pole)
    hanoiHelp(n, 0, 1, 2, pole)

def main():
    
    WIDTH  = 200       
    HEIGHT = 15     
    n = int(sys.argv[1]
    
    stddraw.setCanvasSize(4*WIDTH, (n+3)*HEIGHT)
    stddraw.setXscale(-1, 3)
    stddraw.setYscale(0, n+3)

    hanoi(n)

    stddraw.show()

if __name__ == '__main__':
    main()


