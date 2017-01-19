dicty ={0:0, 1:1, 2:2}
class Solution(object):
    
    
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        global dicty
        
        if n in dicty:
            return dicty[n]
        
        sol = self.climbStairs(n-1) + self.climbStairs(n-2)
        dicty[n] = sol
        
    
        return sol
        
        
        
        