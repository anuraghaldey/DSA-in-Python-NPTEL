#Insertion sort:-O(n^2)
def InsertionSort(l):
    
    for i in range(len(l)):
        
        pos=i
        while(pos>0 and l[pos]<l[pos-1]):
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos=pos-1
            
l=[12,34,573,2,1,56,45]
InsertionSort(l)
print(l)