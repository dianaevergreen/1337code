# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorder(self, root):
        if root.left is None and root.right is None:
            return [root.val]
            
        array = []
        if root.left:
            array.extend(self.inorder(root.left))
        array.append(root.val)
        if root.right:
            array.extend(self.inorder(root.right))
        return array
            
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        a = self.inorder(root)
        print a
        return a[k-1]
        