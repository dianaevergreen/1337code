# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

flag = True
class Solution(object):
    
    def Balanced(self, root):
        if root is None:
            return 0, True
        
        if not root.left and not root.right:
            return 0, True
        else:
            sol = 0
            if root.left:
                leftie, bl = self.Balanced(root.left)
                leftie += 1
            else:
                leftie, bl = 0, True
            if root.right:
                rightie, br = self.Balanced(root.right)
                rightie += 1
            else:
                rightie, br = 0, True
            
            ma, mi = max(leftie, rightie), min(leftie, rightie)
            if ma  - mi > 1 or not bl or not br:
                return ma, False
            
					
            return ma, True

    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.Balanced(root)[1]
        
        