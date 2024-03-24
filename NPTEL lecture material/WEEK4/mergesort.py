def merge(l,r):
    (C,m,n)=([],len(l),len(r))
    (i,j)=(0,0)
    
    while(i<m and j<n):
        if(l[i]<=r[j]):
            C.append(l[i])
            i+=1
        else:
            C.append(r[j])
            j+=1
    
    while(i<m):
        C.append(l[i])
        i+=1
    while(j<n):
        C.append(r[j])
        j+=1
        
    return C
    

def mergesort(a):
    if(len(a)==1):
        return a 
    mid=len(a)//2
    l=mergesort(a[0:mid])
    r=mergesort(a[mid:len(a)])
    
    return merge(l,r)
    

a=[24,3,76,2,1,67,12,0]
b=mergesort(a)
print(b)