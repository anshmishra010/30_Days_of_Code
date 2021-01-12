class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        newnode=Node(data)
        if head is None:
            head=newnode
        else:
            temp=head
            while temp.next != None:
                temp=temp.next
            temp.next = newnode
        return head
    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head); 	  