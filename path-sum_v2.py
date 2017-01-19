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
        
        if not root:
            return False
            
        path_dict = {root:None}
        leaves = []
        
        Q = [root]
        while Q:
            current = Q.pop(0)
            if current.left or current.right:
                if current.left:
                    path_dict[current.left] = current
                    Q.append(current.left)
                    
                if current.right:
                    path_dict[current.right] = current
                    Q.append(current.right)
            else:
                leaves.append(current)
        
    
        for l in leaves:
            acum = l.val
            parent = path_dict[l]
            while parent is not None:
                acum += parent.val
                parent = path_dict[parent]
            if acum == sum:
                return True
                
        return False
                
                
                
            