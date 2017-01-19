class Solution(object):
    
    def MergeSort(self, lista):
        if len(lista)<= 1:
            return lista
        else:    
            mid = len(lista) / 2
            L = self.MergeSort(lista[:mid])
            R = self.MergeSort(lista[mid:])
            
            sol = []
            
            while L and R:
                if L[0] <= R[0]:
                    sol.append(L.pop(0))
                else:
                    sol.append(R.pop(0))
            sol.extend(L)
            sol.extend(R)
            return sol
         
        
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        sol = self.MergeSort(nums)
        return sol[-k]
        