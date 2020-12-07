## 思路

* 可以采用递归，也可以采用迭代
* 递归太耗费时间，迭代即可
  * 从最初开始迭代，为了节省空间，不用数组存储，而用变量循环赋值



## code

```c++
class Solution {
public:
    int fib(int n) {
        int a = 0, b = 1;
        for (int i = 0; i < n; ++i) {
            a %= 1000000007;
            b %= 1000000007;
            int tmp = a;
            a = b;
            b = tmp + b;
        }
        return a % 1000000007;
    }
};
```

