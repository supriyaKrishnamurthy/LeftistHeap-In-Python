import sys


class LeftistNode(object):
    def __init__(self,val):
        self.val=val
        self.dist = 0
        self.right=None
        self.left=None
        self.prnt=None 
        
class LeftistHeap(object):
    
    def inorder(self,root): 
        if root: 
            myHeap.inorder(root.left)
            print(root.val) 
            myHeap.inorder(root.right) 
            
    def distance(self,root):
        if(root is None):
            return -1
        else:
            return root.dist
    
    def merge(self,rootA,rootB):
        if(rootA is None):
            return rootB
        if(rootB is None):
            return rootA
        if(rootB.val>rootA.val):
            temp=rootB
            rootB=rootA
            rootA=temp
        rootA.right=myHeap.merge(rootA.right,rootB)
        if(myHeap.distance(rootA.right)>myHeap.distance(rootA.left)):
            temp=rootA.right
            rootA.right=rootA.left
            rootA.left=temp
        if(rootA.right is None):
            rootA.dist=0
        else:
            rootA.dist=1+(rootA.right.dist)
        return(rootA)
        
    def deletion(self,root):
        print("deleted element is ",root.val)
        root=myHeap.merge(root.right,root.left)
        return root
        
    def insert(self,root):
        newnode=LeftistNode(int(input("enter value\n")))
        root=myHeap.merge(root,newnode)
        print("root element is ",root.val," inorder traversal of tree is:")
        myHeap.inorder(root)
        return(root)
        
#driver program
val=int(input("enter root node: "))
root=LeftistNode(val)
myHeap=LeftistHeap()
while(1):
    print("\n 1.insert 2.print 3.delete 4.exit\n")
    val=int(input("enter your option: "))
    if(val==1):
        root=myHeap.insert(root)
    elif(val==2):
        myHeap.inorder(root)
    elif(val==3):
        root=myHeap.deletion(root)
    else:
        sys.exit()