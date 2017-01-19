# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if root is None:
            return ""
            
        s = ""
        
        Q = [root]
        while Q:
            current = Q.pop(0)
            
            if current is not None:
                s += str(current.val) + ","
                
                if current.left:
                    Q.append(current.left)
                else:
                    Q.append(None)
                    
                if current.right:
                    Q.append(current.right)
                else:
                    Q.append(None)
                    
            else:
                s += "None,"
        return s    
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        a = data.split(",")
        
        r = a.pop(0)
        
        if r == "":
            return None
            
        root = TreeNode(int(r))
        
        
        Q = [root]
        while Q:
            current = Q.pop(0)
            l = a.pop(0)
            r = a.pop(0)
            
            if l != "None":
                current.left = TreeNode(int(l))
                Q.append(current.left)
            if r != "None":
                current.right = TreeNode(int(r))
                Q.append(current.right) 
        return root
                
            
            
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))