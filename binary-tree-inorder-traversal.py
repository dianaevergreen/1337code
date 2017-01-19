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
        if root is None:
            return []
        sol = []
        if root.left:
            sol.extend(self.inorderTraversal(root.left))
        sol.append(root.val)
        if root.right:
            sol.extend(self.inorderTraversal(root.right))
        return sol