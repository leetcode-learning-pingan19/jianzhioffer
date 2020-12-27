# 思路
两个栈，s1和s2，如果s1的元素全pop出在add入s2中，则s2的pop顺序刚好是先进先出的顺序，所以在deleteHead的时候有两种情况
1. 如果s2中有值，则直接pop
2. 如果s2为空，则将s1的元素全部pop后add入s2后，再pops2

# 代码
```python
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```