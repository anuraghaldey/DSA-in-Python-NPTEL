#Scope :-Global immutable values
def f():
    global x
    y=x
    x=22
    print(y)

x=4
f()
print(x)


#Defining functions within function
def f1():
    def g(a):
        return(a+1)
    def h(b):
        return (2*b)
    
    global x
    y=g(x1)+h(x1)
    print(y)
    x=22

x1=6
f1()