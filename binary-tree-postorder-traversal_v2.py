# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
            
        r = []
        
        if root.left:
            r.extend(self.postorderTraversal(root.left))
        if root.right:
            r.extend(self.postorderTraversal(root.right))
        r.append(root.val)
        return r