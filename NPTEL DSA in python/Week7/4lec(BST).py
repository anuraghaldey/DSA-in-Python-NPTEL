#Binary Search Trees-Dynamic data in a sorted manner:-Searching is in logn time
#smaller values are to left o current node and greater are to right,no duplicate values

#Implementation:-

class Tree():
    def __init__(self,inval=None):
        self.value=inval
        if(self.value):
            self.left=Tree()
            self.right=Tree()
        else:
            self.left=None
            self.right=None
        
    
    def isempty(self):
        return (self.value==None)
    
    def inorder(self):
        if(self.isempty()):
            return ([])
        else:
            return (self.left.inorder()+[self.value]+self.right.inorder())
        
    def __str__(self):
        return str(self.inorder())
    
    def search(self,v):
        if(self.isempty()):
            return False
        if(self.value==v):
            return True
        elif(self.value>v):
            return self.left.search(v)
        return self.right.search(v)
    
    def minimum(self):
        if((self.left)==None):
            return self.value
        return self.left.minimum()
    def maximum(self):
        if((self.right)==None):
            return self.value
        return self.right.minimum()
    def foo(self):
        if self.isempty():
            return(0)
        elif self.isleaf():
            return(self.value)
        else:
            return(self.value + max(self.left.foo(),
                                    self.right.foo()))
    def insert(self,x):
        if(self.isempty()):
            self.value=x
            self.left=Tree()
            self.right=Tree()
        if(self.value==x):
            return
        elif(self.value>x):
            self.left.insert(x)
            return
        self.right.insert(x)
        return 
    def isleaf(self):
        return (self.left==None and self.right==None)
    def makeempty(self):
        self.value=None
        self.left=None
        self.right=None
        return
    def copyright(self):
        self.value=self.right.value
        self.left=self.right.left
        self.right=self.right.right
        return 
    def delete(self,x):
        if(self.isempty()):
            return
        if(x<self.value()):
            self.left.delete(x)
        elif(x>self.value()):
            self.right.delete(x)
        
        if(self.value==x):
            if(self.isleaf()):
                self.makeempty()
            elif(self.left.isempty()):
                self.copyright()
            else:
                self.value=self.left.maximum()
                self.left.delete(self.left.maximum())
            return
        

l1=Tree(1)
l1.insert(5)
l1.insert(4)
l1.insert(7)
l1.insert(3)
l1.insert(2)

print(l1)
print(l1.foo())