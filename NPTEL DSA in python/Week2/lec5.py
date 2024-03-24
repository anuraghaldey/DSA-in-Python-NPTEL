def power(x, n):
    ans = 1
    for i in range(0, n):
        ans = ans*x
    return ans

x=3
n=5
print(power(x,n))

#Side effect of function for a immutable and mutable value
def update(l,i,v):
    if (i>=0 and i<len(l)):
        l[i]=v
        return True
    else:
        v=v+1
        return False
    
l=[3,11,12]#mutable
i=4
v=8#immutable
update(l,i,v)
print(v)


#Recursion
def factorial(n):
    if(n<=0):
        return(1)
    else:
        val=n*factorial(n-1)
        return val
    
print (factorial(3))
    
