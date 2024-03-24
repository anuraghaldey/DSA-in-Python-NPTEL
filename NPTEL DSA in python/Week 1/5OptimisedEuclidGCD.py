def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
        
    if (m%n)==0:
        return (n)
    else:
        return gcd(n,m%n)
    
def gcd1(m,n):
    if m<n:
        (m,n)=(n,m)
        
    while (m%n)!=0:
        (m,n)=(n,m%n)
        
    return (n)


print (gcd1(101,2))