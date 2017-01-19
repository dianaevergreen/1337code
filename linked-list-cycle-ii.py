# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
            
        marked = set([head])
        
        current = head.next
        while current != None:
            if current in marked:
                return current
            marked.add(current)
            current = current.next
            
        return None