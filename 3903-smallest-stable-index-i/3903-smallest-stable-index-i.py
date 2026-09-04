class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        i=0
       
        for i in range(len(nums)):
            left=max(nums[:i+1])
            right=min(nums[i:])
            d=left-right
            if d <=k:
                return i
        return -1        
                
            

        
            
        