# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        Q = [[root,0]]
        
        sol = [[]]
        
        while Q:
            current, level = Q.pop(0)
            if level+1 > len(sol):
                if current is None:
                    sol.append([None])
                else:
                    sol.append([current.val])
            else:
                if current is None:
                    sol[level].append(None)
                else:
                    sol[level].append(current.val)
            
            if current is not None:
                Q.append([current.left, level+1])
                Q.append([current.right, level+1])
       
            
        for s in sol[1:]:
            if len(s) % 2 != 0:
                return False
            mid = len(s)/2
            ctr = len(s)-1
            
            for a in range(mid):
                print s[a] , s[ctr] 
                if s[a] != s[ctr]:
                    return False
                else:
                    ctr -=1
        return True
                
                
        
        
        