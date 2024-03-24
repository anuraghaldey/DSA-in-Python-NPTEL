#Selection Sort:-O(n^2)
def SelectionSort(l):
    for start in range(len(l)):
        
        minpos=start
        for i in range(start,len(l)):
            if (l[i]<l[minpos]):
                minpos=i
                
        (l[start],l[minpos])=(l[minpos],l[start])
        
l=[23,12,8,45,3,466]
SelectionSort(l)
print(l)