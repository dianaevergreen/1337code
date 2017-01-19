# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def List2BST(self, head, i, f):
        if i == f:
            return TreeNode(head.val)
        if i > f:
            return None
        
        else:
            mid = (f-i)/2
            init = head
            counter = 0
            while counter < mid:
                init = init.next
                counter += 1
            root = TreeNode(init.val)
            
            
            root.left = self.List2BST(head,i, i+mid-1)
            
            root.right = self.List2BST(init.next,i+counter+1,f)
            
            return root
       
    
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        if head is None:
            return None
        
        init = head
        counter = 0
        while init.next != None:
            init= init.next
            counter +=  1
        
        root = self.List2BST(head, 0, counter)
        
        return root
        