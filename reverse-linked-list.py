# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        if head.next == None:
            return head
            
        if head.next.next == None:
            cabeza = head.next
            cabeza.next = head
            head.next = None
            return cabeza
            
            
        prev = None
        current = head
        next = head.next
        
        while next != None:
            current.next = prev
            #Me corro
            prev = current
            current = next
            next = next.next
        
        
        current.next = prev
        return current
        
        
        