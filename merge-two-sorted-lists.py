# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        c1 = l1
        c2 = l2
        
        if c1 is None and c2 is None:
            return None
        
        if c1 is not None and c2 is None:
            return c1
        if c1 is None and c2 is not None:
            return c2
        
        
        if c1 is not None and c2 is not None:
            if c1.val >= c2.val:
                c3 = ListNode(c2.val)
                sol = c3
                c2 = c2.next
                
            else:
                c3 = ListNode(c1.val)
                c1 = c1.next
                sol = c3
        
        while c1 is not None and c2 is not None:
            if c1.val >= c2.val:
                c3.next = ListNode(c2.val)
                c3 = c3.next
                c2 = c2.next
            else:
                c3.next = ListNode(c1.val)
                c3 = c3.next
                c1 = c1.next
                
        if c1 is None and c2 is not None:
            while c2 is not None:
                c3.next = ListNode(c2.val)
                c3 = c3.next
                c2 = c2.next
                
        if c1 is not None and c2 is None:
            while c1 is not None:
                c3.next = ListNode(c1.val)
                c3 = c3.next
                c1 = c1.next
        return sol
                
        