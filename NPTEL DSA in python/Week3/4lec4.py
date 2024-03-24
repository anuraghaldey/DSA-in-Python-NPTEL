def BinarySearch(list,v,l,h):
    if(l>h):
        return -1
    
    mid=(l+h)//2
    if(list[mid]==v):
        return mid
    elif(list[mid]>v):
        return BinarySearch(list,v,l,mid-1)
    
    return BinarySearch(list,v,mid+1,h)


list=[1,4,8,10,23,46]
print(BinarySearch(list,23,0,len(list)-1))
    