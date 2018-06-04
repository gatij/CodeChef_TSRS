t=int(input())
while t>0:
    t-=1
    s=input()
    s_list=s.split()
    n=int(s_list[0])
    k=int(s_list[1])
    mx=-1
    while k>0:
        if mx<(n%k):
            mx=(n%k)
        k-=1
    print(mx)    
