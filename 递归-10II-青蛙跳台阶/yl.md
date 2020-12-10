# 思路
sn = sn-1 + sn-2

# 代码
```python
class Solution:
    def numWays(self, n: int) -> int:
        # Sn = Sn-1 + Sn-2
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2      
        s1 = 1
        s2 = 2 
        sn = 0
        for _ in range(3, n+1):
            sn = s1+s2
            s1 = s2
            s2 = sn
            if sn > 1000000007:
                sn = sn % 1000000007

        return sn
```