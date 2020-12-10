# 思路
dp[1] = dp[2] = 1
递推公式：dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
max()里面的个参数分别表示：
- dp[i] 其实就是从j=1~(i//2)里选一个最大值, >i//2时，和0～i//2的情况一样
- j*(i-j) j处切一刀，i-j不切, (dp[i-j]里存的是i-j必须切一刀的值)
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
            for j in range(1, (i//2)+1):
                # 从第j处剪一刀
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]
```