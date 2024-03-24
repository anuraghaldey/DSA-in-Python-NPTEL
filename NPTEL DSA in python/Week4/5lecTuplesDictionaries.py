#Tuples:-They are immutable eg:-
date=(12,3,2024)
print(date[0:])

#Dictionaries:-Key value pair ,same like maps.Store of values can be searched by a key (arbitrary index)
#Any immutable value can be a key
#We can update the dictionaries as we want -Means it is mutable

#Initialisation:-
l={}
l[["Kohli"]]=76
l["Rohit"]=102
l["Pujara"]=101

print(l["Kohli"])
#we can use nested too:-
a={}

a["Anurag"]={}
a["Parth"]={}
a["Anurag"]["Haldey"]=2
a["Parth"]["Sharma"]=4
print(a["Anurag"]["Haldey"])

b={"Anurag":13,"Parth":45}
print(b["Anurag"])

print(b.keys())

#Performing:-

    