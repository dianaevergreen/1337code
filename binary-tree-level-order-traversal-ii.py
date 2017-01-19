# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        
        Q = [[root,0]]
        
        sol = [[]]
        
        while Q:
            current, level = Q.pop(0)
            
            if len(sol) < level + 1:
                sol.append([current.val])
            else:
                sol[level].append(current.val)
            
            if current.left:
                Q.append([current.left, level+1])
            if current.right:
                Q.append([current.right, level+1])
        
        sol.reverse()
        
        print sol
        
        return sol
        
        