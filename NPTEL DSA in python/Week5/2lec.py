#Taking input and storing value in the variable

a=int(input(("Enter aa number: ")))
b=int(input("Enter another number:\n"))
print(a+b)

#Exception Handling:-

while(1):
    try:
        g=int(input("Enter a number"))
    except:
        print("Sorry it is not a number") 
    else:
        break
    
#Printing:-
print("Anurag is my name and age :",20 ," and what",67)

print("continue ",end=" ")
print(" on the same line",end='\n')
print("Next line")
print(2,3)#comma brings space by default
print(2,3,sep="")#sep decides how much space to keep in place of commas 
