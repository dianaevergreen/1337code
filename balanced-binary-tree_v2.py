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
            return 0
        global flag
        if not root.left and not root.right:
            return 0
        else:
            sol = 0
            if root.left:
                leftie = self.Balanced(root.left) + 1
            else:
                leftie = 0
            if root.right:
                rightie = self.Balanced(root.right)+ 1
            else:
                rightie = 0
            
            ma, mi = max(leftie, rightie), min(leftie, rightie)
            if ma  - mi > 1:
                flag = False
            sol = ma
					
            return sol

    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        global flag
        flag = True
        self.Balanced(root)
        return flag
        
        