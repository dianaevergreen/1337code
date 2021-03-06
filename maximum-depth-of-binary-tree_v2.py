# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       
        if root is None:
            return 0
            
        max_depth = 0    
        Q = [[root, 1]]
        
        while Q:
            current, level = Q.pop(0)
            if level > max_depth:
                max_depth = level
                
            if current.left:
                Q.append([current.left, level +1])
            if current.right:
                Q.append([current.right, level + 1])
                
                
        return level
            
        
        