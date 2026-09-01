class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        wt=coins
        W=amount
        dp=[float('inf')]*(W+1)
        dp[0]=0
        n=len(wt)
        for i in range(n):
            for w in range(wt[i],W+1):
                dp[w]=min(dp[w],1+dp[w-wt[i]])
        return dp[W] if dp[W] != float('inf') else -1      

        