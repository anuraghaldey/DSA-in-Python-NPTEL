# 1
def orangecap(d):
    l = {}
    for i in d.values():
        for j, k in i.items():
            if (j in l):
                l[j] += k
            else:
                l[j] = k

    hp = None
    hs = -1
    for i, j in l.items():
        if (j > hs):
            hp = i
            hs = j
    pair1 = (hp, hs)
    return pair1


def addpoly(p1, p2):
    pairlist = []

    i = 0
    j = 0

    while i < len(p1) and j < len(p2):
        if p1[i][1] == p2[j][1]:
            cs = p1[i][0] + p2[j][0]
            if cs != 0:
                pairlist.append((cs, p1[i][1]))
            i += 1
            j += 1
        elif p1[i][1] > p2[j][1]:
            pairlist.append(p1[i])
            i += 1
        else:
            pairlist.append(p2[j])
            j += 1

    while i < len(p1):
        pairlist.append(p1[i])
        i += 1

    while j < len(p2):
        pairlist.append(p2[j])
        j += 1

    return pairlist


def mul(a, b):
    x = a[0] * b[0]
    y = a[1] + b[1]
    p = (x, y)
    return p


def multpoly(p1, p2):
    wholelist=[]
    
    for i in p1:
        list=[]
        for j in p2:
            a=mul(i,j)
            list.append(a)
        wholelist.append(list)
        
    total=addpoly(wholelist[0],wholelist[1])
    
    for i in range(2,len(wholelist)):
        total=addpoly(total,wholelist[i])
        
    return total

