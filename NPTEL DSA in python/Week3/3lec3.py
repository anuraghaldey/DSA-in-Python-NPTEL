#Breaking the list
def search(l,v):
    (pos,i)=(-1,0)
    for x in l:
        if x==v:
            pos=i
            break#Break statement
        i=i+1
    return pos

l=[23,34,56,8,9,90,8]
print(search(l,8))