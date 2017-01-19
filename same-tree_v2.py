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
        elif p is None or q is None:
            return False
        
            
        if not p.left and not p.right and not q.left and not q.right and p.val == q.val:
            return True
        
        else:
            if p.val != q.val:
                return False
            else:
                if p.left and q.left:
                    IsitL= self.isSameTree(p.left, q.left)
                elif p.left or q.left:
                    return False
                else:
                    IsitL = True
                    
                if p.right and q.right:
                    IsitR = self.isSameTree(p.right, q.right)
                elif p.right or q.right: 
                    return False
                else:
                    IsitR = True
                
                if not IsitL or not IsitR:
                    return False
                else:
                    return True
                    
 
      
      