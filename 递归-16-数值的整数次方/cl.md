### solution

[题解参考](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/)

利用十进制可以转换成二进制的加和

$$n = 9$$
$$n = 1*1 + 0*2 + 0*4 + 1*8$$

则$x^n$可以写成对应的二进制次幂的乘积

具体实现，使用位运算，将n不断地整除2，如果当前位为1，则res应该乘以当前次幂

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0
        res = 1
        if n<0:
            n = -1*n
            x = 1/x
        while n:
            if n&1==1:
                res*=x
            x *= x
            n = n>>1
        return res
```