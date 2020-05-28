import sys

N = int(sys.argv[1])

BT = [1,1]

while len(BT) < N+1:
    n = len(BT)
    count = 0
    for i in range(n//2):
        count += 2*BT[i]*BT[n-1-i]
    if n % 2 == 1:
        count += BT[n//2]**2
#    for i in range(n):
#        count += BT[i]*BT[n-1-i]
    BT.append(count)

for i,n in enumerate(BT):
    print('%02i %d'%(i,n))

