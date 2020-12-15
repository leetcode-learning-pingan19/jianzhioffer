### solution
手写正则表达式

```python
class Solution(object):
    def getUnsignedInteger(self,s):
        if not s:
            return False
        for i,chas in enumerate(s):
            if not "0"<=chas<="9":
                return False
        return True

    def getInteger(self,s):
        if not s:
            return False
        if s[0] in {"+","-"}:
            return self.getUnsignedInteger(s[1:])
        return self.getUnsignedInteger(s)
    
    def getXiaoshu(self,s):
        i = 0
        while i<len(s) and s[i]!="." :
            i+=1
        if i == len(s):
            return self.getInteger(s)
        if i==len(s)-1:
            return self.getInteger(s[:-1])
        if i==0:
            return self.getUnsignedInteger(s[i+1:])
        return self.getInteger(s[:i]) and self.getUnsignedInteger(s[i+1:])
        
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        if s[0] in {"+","-"}:
            s = s[1:]
        i = 0
        while i<len(s) and s[i] not in {"e","E"}:
            i+=1
        if i==len(s)-1:
            return False
        return self.getXiaoshu(s[:i]) and (i==len(s) or self.getInteger(s[i+1:]))


```