#Recursion
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

def multiply(m,n):
    if(n==1):
        return(m)
    return (m+multiply(m,n-1))

def sum(l):
    if(l==[]):
        return 0
    return (l[0]+sum(l[1:]))

l=[23,34,21]
print(sum(l))
print(factorial(3 ))
print(multiply(9,34))


def recursiveInsertionSort(l):
    isort(l,len(l))

def isort(l,n):
    if(n>1):
        isort(l,n-1)
        insert(l,n-1)
        
def insert(l,k):
    pos=k
    while(pos>0 and l[pos]<l[pos-1]):
        (l[pos],l[pos-1])=(l[pos-1],l[pos])
        pos=pos-1
        
l3=[23,43,1,2,78,4,5]
recursiveInsertionSort(l3)
print(l3)
        
    