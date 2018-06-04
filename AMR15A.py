n=int(input())
s=input()
s_list=s.split()
lucky=0
unlucky=0
l=len(s_list)
while l>0:
    if int(s_list[l-1])%2==0:
        lucky+=1
    else:
        unlucky+=1
    l-=1
if lucky>unlucky:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
