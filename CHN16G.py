t=int(input())
while t>0:
    t-=1
    n=int(input())
    s=input()
    s_list=s.split()
    myset=set(s_list)
    print(n-len(myset))
