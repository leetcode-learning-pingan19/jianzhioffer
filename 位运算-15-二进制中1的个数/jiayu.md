## 思路

每次除2判断是否余1，余的话说明最右边是1，然后>>1 向右移动一位，继续循环

## code

```c++
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        while (n != 0) {
            if (n % 2 != 0) {
                res += 1;
            }
            n = n >> 1;
        }
        return res;
    }
};
```

