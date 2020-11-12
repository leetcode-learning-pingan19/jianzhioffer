
# 思路
1. 用一个有序字典记录每个字符是否唯一
2. py3.6以后的默认字典为有序字典
3. [TODO](https://www.cnblogs.com/xieqiankun/p/python_dict.html)

# 代码
```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic

        for k, v in dic.items():
            if v:
                return k
        return " "
```