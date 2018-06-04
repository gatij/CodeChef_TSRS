t=int(input())
while t>0:
    s=input()
    s_list=s.split()
    a=int(s_list[0])
    b=int(s_list[1])
    print(a%b)
    t=t-1
