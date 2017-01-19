dicty = {1:1}

class Solution(object):
    
    def calculator(self, lista):
        global dicty
        if dicty.get(len(lista)):
            return dicty[len(lista)]
        
        
        counter = 0
        
        if len(lista) == 1:
            return 1
            
        for l in range(len(lista)):
            
            
            if l == 0:
                counter += self.calculator(lista[1:])
                
            elif l == len(lista) -1 :
                counter += self.calculator(lista[:len(lista)-1])
                
            else:
                counter += self.calculator(lista[:l]) * self.calculator(lista[l+1:])
        dicty[len(lista)] = counter
        return counter
            
        
        
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0 or n ==1:
            return 1
       
            
        array = range(1,n+1)
        
        
        return self.calculator(array)
        
        
        