class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        ans.append(nums[0])
        for i in range(1,len(nums)):
            left=sum(nums[:i+1])
            ans.append(left)
        return ans    

        
    