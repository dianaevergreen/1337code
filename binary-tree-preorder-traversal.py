# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
            
        I = [root]
        D = []
        sol = []
        while I or D:
            while I:
                current = I.pop(0)
                sol.append(current.val)
                if current.left :
                    I.append(current.left)
                if current.right:
                    D.append(current.right)	
                
            while D:
                current = D.pop(-1)
                sol.append(current.val)
                if current.left:
                    I.append(current.left)
                if current.right:
                    D.append(current.right)
                if I:
                    break
        return sol