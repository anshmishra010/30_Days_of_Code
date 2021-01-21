class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data=data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
            return root

    def getHeight(self,root):
        lh=rh=0
        if root.left is not None:
            lh=1+Solution.getHeight(self,root.left)
        if root.right is not None:
            rh=1+Solution.getHeight(self,root.right)
        if(lh>rh):
            return lh
        else:
            return rh


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
      