## 思路

1. matrix的上下左右边界分别为t, b, l, r, 初始化为0, len(matrix), 0, len(matrix[0])
2. 分别按照从左到右，从上到下，从右到左，从下到上的顺序执行
3. 每执行一个边，对应的边界缩小1

## 代码

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        ret = []
        while True:
            for j in range(l, r+1):
                ret.append(matrix[t][j])
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                ret.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for j in range(r, l-1, -1):
                ret.append(matrix[b][j])
            b -= 1
            if t > b:
                break
            for i in range(b, t-1, -1):
                ret.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return ret
```
