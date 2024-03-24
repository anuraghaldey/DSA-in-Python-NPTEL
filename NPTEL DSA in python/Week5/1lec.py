scores={'Anurag':[23,45,56],'Parth':[445,67,64]}

#Traditional approach to handle exception:-
if 'Anura' in scores.keys():
    scores['Anura'].append(234)
else :
    scores['Anura']=345
    
#Eception handling:
try:
    scores['Anil'].append([235])
except :
    scores['Anil']=[67,89]
print(scores)