### solution
解决方法：使用双向队列
python中collection(Queue)的deque

更新策略，新来一个元素，从尾部开始遍历，如果新元素大于尾部元素，将尾部元素删除，直到队列对空或者遇到大于新元素的元素，将新元素压入队列，这样形成的队列永远是从大到小的单调队列，第一位置的元素永远是当前的最大元素

如何处理窗口的限制呢，很简单，压入队列的不是元素本身而是元素的index，这样在加入新元素之前队列中小于i-k的头部元素依次删除掉即可

这样的时间复杂度O(N)，空间复杂度O（k）

```python
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        que = deque()
        if not nums or k<=0:
            return []
        
        for i,item in enumerate(nums):
            while que and que[0]<=i-k:
                que.popleft()
            while que and item>nums[que[-1]]:
                que.pop()
            que.append(i)
            if i>=k-1:
                res.append(nums[que[0]])
        return res


```