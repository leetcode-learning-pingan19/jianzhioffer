### solution

反转两次
时间复杂度O(n),空间复杂度O(n)

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        stack = []
        if not s:
            return ''
        for i in s:
            if i== ' ' and not stack:
                continue
            if i==' ' and stack:
                while stack:
                    res.append(stack.pop())
                res.append(' ')
            else:
                stack.append(i)
        while stack:
            res.append(stack.pop())
        if res and res[-1]==" ":
            res.pop()
        while res:
            stack.append(res.pop())
        return "".join(stack)

```