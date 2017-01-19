# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
            
        marked = set([head])
        
        current = head.next
        while current != None:
            if current in marked:
                return True
            marked.add(current)
            current = current.next
            
        return False
            