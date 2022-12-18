import stdio
import stddraw
import sys

n= int(sys.argv[1])

stddraw.setXscale(0 , 2*n)
stddraw.setYscale(0 , 2*n)
stddraw.setPenColor(stddraw.RED)
for i in range((n+1)//2):
    for j in range((n+1)//2):
        stddraw.filledSquare(4*j+1, 4*i+1, 1)
for k in range(n//2):
    for l in range(n//2):
        stddraw.filledSquare(4*l+3, 4*k+3, 1)

stddraw.setPenColor(stddraw.BLACK)
for i in range((n + 1)//2):
    for j in range(n//2):
        stddraw.filledSquare(4*j+3, 4*i+1, 1)
for k in range((n+1)//2):
    for l in range((n+1)//2):
        stddraw.filledSquare(4*l+1, 4*k+3, 1)

stddraw.show()
