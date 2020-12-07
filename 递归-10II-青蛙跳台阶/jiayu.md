## 思路

和斐波那契数列原理一样

## code

```c++
class Solution {
public:
    int numWays(int n) {
        int a = 1, b = 1;
        for (int i = 0; i < n; ++i) {
            a %= 1000000007;
            b %= 1000000007;
            int tmp = a;
            a = b;
            b += tmp;
        }
        return a % 1000000007;
    }
};
```

