t=int(input())
s=[]
while t>0:
    t=t-1
    n=int(input())
    s.append(n)

s.sort()
l=len(s)
i=0
while i<l:
    print(s[i])
    i=i+1
    
