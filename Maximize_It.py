import itertools
line = input()
K = int(line.split()[0])
M = int(line.split()[1])
N = []
for i in range(K):
  l = input().split()
  l = [ int(n) for n in l ]
  l = l[1:]
  N.append(l)
pro = list( itertools.product( *N ) )
maxi = 0
for item in pro:
  sum=0
  for num in item:
    sum += num**2
  modu = sum % M
  if (modu > maxi):
    maxi = modu
print (maxi)