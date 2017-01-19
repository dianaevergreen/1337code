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
        if head.next == None:
            return False
            
        ptr1 = head
        ptr2 = head.next
        
        while ptr2 != None:
            if ptr1 == ptr2:
                return True
            else:
                if ptr2.next != None:
                    ptr2 = ptr2.next.next
                else:
                    return False
                ptr1 = ptr1.next
        return False
                    