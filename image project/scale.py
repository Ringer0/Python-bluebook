import sys
import stddraw
from picture import Picture

file = sys.argv[1]
wT = int(sys.argv[2])
hT = int(sys.argv[3])

source = Picture(file)
target = Picture(wT, hT)

for colT in range(wT):
    for rowT in range(hT):
        colS = colT * source.width()  //wT
        rowS = rowT * source.height() //hT
        target.set(colT, rowT, source.get(colS,rowS))

stddraw.setCanvasSize(wT, hT)
stddraw.picture(target)
stddraw.show()
