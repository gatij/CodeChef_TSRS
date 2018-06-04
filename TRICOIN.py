import math
t=int(input())
while t>0:
    t-=1
    n=int(input())
    h=(-1+math.sqrt((1+8*n)))/2
    print(int(h))
