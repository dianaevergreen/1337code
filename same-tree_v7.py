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
        
        if p and q:
            a  = 0
        
        elif p or q:
            return False
        if p is None and q is None:
            return True
        
        Q1 = [p]
        Q2 = [q]
        
        while Q1 and Q2:
            current1 = Q1.pop(0)
            current2 = Q2.pop(0)
            
            if current1.val != current2.val:
                return False
            if current1.left and current2.left:
                if current1.left.val != current2.left.val:
                    return False
                else:
                    Q1.append(current1.left)
                    Q2.append(current2.left)
                
                
            else:
                if current1.left or current2.left:
                    return False
            
            
            if current1.right and current2.right:
                if current1.right.val != current2.right.val:
                    return False
                else:
                    Q1.append(current1.right)
                    Q2.append(current2.right)
                    
            else:
                if current1.right or current2.right:
                    return False
                    
        if Q1 or Q2:
            return False
        else:
            return True