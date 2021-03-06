## 思路

* 所有的丑数一定是2、3、5的组合，当按照大小进行排序的时候，相当于从三个序列中依照大小挑选合并为一个序列，三个序列为：

  * ```
    nums2 = {1*2, 2*2, 3*2, 4*2, 5*2, 6*2, 8*2...}
    nums3 = {1*3, 2*3, 3*3, 4*3, 5*3, 6*3, 8*3...}
    nums5 = {1*5, 2*5, 3*5, 4*5, 5*5, 6*5, 8*5...}
    ```

* 适用指针维护每个序列，同时使用if而不是if else，来使得不同序列中相同值可以被跳过。

## code

```cpp
// 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
class Solution {
public:
	int nthUglyNumber(int n) {
		vector<int> dp(n, 0);
		dp[0] = 1;
		int p2 = 0, p3 = 0, p5 = 0;
		for (int i = 1; i < n; i++) {
			dp[i] = min(min(dp[p2] * 2, dp[p3] * 3), dp[p5] * 5);
			if (dp[i] == dp[p2] * 2)
				p2++;
			if (dp[i] == dp[p3] * 3)
				p3++;
			if (dp[i] == dp[p5] * 5)
				p5++;
		}
		return dp[n - 1];
	}
};
```

