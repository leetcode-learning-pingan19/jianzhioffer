### solution 
使用双头队列作为辅助，保证目前队列中最大值一直位于头部python2中的Queue貌似有问题
python 3中 
```python
from queque import Queue,deque
```

```python
from Queue import Queue,deque
# import queue
class MaxQueue(object):
    def __init__(self):
        self.que_main =[]
        self.stack =[]

    def max_value(self):
        """
        :rtype: int
        """
        return self.stack[0] if self.stack else -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        
        while self.stack and value>self.stack[-1]:
            self.stack.pop()
        self.stack.append(value)
        self.que_main.append(value)
        print(self.stack)
        

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.que_main:
            return -1
        ans = self.que_main.pop(0)
        if self.stack[0]==ans:
            self.stack.pop(0)
        return ans
```