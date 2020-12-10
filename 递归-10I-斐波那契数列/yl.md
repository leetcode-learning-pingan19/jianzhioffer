# 思路
sn = sn-1 + sn-2

# 代码
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1      
        s0 = 0
        s1 = 1
        for _ in range(2, n+1):
            sn = (s0 + s1) % 1000000007
            s0 = s1
            s1 = sn 
        return sn
```