# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        
        current_left = root
        current_right = root
        
        level_left = 0
        level_right = 0
        
        
        while current_left.left:
            if current_left.left:
                current_left = current_left.left
                level_left += 1
         
        
        while current_right.right:
            if current_right.right:
                current_right = current_right.right
                level_right += 1
                
        
        
        if level_left == level_right:
            return 2**(level_left +1) - 1
       
        else:
            total_nodes = self.countNodes(root.left) + self.countNodes(root.right) + 1
            return total_nodes
        
        
        
        
            