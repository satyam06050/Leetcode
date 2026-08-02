from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        n=len(nums)
        if total%2!=0:
            return False
        t=total//2
        dp=[[-1]*(t+1) for _ in range(n+1)]
        def ss(arr,n,t,dp):
            if t==0:
                return True
            if n==0:
                return False
            if dp[n][t]!=-1:
                return dp[n][t]
            if arr[n-1]>t:
                dp[n][t]=ss(arr,n-1,t,dp)
            else:
                dp[n][t]=(ss(arr,n-1,t-arr[n-1],dp)or ss(arr,n-1,t,dp))
            return dp[n][t]
        return ss(nums,n,t,dp)                             
        