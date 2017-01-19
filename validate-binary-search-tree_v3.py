# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ## Brilliant Solution. Short and elegant. By wz2326 
    
    def isValidBST(self, root, floor = float('-inf'), celing = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        if root.val <= floor or root.val >= celing:
            return False
            
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, celing)
        
       
        
        
      
        