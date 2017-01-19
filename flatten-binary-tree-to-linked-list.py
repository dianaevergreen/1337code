# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is not None:
            rightie = root.right
            
            if root.left:
                root.right = root.left
                self.flatten(root.right)
               
                
            if root.right:
                if root.left:
                    r = root.right
                    while r.right != None:
                        r = r.right
                    r.right = rightie
                self.flatten(rightie)
                    
            root.left = None 
            
                
    
            
            