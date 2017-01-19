# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        
        Qp = [p]
        Qq = [q]
        
        while Qp and Qq:
            currentp = Qp.pop(0)
            currentq = Qq.pop(0)
            
            if currentp.val != currentq.val:
                return False
            
            if currentp.left and currentq.left:
                if currentp.left.val == currentq.left.val:
                    Qp.append(currentp.left)
                    Qq.append(currentq.left)
                else:
                    return False
            elif currentp.left or currentq.left:
                return False
                    
            if currentp.right and currentq.right:
                if currentp.right.val == currentq.right.val:
                    Qp.append(currentp.right)
                    Qq.append(currentq.right)
                else:
                    return False
            elif currentp.right or currentq.right:
                return False
                    
        return True