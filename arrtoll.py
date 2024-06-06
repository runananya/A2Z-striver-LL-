#Geek loves linked list data structure.
#Given an array of integer arr of size n, Geek wants to construct the linked list from arr.
#Construct the linked list from arr and return the head of the linked list.

class Solution:
    def constructLL(self, arr):
      curr=Node(0)
      head=curr
      for i in range(len(arr)):
        curr.data=arr[i]
        if i<len(arr)-1:
            curr.next=Node(0)
            curr=curr.next
        return head
