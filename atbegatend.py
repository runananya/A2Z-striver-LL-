#Create a link list of size N according to the given input literals. Each integer input is accompanied by an indicator which can either be 0 or 1. If it is 0, insert the integer in the beginning of the link list. If it is 1, insert the integer at the end of the link list.
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        temp=Node(x)
        temp.next=head
        return temp
        
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        if head is None:
            return Node(x)
        curr=head
        while curr.next!=None:
            curr=curr.next
        curr.next=Node(x)
        return head
            
