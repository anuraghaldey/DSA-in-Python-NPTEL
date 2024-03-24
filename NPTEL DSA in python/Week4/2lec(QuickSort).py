#QuickSort -Overcomes problems in merge sort of extra space-O(logn)without extra space.
#Built in sort function uses quicksort.
def QuickSort(a,l,r):
    if(l>=r):
        return ()
    
    yellow=l+1
    
    for green in range(l+1,r):
        if(a[green]<=a[l]):
            (a[yellow],a[green])=(a[green],a[yellow])
            yellow+=1
    
    (a[l],a[yellow-1])=(a[yellow-1],a[l])
    
    QuickSort(a,l,yellow-1)
    QuickSort(a,yellow,r)
    
l=[35,45,2,1,23,4,57,89]

QuickSort(l,0,8)
for i in l:
    print(i)