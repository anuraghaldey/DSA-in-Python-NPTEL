def quicksort(a,l,r):
    if(r-l<=1):
        return a
    
    y=l+1
    for g in range(l+1,r):
        if(a[g]<=a[l]):
            (a[g],a[y])=(a[y],a[g])
            y+=1
    a[l],a[y-1]=a[y-1],a[l]
    quicksort(a,l,y-1)
    quicksort(a,y,r)
    
f=[23,3,4,6,12,2,1]
quicksort(f,0,len(f))
print(f)