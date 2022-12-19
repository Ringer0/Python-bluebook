import stdarray
import stdio

n = stdio.readInt()

linkCounts = stdarray.create2D(n, n, 0)
outDegrees = stdarray.create1D(n, 0)

while not stdio.isEmpty():
    i = stdio.readInt()
    j = stdio.readInt()
    outDegrees[i] += 1
    linkCounts[i][j] += 1

stdio.writeln(str(n) + ' '+ str(n))

for i in range(n):
    for j in range(n):
        p = (0.9 * linkCounts[i][j] / outDegrees[i]) + (0.10/n)
        stdio.writef('%8.5f', p)
    stdio.writeln()
