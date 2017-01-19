# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        Q = [(root,0)]
        sol = [[root.val]]
        
        while Q:
            current, level = Q.pop(0)
            if len(sol) == level + 1 and (current.left or current.right ):
                sol.append([])
            if current.left:
                sol[level+1].append(current.left.val)
                Q.append((current.left, level+1))
            if current.right:
                sol[level+1].append(current.right.val)
                Q.append((current.right, level+1))
            
        return sol
                