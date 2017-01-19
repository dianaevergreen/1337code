class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ptr1 = 0
        ptr2 = len(s) - 1
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        sol = [None] * len(s)
        
        
        while ptr1 <= ptr2:
            if s[ptr1] not in vowels:
                sol[ptr1] = s[ptr1]
                ptr1 += 1
                
            else:
                
                while s[ptr2] not in vowels and ptr2 > ptr1:
                    sol[ptr2] = s[ptr2]
                    ptr2 -= 1
                
                sol[ptr1] = s[ptr2]
                sol[ptr2] = s[ptr1]
            
                ptr1 += 1
                ptr2 -= 1
              
        a = ''.join(x for x in sol)   
        
        return a
            
            