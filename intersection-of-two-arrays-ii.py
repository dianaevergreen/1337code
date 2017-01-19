class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sol = []
        
        hash1 = {}
        hash2 = {}
        
        for n1 in nums1:
            if n1 not in hash1:
                hash1[n1] = 1
            else:
                hash1[n1] += 1
                
        for n2 in nums2:
            if n2 in hash1:
                sol.append(n2)
                if hash1[n2] == 1:
                    del hash1[n2]
                else:
                    hash1[n2] -= 1
                    
                
        return sol   
            