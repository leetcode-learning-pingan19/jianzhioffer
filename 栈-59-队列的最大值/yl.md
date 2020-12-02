# 思路
看注释

# 代码
```python
import queue

class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()



    def max_value(self) -> int:
        # 双向队列里的第一个值为当前最大值
        return self.deque[0] if self.deque else -1



    def push_back(self, value: int) -> None:
        # 把双向队列里比当前值小的值全部取出来，这样保证里队列顶部的值一直是最大值
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)


    def pop_front(self) -> int:
        # 如果pop出的值是双线队列的顶部，则双向队列需要leftpop以保障双向队列顶部永远是最大值

        if self.queue.empty():
            return -1
        value = self.queue.get()

        if value == self.deque[0]:
            self.deque.popleft()
        return value



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
```