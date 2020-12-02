### solution 1
队列要求先入先出
每次push一个新的，直接加入到stack1中；
每次pop一个，需要找到最先入栈的，这时候将stack1中的元素依次pop并push入stack2，这样stack2的栈顶元素就是最早入栈的；每次pop的时候，若stack2非空，则取栈顶元素，若空，将stack1中元素压入stack2再取栈顶元素即可
时间复杂度分析：
这样的push时间复杂度为O(1),
pop时间复杂度也为O（1），看起来像是N，但是每个被插入和弹出stack2一次，所以取一个元素的平均时间复杂度为O(1)

```python 
class CQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack_1.append(value)



    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.stack_1 and not self.stack_2:
            return -1
        if self.stack_2:
            return self.stack_2.pop()
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()
    




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

### java

```java
class CQueue {
    Stack<Integer> stack_1;
    Stack<Integer> stack_2;

    public CQueue() {
        stack_1 = new Stack<>();
        stack_2 = new Stack<>();
    }
    
    public void appendTail(int value) {
        stack_1.push(value);
    }
    
    public int deleteHead() {
        if(stack_1.isEmpty()&&stack_2.isEmpty()){
            return -1;
        }
        if(!stack_2.isEmpty()){
            return stack_2.pop();
        }
        while(!stack_1.isEmpty()){

            stack_2.push(stack_1.pop());
        }
        return stack_2.pop();
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = new CQueue();
 * obj.appendTail(value);
 * int param_2 = obj.deleteHead();
 */
```

