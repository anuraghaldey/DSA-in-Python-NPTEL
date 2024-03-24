list1=[1,2,4,5]
list2=list1
list1[3]=10
print(list2[3])
#lists are mutable


#But here it is different iin this scenario:-
#concatenation produces a new list but you can see l2 was pointing to old l1 so it remains same
l1=[23,34,5,6]
l2=l1
l1=l1[0:2]+[341,462]
print(l1)
print(l2)

#Adding elements to a list
li1=[23,34,45,56]
li2=li1
li1.append(23)
print(li2)

#But here it changes as the new list is formed
lii1=[45,56,67,89]
lii2=lii1
lii1=lii1+[452]#this is again concatenation
print(lii2)

lii2.extend(lii1)#for adding whole list
print(lii2)


#Removing Elements:-
x=[23,35,23,79,9]
x.remove(23)#this removes the first occarance of 23 in the list
x.remove(23)#if there is no x then it gives error
print(x)

#Mainpulating subarray of lists
a=[34,24,67,89]
b=a
a[2:4]=[10,20]
print(b)


#Expanding and shrinking a list
a1=[2,3,5,7]
a1[0:2]=[12]
print(a1)
a1[2:]=[34,45,68,9]
print(a1)


#List Membership
a11=[1,2,3,4]
print(3 in a11)#This will search 3 in a11 and return true if it is present or false

a22=[34,3,45,3,56,7,3,3,12,3]

while 3 in a22:
    a22.remove(3)#Removing all 3's from the llist
    
print(a22)


#General functions
#:-
a22.reverse()
a22.sort()
a22.index(56)
