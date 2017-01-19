# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root):
        if not root:
            return []
        r = []
        if root.left:
            r.extend(self.inorder(root.left))
        r.append(root.val)
            
        if root.right:
            r.extend(self.inorder(root.right))
                
        return r
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        sol = self.inorder(root)
        
        sorted_sol = sorted(sol)
        
        if len(set(sol)) != len(sorted_sol) or sol != sorted_sol:
            return False
        return True
        
        
      
        