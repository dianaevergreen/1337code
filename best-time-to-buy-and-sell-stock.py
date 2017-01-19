class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) == 0:
            return 0
        
        compro = prices[0]
        
        diff = 0
        
        for i in range(len(prices)):
            vendo = prices[i]
            if vendo - compro > diff:
                diff = vendo - compro
            if prices[i] < compro:
                compro = prices[i]
            
                
        
        
            
        return  diff
                
          
            
         
        
        