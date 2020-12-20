### solution

确定是几位数
确定n位数对应的数字个数
锁定目标数，并且锁定目标位数

```python
class Solution(object):
    def countOfInt(self,digits):
        if digits==1:
            return 10
        return 9*(10**(digits-1))

    def getBeginDigit(self,digits):
        if digits==1:
            return 0
        return (10**(digits-1))

    def getDigit(self,index,digits):
        num = self.getBeginDigit(digits)+index/digits # 确定目标数字
        move_num= digits - index%digits # 选第几个数字,从右边数
        for i in range(1,move_num):
            num /= 10
        return  num%10




    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 
        digits = 1
        while True:
            nums = digits * self.countOfInt(digits)
            if n<nums:
                return self.getDigit(n,digits)
            n -= nums
            digits +=1
        return -1

```