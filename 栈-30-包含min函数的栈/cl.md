### solution
使用一个辅助栈，当加入新元素的时候，保证辅助栈的栈顶元素为最小元素；
新来的元素若小于辅助栈栈顶元素，则直接插入，若大于，则重复插入一次栈顶元素
主栈的操作与普通栈相同

```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_main = []
        self.stack_min = [] 


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_main.append(x)
        if not self.stack_min or x<=self.stack_min[-1]:
            self.stack_min.append(x)
        else:
            self.stack_min.append(self.stack_min[-1])


    def pop(self):
        """
        :rtype: None
        """
        self.stack_min.pop()
        return self.stack_main.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack_main[-1]


    def min(self):
        """
        :rtype: int
        """
        return self.stack_min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
```

### java

```java
class MinStack {
    Stack<Integer> stack_main;
    Stack<Integer> stack_min;
    /** initialize your data structure here. */
    public MinStack() {
        stack_main = new Stack<>();
        stack_min = new Stack<>();
    }
    
    public void push(int x) {
        stack_main.push(x);
        if(stack_min.isEmpty()||stack_min.peek()>=x){
            stack_min.push(x);
        }
        else{
            stack_min.push(stack_min.peek());
        }
    }
    
    public void pop() {
        stack_min.pop();
        stack_main.pop();
    }
    
    public int top() {
        return stack_main.peek();
    }
    
    public int min() {
        return stack_min.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.min();
 */
```