# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
            
        ptr1 = head
        ptr2 = head.next
        
        while ptr2 is not None:
            while ptr2 is not None and ptr2.val == ptr1.val:
                ptr2 = ptr2.next
                
            if ptr2 is not None:
                ptr1.next = ptr2
                ptr1 = ptr2
                ptr2 = ptr2.next
                
            else:
                ptr1.next = None
            
        return head