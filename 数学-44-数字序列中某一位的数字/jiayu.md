## 思路

根本就不想做这种题

## 代码

```c++
class Solution {
public:
    int findNthDigit(int n) {
        // digit表示几位数,start表示几位数的起始数字
        // start*9表示几位数有几个,count=9*start*digit表示几位数总共有几位
        long digit = 1,start = 1,count = 9;
        // 确定所求的数是几位数
        while(n > count){
            n -= count;
            start *= 10; //1,10,100
            digit += 1;  //1,2,3
            count = 9 * start * digit;
        }
        long num = start + (n-1)/digit;
        int res = int(to_string(num)[(n-1) % digit] - '0');
        return res;
    }
};
```

