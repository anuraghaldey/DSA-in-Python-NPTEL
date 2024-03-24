def remdup(l):
    b=[]
    for i in l:
        if(i in b):
            continue
        else:
            b.append(i)
    
    l.clear()
    
    for i in b:
        l.append(i)
    return l
        
            
        
        
    
def sumsquare(l):
    x=[0,0]
    for i in range(0,len(l)):
        if(l[i]%2):
            x[0]+=(l[i]*l[i])
        else:
            x[1]+=(l[i]*l[i])
    return x

def transpose(m):
    l = []
    for i in range(len(m[0])):
        temp = []
        for j in range(len(m)):
            temp.append(m[j][i])
        l.append(temp)
    return l
                