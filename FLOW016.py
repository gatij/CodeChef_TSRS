t=int(input())
while t>0:
    t=t-1
    s=input()
    s_list=s.split()
    a=int(s_list[0])
    b=int(s_list[1])
    lcm=a*b
    while b>0:
        a,b=b,a%b
    gcd=a
    lcm//=gcd
    print(gcd,lcm)
