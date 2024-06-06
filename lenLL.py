#Given a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.
class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        #code here
        count=0
        curr=head_node
        while curr!= None:
            count+=1
            curr=curr.next
        return count
