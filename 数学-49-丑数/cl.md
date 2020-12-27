# solution
上一个丑数乘以2，3，5会变成后续的丑数，所以需要合并这三个序列
```python
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p2,p3,p5 = 0,0,0
        dp = [0]*n
        dp[0] = 1
        for i in range(1,n):
            dp[i]=min(dp[p2]*2,dp[p3]*3,dp[p5]*5)
            while dp[i]==dp[p2]*2:
                p2+=1
            while dp[i]==dp[p3]*3:
                p3+=1
            while dp[i]==dp[p5]*5:
                p5+=1
        return dp[-1]

        
```