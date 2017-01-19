class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        results = set([n])
        
            
        
        while n != 1:
            if n >= 10:
                lista_nums = [int(x) for x in str(n)]
                n = 0
                
                for l in lista_nums:
                    n += l*l
                    
                if n in results:
                    return False
                else:
                    results.add(n)
            else: 
                n = n*n
                if n in results:
                    return False
                else:
                    results.add(n)
                
            
        
        return True