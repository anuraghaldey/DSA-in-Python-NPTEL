#We can reduce the number of lookups for recursive lookups which are repeated,
# i.e for the value we computed before ,we have to comppute again and again.
# To prevent this we can maintain a memory table,and then search the value in 
# the table first instead of direct calculating.This is method is called memoization(Dynamic Programming).
#Memoized Fibonacci:-This reduces time complexity
def fib(n): 
    if(fibtable[n]):
        return fibtable[n]
    if(n==0 or n==1):
        val=n
    else:
        val=fib(n-1)+fib(n-2)
        fibtable[n]=val
        return val
    
#General:-
# func(x,y,z):
#     if(ftable[x][y][z]):
#         return ftable[x][y][z]
#     value=expressions in terms of subproblems
#     ftable[x][y][z]=value
#     return value

def fib(n):
    ftable[0]=0
    ftable[1]=1
    for i in range(2,n+1):
        ftable[i]=ftable[i-1]+ftable[i-2]
    return ftable[n]