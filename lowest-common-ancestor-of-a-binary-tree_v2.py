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
        def FindBothPaths(root, p, q):
            paths = [[p],[q]]
            dict_parents = {root:None}
            
            Q = [root]
            while Q:
                current = Q.pop(0)
                if current.left:
                    dict_parents[current.left] = current
                    Q.append(current.left)
                if current.right:
                    dict_parents[current.right] = current
                    Q.append(current.right)
                    
            for i in range(len(paths)):
                current = paths[i][0]
                
                while current:
                    paths[i].append(dict_parents[current])
                    current = dict_parents[current]
                    
            return paths
                    
                
        path_p, path_q = FindBothPaths(root, p, q)
        ancestor = None
    
        path_p.reverse()
        path_q.reverse()
    
        for i in range(len(zip(path_p, path_q))):
            if path_p[i] != path_q[i]:
                return ancestor
            else:
                ancestor = path_p[i]
    
        return ancestor
            
        
                
                
            