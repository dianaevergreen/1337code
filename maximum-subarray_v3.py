class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if all([x<0 for x in nums]):
            return max(nums)    
            
        current_sum = max_sum = 0
        
        for n in nums:
            current_sum += n
            if current_sum < 0:
                current_sum = 0
            else:
                if current_sum > max_sum:
                    max_sum = current_sum
        
        return max_sum