# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r= []
        
        if root.left:
            r.extend(self.inorderTraversal(root.left))
        r.append(root.val)
        
        if root.right:
            r.extend(self.inorderTraversal(root.right))
            
        return r