### solution

动态规划

```python
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        res = [1,1]
        for i in range(2,n+1):
            s = (res[0]+res[1])%1000000007
            res[0] = res[1]
            res[1] = s
        return res[-1]
```