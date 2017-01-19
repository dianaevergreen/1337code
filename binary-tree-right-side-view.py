# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
            
        else:
            
            current = root
            an_array = [root.val]
            right_level = 1
            
            while current.right:
                an_array.append(current.right.val)
                current = current.right
                right_level += 1
                
            Q = [[root,1]]
            while Q:
                current, level = Q.pop(0)
                if level > right_level:
                    an_array.append(current.val)
                    right_level = level
                if current.right:
                    Q.append([current.right, level+1])
                if current.left:
                    Q.append([current.left, level+1])
            return an_array
               