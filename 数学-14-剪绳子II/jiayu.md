## 思路

分割为2和3，且3优先

## code

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, p = n // 3, n % 3, 1000000007
        if b == 0: return 3 ** a % p
        if b == 1: return 3 ** (a - 1) * 4 % p
        return 3 ** a * 2 % p
```

