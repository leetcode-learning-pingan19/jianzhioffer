### solution

[参考](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/)


使用小顶堆A和大顶堆B，
若数组长度为偶数，ab各维护一半的数据，A维护大的一部分，B维护小的一部分，若为奇数，a多维护一个

插入数据时：
首先判断
$$ len(a)==len(b) $$

新数据插入b中再将b堆顶元素推出，插入a中

$$ len(a)!=len(b) $$

新数据插入a中再将a堆顶元素推出，插入a中


中位数 需要判断奇偶数

坑在最后2.0而不是2
```python
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = [] # 大数，小顶堆
        self.b = [] # 小数，大顶堆


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.a)==len(self.b):
            heapq.heappush(self.b,-num)
            heapq.heappush(self.a,-heapq.heappop(self.b))
        else:
            heapq.heappush(self.a,num)
            heapq.heappush(self.b,-heapq.heappop(self.a))



    def findMedian(self):
        """
        :rtype: float
        """
        return self.a[0] if len(self.a)!=len(self.b) else (self.a[0]-self.b[0])/2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```



