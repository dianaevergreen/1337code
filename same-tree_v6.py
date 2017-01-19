# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorder(self, root):
        sol = []
        if root.left:
            sol.extend(self.inorder(root.left))
        else:
            sol.append(None)
        sol.append(root.val)
        if root.right:
            sol.extend(self.inorder(root.right))
        else:
            sol.append(None)
        return sol
            
       
    def preorder(self, root):
        sol = []
        sol.append(root.val)
        if root.left:
            sol.extend(self.preorder(root.left))
        else:
            sol.append(None)
        if root.right:
            sol.extend(self.preorder(root.right))
        else:
            sol.append(None)
        return sol
        
    
   
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
        
        ip = self.inorder(p)
        iq = self.inorder(q)
        
        pp = self.preorder(p)
        pq = self.preorder(q)
    
        if ip == iq and pp == pq:
            return True
        else:
            return False
        
      