# 剑指 Offer 53 - I. 在排序数组中查找数字 I
### solution: 
遍历一遍的时间复杂度为O(N)，本题目可以使用两次二分法，分别找到初始和结束为止,时间复杂度为O(logN)
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 两个二分法 一个找起始位置，一个找结束为止O(logn)
        def _search(start,end,mode='first'):
            if start>end:
                return -1
            mid = (start+end)//2
            if nums[mid]==target and mode=='first' and (mid==0 or nums[mid-1]!=target):
                return mid
            elif nums[mid]==target and mode!='first' and (mid==len(nums)-1 or nums[mid+1]!=target):
                return mid
            elif nums[mid]>target or (nums[mid]==target and mode=="first"):
                return _search(start,mid-1,mode=mode)
            else:
                # nums[mid]>target or (nums[mid]==target and mode!="first")
                return _search(mid+1,end,mode=mode)
        start,end,mode = 0,len(nums)-1,"first"
        firstk = _search(start,end,mode)  
        start,end,mode = 0,len(nums)-1,"last"
        lastk = _search(start,end,mode)  
        if firstk!=-1 and lastk!=-1:
            return lastk-firstk+1
        return 0
```

### java版本

```java
class Solution {
    private int search_first(int[] nums,int start, int end,int target){
        if(start>end){
            return -1;
        }
        int mid = (start+end)/2;
        if(nums[mid]==target&&(mid==0||nums[mid-1]!=target)){
            return mid;
        }
        else if(nums[mid]>=target){
            return this.search_first(nums,start,mid-1,target);
        }
        else{
            return this.search_first(nums,mid+1,end,target);
        }
    }
        private int search_last(int[] nums,int start, int end,int target){
        if(start>end){
            return -1;
        }
        int mid = (start+end)/2;
        if(nums[mid]==target&&(mid==nums.length-1||nums[mid+1]!=target)){
            return mid;
        }
        else if(nums[mid]>target){
            return this.search_last(nums,start,mid-1,target);
        }
        else{
            return this.search_last(nums,mid+1,end,target);
        }
    }
    public int search(int[] nums, int target) {
        int firstk = this.search_first(nums,0,nums.length-1,target);
        int lastk = this.search_last(nums,0,nums.length-1,target);
        if(firstk!=-1&&lastk!=-1){
            return lastk-firstk+1;
        }
        return 0;
    }
}
```

# 剑指 Offer 53 - II. 0～n-1中缺失的数字

### solution: 
二分法 找到第一个数字和index不匹配的位置，返回该位置即可，如果全都匹配，一定会在最后一个位置，返回位置+1

```python
class Solution(object):
    def _search(self,nums,start,end):
        mid = (start+end)//2
        if nums[mid]==mid and mid!=len(nums)-1:
            return self._search(nums,mid+1,end)
        elif nums[mid]==mid and mid==len(nums)-1:
            return mid+1
        elif nums[mid]!=mid and (mid==0 or nums[mid-1]==mid-1):
            return mid
        else:
            return self._search(nums,start,mid-1)
        
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end = 0,len(nums)-1
        return self._search(nums,start,end)

        
```

### java版本：
```java
class Solution {
    private int _search(int[] nums, int start,int end){
        int mid = (start+end)/2;
        if(nums[mid]!=mid&&(mid==0||nums[mid-1]==mid-1)){
            return mid;
        }
        else if(nums[mid]!=mid){
            return this._search(nums,start,mid-1);
        }
        else if(nums[mid]==mid&&mid!=nums.length-1){
            return this._search(nums,mid+1,end);
        }
        else{
            return mid+1;
        }
    }
    public int missingNumber(int[] nums) {
        return this._search(nums,0,nums.length-1);
    }
}
```