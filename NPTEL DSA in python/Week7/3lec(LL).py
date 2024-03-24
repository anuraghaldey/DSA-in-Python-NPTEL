# Linked List
class Node:
    def __init__(self, inval=None):
        self.value = inval
        self.next = None

    def isempty(self):
        return (self.value == None)
    #Insert at tail
    def append(self,x):
        if self.isempty():
            self.value=x
        elif self.next==None:
            self.next=Node(x)
        else:
            while(self.next!=None):
                self=self.next
            self.next=Node(x)
            #self.next.append(x)#Recursively go to last node
        return ()
    #Insert at head
    def Iathead(self,x):
        if(self.isempty()):
            self.value=x
        else:
            newNode=Node(x)
            (self.value,newNode.value)=(newNode.value,self.value)
            temp=self.next
            self.next=newNode
            newNode.next=temp
        return()
    def delete(self,x):
        if self.isempty():
            return()
        elif self.value==x:
            if(self.next):
                self.value=self.next.value
                self.next=self.next.next
            else:
                self.value=None
            return()
        else:
            while(self.next.value!=x):
                self=self.next
            self.next=self.next.next
            return ()
    def sum(self):
        if(self.value==None):
            return 0
        elif(self.next==None):
            return self.value
        else:
            return self.value+self.next.sum()
        
    def __str__(self):
        selflist=[]
        if(self.value==None):
            return str(selflist)
        else:
            temp=self
            selflist.append(temp.value)
            selflist.append("->")
            while(temp.next):
                temp=temp.next
                selflist.append(temp.value)
                selflist.append("->")
            return str(selflist)
l1 = Node(5)  # Memory allocation of head of a list
l1.append(34)
l1.append(45)
l1.append(123)
l1.Iathead(345)
l1.delete(345)
print(l1.sum())
print(l1)
