# 思路
dp[1] = dp[2] = 1
递推公式：dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
max()里面的个参数分别表示：
- dp[i] 其实就是从j=0~i里选一个最大值
- j*(i-j) 题目要求必须要剪一刀，这个就是只剪一刀的值
- j*dp[i-j] 当在j剪一刀的时候，剩下的i-j一定要剪出最大值，才能保证积最大，这个最大值保存在dp[i-j]中，且在前面的迭代中已经被计算了

# 代码

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            # 长度为i的绳子
            for j in range(i):
                # 从第j处剪一刀
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]
```