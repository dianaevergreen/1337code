# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def left_subtree(self, root, valie):
        if root is None:
            return True
            
        if root.val < valie:
            if root.left:
                l = self.left_subtree(root.left, valie)
            else:
                l = True
            if root.right:
                r = self.left_subtree(root.right,valie)
            else:
                r = True
            return l and r
        else:
            return False
            
        
    def right_subtree(self, root, valie):
        if root is None:
            return True
            
        if root.val > valie:
            if root.left:
                l = self.right_subtree(root.left, valie)
            else:
                l = True
            if root.right:
                r = self.right_subtree(root.right,valie)
            else:
                r = True
            return l and r
        else:
            return False
                    
        
        
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            
            if root.left:
                if self.left_subtree(root.left, root.val):
                    leftie = self.isValidBST(root.left)
                else:
                    return False
            else:
                leftie = True
            
            if root.right:
                if self.right_subtree(root.right, root.val):
                    rightie = self.isValidBST(root.right)
                else:
                    return False
            else:
                rightie = True
                
            return leftie and rightie
                    