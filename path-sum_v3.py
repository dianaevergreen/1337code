# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def DFS(self, root):
        if not root:
            return None
        
        if not root.left and not root.right:
            return [root.val]
            
        leftie = self.DFS(root.left)
        rightie = self.DFS(root.right)
        
        sol = []
        
        if leftie is not None:
            for l in leftie:
                sol.append(root.val + l)
                
        if rightie is not None:
            for r in rightie:
                sol.append(root.val + r)
                
        return sol
            
            
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        answer = self.DFS(root)
        if answer is None:
            return False
            
        for a in answer:
            if a == sum:
                return True
        return False
        
            
        
            
        
                
                
                
            