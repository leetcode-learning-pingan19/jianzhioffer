### solution 
本题有个bug，要求返回的整数列表，所以不存在大数越界的问题，实际上这一问题的难点就在于大数的打印，应该返回的是字符串，本题按照这个思路去想吧

```python
class Solution(object):
    def printOneNumber(self,s,res):
        # 打印某一数字,不打印前面的0
        i = 0
        while i<len(s):
            if s[i]!="0":
                break
            else:
                i+=1
        if i==len(s):
            return 
        res.append("".join(s[i:]))
        return
    def printRecursively(self,s,n,idx,res):
        if idx==n-1:
            return self.printOneNumber(s,res)
        for i in range(10):
            s[idx+1] = str(i)
            self.printRecursively(s,n,idx+1,res)
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n<=0:
            return n;
        s = ["0"]*n
        for i in range(10):
            s[0] = str(i)
            self.printRecursively(s,n,0,res)
        res = [int(x) for x in res]
        return res
        

```