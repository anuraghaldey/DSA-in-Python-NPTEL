#String functionss

#to remove leading whitespaces
s="     hello       "
print(s)
t=s.lstrip()#removes left space
t=s.rstrip()#Removes right space
t=s.strip()#Both sides

print(t)

#Searching in a string:-
s="Anurag"
print(s.find("Anu"))#Will return 1st position in the pattern where Anu occurs if not occurs then -1

#Searching only in part of string:
print(s[1:4].find("ur"))

#same function is s.index() but instead of returning -1 it causes value error if not found

#Search and Replace
s="AnuAnu RagRag"
print(s.replace("Anu","Hal"))
print(s)
#it will replace every occurance of that string by mentioned

#Replace for first n copies
print(s.replace("Anu","Hal",1))
#But s itself is unchanged because strings are immutable


#Splitting a strring
a="1,2,4,5,6,7,8,9,0"

print(a.split(","))
#Upto n places
print(a.split(",",6))


#Joining string
#Recombine a list of strings using separator
columns=a.split(",")
joinstring=","
csvline=joinstring.join(columns)
print(csvline)


date="16"
month="08"
year="2024"
today="-".join([date,month,year])
print(today)

#uppercase etc:-
# s.capitalize()#1st char capital
# s.upper()
# s.lower()
#s.title()
# s.swapcase()

#Resizing strings:-
a='Anurag'
print(a.center(40,"_"))
print(a.ljust(50,"*"))
print(a.rjust(50,"#"))

#Checking the nature of the string:-
# a.isalpha()
# a.isnumeric()