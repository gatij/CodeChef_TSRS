
a=[]
i=0

while i<1299827:
    a.append(1)
    i+=1
p=2
while p<1299827:
    if a[p]==1:
        j=2
        while j*p<1299827:
            a[j*p]=0
            j+=1
    p+=1
c=0
k=2
n=int(input())
while c<n:
    if a[k]==1:
        print(k)
        c+=1
    k+=1    
        
        
    
        
    
    

    
    

        
        
    
