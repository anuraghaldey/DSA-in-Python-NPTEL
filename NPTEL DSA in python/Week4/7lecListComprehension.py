def f(n):
    return 2 * n

def apply(f, l):
    return [f(x) for x in l]

l = [12, 23, 34, 45]
a = apply(f, l)
print(a)

#Python has a built in function map(f,l) to do this

l=list(map(f,l))
print(l)

#Selecting a sublist:-
def check(n):
    return not(n%2)
def select(check,l):
    sublist=[]
    for x in l:
        if(check(x)):
            sublist.append(x)
    return sublist

b=[12,2,3,4,5,9]
c=select(check,b)
print(c)

#We can achieve above by built in function filter
h=list(filter(check,b))
print(h)


#Example:-
def square(x):
    return (x*x)
def iseven(x):
    return (x%2==0)
#Program for squares of even number below 100
t=list(map(square,list(filter(iseven,range(0,100)))))
print(t)


#Program for writing all the pythagorean triplet below 100
list1=[(x,y,z) for x in range(0,100)for y in range(x,100)for z in range(y,100) if(square(x)+square(y)==square(z) and x<y and y<z)]
print(list1)

#For initialising a matrix of 3*3 size with all zeroes
list2=[[0 for i in range(3)]for j in range(3)]
#here if we update:-
list2[1][1]=7
print(list2)

#But when we do here:-
zerolist=[0 for i in range(3)]
list3=[zerolist for i in range(3)]
list3[1][1]=7
print(list3)
#Here every row in list3 points to a same list zerolist 