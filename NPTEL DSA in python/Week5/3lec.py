#Opening a file
c=open("file.txt","r") #This is method of saving file contents in c buffer
#r=read,w=write,a=append
contents=c.readline()
print(contents)
#Now the pointer has moved to next \n
#Each successive readline moves pointer till next \n
contents1=c.readline()
print(contents1)
contents2=c.readline()
print(contents2)

#Moving pointer in the file to specific position in the string
c.seek(11)
contents3=c.readline()
print(contents3)
c.seek(0)
whole=c.readlines()
print(whole)

c.seek(13)
mid=c.readlines()
print(mid)

#Reading a fix number of characters:-
c.seek(0)
j=c.read(10)#This will read first 10 char from the pointer
print(j)

#How to know if file has ended 
k=c.readlines()
k1=c.readline()
print(k1)#This will return an empty string as the pointer is at the end



#Writing a file
#This will delete all the content of the file and add your content
q=open("file.txt","w")
s="Love for competitive coding"
q.write(s)
#
c.seek(0)
t=c.readlines()
print(t)

p="Anurag\nParth\nMandar"
q.seek(0)
q.write(p) 
c.seek(0)
p1=c.readlines()
print(p1)


#Closing 
c.flush()#This commits all the writes
c.close()
q.close()
#Buffers are flushed


#Processing file line by line:-
#contents=fh.readlines()
#for l in contents
#-----

#Even better:-for l in fh.readlines():

#Copying a file
infile=open("file.txt","r")
outfile=open("Output.txt","w")

for line in infile.readlines():
    outfile.write(line)
    
infile.close()
outfile.close()

#Copying in oneshot:-
infile=open("file.txt","r")
outfile=open("Output.txt","w")
conts=infile.readlines()
outfile.writelines(conts)
infile.close()
outfile.close()

#Get rid of trailing '\n':
# conts1=fh.readlines()
# for line in conts1:
#     s=line[:-1]

# instead,use rstrip() to remove trailing whitespace
#  for line in contents:
#      s=line.rstrip()
#Also strip both side lstrip()

