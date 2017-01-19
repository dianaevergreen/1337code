# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        sol = []
        
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [str(root.val)]
        else:
            left_sub = [str(root.val) + '->' + str(x) for x in self.binaryTreePaths(root.left)]
            
            right_sub = [str(root.val) + '->' + str(x) for x in self.binaryTreePaths(root.right)]
        return left_sub + right_sub
            
                
                
                
                