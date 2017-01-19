class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    

    
        letter_map = {}        
        for i in range(len(s)):
            if s[i] not in letter_map:
                if t[i] not in letter_map.values():
                    letter_map[s[i]] = t[i]
                else:
                    return False
            else:
                if letter_map[s[i]] != t[i]:
                    return False
        return True