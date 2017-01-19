# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            tmp_root = preorder.pop(0)
            root = TreeNode(tmp_root)
            index_root = inorder.index(tmp_root)
            root.left = self.buildTree(preorder, inorder[:index_root])
            root.right = self.buildTree(preorder, inorder[index_root+1:])
            
            return root
            
            
            