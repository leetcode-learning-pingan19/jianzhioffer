### solution
归纳法

```python
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 长度1234的时候可以手动推导，大于5的时候尽可能剪成长度为3的，若剩下绳子为4，则剪成2和2
        if n==0 or n==1:
            return 0
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        cnt_3 = n//3 # 剪成3的段数
        if n-cnt_3*3==1:
            cnt_3-=1 
        cnt_2 = (n-cnt_3*3)//2
        res = 1
        for i in range(cnt_3):
            res*=3
        for i in range(cnt_2):
            res*=2
        return res
        
```