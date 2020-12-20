### solution

```python
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        high = n//10
        low = 0
        cur = n%10
        digit = 1
        res = 0
        while high!=0 or cur!=0:
            if cur==0:
                res+=high*digit
            elif cur==1:
                res+=(high*digit+low+1)
            else:
                res+=((high+1)*digit)
            low += cur*digit
            cur = high%10
            high =high//10
            digit *=10
        return res
```