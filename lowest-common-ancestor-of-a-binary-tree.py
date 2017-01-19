# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    
            
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        counter = 0
        Q = [root]
        
        dicty = {root:None}
        
        while Q and counter < 2:
            current = Q.pop(0)
            if current.val == p or current == q:
                    counter += 1
                    
            if current.left:
                Q.append(current.left)
                dicty[current.left] = current
                
            if current.right:
                Q.append(current.right)
                dicty[current.right] = current
                
        pcopy = p
        ap = [p]
        
        while dicty[pcopy] != None:
            parent = dicty[pcopy]
            ap.append(parent)
            pcopy = parent
            
        qcopy = q
        aq = [q]
        
        while dicty[qcopy] != None:
            parent = dicty[qcopy]
            aq.append(parent)
            qcopy = parent
            
        mini = min (len(aq), len(ap))
        aq.reverse()
        ap.reverse()
        
        ancestor = aq[0]
        for i in range(mini):
            if aq[i] != ap[i]:
                return ancestor
            else:
                ancestor = aq[i]
        return ancestor
            
            
            
                
                