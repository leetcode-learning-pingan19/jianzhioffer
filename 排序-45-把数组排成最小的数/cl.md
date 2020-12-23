### solution


```python
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def sort_val(x,y):
            a,b = x+y,y+x
            if a>b:return 1
            elif a<b: return -1
            return 0
        
        nums = [str(x) for x in nums]
        nums.sort(key=functools.cmp_to_key(sort_val))
        return "".join(nums)

````