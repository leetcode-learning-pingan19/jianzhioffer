## 思路

排序数组就想到二分法，而长度为n-1的排序数组，每个数字都在n-1范围内，可知这个数组分成了左右两个部分，需要找到的就是分界点+1

## 代码

```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int left = 0;
        int right = nums.size()-1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == mid) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
```

