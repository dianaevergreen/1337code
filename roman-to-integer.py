class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        table = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        
    
        

        ptr1 = 0
        ptr2 = 1
        numero = 0
        
        while ptr1 < len(s):
            if ptr2 < len(s) and table[s[ptr2]]  > table[s[ptr1]]:
                numero += table[s[ptr2]] - table[s[ptr1]]
                ptr1 += 2
                ptr2 += 2
                
            else:
                numero += table[s[ptr1]]
                ptr1 += 1
                ptr2 += 1
        
       
        return numero     
            
            