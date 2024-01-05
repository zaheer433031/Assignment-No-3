from itertools import groupby
for a, b in groupby(input()):
    print("(%d, %d)" % (len(list(b)), int(a)), end=' ')