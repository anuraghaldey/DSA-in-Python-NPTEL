fibtable={}
def fib(n):
    try:
        value = fibtable[n]
    except KeyError:
        if n == 0 or n == 1:
            value = n
        else:
            value = fib(n-1) + fib(n-2)
        fibtable[n] = value
   
    return value

print(fib(7))  


#Solve subproblems in order of dependencies
fibtable1={}
def fib1(n):
    fibtable1[0]=0
    fibtable1[1]=1
    
    for i in range(2,n+1):
        fibtable1[i]=fibtable1[i-1]+fibtable1[i-2]
    return fibtable1[n]    

print(fib1(4))