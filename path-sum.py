# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return False
        
        leaves = []
        dicty_parents = {root:None}
        
        Q = [root]
        
        while Q:
            current = Q.pop(0)
            if current.left:
                dicty_parents[current.left] = current
                Q.append(current.left)
            if current.right:
                dicty_parents[current.right] = current
                Q.append(current.right)
                
            if current.left is None and current.right is None:
                leaves.append(current)
        
        
        for l in leaves:
            
            current = l
            suma = current.val
            
            while dicty_parents[current] is not None:
                current = dicty_parents[current]
                suma += current.val
            
            if suma == sum:
                return True
        return False
                
                
        
        
        