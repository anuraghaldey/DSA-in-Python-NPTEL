#String format method:-
s="first:{0},second:{1}".format(12,24)
print(s)
#Same like arguments we pass as to a function
 
s="first:{s},second{n}".format(n=45,s=60)
print(s)

#Real Formatting
s="value:{0:2d}".format(5)#Here d=integer value and 2 denotes 2 blank spaces before
print(s)
s="value:{0:6.2f}".format(46.23234)
print(s)