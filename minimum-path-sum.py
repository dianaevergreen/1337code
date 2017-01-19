class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if len(grid) == 0:
            return 0
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        
        row = len(grid)
        column = len(grid[0])
        
        rematrix = [x[:] for x in grid]
        
        
        for r in range(row):
            for c in range(column):
                if r ==0 and c == 0:
                    continue
                elif r == 0 and c != 0:
                    rematrix[r][c] += rematrix[r][c-1] 
                elif c == 0 and r != 0:
                    rematrix[r][c] += rematrix[r-1][c]
                else: 
                    rematrix[r][c] += min(rematrix[r][c-1], rematrix[r-1][c])
                
                
        return rematrix[-1][-1]        