import random
import sys
import stdarray
import stdio
import stddraw

moves = int(sys.argv[1])
stddraw.setXscale(-1, 5)
stddraw.setYscale(0, 50000)

n = stdio.readInt()
stdio.readInt()
p = stdarray.create2D(n, n, 0)
for i in range(n):
    for j in range(n):
        p[i][j] = stdio.readFloat()

hits = stdarray.create1D(n, 0)
page = 0
for i in range(moves):
    r = random.random()
    total = 0.0
    for j in range(0, n):
        total += p[page][j]
        if r < total:
            page =  j
            break
    hits[page] += 1
    if i % 1000 == 0:
        stddraw.clear()
        for k in range(n):
            stddraw.filledRectangle(k-0.25, 0.0, 0.5, hits[k])
stddraw.show()
for v in hits:
    stdio.writef('%8.5f' , 1.0 * v / moves)
stdio.writeln()
