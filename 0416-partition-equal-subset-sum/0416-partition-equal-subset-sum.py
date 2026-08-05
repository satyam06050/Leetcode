from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr=nums
        n=len(nums)
        t=sum(nums)
        if t%2!=0:
            return False
        t=t//2
        dp=[[False]*(t+1) for _ in range(n+1)]
        for i in range(n + 1):
            dp[i][0] = True

        for j in range(1, t + 1):
            dp[0][j] = False
        for i in range(1,n+1):
            for j in range(1,t+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][t]                    