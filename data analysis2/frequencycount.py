import sys
import stdio
from counter import Counter
from outstream import OutStream

words = stdio.readAllStrings()
words.sort()
zipf = []
for i in range(len(words)):
    if (i == 0) or (words[i] != words[i-1]):
        entry = Counter(words[i], len(words))
        zipf += [entry]
    zipf[len(zipf) -1].increment()
zipf.sort()
zipf.reverse()

outstream = OutStream('결과물.txt')
outstream.writeln(len(words))
for entry in zipf:
    outstream.writeln(entry)
