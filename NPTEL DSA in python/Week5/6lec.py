while(1):
    try:
        userdata=int(input("Enter a number"))
    except ValueError:
        pass#This mentions do nothing
    else:
        break
    
#Removing a list element 
l=[233,3,35,5,7,8]
del(l[1])
print(l)

#Also works for dictionary:
d={"Rohit":12,"Virat":34}
del(d["Virat"])
print(d)


#Checking undefined names
#eg:-
x=6
del(x)
#Now x is undefined and thus can cause name error

try:
    y=x
except NameError:
    x=56
    y=x
    print(y)
    
#None keyword is used to mention nothing
x=None

if x is None:
    y=x
    
print(y)