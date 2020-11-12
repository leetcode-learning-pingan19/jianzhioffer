# 第一题

## 思路

1. 使用二分法，先找右边界，在找左边界
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        i, j = 0 , len(nums) - 1
        # 先找右边界
        while i <= j:
            m = (i+j) // 2
            if nums[m] <= target:
                # 中间值比目标值大或等于目标值，左侧边界要移动过来
                i = m + 1
            else:
                # 中间值比目标值小, 右侧边界移过来
                j = m - 1
        right = i

        i = 0
        while i <= j:
            m = (i+j) // 2
            if nums[m] >= target:
                # 中间值比目标值小或等于目标值，侧边界要移动过来
                j = m - 1
            else:
                # 中间值比目标值小, 右侧边界移过来
                i = m + 1
        left = j

        return right - left - 1
```

# 第二题

## 思路

1. 二分法: 如果当前值小于里面的数字：右边界移动, 如果当前值等于里面的数字：左边界移动

## 代码

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
   
        i, j = 0, len(nums) - 1

        # 如果当前值小于里面的数字：
            # 右边界移动
        # 如果当前值等于里面的数字：
            # 左边界移动

        while i <= j:
            m = (i + j) // 2

            if m < nums[m]:
                j = m - 1
            else:
                i = m + 1
            
        return i
```