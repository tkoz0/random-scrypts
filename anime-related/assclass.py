from math import sqrt
from random import random

SQP = [(1,1),(1,-1),(-1,1),(-1,-1)]
CBP = [(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)]

def dist(a,b):
  assert len(a) == len(b)
  return sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))

total = 1000000
count = 0

for _ in range(total):
  x,y,z = random(),random(),random()
  P = (x,y,z)
  if dist((0,0,0),P) < min(dist(P,p) for p in CBP): count += 1
print(count/total)



