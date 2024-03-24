def gcd(m,n):
    #Assume m>=n
    if m<n:
        (m,n)=(n,m)
        
    if(m%n)==0:
        return n
    else:
        diff=m-n
        return gcd(n,diff)
    
print(gcd(12,84))