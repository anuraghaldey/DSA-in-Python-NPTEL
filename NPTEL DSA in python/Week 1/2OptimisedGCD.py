def gcd(m,n):
    i=min(m,n)
    
    while(i):
        if(m%i and n%i):
            return i
    return -1

print(gcd(12,4))