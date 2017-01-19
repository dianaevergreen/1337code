class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bestSum = nums[0]
        curSum = 0
        
        if all([x<0 for x in nums]):
            return max(nums)
        
        for x in nums:
            if x>=0:
                curSum+=x
            else:
                bestSum=max(bestSum, curSum)
                curSum=max(0, curSum+x)
                
        bestSum=max(bestSum, curSum)
        return bestSum
            
            
            
        
        
            