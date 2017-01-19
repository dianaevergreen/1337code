class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        parallel = [nums[0]]
        
        for n in range(1,len(nums)):
            if nums[n] + parallel[n-1] > nums[n]:
                parallel.append(nums[n]+parallel[n-1])
            else:
                parallel.append(nums[n])
                
            
        maxi = max(parallel)
        return maxi
            
            
            
        
        
            