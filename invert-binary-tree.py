# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root

        if root.left:
            tmp_left = root.left
            flag_left = True
        else:
            tmp_left = None
            flag_left = False


        if root.right:
            tmp_right = root.right
            flag_right = True
        else:
            flag_right = False

        
        if flag_right:
            root.left = self.invertTree(tmp_right)
        else:
            root.left = None

        if flag_left:
            root.right = self.invertTree(tmp_left)
        else:
            root.right = None
        return root			

            
            