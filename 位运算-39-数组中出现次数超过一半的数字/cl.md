### solution 
O(N)

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [nums[0],1]
        for i in nums[1:]:
            if i==count[0]:
                count[-1]+=1  # 若与保存数字一致+1
            elif i!=count[0] and count[-1]==0:
                count=[i,1] # 若保存数字的对应次数为0，则换新的数字
            else:
                count[-1]-=1 # 若与保存数字不同，则减去1
        return count[0]
```