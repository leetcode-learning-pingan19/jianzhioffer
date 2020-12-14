## 思路

很明显可以用map和排序来做

还可以用生死一对一来解决。

循环数组，每次根据当前的数字与记录的数字相同与否，对投票进行+1 -1，一旦投票为0，说明之前的都已经抵消，最后一定只剩下多于一半的数字

## code

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int res = 0;
        int votes = 0;
        for (int num : nums) {
            if (votes == 0) {
                res = num;
                votes = 1;
            } else {
                votes += num == res ? 1 : -1;
            }
        }
        return res;
    }
};
```

