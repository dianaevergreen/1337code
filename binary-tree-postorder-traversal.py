# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        
        """
        if root == None:
            return []
            
        I = [root]
        D = []
        Raiz = []
        sol = []

        while I or D:
            while I:
                current = I.pop(0)
                if not current.left and not current.right:
                    sol.append(current)
                    while Raiz and (Raiz[-1].left in sol or Raiz[-1].left == None) and (Raiz[-1].right in sol or Raiz[-1].right == None):
                        sol.append(Raiz.pop(-1))
                else:
                    Raiz.append(current)
                    if current.left:
                        I.append(current.left)
                    if current.right:
                        D.append(current.right)
            while D:
                current = D.pop(-1)
                if not current.right and not current.left:
                    sol.append(current)
					
                    while Raiz and (Raiz[-1].left in sol or Raiz[-1].left == None) and (Raiz[-1].right in sol or Raiz[-1].right == None):
                        sol.append(Raiz.pop(-1))
                else:
                    Raiz.append(current)
                    if current.right:
                        D.append(current.right)
                    if current.left:
                        I.append(current.left)
                        break
			
				
        Raiz.reverse()
        sol.extend(Raiz)
        for s in range(len(sol)):
            sol[s] = sol[s].val
			
        return sol		
        