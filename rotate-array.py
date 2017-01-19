class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        
        """
        k = k%len(nums)
        a = nums[-k:]+nums[:-k]
        
        while nums:
            nums.pop()
        nums.extend(a)
       