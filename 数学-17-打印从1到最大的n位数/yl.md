# 思路
模拟加法，但是自己写的速度巨慢

# 代码

```python
class Solution:
    def add_one(self, num):
        # 模拟加法，主要是进位
        # 加减应该用ascii码，这里为了省事直接用int
        i = len(num) - 1
        num[i] += 1
        while i > 0 and num[i] == 10:
            num[i] = 0
            num[i-1] += 1
            i -= 1
        if num[0] < 10:
            return num
        else:
            return None

    
    def printNumbers(self, n: int) -> List[int]:
        num = [0] * n
        ret = []
        while num is not None:
            num = self.add_one(num)
            if num:
                # 使用ascii的话不存在转str这一步
                ret.append("".join([str(a) for a in num]))
        ret = [int(r.lstrip("0")) for r in ret]
        return ret
```