# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            
        Q = [[root, 1]]
       
        tmp = 0
        
        while Q:
            current, depth = Q.pop(0)
            
            if current.left or current.right:
                if current.left:
                    Q.append([current.left, depth+1])
                if current.right:
                    Q.append([current.right, depth+1])
                
            else:
                if depth > tmp:
                    tmp = depth
       
        
        return tmp
        