### solution 1
offer书里面的解法

对于n来说，减去1再与n本身做与运算，则相当于将最右边一个1变成0
以1011为例，减去1得到1010，
再与1011做与运算，变成1010，则是把最右一个1变成0

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = (n-1)&n
            count+=1
        return count
```


### solution 2
更常规的一个思路
每个位比较一下

```python
```