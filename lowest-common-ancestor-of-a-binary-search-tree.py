# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        mini = min(p.val,q.val)
        maxi = max(p.val,q.val)
        
        current = root
        
        while current is not None:
            if current.val == mini or current.val == maxi:
                return current.val
            if mini < current.val and maxi > current.val:
                return current.val
            if mini < current.val and maxi < current.val:
                current = current.left
            if mini > current.val and maxi > current.val:
                current = current.right
        return None