### solution 
[题解参考了](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/solution/mian-shi-ti-67-ba-zi-fu-chuan-zhuan-huan-cheng-z-4/)
1. 删除首部的空白字符
2. 符号位保存符号
3. 遇到第一个数字或者符号位的下一个数字，开始拼接
$$res =res*10+x$$
$$x = int(x-'0')$$
4. 遇到第一个非数字字符，跳出，返回结果
5. 边界处理，对于每一次拼接提前判断是否越界，即拼接后是否超过2147483647,
$$b = 2147483647//10=214748364$$

越界的两种情况：
(1)如果当前$res>b$,则一定会越界
(2)如果当前$res=b,x>7$则一定会越界


```python
class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign,res,i=1,0,0
        int_max,int_min =2**31-1,-2**31
        b = 2**31//10
        while i<len(str):
            if str[i]!=" ":
                break
            i+=1
        if i==len(str): return 0
        sign = -1 if str[i]=="-" else 1
        if str[i] in {'-','+'}: i+=1
        for idx in range(i,len(str)):
            if not '0'<=str[idx]<='9': break
            if res>b or res==b and str[idx]>'7':
                return int_max if sign>0 else int_min
            else:
                res = 10*res + ord(str[idx])-ord('0')
            
        return res if sign>0 else -1*res


```