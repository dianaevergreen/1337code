class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        
        path_matrix = [[None for x in range(n)] for y in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    path_matrix[0][0] = 1
                    continue
                    
                if i == 0:
                    path_matrix[i][j] = path_matrix[i][j-1]
                elif j == 0:
                    path_matrix[i][j] = path_matrix[i-1][j]
                
                else:
                    path_matrix[i][j] = path_matrix[i-1][j] + path_matrix[i][j-1]
        return path_matrix[-1][-1]