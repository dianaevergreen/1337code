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
    
    def List2BST(self, a, i, f):
        if i == f:
            return TreeNode(a[i])
        if i > f:
            return None
        else:    
            mid = (i + f) / 2
            root = TreeNode(a[mid])
            root.left = self.List2BST(a,i,mid-1)
            root.right = self.List2BST(a,mid+1,f)
            
            return root
        
    
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        init = head
        while init != None:
            array.append(init.val)
            init = init.next
            
        root = self.List2BST(array, 0, len(array)-1)
        
        return root
        