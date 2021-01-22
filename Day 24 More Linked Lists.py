class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
 
    def removeDuplicates(self,head):
        #Write your code here
        if head is None:
            return
        
        res = []
        res.append(head.data)
        start=head
        
        while head.next is not None:
            if head.next.data not in res:
                res.append(head.next.data)
                head=head.next
            else:
                head.next = head.next.next
                
        return start
                
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 