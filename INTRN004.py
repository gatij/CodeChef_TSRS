t=int(input())
while t>0:
    n=int(input())
    s=''
    while (n//2)>0:
        s+=str(n%2)
        n=(n//2)
    s+='1'
    l=len(s)
    rs=''
    while l>0:
        rs+=s[l-1]
        l=l-1
    print(rs)
    t=t-1
        
        
