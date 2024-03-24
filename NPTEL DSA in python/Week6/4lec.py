colours={'Red','Green','Red','Blue'}#Sets in python are kind of built in dictionaries

print(colours)


#Definition
colours=set()#Set
colours1={}#This is empty dictionary

#We can convert any list to set using set function
numbers=set([12,24,34,56])
print(numbers)

#Set operations:-
odd=set([1,3,5,7,9])
prime=set([2,3,5,7,])
#Finding union:-
print(odd|prime)
#Intersection:-
print(odd&prime)
#Set difference:-
print(odd-prime)
#Exclusive Or:-
print(odd^prime)
print(prime^odd)



#Stack:-
#Last in first out
#Implemented using  list:-
#Push and pop from the right:-
#Push(s,x):-pushing x in stack named s:- s.append(x) s is here list
#Pop(x):-s.pop() s is here list
stack=[12,23,34,5]
stack.append(56)
print(stack)
stack.pop()
print(stack)

# #Queue:-
# # First in first out
# add(q,x):- adding at back of the queue i.e left:- q.insert(x) ,this inserts in left of list
# remove(x):-removing element from front of the queue i.e right ,q.pop(),removal from right
q=[12,23,33]
q.insert(0,4567)#Inserting at left /rear
print(q)
q.pop()
print(q)

# #Implementation of queue:-
# A knight on the chess board can be represented by (sx,sy) as start and a given cell is target
# which is (tx,ty),We need to check if the knight is reachable to the target or not

def explore((sx,sy),(tx,ty),n,m):
    marked=[[0 for i in range(n)]for j in range m]
    marked[sx][sy]=1
    q=[(sx,sy)]
    
    while(q!=[]):
        (ax,ay)=q.pop()
        for(nx,ny) in neighbours((ax,ay)):
            if(!(marked[nx][ny])):
                marked[nx][ny]=1
                q.insert(0,(nx,ny))
    return marked[tx][ty]