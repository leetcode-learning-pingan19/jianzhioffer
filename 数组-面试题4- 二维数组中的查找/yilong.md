## 思路

1. 从matrix的右上角开始，坐标为i，j
2. target小于当前数，向左找更小的数，i-=1；当target大于当前数，向下找更大的数，j+=1

## 代码

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False
```
