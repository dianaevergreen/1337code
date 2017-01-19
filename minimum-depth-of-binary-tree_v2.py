# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        Q = [(root, 1)]
        
        while Q:
            current, level = Q.pop(0)
            if not current.left and not current.right:
                return level
                
            if current.left:
                Q.append((current.left, level+1))
            if current.right:
                Q.append((current.right, level+1))
                
                