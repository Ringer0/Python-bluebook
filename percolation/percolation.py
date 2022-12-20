import stdarray
import stdio
import stddraw

def _flow(isOpen, isFull, i, j):
    n = len(isFull)
    if (i < 0) or (i >= n): return
    if (j < 0) or (j >= n): return
    if not isOpen[i][j]: return
    if isFull[i][j]: return

    isFull[i][j] = True
    stddraw.setXscale(-0.5, n-0.5)
    stddraw.setYscale(-0.5, n-0.5)
    if isFull[i][j] == True:
        stddraw.filledSquare(j, n-i-1, 0.5)
        stddraw.show(100)
    _flow(isOpen, isFull, i+1, j)
    _flow(isOpen, isFull, i, j+1)
    _flow(isOpen, isFull, i, j-1)
    _flow(isOpen, isFull, i-1, j)

def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n, n, False)
    for j in range(n):
        _flow(isOpen, isFull, 0, j)
    return isFull

def percolates(isOpen):
    isFull = flow(isOpen)
    n = len(isFull)
    for j in range(n):
        if isFull[n-1][j]: return True
    return False

def main():
    isOpen = stdarray.readBool2D()
    stdarray.write2D(flow(isOpen))
    stdio.writeln(percolates(isOpen))

if __name__ == '__main__' : main()
