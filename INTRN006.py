t=int(input())
while t>0:
    n=int(input())
    i=2
    sum1=0
    while i*i<=n:
        if n%i==0:
            if i*i!=n:
                sum1+=i
                sum1+=(n//i)
            else:
                sum1+=i
        i+=1
    sum1+=1
    if sum1==n:
        print("YES")
    else:
        print("NO")
    t=t-1    
        
        
