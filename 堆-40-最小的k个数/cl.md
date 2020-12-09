### solution 1 
使用大顶堆维护$k$个数字,数字若比堆顶元素小，pop出堆顶元素并且插入新数据
插入一个元素的时间复杂度为$log（k）$
时间复杂度$nlog(k)$

python只有小顶堆，可以将元素*-1变成大顶堆

```python
import heapq

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k==0:
            return []
        hp = [-x for x in arr[:k]] 
        heapq.heapify(hp)
        for i in range(k,len(arr)):
            x = arr[i]
            if x< -hp[0]:
                # 插入
                heapq.heappop(hp)
                heapq.heappush(hp,-x)
        
        return [-x for x in hp]

```


### solution 2
快排,注意边界写法，别绕进去了

```python
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k==0:
            return []
        def _partition(arr,left,right):
            v= arr[left]
            while left<right:
                while left<right and arr[right]>=v:
                    right-=1
                if left<right:
                    arr[left] = arr[right]
                while left<right and arr[left]<=v:
                    left+=1
                if left<right:
                    arr[right] = arr[left]
            arr[right] = v 
            return right

        def _judge(arr,left,right,k):
            v = _partition(arr,left,right)
            if v-left+1==k:
                return
            if v-left+1>k:
                return _judge(arr,left,v-1,k)
            return _judge(arr,v+1,right,k-(v-left+1))

        _judge(arr,0,len(arr)-1,k)
        return arr[:k]
```


