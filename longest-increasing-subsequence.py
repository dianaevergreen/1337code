class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
            
        L = [[nums[0]]]  
        
        for n in range(1,len(nums)):
            longi = 0
            tmp = []
            for l in range(len(L)-1,-1,-1):
                if nums[n] > L[l][-1]:
                    if longi < len(L[l]):
                        longi = len(L[l])
                        tmp = L[l][:]
                        
            tmp.append(nums[n])
            L.append(tmp)
            
       
        
        return max(len(x) for x in L)
                    
                    
                    
                
                    
  