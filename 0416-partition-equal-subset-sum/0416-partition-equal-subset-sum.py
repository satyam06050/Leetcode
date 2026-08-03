from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        n=len(nums)
        if total%2!=0:
            return False
        t=total//2
        dp=[[0]*(t+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,t+1):
                if nums[i-1]<=j:
                    dp[i][j]=max(nums[i-1]+dp[i-1][j-nums[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]    

                

        return dp[n][t]==t        