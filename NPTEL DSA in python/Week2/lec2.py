s = 'Anurag'
print(s)

n = "Anurag's"
print(n)

g = ''' "Anurag's Phone"'''
print(g)

#  01234
i = 'hello'
# -5-4-3-2-1

print(i[-2])

print(s+" "+n)#Concatenation
print(len(s))#returns length of a string



#segment of a string
r='Indians'
print(r[1:4])#range (1,m+1)

print(r[:4])#default start from 0

print(r[2:])#default end and -1


#Modifying strings:-
h='Hello'

#Error:- h[3]='i' 
#instead we can do
h=h[0:3]+"i"+h[4:]
print(h)