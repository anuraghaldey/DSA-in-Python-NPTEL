#Pass Arguments by name:-
def diff(a,b):
    print(a-b)
    
    
diff(b=10,a=1)#We can change the parameter by mentioning by name

#default Arguments:-
def sum(a,b,c=10,d=10):
    print(a+b+c+d)
    
sum(12,24)#c and d values will be default set if the function calling does not mentioned parameters
sum(1,2,3,4)#Here it will consider the values passed as, we are passing 
sum(1,2,3)

#We can also define function conditionally i.e IF ELSE
#We can assign function with a new name
def f(a,b,c):
    print(a+b+c)
g=f#Now g will be pointing to f

#Passing functions as parameters
def square(x):
    return(x*x)

def apply(f,x,n):
    res=x
    for i in range(n):
        res=f(res)
    return res

print(apply(square,5,2))
