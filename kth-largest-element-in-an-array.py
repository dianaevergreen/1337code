class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        solution = [nums[-1]]
        
        for i in nums[:-1]:
            if i >= solution[0]:
                if i >= solution[-1]:
                    solution.append(i)
                else:
                    for s in range(len(solution)):
                        if i < solution[s]:
                            solution.insert(s,i)
                            break
            else:
                solution.insert(0,i)
        
                
        return solution[-k]
            