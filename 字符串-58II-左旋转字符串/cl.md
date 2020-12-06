### solution 1
关键是如何用原地，而不是用额外空间
方法是局部反转+整体反转

有个bug，string本身不能assign，所以转换成list的过程，空间也是用了O（N），可能只有C++可以用使用指针的方式改变这个方法了，以下就是写着玩； 

```python
class Solution(object):
    def _reverse(self,s,left,right):

        while left<right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left +=1
            right -=1
        return s 
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if not s:
            return s
        s = list(s)
        l = len(s)
        n %= l 
        left =0 
        right = 0+n
        s = self._reverse(s,0,n-1)
        s = self._reverse(s,n,l-1)
        s = self._reverse(s,0,l-1)
        return "".join(s)
```

### solution 2
拼接两个片段

```python
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        l = len(s)
        n%=l
        return s[n:]+s[:n]
```

```java
class Solution {
    public String reverseLeftWords(String s, int n) {
        int l = s.length();
        n %= l;
        return s.substring(n,l)+ s.substring(0,n);
    }
}
```