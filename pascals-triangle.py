class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
            
        if numRows == 2:
            return [[1],[1,1]]
            
        counter = 2
        
        triangle = [[1],[1,1]]
        
        while counter < numRows:
            tmp = [1]
            
            for i in range(len(triangle[-1])-1):
                tmp.append(triangle[-1][i] + triangle[-1][i+1])

            tmp.append(1)
            
            triangle.append(tmp)
            
            counter += 1
        return triangle
            
        