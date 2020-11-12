1. 使用动态规划， 转移矩阵dp
2. dp[j] 为以j结尾的最长不重复字串长度， i表示j之前的第一个重复字符
3. 当 i < 0：dp[j] = d[j-1] + 1; 当 dp[j] < j-i: dp[j] = dp[j-1] + 1; 当 dp[j] >= j-i(j前的重复字符在j-1的不重复字符之内，此时有i决定长度): dp[j] = j-i
4. 用一个哈希表储存i的位置

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        record = {}
        dp [0] = 1
        for i, c in enumerate(s):
            if i == 0:
                record[c] = i
                continue
            pre_same_index = record.get(c, -1)
            if pre_same_index < 0:
                dp[i] = dp[i-1] + 1
            elif dp[i-1] >= i - pre_same_index:
                dp[i] = i - pre_same_index
            else:
                dp[i] = dp[i-1] + 1
            record[c] = i

        return max(dp)
```