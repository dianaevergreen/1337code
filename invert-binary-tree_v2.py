# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None:
            return None
        leftie , rightie = None, None   
        if root.left:
            leftie = self.invertTree(root.left)
            
        if root.right:
            rightie = self.invertTree(root.right)
            
        
        root.left = rightie
        root.right = leftie
            
        return root