dict_paths = {}
class Solution(object):
    
    
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        global dict_paths
        
        if m-1 == 0 or n -1 == 0:
            return 1
            
        if (m-1, n-1) in dict_paths:
            return dict_paths[(m-1, n-1)]
            
        else:
            dict_paths[(m-1,n-1)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
            
            return dict_paths[(m-1, n-1)]
        
       