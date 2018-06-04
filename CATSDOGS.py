t=int(input())
while t>0:
    t-=1
    s=input()
    s_list=s.split()
    c=int(s_list[0])
    d=int(s_list[1])
    l=int(s_list[2])
    if l%4!=0 or l>4*(c+d) or l<4*d:
        print("no")
    else:
        if c>=2*d and l>=(c-d)*4 and l<=(c+d)*4:
            print("yes")
        elif c<2*d and l>=4*d and l<=(c+d)*4:
            print("yes")
        else:
            print("no")
            
    
