from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr=nums
        t=sum(nums)
        if t%2!=0:
            return False
        t=t//2   
        n=len(arr)
        dp=[[0]*(t+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,t+1):
                if arr[i-1]<=j:
                    dp[i][j]=max(arr[i-1]+dp[i-1][j-arr[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][t]==t                


                
       