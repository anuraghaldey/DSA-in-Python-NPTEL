s1=set([1,2,3,5])
s2=set([6,7,8,9])
print(s1-(s2-s1)==s1)

s1=set([1,2,3,6])
s2=set([2,3,5,7])
print(s1|s2 != s1^s2)