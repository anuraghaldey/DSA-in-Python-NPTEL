#Function to check prime
def factors(n):
    l=[]
    for i in range(1,n+1):
        if(n%i==0):
            l=l+[i]
    return l

def isprime(n):
    return (factors(n)==[1,n])

print(isprime(1))

#Primes upto n
def PN(n):
    primes=[]
    for i in range(1,n+1):
        if(isprime(i)):
            primes=primes+[i]
            
    return primes

print(PN(10))

#First n primes

def FNP(n):
    (count,i,list)=(0,1,[])
    while count<n:
        if isprime(i):
            (count,list)=(count+1,list+[i])
        i=i+1
    return list

print(FNP(10))