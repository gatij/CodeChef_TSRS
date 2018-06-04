t=int(input())
while t>0:
    s1=input()
    s1_list=s1.split()
    n=int(s1_list[0])
    k=int(s1_list[1])
    s2=input()
    s2_list=s2.split()
    i=0
    num_list=[]
    sumn=0
    while i<n:
        sumn+=(int(s2_list[i]))
        num_list.append(int(s2_list[i]))
        i+=1
    num_list.sort()
    j=0
    p=n-1
    while j<k:
        v1=num_list[j]
        v2=num_list[p]
        sumn-=int(v1)
        sumn-=int(v2)
        j+=1
        p-=1    
    t-=1
    ans=float(float(sumn)/float(n-2*k))+0.000000001
    print(ans)
    
