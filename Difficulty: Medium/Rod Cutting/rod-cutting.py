class Solution:
    def cutRod(self, price):
        #code here
        n=len(price)
        arr=[i for i in range(1,n+1)]
        
        dp=[[0]*(n+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if arr[i-1]<=j:
                    dp[i][j]=max(price[i-1]+dp[i][j-arr[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][n]                
                    