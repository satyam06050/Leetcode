class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        mi=nums[0]
        ma=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                mi,ma=ma,mi
            mi=min(nums[i],nums[i]*mi)
            ma=max(nums[i],nums[i]*ma)
            ans=max(ans,ma)
        return ans    


        
        