n=int(input())
while n>0:
    s=input()
    s_list=s.split()
    #print(s.split())
    #print(s_list[0],s_list[1],s_list[2])
    a=int(s_list[0])
    b=int(s_list[1])
    c=int(s_list[2])
    if a>=b>=c or a<=b<=c:
        print(b)
    elif b>=a>=c or b<=a<=c:
        print(a)
    else:
        print(c)
    n=n-1
    
